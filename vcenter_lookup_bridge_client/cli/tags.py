import sys

import click

from vcenter_lookup_bridge_client import TagsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_api_error, output_json, output_table
from .i18n import _

_TAG_COLUMNS = ["name", "tag_category", "vcenter", "description", "object_name", "object_id"]
_OBJECT_TYPES = ["VirtualMachine", "HostSystem", "Datastore", "ClusterComputeResource", "Network"]


@click.group(help=_("Tag operations"))
def tags():
    pass


@tags.command("list", help=_("List tags, or tags assigned to the specified object"))
@click.option("--tag-category", default=None, help=_("Tag category name"))
@click.option("--object-type", default=None, type=click.Choice(_OBJECT_TYPES), help=_("Type of the object to look up assignments for"))
@click.option("--object-name", default=None, help=_("Name of the object to look up assignments for"))
@click.option("--object-id", default=None, help=_("Instance UUID of the VM to look up assignments for (VirtualMachine only)"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_tags(ctx, tag_category, object_type, object_name, object_id, offset, max_results, vcenter):
    api = TagsApi(ctx.obj["api_client"])
    try:
        response = api.list_tags(
            tag_category=tag_category,
            object_type=object_type,
            object_name=object_name,
            object_id=object_id,
            offset=offset,
            max_results=max_results,
            vcenter=vcenter,
        )
    except ApiException as e:
        output_api_error(e)
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _TAG_COLUMNS)
