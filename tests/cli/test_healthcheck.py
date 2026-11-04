"""Healthcheck サブコマンドのテスト (RED → GREEN)"""

import json

import pytest
from unittest.mock import patch

from vcenter_lookup_bridge_client.cli.main import cli
from vcenter_lookup_bridge_client.exceptions import ApiException
from vcenter_lookup_bridge_client.models.thread_pool_response_schema import (
    ThreadPoolResponseSchema,
)
from tests.cli.conftest import (
    BASE_ARGS,
    make_healthcheck_response,
    make_threadpool_response,
)


@pytest.mark.unit
class TestHealthcheck:
    def test_healthcheck_success(self, cli_runner):
        """healthcheck が成功し、status が出力される"""
        mock_resp = make_healthcheck_response()
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_service_status.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck"])
        assert result.exit_code == 0
        assert "status" in result.output

    def test_healthcheck_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_healthcheck_response()
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_service_status.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["--format", "json", "healthcheck"])
        assert result.exit_code == 0
        assert "{" in result.output

    def test_healthcheck_api_error(self, cli_runner):
        """API 例外発生時 exit_code=1"""
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_service_status.side_effect = ApiException(status=503, reason="Service Unavailable")
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck"])
        assert result.exit_code == 1
        assert "503" in result.output


@pytest.mark.unit
class TestHealthcheckThreadpool:
    def test_threadpool_success(self, cli_runner):
        """healthcheck threadpool が成功し、status が出力される"""
        mock_resp = make_threadpool_response()
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_threadpool_status.return_value = mock_resp
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck", "threadpool"])
        assert result.exit_code == 0
        assert "status" in result.output
        assert "ok" in result.output

    def test_threadpool_json(self, cli_runner):
        """--format json で JSON が出力される"""
        mock_resp = make_threadpool_response()
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_threadpool_status.return_value = mock_resp
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["--format", "json", "healthcheck", "threadpool"]
            )
        assert result.exit_code == 0
        assert "{" in result.output

    def test_threadpool_saturated_shows_body(self, cli_runner):
        """503 のとき body から status=saturated を表示し、exit_code=1"""
        body = json.dumps(
            {
                "results": {
                    "status": "saturated",
                    "process_id": 99,
                    "total_tokens": 40,
                    "borrowed_tokens": 40,
                    "available_tokens": 0,
                    "tasks_waiting": 3,
                },
                "success": False,
                "partialFailure": False,
                "message": "スレッド枠に空きがありません",
                "timestamp": "2026-11-04T12:00:00.000000+09:00",
            }
        )
        exc = ApiException(status=503, reason="Service Unavailable", body=body)
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_threadpool_status.side_effect = exc
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck", "threadpool"])
        assert result.exit_code == 1
        assert "saturated" in result.output
        # available_tokens=0 が空セルにならないこと
        data_line = next(line for line in result.stdout.splitlines() if "saturated" in line)
        assert "0" in data_line.split()

    def test_threadpool_saturated_uses_deserialized_data(self, cli_runner):
        """本番経路と同様、e.data に復元済みモデルがある場合も表示する"""
        response = ThreadPoolResponseSchema.from_dict(
            {
                "results": {
                    "status": "saturated",
                    "process_id": 99,
                    "total_tokens": 40,
                    "borrowed_tokens": 40,
                    "available_tokens": 0,
                    "tasks_waiting": 3,
                },
                "success": False,
                "partialFailure": False,
                "message": "スレッド枠に空きがありません",
                "timestamp": "2026-11-04T12:00:00.000000+09:00",
            }
        )
        exc = ApiException(status=503, reason="Service Unavailable")
        exc.data = response
        exc.headers = {"Retry-After": "1"}
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_threadpool_status.side_effect = exc
            result = cli_runner.invoke(cli, BASE_ARGS + ["healthcheck", "threadpool"])
        assert result.exit_code == 1
        assert "saturated" in result.stdout
        assert "Retry-After: 1" in result.stderr
        assert "Retry-After" not in result.stdout

    def test_threadpool_saturated_json_keeps_stdout_parseable(self, cli_runner):
        """--format json のとき Retry-After は stderr に出し、stdout の JSON を壊さない"""
        response = ThreadPoolResponseSchema.from_dict(
            {
                "results": {
                    "status": "saturated",
                    "process_id": 99,
                    "total_tokens": 40,
                    "borrowed_tokens": 40,
                    "available_tokens": 0,
                    "tasks_waiting": 3,
                },
                "success": False,
                "partialFailure": False,
                "message": "スレッド枠に空きがありません",
                "timestamp": "2026-11-04T12:00:00.000000+09:00",
            }
        )
        exc = ApiException(status=503, reason="Service Unavailable")
        exc.data = response
        exc.headers = {"Retry-After": "1"}
        with patch("vcenter_lookup_bridge_client.cli.healthcheck.HealthcheckApi") as mock_cls:
            mock_cls.return_value.get_threadpool_status.side_effect = exc
            result = cli_runner.invoke(
                cli, BASE_ARGS + ["--format", "json", "healthcheck", "threadpool"]
            )
        assert result.exit_code == 1
        parsed = json.loads(result.stdout)
        assert parsed["results"]["status"] == "saturated"
        assert "Retry-After: 1" in result.stderr
