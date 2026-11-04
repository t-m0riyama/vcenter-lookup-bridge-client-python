import sys

import click

from vcenter_lookup_bridge_client import HealthcheckApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from vcenter_lookup_bridge_client.models.thread_pool_response_schema import (
    ThreadPoolResponseSchema,
)
from .formatters import output_api_error, output_json, output_retry_after, output_table
from .i18n import _

_HEALTHCHECK_COLUMNS = ["status", "vcenter_service_instances"]
_THREADPOOL_COLUMNS = [
    "status",
    "process_id",
    "total_tokens",
    "borrowed_tokens",
    "available_tokens",
    "tasks_waiting",
]


def _output_threadpool(ctx, response: ThreadPoolResponseSchema) -> None:
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table([response.results], _THREADPOOL_COLUMNS)


@click.group(
    "healthcheck",
    invoke_without_command=True,
    help=_("Service health check operations"),
)
@click.pass_context
def healthcheck(ctx):
    if ctx.invoked_subcommand is not None:
        return
    api = HealthcheckApi(ctx.obj["api_client"])
    try:
        response = api.get_service_status()
    except ApiException as e:
        output_api_error(e)
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table([response.results], _HEALTHCHECK_COLUMNS)


@healthcheck.command("threadpool", help=_("Check the AnyIO default thread pool status"))
@click.pass_context
def threadpool(ctx):
    api = HealthcheckApi(ctx.obj["api_client"])
    try:
        response = api.get_threadpool_status()
    except ApiException as e:
        # 503 のボディはスレッド枠スキーマ。表または JSON で出し、終了コード 1 にする
        if e.status == 503:
            response = e.data
            if response is None and e.body:
                try:
                    response = ThreadPoolResponseSchema.from_json(e.body)
                except Exception:
                    response = None
            if response is not None:
                _output_threadpool(ctx, response)
                output_retry_after(e)
                sys.exit(1)
        output_api_error(e)
        sys.exit(1)
    _output_threadpool(ctx, response)
