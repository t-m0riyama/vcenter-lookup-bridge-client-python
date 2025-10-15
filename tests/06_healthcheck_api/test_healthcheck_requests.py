# coding: utf-8

"""
vCenter Lookup Bridge API - Healthcheck APIテスト(requestsモジュール版)
"""

import os
import pytest
import requests
import importlib
import urllib3
from requests.auth import HTTPBasicAuth
from typing import Dict, Any

dataset_name = f"tests.test_datasets.{os.environ['TEST_DATASET']}"
api_server_settings = importlib.import_module(f"{dataset_name}.shared.api_server_settings")

from vcenter_lookup_bridge_client.configuration import Configuration


@pytest.fixture
def api_config():
    """API設定のフィクスチャ"""
    return Configuration(**api_server_settings.VALID_API_SERVER_SETTINGS)


class TestHealthcheck:
    """Healthcheck API unit test"""

    def test_healthcheck(self, api_config):
        """Healthcheck APIのテスト(requestsモジュール版)"""
        try:
            # Suppress only the single warning from urllib3.
            urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

            # ヘルスチェックエンドポイントを使用して接続をテスト
            health_url = f"{api_config.host}/healthcheck/"
            response = requests.get(
                health_url,
                auth=HTTPBasicAuth(
                    api_server_settings.VALID_API_SERVER_SETTINGS["username"],
                    api_server_settings.VALID_API_SERVER_SETTINGS["password"],
                ),
                verify=False,
                timeout=10,
            )

            # 接続が成功することを確認
            assert response.status_code in [200]

            print("✅ Healthcheck APIのテスト(requestsモジュール版)成功")

        except requests.exceptions.ConnectionError:
            pytest.skip("APIサーバーに接続できません。サーバーが起動していることを確認してください。")
        except Exception as e:
            pytest.fail(f"Healthcheck APIのテスト(requestsモジュール版)でエラーが発生しました: {health_url} {str(e)}")
