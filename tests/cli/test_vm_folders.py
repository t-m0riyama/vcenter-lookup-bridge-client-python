"""VM Folders サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_vm_folder_list_response


@pytest.mark.unit
class TestVmFoldersList:
    def test_vm_folders_list_success(self, cli_runner):
        """vm-folders list が成功し、テーブル出力にカラム名が含まれる"""
        mock_resp = make_vm_folder_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vm_folders.VmFoldersApi") as mock_cls:
            mock_cls.return_value.list_vm_folders.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["vm-folders", "list"])
        assert result.exit_code == 0
        assert "name" in result.output

    def test_vm_folders_list_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_vm_folder_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vm_folders.VmFoldersApi") as mock_cls:
            mock_cls.return_value.list_vm_folders.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "vm-folders", "list"])
        assert result.exit_code == 0
        assert "{" in result.output or "[" in result.output

    def test_vm_folders_list_with_filter(self, cli_runner):
        """--vm-folders オプションが API に渡される"""
        mock_resp = make_vm_folder_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vm_folders.VmFoldersApi") as mock_cls:
            mock_instance = mock_cls.return_value
            mock_instance.list_vm_folders.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["vm-folders", "list", "--vm-folders", "F1,F2"])
        assert result.exit_code == 0
        call_kwargs = mock_instance.list_vm_folders.call_args.kwargs
        assert call_kwargs.get("vm_folders") == ["F1", "F2"]

    def test_vm_folders_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.vm_folders.VmFoldersApi") as mock_cls:
            mock_cls.return_value.list_vm_folders.side_effect = ApiException(status=404, reason="Not Found")
            result = cli_runner.invoke(cli, BASE_ARGS + ["vm-folders", "list"])
        assert result.exit_code == 1
        assert "404" in result.output
