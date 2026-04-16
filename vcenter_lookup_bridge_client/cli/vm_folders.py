import sys

import click

from vcenter_lookup_bridge_client import VmFoldersApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table

_VM_FOLDER_COLUMNS = ["name", "vcenter", "datacenter", "path"]


@click.group()
def vm_folders():
    """仮想マシンフォルダ操作"""


@vm_folders.command("list")
@click.option("--vm-folders", "vm_folder_names", default=None, help="VMフォルダ名 (カンマ区切りで複数指定可)")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_vm_folders(ctx, vm_folder_names, offset, max_results, vcenter):
    """仮想マシンフォルダ一覧を取得します"""
    api = VmFoldersApi(ctx.obj["api_client"])
    folders = [f.strip() for f in vm_folder_names.split(",")] if vm_folder_names else None
    try:
        response = api.list_vm_folders(vm_folders=folders, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _VM_FOLDER_COLUMNS)
