import sys

import click

from vcenter_lookup_bridge_client import VmFoldersApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_VM_FOLDER_COLUMNS = ["name", "vcenter", "datacenter", "path"]


@click.group(help=_("VM folder operations"))
def vm_folders():
    pass


@vm_folders.command("list", help=_("List VM folders"))
@click.option("--vm-folders", "vm_folder_names", default=None, help=_("VM folder name(s) (comma-separated)"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_vm_folders(ctx, vm_folder_names, offset, max_results, vcenter):
    api = VmFoldersApi(ctx.obj["api_client"])
    folders = [f.strip() for f in vm_folder_names.split(",")] if vm_folder_names else None
    try:
        response = api.list_vm_folders(vm_folders=folders, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _VM_FOLDER_COLUMNS)
