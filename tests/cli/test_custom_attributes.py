"""Custom-attributes サブコマンドのテスト"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_custom_attribute_list_response, make_custom_attribute_response


@pytest.mark.unit
class TestCustomAttributesList:
    def test_custom_attributes_list_success(self, cli_runner):
        """custom-attributes list が成功し、テーブル出力に属性と値が含まれる"""
        mock_resp = make_custom_attribute_list_response(
            [make_custom_attribute_response(name="owner", value="taro", object_name="vm01")]
        )
        with patch("vcenter_lookup_bridge_client.cli.custom_attributes.CustomAttributesApi") as mock_cls:
            mock_cls.return_value.list_custom_attributes.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["custom-attributes", "list"])
        assert result.exit_code == 0
        assert "object_type" in result.output
        assert "owner" in result.output
        assert "taro" in result.output

    def test_custom_attributes_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_custom_attribute_list_response()
        with patch("vcenter_lookup_bridge_client.cli.custom_attributes.CustomAttributesApi") as mock_cls:
            mock_cls.return_value.list_custom_attributes.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "custom-attributes", "list"])
        assert result.exit_code == 0
        assert "{" in result.output

    def test_custom_attributes_list_passes_options(self, cli_runner):
        """--object-type は Global のような任意の種別も API に渡される"""
        mock_resp = make_custom_attribute_list_response()
        with patch("vcenter_lookup_bridge_client.cli.custom_attributes.CustomAttributesApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_custom_attributes.return_value = mock_resp
            result = cli_runner.invoke(
                cli,
                BASE_ARGS + [
                    "custom-attributes", "list", "--object-type", "Global", "--object-name", "vm01",
                    "--object-id", "xxxx", "--offset", "1", "--max-results", "2", "--vcenter", "vcenter01",
                ],
            )
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_custom_attributes.call_args.kwargs
        assert call_kwargs == {
            "object_type": "Global",
            "object_name": "vm01",
            "object_id": "xxxx",
            "offset": 1,
            "max_results": 2,
            "vcenter": "vcenter01",
        }

    def test_custom_attributes_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.custom_attributes.CustomAttributesApi") as mock_cls:
            mock_cls.return_value.list_custom_attributes.side_effect = ApiException(status=404, reason="Not Found")
            result = cli_runner.invoke(cli, BASE_ARGS + ["custom-attributes", "list"])
        assert result.exit_code == 1
        assert "404" in result.output
