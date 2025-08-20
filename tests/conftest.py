import importlib
import os
import pytest
import urllib3

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.configuration import Configuration
from py.xml import html


def pytest_html_report_title(report):
   report.title = 'vcenter-lookup-bridge-client Test results'


def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))


def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

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
def test_dataset(dataset_name, api_name):
    """テストデータセットのフィクスチャ"""
    return importlib.import_module(f"{dataset_name}.{api_name}.settings")
