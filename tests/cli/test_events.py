"""Events サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_pagination, make_event_list_response, make_event_response


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


@pytest.mark.unit
class TestEventsListCursor:
    def test_events_list_cursor_passed_without_offset(self, cli_runner):
        """--cursor が API に渡され、offset は送られない"""
        mock_resp = make_event_list_response()
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list", "--days-ago-begin", "7", "--cursor", "abc"])
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_events.call_args.kwargs
        assert call_kwargs.get("cursor") == "abc"
        assert "offset" not in call_kwargs

    def test_events_list_without_cursor(self, cli_runner):
        """--cursor を指定しない場合は cursor を送らず、offset を送る"""
        mock_resp = make_event_list_response()
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list", "--offset", "5"])
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_events.call_args.kwargs
        assert "cursor" not in call_kwargs
        assert call_kwargs.get("offset") == 5

    def test_events_list_cursor_with_offset_error(self, cli_runner):
        """--cursor と --offset を同時に指定するとエラーになり、API は呼ばれない"""
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list", "--cursor", "abc", "--offset", "5"])
        assert result.exit_code != 0
        assert "--cursor" in result.output
        mock_cls.return_value.list_events.assert_not_called()

    def test_events_list_next_cursor_to_stderr(self, cli_runner):
        """次のページのカーソルは標準エラーに出力され、標準出力の表には混ざらない"""
        mock_resp = make_event_list_response(pagination=make_pagination(has_next=True, next_cursor="next-abc"))
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list"])
        assert result.exit_code == 0
        assert "Next cursor: next-abc" in result.stderr
        assert "next-abc" not in result.stdout

    def test_events_list_no_next_cursor(self, cli_runner):
        """次のページがない場合はカーソルを出力しない"""
        mock_resp = make_event_list_response(pagination=make_pagination())
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list"])
        assert result.exit_code == 0
        assert "Next cursor" not in result.stderr

    def test_events_list_json_does_not_print_cursor(self, cli_runner):
        """JSON 出力ではカーソルを別途出力しない (pagination.next_cursor に含まれるため)"""
        mock_resp = make_event_list_response(pagination=make_pagination(has_next=True, next_cursor="next-abc"))
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "events", "list"])
        assert result.exit_code == 0
        assert "Next cursor" not in result.stderr

    def test_events_list_key_column(self, cli_runner):
        """テーブル出力に key 列が含まれる"""
        mock_resp = make_event_list_response([make_event_response(key=98765)])
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list"])
        assert result.exit_code == 0
        assert "key" in result.stdout
        assert "98765" in result.stdout

    def test_events_list_message_column(self, cli_runner):
        """テーブル出力にイベントのメッセージ(message列)が表示される"""
        mock_resp = make_event_list_response([make_event_response(message="User admin logged in")])
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list"])
        assert result.exit_code == 0
        assert "message" in result.stdout
        assert "User admin logged in" in result.stdout


@pytest.mark.unit
class TestEventsListTruncated:
    def test_events_list_truncated_warning_to_stderr(self, cli_runner):
        """取得上限で打ち切られた場合、サーバのメッセージが標準エラーに出力される"""
        mock_resp = make_event_list_response(truncated=True, message="取得上限に達したvCenter(vcenter01)があります。")
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list"])
        assert result.exit_code == 0
        assert "取得上限に達したvCenter(vcenter01)があります。" in result.stderr
        assert "取得上限" not in result.stdout

    def test_events_list_not_truncated(self, cli_runner):
        """打ち切られていない場合は、メッセージを出力しない"""
        mock_resp = make_event_list_response(truncated=False, message="2件のイベントを取得しました。")
        with patch("vcenter_lookup_bridge_client.cli.events.EventsApi") as mock_cls:
            mock_cls.return_value.list_events.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["events", "list"])
        assert result.exit_code == 0
        assert result.stderr == ""

