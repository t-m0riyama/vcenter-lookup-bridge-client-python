# coding: utf-8

"""
vCenter Lookup Bridge API - DATASTORES APIテスト
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
api_dataset = importlib.import_module(f"{dataset_name}.vm_folders_api.settings")

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.configuration import Configuration
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.datastore_response_schema import (
    DatastoreResponseSchema,
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
def datastores_api(api_client):
    """Datastores APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.DatastoresApi(api_client)


class TestDatastoresApi:
    """Datastores API unit test"""

    def test_list_datastore_not_found_with_invalid_datastore(self, datastores_api):
        """存在しないデータストア取得のテスト(datastores指定)"""
        try:
            # 存在しないデータストア名でDATASTORES APIを呼び出し
            response = datastores_api.list_datastores(
                **api_dataset.INVALID_LIST_PARAMETERS_VM_FOLDERS
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないデータストア取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(
                    "✅ 存在しないデータストア取得テスト成功: 404エラーが正しく返されました"
                )
            else:
                pytest.fail(
                    f"存在しないデータストア取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_datastore_not_found_with_invalid_vcenter(self, datastores_api):
        """存在しないデータストア取得のテスト(vCenter指定)"""
        try:
            # 存在しないvCenterでAPIを呼び出し
            response = datastores_api.list_datastores(
                **api_dataset.INVALID_LIST_PARAMETERS_VCENTER
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないデータストア取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(
                    f"✅ 存在しないデータストア取得テスト成功: 404エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"存在しないデータストア取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_datastores_success(self, datastores_api):
        """データストアリスト取得の成功テスト"""
        # APIを呼び出し
        response = datastores_api.list_datastores(**api_dataset.VALID_LIST_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数の仮想マシンが返却されることをチェック
        assert len(results) == len(api_dataset.EXPECTED_DATASTORE_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, DatastoreResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            api_dataset.EXPECTED_VM_FOLDER_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.vcenter == expected_result["vcenter"]

        print(
            f"✅ データストアリスト取得テスト成功: {len(response.results)}件のデータストアが見つかりました"
        )

    def test_list_datastores_with_invalid_max_results(self, datastores_api):
        """データストアリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""

        # max_resultsに制限（<=1000)を超える値を指定してAPIを呼び出し
        try:
            response = datastores_api.list_datastores(
                **api_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"max_resultsに制限を超える値(>1000, {api_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS['max_results']})を指定したテストでエラーが発生しました"
            )

        except pydantic.ValidationError as e:
            print(
                f"✅ max_resultsに制限を超える値(>1000)を指定した場合、正しくエラーが返却されました: {e}"
            )

        # max_resultsに制限（>=1)を超える値を指定してAPIを呼び出し
        try:
            response = datastores_api.list_datastores(
                **api_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"max_resultsに制限を超える値(<0, {api_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2['max_results']})を指定したテストでエラーが発生しました"
            )

        except pydantic.ValidationError as e:
            print(
                f"✅ max_resultsに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}"
            )

    def test_list_datastores_with_invalid_offset(self, datastores_api):
        """データストアリスト取得のテスト（パラメータ制限が有効であることを確認）"""
        # offsetに制限を超える値をを指定してAPIを呼び出し
        try:
            response = datastores_api.list_datastores(
                **api_dataset.INVALID_LIST_PARAMETERS_OFFSET
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"offsetに制限を超える値を指定したテストでエラーが発生しました")

        except pydantic.ValidationError as e:
            print(
                f"✅ offsetに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}"
            )

    def test_list_datastores_with_pagination(self, datastores_api):
        """ページネーション付きデータストアリスト取得のテスト"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = datastores_api.list_datastores(
            **api_dataset.VALID_LIST_PARAMETERS_VCENTER
        )

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        assert isinstance(response.results, list)

        # ページネーション情報のチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        expected_pagination = api_dataset.EXPECTED_VM_FOLDER_LIST["pagination"]
        assert pagination.total_count == expected_pagination["totalCount"]
        assert pagination.offset == expected_pagination["offset"]
        assert pagination.limit == expected_pagination["limit"]
        assert pagination.has_next == expected_pagination["hasNext"]
        assert pagination.has_previous == expected_pagination["hasPrevious"]

        # データ件数のチェック（per_page以下であることを確認）
        assert len(response.results) <= 100

        print(
            f"✅ ページネーション付きデータストアリスト取得テスト成功: ページ1, 1ページあたり100件"
        )
