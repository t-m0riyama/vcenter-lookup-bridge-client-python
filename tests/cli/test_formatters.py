"""フォーマッタのテスト (RED → GREEN)"""

import json
import pytest
from io import StringIO
from unittest.mock import MagicMock

from vcenter_lookup_bridge_client.cli.formatters import output_json, output_table


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
