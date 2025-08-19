# coding: utf-8

"""
vCenter Lookup Bridge API - Healthcheck APIテスト
"""

import pytest
from typing import Dict, Any

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.healthcheck_response_schema import (
    HealthcheckSchema,
)

@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "healthcheck_api"

@pytest.fixture
def api_instance(api_client):
    """Healthcheck APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.HealthcheckApi(api_client)


class TestHealthcheckApi:
    """Healthcheck API unit test"""

    def test_healthcheck(self, api_instance, api_dataset):
        """Healthcheck APIのテスト"""
        # APIを呼び出し
        response = api_instance.get_service_status()

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert results is not None
        assert isinstance(results, HealthcheckSchema)

        # 期待結果との比較
        expected_results = api_dataset.EXPECTED_HEALTHCHECK_STATUS["results"]
        assert results.status == expected_results["status"]
        assert (
            results.vcenter_service_instances
            == expected_results["vcenter_service_instances"]
        )

        print(f"✅ Healthcheck APIのテスト成功")
