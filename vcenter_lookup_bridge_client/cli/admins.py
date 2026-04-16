import sys

import click

from vcenter_lookup_bridge_client import AdminsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json


@click.group()
def admins():
    """管理操作"""


@admins.command("flush-caches")
@click.pass_context
def flush_caches(ctx):
    """キャッシュ済みの全レスポンスをクリアします"""
    api = AdminsApi(ctx.obj["api_client"])
    try:
        response = api.flush_caches()
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        click.echo(f"success={response.success} message={response.message or ''}")


@admins.command("reset-ws-session")
@click.pass_context
def reset_ws_session(ctx):
    """全 vCenter のダウンマークをクリアします"""
    api = AdminsApi(ctx.obj["api_client"])
    try:
        response = api.reset_ws_session()
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}", err=True)
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        click.echo(f"success={response.success} message={response.message or ''}")
