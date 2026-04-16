"""Admins サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_admin_response


@pytest.mark.unit
class TestAdmins:
    def test_flush_caches_success(self, cli_runner):
        """admins flush-caches が成功し、success が出力される"""
        mock_resp = make_admin_response()
        with patch("vcenter_lookup_bridge_client.cli.admins.AdminsApi") as mock_cls:
            mock_cls.return_value.flush_caches.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["admins", "flush-caches"])
        assert result.exit_code == 0
        assert "success" in result.output.lower() or "True" in result.output

    def test_flush_caches_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_admin_response()
        with patch("vcenter_lookup_bridge_client.cli.admins.AdminsApi") as mock_cls:
            mock_cls.return_value.flush_caches.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "admins", "flush-caches"])
        assert result.exit_code == 0
        assert "{" in result.output

    def test_flush_caches_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.admins.AdminsApi") as mock_cls:
            mock_cls.return_value.flush_caches.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["admins", "flush-caches"])
        assert result.exit_code == 1
        assert "500" in result.output

    def test_reset_ws_session_success(self, cli_runner):
        """admins reset-ws-session が成功し、success が出力される"""
        mock_resp = make_admin_response()
        with patch("vcenter_lookup_bridge_client.cli.admins.AdminsApi") as mock_cls:
            mock_cls.return_value.reset_ws_session.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["admins", "reset-ws-session"])
        assert result.exit_code == 0
        assert "success" in result.output.lower() or "True" in result.output

    def test_reset_ws_session_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.admins.AdminsApi") as mock_cls:
            mock_cls.return_value.reset_ws_session.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["admins", "reset-ws-session"])
        assert result.exit_code == 1
        assert "500" in result.output
