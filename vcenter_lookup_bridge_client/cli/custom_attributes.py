import sys

import click

from vcenter_lookup_bridge_client import CustomAttributesApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_api_error, output_json, output_table
from .i18n import _

_CUSTOM_ATTRIBUTE_COLUMNS = ["name", "object_type", "type", "vcenter", "value", "object_name"]


@click.group(help=_("Custom attribute operations"))
def custom_attributes():
    pass


@custom_attributes.command("list", help=_("List custom attribute definitions, or values set on the specified object"))
@click.option("--object-type", default=None, help=_("Object type (alone: filter definitions by type, e.g. Global; with --object-name/--object-id: type of the object to look up)"))
@click.option("--object-name", default=None, help=_("Name of the object to look up assignments for"))
@click.option("--object-id", default=None, help=_("Instance UUID of the VM to look up assignments for (VirtualMachine only)"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_custom_attributes(ctx, object_type, object_name, object_id, offset, max_results, vcenter):
    api = CustomAttributesApi(ctx.obj["api_client"])
    try:
        response = api.list_custom_attributes(
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
        output_table(response.results, _CUSTOM_ATTRIBUTE_COLUMNS)
