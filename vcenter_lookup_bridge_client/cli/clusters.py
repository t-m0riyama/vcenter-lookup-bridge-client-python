import sys

import click

from vcenter_lookup_bridge_client import ClustersApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table

_CLUSTER_COLUMNS = ["name", "vcenter", "datacenter", "num_hosts", "num_cpu_cores", "memory_size_mb"]


@click.group()
def clusters():
    """クラスタ操作"""


@clusters.command("list")
@click.option("--clusters", "cluster_names", default=None, help="クラスタ名 (カンマ区切りで複数指定可)")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_clusters(ctx, cluster_names, offset, max_results, vcenter):
    """クラスタ一覧を取得します"""
    api = ClustersApi(ctx.obj["api_client"])
    names = [n.strip() for n in cluster_names.split(",")] if cluster_names else None
    try:
        response = api.list_clusters(clusters=names, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _CLUSTER_COLUMNS)
