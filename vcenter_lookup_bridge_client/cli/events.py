import sys

import click

from vcenter_lookup_bridge_client import EventsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_EVENT_COLUMNS = ["created_time", "event_type", "vcenter", "event_source", "user_name", "ip_address", "description"]


@click.group()
def events():
    """イベント操作"""


@events.command("list")
@click.option("--begin-time", default=None, help="開始時間 (ISO 8601形式)")
@click.option("--end-time", default=None, help="終了時間 (ISO 8601形式)")
@click.option("--days-ago-begin", default=None, type=int, help="開始: 現在から遡る日数")
@click.option("--days-ago-end", default=None, type=int, help="終了: 現在から遡る日数")
@click.option("--hours-ago-begin", default=None, type=int, help="開始: 現在から遡る時間数")
@click.option("--hours-ago-end", default=None, type=int, help="終了: 現在から遡る時間数")
@click.option("--event-types", default=None, help="イベント種別 (カンマ区切りで複数指定可)")
@click.option("--event-sources", default=None, help="イベントソース (カンマ区切りで複数指定可)")
@click.option("--user-names", default=None, help="ユーザー名 (カンマ区切りで複数指定可)")
@click.option("--ip-addresses", default=None, help="IPアドレス (カンマ区切りで複数指定可)")
@click.option("--offset", default=0, show_default=True, help="取得開始位置")
@click.option("--max-results", default=100, show_default=True, help="最大取得件数")
@click.option("--vcenter", default=None, help="vCenter 名")
@click.pass_context
def list_events(ctx, begin_time, end_time, days_ago_begin, days_ago_end,
                hours_ago_begin, hours_ago_end, event_types, event_sources,
                user_names, ip_addresses, offset, max_results, vcenter):
    """イベント一覧を取得します"""
    api = EventsApi(ctx.obj["api_client"])

    def _split(val):
        return [v.strip() for v in val.split(",")] if val else None

    kwargs = {
        "offset": offset,
        "max_results": max_results,
        "vcenter": vcenter,
        "event_types": _split(event_types),
        "event_sources": _split(event_sources),
        "user_names": _split(user_names),
        "ip_addresses": _split(ip_addresses),
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
        response = api.list_events(**kwargs)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _EVENT_COLUMNS)
