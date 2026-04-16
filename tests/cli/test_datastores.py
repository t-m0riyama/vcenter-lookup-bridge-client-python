"""Datastores サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_datastore_list_response


@pytest.mark.unit
class TestDatastoresList:
    def test_datastores_list_success(self, cli_runner):
        """datastores list が成功し、テーブル出力にカラム名が含まれる"""
        mock_resp = make_datastore_list_response()
        with patch("vcenter_lookup_bridge_client.cli.datastores.DatastoresApi") as mock_cls:
            mock_cls.return_value.list_datastores.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["datastores", "list", "--tag-category", "cat1", "--tags", "tag1"]
            )
        assert result.exit_code == 0
        assert "name" in result.output

    def test_datastores_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_datastore_list_response()
        with patch("vcenter_lookup_bridge_client.cli.datastores.DatastoresApi") as mock_cls:
            mock_cls.return_value.list_datastores.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["--format", "json", "datastores", "list", "--tag-category", "cat1", "--tags", "tag1"]
            )
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_datastores_list_missing_tag_category(self, cli_runner):
        """--tag-category 省略時は exit_code=2"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["datastores", "list", "--tags", "tag1"])
        assert result.exit_code == 2

    def test_datastores_list_missing_tags(self, cli_runner):
        """--tags 省略時は exit_code=2"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["datastores", "list", "--tag-category", "cat1"])
        assert result.exit_code == 2

    def test_datastores_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.datastores.DatastoresApi") as mock_cls:
            mock_cls.return_value.list_datastores.side_effect = ApiException(status=404, reason="Not Found")
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["datastores", "list", "--tag-category", "cat1", "--tags", "tag1"]
            )
        assert result.exit_code == 1
        assert "404" in result.output
