import sys

import click

from vcenter_lookup_bridge_client import PortgroupsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_PORTGROUP_COLUMNS = ["name", "vcenter", "datacenter", "vlan_id", "vswitch_name"]


@click.group(help=_("Port group operations"))
def portgroups():
    pass


@portgroups.command("list", help=_("List port groups filtered by tag"))
@click.option("--tag-category", required=True, help=_("Tag category name"))
@click.option("--tags", required=True, help=_("Tag name(s) (comma-separated)"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_portgroups(ctx, tag_category, tags, offset, max_results, vcenter):
    api = PortgroupsApi(ctx.obj["api_client"])
    tag_list = [t.strip() for t in tags.split(",")]
    try:
        response = api.list_portgroups(tag_category=tag_category, tags=tag_list, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _PORTGROUP_COLUMNS)
