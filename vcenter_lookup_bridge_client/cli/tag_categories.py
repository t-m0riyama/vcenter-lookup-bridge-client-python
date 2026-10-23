import sys

import click

from vcenter_lookup_bridge_client import TagCategoriesApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_TAG_CATEGORY_COLUMNS = ["name", "cardinality", "associable_types", "vcenter", "description"]


@click.group(help=_("Tag category operations"))
def tag_categories():
    pass


@tag_categories.command("list", help=_("List tag categories"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_tag_categories(ctx, offset, max_results, vcenter):
    api = TagCategoriesApi(ctx.obj["api_client"])
    try:
        response = api.list_tag_categories(offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _TAG_CATEGORY_COLUMNS)
