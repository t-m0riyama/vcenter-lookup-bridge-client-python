"""Events サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_event_list_response


@pytest.mark.unit
class TestEventsList:
    def test_events_list_with_days_ago(self, cli_runner):
        """--days-ago-begin 指定で events list が成功する"""
        mock_resp = make_event_list_response()
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_events.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["events", "list", "--days-ago-begin", "7", "--days-ago-end", "0"]
            )
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_events.call_args.kwargs
        assert call_kwargs.get("days_ago_begin") == 7

    def test_events_list_with_time_range(self, cli_runner):
        """--begin-time / --end-time 指定で events list が成功する"""
        mock_resp = make_event_list_response()
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_events.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["events", "list", "--begin-time", "2026-04-01T00:00:00Z", "--end-time", "2026-04-16T00:00:00Z"]
            )
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_events.call_args.kwargs
        assert call_kwargs.get("begin_time") == "2026-04-01T00:00:00Z"

    def test_events_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_event_list_response()
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "events", "list"])
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_events_list_with_filters(self, cli_runner):
        """--event-types / --user-names フィルタが API に渡される"""
        mock_resp = make_event_list_response()
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_events.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["events", "list", "--event-types", "VmPoweredOnEvent,VmPoweredOffEvent", "--user-names", "admin"]
            )
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_events.call_args.kwargs
        assert call_kwargs.get("event_types") == ["VmPoweredOnEvent", "VmPoweredOffEvent"]
        assert call_kwargs.get("user_names") == ["admin"]

    def test_events_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list"])
        assert result.exit_code == 1
        assert "500" in result.output
