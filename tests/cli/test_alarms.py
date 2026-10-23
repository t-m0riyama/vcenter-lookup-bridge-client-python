"""Alarms サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_pagination, make_alarm_list_response, make_alarm_response


@pytest.mark.unit
class TestAlarmsList:
    def test_alarms_list_with_days_ago(self, cli_runner):
        """--days-ago-begin 指定で alarms list が成功する"""
        mock_resp = make_alarm_list_response()
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["alarms", "list", "--days-ago-begin", "7"]
            )
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_alarms.call_args.kwargs
        assert call_kwargs.get("days_ago_begin") == 7

    def test_alarms_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_alarm_list_response()
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_cls.return_value.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "alarms", "list"])
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_alarms_list_with_status_filter(self, cli_runner):
        """--statuses フィルタが API に渡される"""
        mock_resp = make_alarm_list_response()
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list", "--statuses", "red,yellow"])
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_alarms.call_args.kwargs
        assert call_kwargs.get("statuses") == ["red", "yellow"]

    def test_alarms_list_acknowledged_filter(self, cli_runner):
        """--acknowledged true が bool で API に渡される"""
        mock_resp = make_alarm_list_response()
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list", "--acknowledged", "true"])
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_alarms.call_args.kwargs
        assert call_kwargs.get("acknowledged") is True

    def test_alarms_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_cls.return_value.list_alarms.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list"])
        assert result.exit_code == 1
        assert "500" in result.output


@pytest.mark.unit
class TestAlarmsListCursor:
    def test_alarms_list_cursor_passed_without_offset(self, cli_runner):
        """--cursor が API に渡され、offset は送られない"""
        mock_resp = make_alarm_list_response()
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list", "--days-ago-begin", "7", "--cursor", "abc"])
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_alarms.call_args.kwargs
        assert call_kwargs.get("cursor") == "abc"
        assert "offset" not in call_kwargs

    def test_alarms_list_without_cursor(self, cli_runner):
        """--cursor を指定しない場合は cursor を送らず、offset を送る"""
        mock_resp = make_alarm_list_response()
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list", "--offset", "5"])
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_alarms.call_args.kwargs
        assert "cursor" not in call_kwargs
        assert call_kwargs.get("offset") == 5

    def test_alarms_list_cursor_with_offset_error(self, cli_runner):
        """--cursor と --offset を同時に指定するとエラーになり、API は呼ばれない"""
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list", "--cursor", "abc", "--offset", "5"])
        assert result.exit_code != 0
        assert "--cursor" in result.output
        mock_cls.return_value.list_alarms.assert_not_called()

    def test_alarms_list_next_cursor_to_stderr(self, cli_runner):
        """次のページのカーソルは標準エラーに出力され、標準出力の表には混ざらない"""
        mock_resp = make_alarm_list_response(pagination=make_pagination(has_next=True, next_cursor="next-abc"))
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_cls.return_value.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list"])
        assert result.exit_code == 0
        assert "Next cursor: next-abc" in result.stderr
        assert "next-abc" not in result.stdout

    def test_alarms_list_no_next_cursor(self, cli_runner):
        """次のページがない場合はカーソルを出力しない"""
        mock_resp = make_alarm_list_response(pagination=make_pagination())
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_cls.return_value.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list"])
        assert result.exit_code == 0
        assert "Next cursor" not in result.stderr

    def test_alarms_list_json_does_not_print_cursor(self, cli_runner):
        """JSON 出力ではカーソルを別途出力しない (pagination.next_cursor に含まれるため)"""
        mock_resp = make_alarm_list_response(pagination=make_pagination(has_next=True, next_cursor="next-abc"))
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_cls.return_value.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "alarms", "list"])
        assert result.exit_code == 0
        assert "Next cursor" not in result.stderr

    def test_alarms_list_key_column(self, cli_runner):
        """テーブル出力に key 列が含まれる"""
        mock_resp = make_alarm_list_response([make_alarm_response(key="107.10")])
        with patch("vcenter_lookup_bridge_client.cli.alarms.AlarmsApi") as mock_cls:
            mock_cls.return_value.list_alarms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["alarms", "list"])
        assert result.exit_code == 0
        assert "key" in result.stdout
        assert "107.10" in result.stdout
