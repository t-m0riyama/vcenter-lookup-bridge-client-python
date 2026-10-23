import sys

import click

from vcenter_lookup_bridge_client import DatastoresApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_api_error, output_json, output_table
from .i18n import _

_DATASTORE_COLUMNS = ["name", "vcenter", "datacenter", "type", "capacity_gb", "free_space_gb"]


@click.group(help=_("Datastore operations"))
def datastores():
    pass


@datastores.command("list", help=_("List datastores filtered by tag, or all datastores with --all"))
@click.option("--tag-category", default=None, help=_("Tag category name"))
@click.option("--tags", default=None, help=_("Tag name(s) (comma-separated)"))
@click.option("--all", "all_datastores", is_flag=True, default=False, help=_("List all datastores regardless of tags"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_datastores(ctx, tag_category, tags, all_datastores, offset, max_results, vcenter):
    if not all_datastores and (tag_category is None or tags is None):
        raise click.UsageError(_("Specify both --tag-category and --tags, or use --all"))
    api = DatastoresApi(ctx.obj["api_client"])
    tag_list = [t.strip() for t in tags.split(",")] if tags is not None else None
    try:
        response = api.list_datastores(
            tag_category=tag_category,
            tags=tag_list,
            offset=offset,
            max_results=max_results,
            vcenter=vcenter,
            all_datastores=all_datastores or None,
        )
    except ApiException as e:
        output_api_error(e)
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _DATASTORE_COLUMNS)
