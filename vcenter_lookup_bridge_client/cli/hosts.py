import sys

import click

from vcenter_lookup_bridge_client import HostsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table

_HOST_LIST_COLUMNS = ["name", "uuid", "vcenter", "datacenter", "status", "esxi_version", "num_cpu_cores", "memory_size_mb"]
_HOST_DETAIL_COLUMNS = ["name", "uuid", "vcenter", "datacenter", "cluster", "ip_address", "status", "power_state", "esxi_version", "cpu_model", "hardware_vendor", "hardware_model"]


@click.group()
def hosts():
    """ESXi ホスト操作"""


@hosts.command("list")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_hosts(ctx, offset, max_results, vcenter):
    """ESXi ホスト一覧を取得します"""
    api = HostsApi(ctx.obj["api_client"])
    try:
        response = api.list_hosts(offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _HOST_LIST_COLUMNS)


@hosts.command("get")
@click.argument("host_uuid")
@click.option("--vcenter", required=True, help="vCenter 名")
@click.pass_context
def get_host(ctx, host_uuid, vcenter):
    """ホスト UUID を指定して ESXi ホストの詳細情報を取得します"""
    api = HostsApi(ctx.obj["api_client"])
    try:
        response = api.get_host(host_uuid=host_uuid, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table([response.results], _HOST_DETAIL_COLUMNS)
