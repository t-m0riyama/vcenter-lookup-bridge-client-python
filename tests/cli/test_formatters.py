"""フォーマッタのテスト (RED → GREEN)"""

import json
import pytest
from io import StringIO
from unittest.mock import MagicMock

from vcenter_lookup_bridge_client.cli.formatters import (
    output_api_error,
    output_json,
    output_next_cursor,
    output_table,
    output_truncated_warning,
)
from vcenter_lookup_bridge_client.exceptions import ApiException


@pytest.mark.unit
class TestOutputJson:
    def test_output_json_with_model_dump(self):
        """model_dump() を持つオブジェクトが JSON として出力される"""
        data = MagicMock()
        data.model_dump = MagicMock(return_value={"name": "test-vm", "status": "ok"})
        buf = StringIO()
        output_json(data, file=buf)
        result = json.loads(buf.getvalue())
        assert result["name"] == "test-vm"
        assert result["status"] == "ok"

    def test_output_json_list(self):
        """リストの各要素が JSON 配列として出力される"""
        items = [MagicMock(), MagicMock()]
        items[0].model_dump = MagicMock(return_value={"name": "vm1"})
        items[1].model_dump = MagicMock(return_value={"name": "vm2"})
        buf = StringIO()
        output_json(items, file=buf)
        result = json.loads(buf.getvalue())
        assert isinstance(result, list)
        assert result[0]["name"] == "vm1"
        assert result[1]["name"] == "vm2"

    def test_output_json_plain_dict(self):
        """通常の dict がそのまま JSON として出力される"""
        buf = StringIO()
        output_json({"key": "value"}, file=buf)
        result = json.loads(buf.getvalue())
        assert result["key"] == "value"

    def test_output_json_is_indented(self):
        """出力が整形 (indent=2) されている"""
        data = MagicMock()
        data.model_dump = MagicMock(return_value={"name": "vm"})
        buf = StringIO()
        output_json(data, file=buf)
        assert "\n" in buf.getvalue()


@pytest.mark.unit
class TestOutputTable:
    def test_output_table_with_data(self):
        """テーブル出力にヘッダと行が含まれる"""
        items = [MagicMock()]
        items[0].name = "test-vm"
        items[0].vcenter = "vcenter01"
        buf = StringIO()
        output_table(items, ["name", "vcenter"], file=buf)
        output = buf.getvalue()
        assert "name" in output
        assert "vcenter" in output
        assert "test-vm" in output
        assert "vcenter01" in output

    def test_output_table_empty_results(self):
        """空リストでもカラムヘッダーが出力される"""
        buf = StringIO()
        output_table([], ["name", "vcenter"], file=buf)
        output = buf.getvalue()
        assert "name" in output
        assert "vcenter" in output

    def test_output_table_multiple_rows(self):
        """複数行が正しく出力される"""
        items = [MagicMock(), MagicMock()]
        items[0].name = "vm1"
        items[0].vcenter = "vc1"
        items[1].name = "vm2"
        items[1].vcenter = "vc2"
        buf = StringIO()
        output_table(items, ["name", "vcenter"], file=buf)
        output = buf.getvalue()
        assert "vm1" in output
        assert "vm2" in output

    def test_output_table_none_attribute_shown_as_empty(self):
        """None 属性は空文字として表示される"""
        item = MagicMock()
        item.name = "vm1"
        item.vcenter = None
        buf = StringIO()
        output_table([item], ["name", "vcenter"], file=buf)
        assert "vm1" in buf.getvalue()


@pytest.mark.unit
class TestOutputTableStrColumns:
    def test_str_columns_keep_numeric_like_string(self):
        """str_columns に指定した列は、数値に見える値でも文字列のまま出力される"""
        item = MagicMock()
        item.key = "107.10"
        buf = StringIO()
        output_table([item], ["key"], file=buf, str_columns=["key"])
        assert "107.10" in buf.getvalue()

    def test_without_str_columns_parses_numbers(self):
        """str_columns を指定しない場合は従来どおり数値として整形される"""
        item = MagicMock()
        item.key = "107.10"
        buf = StringIO()
        output_table([item], ["key"], file=buf)
        assert "107.10" not in buf.getvalue()


@pytest.mark.unit
class TestOutputNextCursor:
    def test_output_next_cursor(self):
        """next_cursor がある場合に出力される"""
        pagination = MagicMock()
        pagination.next_cursor = "abc"
        buf = StringIO()
        output_next_cursor(pagination, file=buf)
        assert "abc" in buf.getvalue()

    def test_output_next_cursor_none(self):
        """next_cursor が None、または pagination が None の場合は何も出力しない"""
        pagination = MagicMock()
        pagination.next_cursor = None
        buf = StringIO()
        output_next_cursor(pagination, file=buf)
        output_next_cursor(None, file=buf)
        assert buf.getvalue() == ""


@pytest.mark.unit
class TestOutputApiError:
    def _output(self, capsys, e):
        output_api_error(e)
        return capsys.readouterr().out

    def test_detail_string(self, capsys):
        """detail が文字列の場合 (404 など) はそのまま表示される"""
        e = ApiException(status=404, reason="Not Found", body='{"detail":"指定した条件のタグは見つかりませんでした。"}')
        out = self._output(capsys, e)
        assert "Error 404: Not Found" in out
        assert "  指定した条件のタグは見つかりませんでした。" in out

    def test_detail_validation_errors(self, capsys):
        """detail が検証エラーの一覧の場合 (422) は、パラメータ名とメッセージが行ごとに表示される"""
        body = (
            '{"detail":[{"type":"literal_error","loc":["query","object_type"],"msg":"Input should be \'VirtualMachine\'"},'
            '{"type":"value_error","loc":["query"],"msg":"Value error, cursorの書式が不正です。"}]}'
        )
        out = self._output(capsys, ApiException(status=422, reason="Unprocessable Entity", body=body))
        assert "  object_type: Input should be 'VirtualMachine'" in out
        assert "  cursorの書式が不正です。" in out

    def test_without_body(self, capsys):
        """本文がない、または JSON でない場合はステータスのみ表示される"""
        out = self._output(capsys, ApiException(status=500, reason="Server Error"))
        out += self._output(capsys, ApiException(status=502, reason="Bad Gateway", body="<html>Bad Gateway</html>"))
        assert out.splitlines() == ["Error 500: Server Error", "Error 502: Bad Gateway"]


@pytest.mark.unit
class TestOutputTruncatedWarning:
    def test_truncated_with_message(self):
        """truncated が真なら、レスポンスのメッセージを出力する"""
        response = MagicMock()
        response.truncated = True
        response.message = "取得上限に達したvCenterがあります。"
        buf = StringIO()
        output_truncated_warning(response, file=buf)
        assert buf.getvalue().strip() == "取得上限に達したvCenterがあります。"

    def test_truncated_without_message(self):
        """メッセージがない場合は、既定の文言を出力する"""
        response = MagicMock()
        response.truncated = True
        response.message = None
        buf = StringIO()
        output_truncated_warning(response, file=buf)
        assert "truncated" in buf.getvalue()

    def test_not_truncated(self):
        """truncated が偽、または MagicMock のような真偽値でない値の場合は何も出力しない"""
        buf = StringIO()
        response = MagicMock()
        response.truncated = False
        output_truncated_warning(response, file=buf)
        output_truncated_warning(MagicMock(), file=buf)
        assert buf.getvalue() == ""

