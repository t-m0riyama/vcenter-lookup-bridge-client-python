import sys

import click

from vcenter_lookup_bridge_client import AlarmsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_next_cursor, output_table
from .i18n import _

_ALARM_COLUMNS = ["key", "name", "vcenter", "datacenter", "status", "alarm_source", "acknowledged", "created_time", "description"]


@click.group(help=_("Alarm operations"))
def alarms():
    pass


@alarms.command("list", help=_("List alarms"))
@click.option("--begin-time", default=None, help=_("Start time (ISO 8601)"))
@click.option("--end-time", default=None, help=_("End time (ISO 8601)"))
@click.option("--days-ago-begin", default=None, type=int, help=_("Start: number of days ago"))
@click.option("--days-ago-end", default=None, type=int, help=_("End: number of days ago"))
@click.option("--hours-ago-begin", default=None, type=int, help=_("Start: number of hours ago"))
@click.option("--hours-ago-end", default=None, type=int, help=_("End: number of hours ago"))
@click.option("--statuses", default=None, help=_("Alarm status(es) (comma-separated: red,yellow,green,gray)"))
@click.option("--alarm-sources", default=None, help=_("Alarm source(s) (comma-separated)"))
@click.option("--acknowledged", default=None, type=click.Choice(["true", "false"]), help=_("Acknowledged flag"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--cursor", default=None, help=_("Cursor for the next page (pagination.nextCursor of the previous page)"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_alarms(ctx, begin_time, end_time, days_ago_begin, days_ago_end,
                hours_ago_begin, hours_ago_end, statuses, alarm_sources,
                acknowledged, offset, cursor, max_results, vcenter):
    if cursor and offset:
        raise click.UsageError(_("--cursor cannot be used with --offset"))
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
    # cursorはoffsetと同時に指定できないため、cursorを指定した場合はoffsetを送らない
    if cursor:
        kwargs["cursor"] = cursor
        del kwargs["offset"]
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
        output_table(response.results, _ALARM_COLUMNS, str_columns=["key"])
        output_next_cursor(response.pagination)
