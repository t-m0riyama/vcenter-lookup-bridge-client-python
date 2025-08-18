# coding: utf-8

"""
vCenter Lookup Bridge API - ADMINS API キャッシュ管理テスト
"""

import os
import pydantic
import pytest
import importlib
from typing import Dict, Any

dataset_name = f"tests.test_datasets.{os.environ['TEST_DATASET']}"
api_server_settings = importlib.import_module(
    f"{dataset_name}.shared.api_server_settings"
)
api_dataset = importlib.import_module(f"{dataset_name}.admins_api.settings")

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.configuration import Configuration
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.admin_response_schema import (
    AdminResponseSchema,
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
def admins_api(api_client):
    """Admins APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.AdminsApi(api_client)


class TestAdminsApi:
    """Admins API Cache management unit test"""

    def test_flush_cache_success(self, admins_api):
        """キャッシュクリアの成功テスト"""
        # APIを呼び出し
        response = admins_api.flush_caches()

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is api_dataset.EXPECTED_FLUSH_CACHE["success"]
        assert response.message == api_dataset.EXPECTED_FLUSH_CACHE["message"]

        # レスポンスがスキーマに適合していることをチェック
        assert isinstance(response, AdminResponseSchema)

        # レスポンスデータ本体のチェック
        results = response.results
        assert results == api_dataset.EXPECTED_FLUSH_CACHE["results"]

        # ページネーション情報は非サポートであることをチェック
        pagination = response.pagination
        assert pagination is None

        print(f"✅ ADMINS API キャッシュクリアテスト成功")

    def test_reset_ws_session_success(self, admins_api):
        """Web Service Sessionリセットの成功テスト"""
        # APIを呼び出し
        response = admins_api.reset_ws_session()

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is api_dataset.EXPECTED_RESET_WS_SESSION["success"]
        assert response.message == api_dataset.EXPECTED_RESET_WS_SESSION["message"]

        # レスポンスがスキーマに適合していることをチェック
        assert isinstance(response, AdminResponseSchema)

        # レスポンスデータ本体のチェック
        results = response.results
        assert results == api_dataset.EXPECTED_RESET_WS_SESSION["results"]

        # ページネーション情報は非サポートであることをチェック
        pagination = response.pagination
        assert pagination is None

        print(f"✅ ADMINS API Web Service Sessionリセットテスト成功")
