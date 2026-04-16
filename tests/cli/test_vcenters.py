"""Vcenters サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_vcenter_list_response


@pytest.mark.unit
class TestVcentersList:
    def test_vcenters_list_success(self, cli_runner):
        """vcenters list が成功し、テーブル出力にカラム名が含まれる"""
        mock_resp = make_vcenter_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vcenters.VcentersApi") as mock_cls:
            mock_cls.return_value.list_vcenters.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["vcenters", "list"])
        assert result.exit_code == 0
        assert "name" in result.output

    def test_vcenters_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_vcenter_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vcenters.VcentersApi") as mock_cls:
            mock_cls.return_value.list_vcenters.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "vcenters", "list"])
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_vcenters_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.vcenters.VcentersApi") as mock_cls:
            mock_cls.return_value.list_vcenters.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["vcenters", "list"])
        assert result.exit_code == 1
        assert "500" in result.output
