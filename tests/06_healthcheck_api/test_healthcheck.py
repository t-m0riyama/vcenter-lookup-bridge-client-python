# coding: utf-8

"""
vCenter Lookup Bridge API - Healthcheck APIテスト
"""

import os
import pytest
import importlib
from typing import Dict, Any

dataset_name = f"tests.test_datasets.{os.environ['TEST_DATASET']}"
api_server_settings = importlib.import_module(
    f"{dataset_name}.shared.api_server_settings"
)
api_dataset = importlib.import_module(f"{dataset_name}.healthcheck_api.settings")

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.configuration import Configuration
from vcenter_lookup_bridge_client.models.healthcheck_response_schema import (
    HealthcheckSchema,
)


@pytest.fixture
def api_config():
    """API設定のフィクスチャ"""
    return Configuration(**api_server_settings.VALID_API_SERVER_SETTINGS)


@pytest.fixture
def api_client(api_config):
    """APIクライアントのフィクスチャ"""
    return vcenter_lookup_bridge_client.ApiClient(api_config)


@pytest.fixture
def vcenters_api(api_client):
    """vCenters APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.HealthcheckApi(api_client)


class TestHealthcheckApi:
    """Healthcheck API unit test"""

    def test_healthcheck(self, vcenters_api):
        """Healthcheck APIのテスト"""
        # APIを呼び出し
        response = vcenters_api.get_service_status()

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
