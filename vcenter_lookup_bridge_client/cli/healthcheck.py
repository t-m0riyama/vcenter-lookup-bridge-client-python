import sys

import click

from vcenter_lookup_bridge_client import HealthcheckApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table

_HEALTHCHECK_COLUMNS = ["status", "vcenter_service_instances"]


@click.command("healthcheck")
@click.pass_context
def healthcheck(ctx):
    """サービスのヘルスチェックを実行します"""
    api = HealthcheckApi(ctx.obj["api_client"])
    try:
        response = api.get_service_status()
    except ApiException as e:
        click.echo(f"Error {e.status}: {e.reason}")
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table([response.results], _HEALTHCHECK_COLUMNS)
