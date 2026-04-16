"""エラーハンドリング横断テスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS


@pytest.mark.unit
class TestErrorHandling:
    def test_api_exception_shows_status_and_message(self, cli_runner):
        """ApiException のステータスとメッセージがエラー出力に含まれる"""
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_cls.return_value.list_vms.side_effect = ApiException(status=404, reason="Not Found")
            result = cli_runner.invoke(cli, BASE_ARGS + ["vms", "list", "--vm-folders", "F1"])
        assert result.exit_code == 1
        assert "404" in result.output
        assert "Not Found" in result.output

    def test_api_exception_401_exit_code_1(self, cli_runner):
        """401 エラーで exit_code=1 が返される"""
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_service_status.side_effect = ApiException(status=401, reason="Unauthorized")
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck"])
        assert result.exit_code == 1
        assert "401" in result.output

    def test_api_exception_500_exit_code_1(self, cli_runner):
        """500 エラーで exit_code=1 が返される"""
        with patch("vcenter_lookup_bridge_client.cli.clusters.ClustersApi") as mock_cls:
            mock_cls.return_value.list_clusters.side_effect = ApiException(status=500, reason="Internal Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["clusters", "list"])
        assert result.exit_code == 1

    def test_no_error_on_successful_response(self, cli_runner):
        """正常レスポンスでは exit_code=0"""
        from tests.cli.conftest import make_healthcheck_response
        mock_resp = make_healthcheck_response()
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_service_status.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck"])
        assert result.exit_code == 0
