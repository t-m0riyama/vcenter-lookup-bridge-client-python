"""Tag-categories サブコマンドのテスト"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_tag_category_list_response, make_tag_category_response


@pytest.mark.unit
class TestTagCategoriesList:
    def test_tag_categories_list_success(self, cli_runner):
        """tag-categories list が成功し、テーブル出力にカテゴリが含まれる"""
        mock_resp = make_tag_category_list_response([make_tag_category_response(name="cat-a", cardinality="MULTIPLE")])
        with patch("vcenter_lookup_bridge_client.cli.tag_categories.TagCategoriesApi") as mock_cls:
            mock_cls.return_value.list_tag_categories.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["tag-categories", "list"])
        assert result.exit_code == 0
        assert "cardinality" in result.output
        assert "cat-a" in result.output
        assert "MULTIPLE" in result.output

    def test_tag_categories_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_tag_category_list_response()
        with patch("vcenter_lookup_bridge_client.cli.tag_categories.TagCategoriesApi") as mock_cls:
            mock_cls.return_value.list_tag_categories.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "tag-categories", "list"])
        assert result.exit_code == 0
        assert "{" in result.output

    def test_tag_categories_list_passes_options(self, cli_runner):
        """ページングと vCenter のオプションが API に渡される"""
        mock_resp = make_tag_category_list_response()
        with patch("vcenter_lookup_bridge_client.cli.tag_categories.TagCategoriesApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_tag_categories.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["tag-categories", "list", "--offset", "5", "--max-results", "10", "--vcenter", "vcenter01"]
            )
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_tag_categories.call_args.kwargs
        assert call_kwargs == {"offset": 5, "max_results": 10, "vcenter": "vcenter01"}

    def test_tag_categories_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.tag_categories.TagCategoriesApi") as mock_cls:
            mock_cls.return_value.list_tag_categories.side_effect = ApiException(status=500, reason="Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["tag-categories", "list"])
        assert result.exit_code == 1
        assert "500" in result.output
