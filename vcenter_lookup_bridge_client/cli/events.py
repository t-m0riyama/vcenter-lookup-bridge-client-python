import sys

import click

from vcenter_lookup_bridge_client import EventsApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_next_cursor, output_table
from .i18n import _

_EVENT_COLUMNS = ["key", "created_time", "event_type", "vcenter", "event_source", "user_name", "ip_address", "description"]


@click.group(help=_("Event operations"))
def events():
    pass


@events.command("list", help=_("List events"))
@click.option("--begin-time", default=None, help=_("Start time (ISO 8601)"))
@click.option("--end-time", default=None, help=_("End time (ISO 8601)"))
@click.option("--days-ago-begin", default=None, type=int, help=_("Start: number of days ago"))
@click.option("--days-ago-end", default=None, type=int, help=_("End: number of days ago"))
@click.option("--hours-ago-begin", default=None, type=int, help=_("Start: number of hours ago"))
@click.option("--hours-ago-end", default=None, type=int, help=_("End: number of hours ago"))
@click.option("--event-types", default=None, help=_("Event type(s) (comma-separated)"))
@click.option("--event-sources", default=None, help=_("Event source(s) (comma-separated)"))
@click.option("--user-names", default=None, help=_("Username(s) (comma-separated)"))
@click.option("--ip-addresses", default=None, help=_("IP address(es) (comma-separated)"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--cursor", default=None, help=_("Cursor for the next page (pagination.nextCursor of the previous page)"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_events(ctx, begin_time, end_time, days_ago_begin, days_ago_end,
                hours_ago_begin, hours_ago_end, event_types, event_sources,
                user_names, ip_addresses, offset, cursor, max_results, vcenter):
    if cursor and offset:
        raise click.UsageError(_("--cursor cannot be used with --offset"))
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
        response = api.list_events(**kwargs)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _EVENT_COLUMNS)
        output_next_cursor(response.pagination)
