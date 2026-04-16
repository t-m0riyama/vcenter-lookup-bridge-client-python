"""Clusters サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_cluster_list_response, make_cluster_response


@pytest.mark.unit
class TestClustersList:
    def test_clusters_list_success(self, cli_runner):
        """clusters list が成功し、テーブル出力にカラム名が含まれる"""
        mock_resp = make_cluster_list_response([make_cluster_response(name="Cluster01")])
        with patch("vcenter_lookup_bridge_client.cli.clusters.ClustersApi") as mock_cls:
            mock_cls.return_value.list_clusters.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["clusters", "list"])
        assert result.exit_code == 0
        assert "name" in result.output
        assert "Cluster01" in result.output

    def test_clusters_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_cluster_list_response()
        with patch("vcenter_lookup_bridge_client.cli.clusters.ClustersApi") as mock_cls:
            mock_cls.return_value.list_clusters.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "clusters", "list"])
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_clusters_list_with_filter(self, cli_runner):
        """--clusters オプションが API に渡される"""
        mock_resp = make_cluster_list_response()
        with patch("vcenter_lookup_bridge_client.cli.clusters.ClustersApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_clusters.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["clusters", "list", "--clusters", "C1,C2"])
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_clusters.call_args.kwargs
        assert call_kwargs.get("clusters") == ["C1", "C2"]

    def test_clusters_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.clusters.ClustersApi") as mock_cls:
            mock_cls.return_value.list_clusters.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["clusters", "list"])
        assert result.exit_code == 1
        assert "500" in result.output
