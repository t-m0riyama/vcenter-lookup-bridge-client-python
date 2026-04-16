"""CLI メインエントリポイントのテスト (RED → GREEN)"""

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from tests.cli.conftest import BASE_ARGS


@pytest.mark.unit
class TestCliMain:
    def test_cli_help(self, cli_runner):
        """vlb --help が exit_code=0 でサブコマンド一覧を含む出力を返す"""
        result = cli_runner.invoke(cli, ["--help"])
        assert result.exit_code == 0
        assert "vms" in result.output
        assert "hosts" in result.output
        assert "clusters" in result.output
        assert "healthcheck" in result.output

    def test_cli_version(self, cli_runner):
        """vlb --version が正しいバージョンを返す"""
        result = cli_runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "vlb" in result.output

    def test_cli_missing_host_shows_error(self, cli_runner):
        """--host も VLB_HOST も未設定時にエラーを返す"""
        result = cli_runner.invoke(cli, ["healthcheck"], env={})
        assert result.exit_code != 0
        assert "host" in result.output.lower() or "missing" in result.output.lower()

    def test_cli_subcommand_vms_help(self, cli_runner):
        """vlb vms --help が exit_code=0 を返す"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["vms", "--help"])
        assert result.exit_code == 0
        assert "list" in result.output
        assert "get" in result.output

    def test_cli_subcommand_hosts_help(self, cli_runner):
        """vlb hosts --help が exit_code=0 を返す"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["hosts", "--help"])
        assert result.exit_code == 0

    def test_cli_subcommand_healthcheck_help(self, cli_runner):
        """vlb healthcheck --help が exit_code=0 を返す"""
        result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck", "--help"])
        assert result.exit_code == 0
