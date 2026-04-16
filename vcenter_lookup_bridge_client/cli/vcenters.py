import sys

import click

from vcenter_lookup_bridge_client import VcentersApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_VCENTER_COLUMNS = ["name", "host", "version"]


@click.group(help=_("vCenter operations"))
def vcenters():
    pass


@vcenters.command("list", help=_("List connected vCenters"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_vcenters(ctx, offset, max_results, vcenter):
    api = VcentersApi(ctx.obj["api_client"])
    try:
        response = api.list_vcenters(offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _VCENTER_COLUMNS)
