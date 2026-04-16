"""Portgroups サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_portgroup_list_response


@pytest.mark.unit
class TestPortgroupsList:
    def test_portgroups_list_success(self, cli_runner):
        """portgroups list が成功し、テーブル出力にカラム名が含まれる"""
        mock_resp = make_portgroup_list_response()
        with patch("vcenter_lookup_bridge_client.cli.portgroups.PortgroupsApi") as mock_cls:
            mock_cls.return_value.list_portgroups.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["portgroups", "list", "--tag-category", "cat1", "--tags", "tag1"]
            )
        assert result.exit_code == 0
        assert "name" in result.output

    def test_portgroups_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_portgroup_list_response()
        with patch("vcenter_lookup_bridge_client.cli.portgroups.PortgroupsApi") as mock_cls:
            mock_cls.return_value.list_portgroups.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["--format", "json", "portgroups", "list", "--tag-category", "cat1", "--tags", "tag1"]
            )
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_portgroups_list_missing_required(self, cli_runner):
        """必須オプション省略時は exit_code=2"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["portgroups", "list"])
        assert result.exit_code == 2

    def test_portgroups_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.portgroups.PortgroupsApi") as mock_cls:
            mock_cls.return_value.list_portgroups.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["portgroups", "list", "--tag-category", "cat1", "--tags", "tag1"]
            )
        assert result.exit_code == 1
        assert "500" in result.output
