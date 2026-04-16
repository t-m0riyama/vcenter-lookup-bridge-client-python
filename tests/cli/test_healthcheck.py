"""Healthcheck サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_healthcheck_response


@pytest.mark.unit
class TestHealthcheck:
    def test_healthcheck_success(self, cli_runner):
        """healthcheck が成功し、status が出力される"""
        mock_resp = make_healthcheck_response()
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_service_status.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck"])
        assert result.exit_code == 0
        assert "status" in result.output

    def test_healthcheck_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_healthcheck_response()
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_service_status.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "healthcheck"])
        assert result.exit_code == 0
        assert "{" in result.output

    def test_healthcheck_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_service_status.side_effect = ApiException(status=503, reason="Service Unavailable")
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck"])
        assert result.exit_code == 1
        assert "503" in result.output
