# coding: utf-8

"""
vCenter Lookup Bridge API - ADMINS APIテスト
"""

import pydantic
import pytest
from typing import Dict, Any

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.admin_response_schema import (
    AdminResponseSchema,
)

@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "admins_api"

@pytest.fixture
def api_instance(api_client):
    """Admins APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.AdminsApi(api_client)


class TestAdminsApi:
    """Admins API Cache management unit test"""

    def test_flush_cache_success(self, api_instance, api_dataset):
        """キャッシュクリアの成功テスト"""
        # APIを呼び出し
        response = api_instance.flush_caches()

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

    def test_reset_ws_session_success(self, api_instance, api_dataset):
        """Web Service Sessionリセットの成功テスト"""
        # APIを呼び出し
        response = api_instance.reset_ws_session()

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
