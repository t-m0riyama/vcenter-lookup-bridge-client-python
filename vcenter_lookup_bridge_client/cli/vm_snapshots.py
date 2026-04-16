import sys

import click

from vcenter_lookup_bridge_client import VmSnapshotsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table

_SNAPSHOT_COLUMNS = ["name", "instance_uuid", "vcenter", "vm_name", "create_time", "description"]


@click.group()
def vm_snapshots():
    """仮想マシンスナップショット操作"""


@vm_snapshots.command("list")
@click.option("--vm-folders", required=True, help="VMフォルダ名 (カンマ区切りで複数指定可)")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_vm_snapshots(ctx, vm_folders, offset, max_results, vcenter):
    """指定したフォルダ内の仮想マシンのスナップショット一覧を取得します"""
    api = VmSnapshotsApi(ctx.obj["api_client"])
    folders = [f.strip() for f in vm_folders.split(",")]
    try:
        response = api.list_vm_snapshots(vm_folders=folders, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _SNAPSHOT_COLUMNS)


@vm_snapshots.command("get")
@click.argument("vm_instance_uuid")
@click.option("--vcenter", required=True, help="vCenter 名")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.pass_context
def get_vm_snapshots(ctx, vm_instance_uuid, vcenter, offset, max_results):
    """インスタンス UUID を指定して仮想マシンのスナップショット一覧を取得します"""
    api = VmSnapshotsApi(ctx.obj["api_client"])
    try:
        response = api.get_vm_snapshots(vm_instance_uuid=vm_instance_uuid, vcenter=vcenter, offset=offset, max_results=max_results)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _SNAPSHOT_COLUMNS)
