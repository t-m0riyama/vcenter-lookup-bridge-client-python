import sys

import click

from vcenter_lookup_bridge_client import PortgroupsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table

_PORTGROUP_COLUMNS = ["name", "vcenter", "datacenter", "vlan_id", "vswitch_name"]


@click.group()
def portgroups():
    """ポートグループ操作"""


@portgroups.command("list")
@click.option("--tag-category", required=True, help="タグのカテゴリ名")
@click.option("--tags", required=True, help="タグ名 (カンマ区切りで複数指定可)")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_portgroups(ctx, tag_category, tags, offset, max_results, vcenter):
    """タグを指定してポートグループ一覧を取得します"""
    api = PortgroupsApi(ctx.obj["api_client"])
    tag_list = [t.strip() for t in tags.split(",")]
    try:
        response = api.list_portgroups(tag_category=tag_category, tags=tag_list, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _PORTGROUP_COLUMNS)
