import sys

import click

from vcenter_lookup_bridge_client import AlarmsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_ALARM_COLUMNS = ["name", "vcenter", "datacenter", "status", "alarm_source", "acknowledged", "created_time", "description"]


@click.group()
def alarms():
    """アラーム操作"""


@alarms.command("list")
@click.option("--begin-time", default=None, help="開始時間 (ISO 8601形式)")
@click.option("--end-time", default=None, help="終了時間 (ISO 8601形式)")
@click.option("--days-ago-begin", default=None, type=int, help="開始: 現在から遡る日数")
@click.option("--days-ago-end", default=None, type=int, help="終了: 現在から遡る日数")
@click.option("--hours-ago-begin", default=None, type=int, help="開始: 現在から遡る時間数")
@click.option("--hours-ago-end", default=None, type=int, help="終了: 現在から遡る時間数")
@click.option("--statuses", default=None, help="アラームステータス (カンマ区切りで複数指定可: red,yellow,green,gray)")
@click.option("--alarm-sources", default=None, help="アラームソース (カンマ区切りで複数指定可)")
@click.option("--acknowledged", default=None, type=click.Choice(["true", "false"]), help="確認済みフラグ")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_alarms(ctx, begin_time, end_time, days_ago_begin, days_ago_end,
                hours_ago_begin, hours_ago_end, statuses, alarm_sources,
                acknowledged, offset, max_results, vcenter):
    """アラーム一覧を取得します"""
    api = AlarmsApi(ctx.obj["api_client"])

    def _split(val):
        return [v.strip() for v in val.split(",")] if val else None

    ack_bool = {"true": True, "false": False}.get(acknowledged) if acknowledged else None

    kwargs = {
        "offset": offset,
        "max_results": max_results,
        "vcenter": vcenter,
        "statuses": _split(statuses),
        "alarm_sources": _split(alarm_sources),
        "acknowledged": ack_bool,
    }
    if begin_time or end_time:
        kwargs["begin_time"] = begin_time
        kwargs["end_time"] = end_time
    elif days_ago_begin is not None or days_ago_end is not None:
        kwargs["days_ago_begin"] = days_ago_begin
        kwargs["days_ago_end"] = days_ago_end
    elif hours_ago_begin is not None or hours_ago_end is not None:
        kwargs["hours_ago_begin"] = hours_ago_begin
        kwargs["hours_ago_end"] = hours_ago_end

    try:
        response = api.list_alarms(**kwargs)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _ALARM_COLUMNS)
