import sys

import click

from vcenter_lookup_bridge_client import VmsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table

_VM_LIST_COLUMNS = ["name", "instance_uuid", "vcenter", "datacenter", "vm_folder", "num_cpu", "memory_size_mb"]
_VM_DETAIL_COLUMNS = ["name", "instance_uuid", "vcenter", "datacenter", "cluster", "esxi_hostname", "power_state", "num_cpu", "memory_size_mb", "ip_address"]


@click.group()
def vms():
    """仮想マシン (VM) 操作"""


@vms.command("list")
@click.option("--vm-folders", required=True, help="VMフォルダ名 (カンマ区切りで複数指定可)")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_vms(ctx, vm_folders, offset, max_results, vcenter):
    """指定したフォルダ内の仮想マシン一覧を取得します"""
    api = VmsApi(ctx.obj["api_client"])
    folders = [f.strip() for f in vm_folders.split(",")]
    try:
        response = api.list_vms(vm_folders=folders, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _VM_LIST_COLUMNS)


@vms.command("get")
@click.argument("vm_instance_uuid")
@click.option("--vcenter", required=True, help="vCenter 名")
@click.pass_context
def get_vm(ctx, vm_instance_uuid, vcenter):
    """インスタンス UUID を指定して仮想マシンの詳細情報を取得します"""
    api = VmsApi(ctx.obj["api_client"])
    try:
        response = api.get_vm(vm_instance_uuid=vm_instance_uuid, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table([response.results], _VM_DETAIL_COLUMNS)
