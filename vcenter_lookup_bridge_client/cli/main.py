import sys

import click
import urllib3

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.api_client import ApiClient
from vcenter_lookup_bridge_client.configuration import Configuration

from .vms import vms
from .hosts import hosts
from .clusters import clusters
from .datastores import datastores
from .portgroups import portgroups
from .vm_folders import vm_folders
from .vm_snapshots import vm_snapshots
from .events import events
from .alarms import alarms
from .vcenters import vcenters
from .admins import admins
from .healthcheck import healthcheck


@click.group()
@click.version_option(version=vcenter_lookup_bridge_client.__version__, prog_name="vlb")
@click.option(
    "--host",
    envvar="VLB_HOST",
    required=True,
    help="API サーバの URL (環境変数: VLB_HOST)",
)
@click.option(
    "--username",
    envvar="VLB_USERNAME",
    default="",
    show_default=False,
    help="Basic 認証のユーザー名 (環境変数: VLB_USERNAME)",
)
@click.option(
    "--password",
    envvar="VLB_PASSWORD",
    default="",
    show_default=False,
    help="Basic 認証のパスワード (環境変数: VLB_PASSWORD)",
)
@click.option(
    "--format",
    "output_format",
    type=click.Choice(["table", "json"]),
    default="table",
    show_default=True,
    help="出力フォーマット",
)
@click.option(
    "--no-verify-ssl",
    is_flag=True,
    default=False,
    help="SSL 証明書の検証を無効にする",
)
@click.pass_context
def cli(ctx, host, username, password, output_format, no_verify_ssl):
    """vCenter Lookup Bridge CLI (vlb)

    vCenter Lookup Bridge API に接続して仮想マシン・ホスト・クラスタ等の情報を取得します。

    接続情報は環境変数 VLB_HOST / VLB_USERNAME / VLB_PASSWORD で設定できます。
    """
    ctx.ensure_object(dict)
    config = Configuration(host=host, username=username, password=password)
    config.verify_ssl = not no_verify_ssl
    if not config.verify_ssl:
        urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
    ctx.obj["api_client"] = ApiClient(config)
    ctx.obj["format"] = output_format


cli.add_command(vms)
cli.add_command(hosts)
cli.add_command(clusters)
cli.add_command(datastores)
cli.add_command(portgroups)
cli.add_command(vm_folders, name="vm-folders")
cli.add_command(vm_snapshots, name="vm-snapshots")
cli.add_command(events)
cli.add_command(alarms)
cli.add_command(vcenters)
cli.add_command(admins)
cli.add_command(healthcheck)
