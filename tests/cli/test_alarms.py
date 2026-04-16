"""Alarms サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_alarm_list_response


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
