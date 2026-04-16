"""VM Snapshots サブコマンドのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from tests.cli.conftest import BASE_ARGS, make_snapshot_list_response


@pytest.mark.unit
class TestVmSnapshotsList:
    def test_vm_snapshots_list_success(self, cli_runner):
        """vm-snapshots list が成功し、テーブル出力にカラム名が含まれる"""
        mock_resp = make_snapshot_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vm_snapshots.VmSnapshotsApi") as mock_cls:
            mock_cls.return_value.list_vm_snapshots.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["vm-snapshots", "list", "--vm-folders", "TestFolder"])
        assert result.exit_code == 0
        assert "name" in result.output

    def test_vm_snapshots_list_missing_vm_folders(self, cli_runner):
        """--vm-folders 省略時は exit_code=2"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["vm-snapshots", "list"])
        assert result.exit_code == 2

    def test_vm_snapshots_list_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.vm_snapshots.VmSnapshotsApi") as mock_cls:
            mock_cls.return_value.list_vm_snapshots.side_effect = ApiException(status=404, reason="Not Found")
            result = cli_runner.invoke(cli, BASE_ARGS + ["vm-snapshots", "list", "--vm-folders", "F1"])
        assert result.exit_code == 1
        assert "404" in result.output


@pytest.mark.unit
class TestVmSnapshotsGet:
    def test_vm_snapshots_get_success(self, cli_runner):
        """vm-snapshots get が成功し、スナップショット一覧が出力される"""
        mock_resp = make_snapshot_list_response()
        with patch("vcenter_lookup_bridge_client.cli.vm_snapshots.VmSnapshotsApi") as mock_cls:
            mock_cls.return_value.get_vm_snapshots.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["vm-snapshots", "get", "some-uuid", "--vcenter", "vc01"]
            )
        assert result.exit_code == 0
        assert "name" in result.output

    def test_vm_snapshots_get_missing_vcenter(self, cli_runner):
        """--vcenter 省略時は exit_code=2"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["vm-snapshots", "get", "some-uuid"])
        assert result.exit_code == 2
