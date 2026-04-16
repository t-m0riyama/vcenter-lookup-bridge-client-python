import sys

import click

from vcenter_lookup_bridge_client import VcentersApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table

_VCENTER_COLUMNS = ["name", "host", "version"]


@click.group()
def vcenters():
    """vCenter 操作"""


@vcenters.command("list")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_vcenters(ctx, offset, max_results, vcenter):
    """接続先の vCenter 一覧を取得します"""
    api = VcentersApi(ctx.obj["api_client"])
    try:
        response = api.list_vcenters(offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _VCENTER_COLUMNS)
