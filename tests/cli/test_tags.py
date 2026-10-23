"""Tags サブコマンドのテスト"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_tag_list_response, make_tag_response


@pytest.mark.unit
class TestTagsList:
    def test_tags_list_success(self, cli_runner):
        """tags list が成功し、テーブル出力にタグが含まれる"""
        mock_resp = make_tag_list_response([make_tag_response(name="tag-a", tag_category="cat-a")])
        with patch("vcenter_lookup_bridge_client.cli.tags.TagsApi") as mock_cls:
            mock_cls.return_value.list_tags.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["tags", "list"])
        assert result.exit_code == 0
        assert "tag_category" in result.output
        assert "tag-a" in result.output
        assert "cat-a" in result.output

    def test_tags_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_tag_list_response()
        with patch("vcenter_lookup_bridge_client.cli.tags.TagsApi") as mock_cls:
            mock_cls.return_value.list_tags.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "tags", "list"])
        assert result.exit_code == 0
        assert "{" in result.output

    def test_tags_list_passes_options(self, cli_runner):
        """割り当ての問い合わせのオプションが API に渡される"""
        mock_resp = make_tag_list_response()
        with patch("vcenter_lookup_bridge_client.cli.tags.TagsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_tags.return_value = mock_resp
            result = cli_runner.invoke(
                cli,
                BASE_ARGS + [
                    "tags", "list", "--tag-category", "cat1", "--object-type", "VirtualMachine",
                    "--object-name", "vm01", "--object-id", "xxxx", "--offset", "10",
                    "--max-results", "20", "--vcenter", "vcenter01",
                ],
            )
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_tags.call_args.kwargs
        assert call_kwargs == {
            "tag_category": "cat1",
            "object_type": "VirtualMachine",
            "object_name": "vm01",
            "object_id": "xxxx",
            "offset": 10,
            "max_results": 20,
            "vcenter": "vcenter01",
        }

    def test_tags_list_invalid_object_type(self, cli_runner):
        """サポート外の --object-type は CLI 側でエラーになる"""
        with patch("vcenter_lookup_bridge_client.cli.tags.TagsApi") as mock_cls:
            result = cli_runner.invoke(cli, BASE_ARGS + ["tags", "list", "--object-type", "Folder"])
        assert result.exit_code != 0
        mock_cls.return_value.list_tags.assert_not_called()

    def test_tags_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.tags.TagsApi") as mock_cls:
            mock_cls.return_value.list_tags.side_effect = ApiException(status=404, reason="Not Found")
            result = cli_runner.invoke(cli, BASE_ARGS + ["tags", "list"])
        assert result.exit_code == 1
        assert "404" in result.output

    def test_tags_list_api_error_shows_detail(self, cli_runner):
        """422 のとき、サーバが返した detail の理由が表示される"""
        body = '{"detail":[{"type":"value_error","loc":["query"],"msg":"Value error, object_typeを指定する場合、object_nameまたはobject_idを指定してください。"}]}'
        with patch("vcenter_lookup_bridge_client.cli.tags.TagsApi") as mock_cls:
            mock_cls.return_value.list_tags.side_effect = ApiException(status=422, reason="Unprocessable Entity", body=body)
            result = cli_runner.invoke(cli, BASE_ARGS + ["tags", "list", "--object-type", "Datastore"])
        assert result.exit_code == 1
        assert "422" in result.output
        assert "object_typeを指定する場合、object_nameまたはobject_idを指定してください。" in result.output
        assert "Value error" not in result.output

