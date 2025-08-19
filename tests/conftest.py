import importlib
import os
import pytest
import urllib3

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.configuration import Configuration

@pytest.fixture
def dataset_name():
    """データセット名のフィクスチャ"""
    return f"tests.test_datasets.{os.environ['TEST_DATASET']}"

@pytest.fixture
def api_server_settings(dataset_name):
    """APIサーバ設定のフィクスチャ"""
    return importlib.import_module(f"{dataset_name}.shared.api_server_settings")

@pytest.fixture
def api_config(api_server_settings):
    """API設定のフィクスチャ"""
    return Configuration(**api_server_settings.VALID_API_SERVER_SETTINGS)

@pytest.fixture
def api_client(api_config):
    """APIクライアントのフィクスチャ"""
    # Suppress only the single warning from urllib3.
    urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
    return vcenter_lookup_bridge_client.ApiClient(api_config)

@pytest.fixture
def api_dataset(dataset_name, api_name):
    """APIデータセットのフィクスチャ"""
    return importlib.import_module(f"{dataset_name}.{api_name}.settings")
