import sys

import click

from vcenter_lookup_bridge_client import VmSnapshotsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_SNAPSHOT_COLUMNS = ["name", "instance_uuid", "vcenter", "vm_name", "create_time", "description"]


@click.group(help=_("VM snapshot operations"))
def vm_snapshots():
    pass


@vm_snapshots.command("list", help=_("List snapshots in the specified VM folder"))
@click.option("--vm-folders", required=True, help=_("VM folder name(s) (comma-separated)"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_vm_snapshots(ctx, vm_folders, offset, max_results, vcenter):
    api = VmSnapshotsApi(ctx.obj["api_client"])
    folders = [f.strip() for f in vm_folders.split(",")]
    try:
        response = api.list_vm_snapshots(vm_folders=folders, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _SNAPSHOT_COLUMNS)


@vm_snapshots.command("get", help=_("List snapshots by VM instance UUID"))
@click.argument("vm_instance_uuid")
@click.option("--vcenter", required=True, help=_("vCenter name"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.pass_context
def get_vm_snapshots(ctx, vm_instance_uuid, vcenter, offset, max_results):
    api = VmSnapshotsApi(ctx.obj["api_client"])
    try:
        response = api.get_vm_snapshots(vm_instance_uuid=vm_instance_uuid, vcenter=vcenter, offset=offset, max_results=max_results)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _SNAPSHOT_COLUMNS)
