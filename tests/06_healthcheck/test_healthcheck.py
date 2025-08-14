# coding: utf-8

"""
vCenter Lookup Bridge API - Healthcheck APIテスト
"""

import os
import pytest
import requests
import importlib
import urllib3
from requests.auth import HTTPBasicAuth
from typing import Dict, Any

dataset_name = f"tests.test_datasets.{os.environ['TEST_DATASET']}"
api_server_settings = importlib.import_module(
    f"{dataset_name}.shared.api_server_settings"
)

from vcenter_lookup_bridge_client.configuration import Configuration


@pytest.fixture
def api_config():
    """API設定のフィクスチャ"""
    return Configuration(**api_server_settings.VALID_API_SERVER_SETTINGS)


class TestHealthcheck:
    """Healthcheck API unit test"""

    def test_healthcheck(self, api_config):
        """API接続の基本テスト"""
        try:
            # Suppress only the single warning from urllib3.
            urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

            # ヘルスチェックエンドポイントを使用して接続をテスト
            health_url = f"{api_config.host}/api/v1/healthcheck/"
            response = requests.get(
                    health_url,
                    timeout=10,
                    auth=HTTPBasicAuth(api_server_settings.VALID_API_SERVER_SETTINGS["username"],
                                       api_server_settings.VALID_API_SERVER_SETTINGS["password"]),
                    verify=False
            )

            # 接続が成功することを確認
            assert response.status_code in [
                200,
            ]  # エンドポイントが存在しない場合もある

            print("✅ API接続テスト成功: サーバーに接続できました")

        except requests.exceptions.ConnectionError as e:
            pytest.skip(
                    f"APIサーバーに接続できません。サーバーが起動していることを確認してください: {e}"
            )
        except Exception as e:
            pytest.fail(f"API接続テストでエラーが発生しました: {str(e)}")
