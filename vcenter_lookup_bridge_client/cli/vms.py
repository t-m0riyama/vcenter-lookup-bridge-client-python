import sys

import click

from vcenter_lookup_bridge_client import VmsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_VM_LIST_COLUMNS = ["name", "instance_uuid", "vcenter", "datacenter", "vm_folder", "num_cpu", "memory_size_mb"]
_VM_DETAIL_COLUMNS = ["name", "instance_uuid", "vcenter", "datacenter", "cluster", "esxi_hostname", "power_state", "num_cpu", "memory_size_mb", "ip_address"]


@click.group(help=_("Virtual Machine (VM) operations"))
def vms():
    pass


@vms.command("list", help=_("List VMs in the specified folder"))
@click.option("--vm-folders", required=True, help=_("VM folder name(s) (comma-separated)"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_vms(ctx, vm_folders, offset, max_results, vcenter):
    api = VmsApi(ctx.obj["api_client"])
    folders = [f.strip() for f in vm_folders.split(",")]
    try:
        response = api.list_vms(vm_folders=folders, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _VM_LIST_COLUMNS)


@vms.command("get", help=_("Get VM details by instance UUID"))
@click.argument("vm_instance_uuid")
@click.option("--vcenter", required=True, help=_("vCenter name"))
@click.pass_context
def get_vm(ctx, vm_instance_uuid, vcenter):
    api = VmsApi(ctx.obj["api_client"])
    try:
        response = api.get_vm(vm_instance_uuid=vm_instance_uuid, vcenter=vcenter)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table([response.results], _VM_DETAIL_COLUMNS)
