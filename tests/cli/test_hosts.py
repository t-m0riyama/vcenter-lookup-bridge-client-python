"""Hosts サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_host_list_response, make_host_get_response, make_host_detail_response


@pytest.mark.unit
class TestHostsList:
    def test_hosts_list_success(self, cli_runner):
        """hosts list が成功し、テーブル出力にカラム名が含まれる"""
        mock_resp = make_host_list_response()
        with patch("vcenter_lookup_bridge_client.cli.hosts.HostsApi") as mock_cls:
            mock_cls.return_value.list_hosts.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["hosts", "list"])
        assert result.exit_code == 0
        assert "name" in result.output

    def test_hosts_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_host_list_response()
        with patch("vcenter_lookup_bridge_client.cli.hosts.HostsApi") as mock_cls:
            mock_cls.return_value.list_hosts.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "hosts", "list"])
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_hosts_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.hosts.HostsApi") as mock_cls:
            mock_cls.return_value.list_hosts.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["hosts", "list"])
        assert result.exit_code == 1
        assert "500" in result.output


@pytest.mark.unit
class TestHostsGet:
    def test_hosts_get_success(self, cli_runner):
        """hosts get が成功し、詳細情報が出力される"""
        mock_resp = make_host_get_response(make_host_detail_response(name="esxi01"))
        with patch("vcenter_lookup_bridge_client.cli.hosts.HostsApi") as mock_cls:
            mock_cls.return_value.get_host.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["hosts", "get", "some-uuid", "--vcenter", "vc01"])
        assert result.exit_code == 0
        assert "name" in result.output

    def test_hosts_get_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.hosts.HostsApi") as mock_cls:
            mock_cls.return_value.get_host.side_effect = ApiException(status=404, reason="Not Found")
            result = cli_runner.invoke(cli, BASE_ARGS + ["hosts", "get", "bad-uuid", "--vcenter", "vc01"])
        assert result.exit_code == 1
        assert "404" in result.output

    def test_hosts_get_missing_vcenter(self, cli_runner):
        """--vcenter 省略時は exit_code=2"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["hosts", "get", "some-uuid"])
        assert result.exit_code == 2
