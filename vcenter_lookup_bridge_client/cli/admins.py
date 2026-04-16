import sys

import click

from vcenter_lookup_bridge_client import AdminsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json
from .i18n import _


@click.group(help=_("Admin operations"))
def admins():
    pass


@admins.command("flush-caches", help=_("Clear all cached responses"))
@click.pass_context
def flush_caches(ctx):
    api = AdminsApi(ctx.obj["api_client"])
    try:
        response = api.flush_caches()
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        click.echo(f"success={response.success} message={response.message or ''}")


@admins.command("reset-ws-session", help=_("Clear down-mark for all vCenters"))
@click.pass_context
def reset_ws_session(ctx):
    api = AdminsApi(ctx.obj["api_client"])
    try:
        response = api.reset_ws_session()
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason), err=True)
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        click.echo(f"success={response.success} message={response.message or ''}")
