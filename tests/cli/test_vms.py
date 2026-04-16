"""VMs サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch, MagicMock

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_vm_list_response, make_vm_get_response, make_vm_detail_response


@pytest.mark.unit
class TestVmsList:
    def test_vms_list_success(self, cli_runner):
        """vms list が成功し、テーブル出力にカラム名が含まれる"""
        mock_resp = make_vm_list_response([])
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_cls.return_value.list_vms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["vms", "list", "--vm-folders", "TestFolder"])
        assert result.exit_code == 0
        assert "name" in result.output

    def test_vms_list_returns_results(self, cli_runner):
        """vms list が結果を出力する"""
        from tests.cli.conftest import make_vm_response
        mock_resp = make_vm_list_response([make_vm_response(name="my-vm")])
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_cls.return_value.list_vms.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["vms", "list", "--vm-folders", "TestFolder"])
        assert result.exit_code == 0
        assert "my-vm" in result.output

    def test_vms_list_json_format(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_vm_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_cls.return_value.list_vms.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["--format", "json", "vms", "list", "--vm-folders", "TestFolder"]
            )
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_vms_list_missing_vm_folders(self, cli_runner):
        """--vm-folders 省略時は exit_code=2 (click missing required option)"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["vms", "list"])
        assert result.exit_code == 2
        assert "vm-folders" in result.output.lower() or "missing" in result.output.lower()

    def test_vms_list_passes_vcenter_option(self, cli_runner):
        """--vcenter オプションが API に渡される"""
        mock_resp = make_vm_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_vms.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["vms", "list", "--vm-folders", "F1", "--vcenter", "vc01"]
            )
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_vms.call_args.kwargs
        assert call_kwargs.get("vcenter") == "vc01"

    def test_vms_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1 でエラーメッセージが出力される"""
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_cls.return_value.list_vms.side_effect = ApiException(status=500, reason="Internal Server Error")
            result = cli_runner.invoke(cli, BASE_ARGS + ["vms", "list", "--vm-folders", "F1"])
        assert result.exit_code == 1
        assert "500" in result.output


@pytest.mark.unit
class TestVmsGet:
    def test_vms_get_success(self, cli_runner):
        """vms get が成功し、詳細情報が出力される"""
        mock_resp = make_vm_get_response(make_vm_detail_response(name="detail-vm"))
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_cls.return_value.get_vm.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["vms", "get", "some-uuid", "--vcenter", "vc01"]
            )
        assert result.exit_code == 0
        assert "name" in result.output

    def test_vms_get_json_format(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_vm_get_response()
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_cls.return_value.get_vm.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["--format", "json", "vms", "get", "some-uuid", "--vcenter", "vc01"]
            )
        assert result.exit_code == 0
        assert "{" in result.output

    def test_vms_get_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1 でエラーメッセージが出力される"""
        with patch("vcenter_lookup_bridge_client.cli.vms.VmsApi") as mock_cls:
            mock_cls.return_value.get_vm.side_effect = ApiException(status=404, reason="Not Found")
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["vms", "get", "bad-uuid", "--vcenter", "vc01"]
            )
        assert result.exit_code == 1
        assert "404" in result.output

    def test_vms_get_missing_vcenter(self, cli_runner):
        """--vcenter 省略時は exit_code=2"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["vms", "get", "some-uuid"])
        assert result.exit_code == 2
