# coding: utf-8

"""
vCenter Lookup Bridge API - CLUSTERS APIテスト
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
api_dataset = importlib.import_module(f"{dataset_name}.clusters_api.settings")

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.configuration import Configuration
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.cluster_response_schema import (
    ClusterResponseSchema,
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
def clusters_api(api_client):
    """Clusters APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.ClustersApi(api_client)


class TestClustersApi:
    """Clusters API unit test"""

    def test_get_cluster_success(self, clusters_api):
        """単一クラスタ取得の成功テスト"""
        # APIを呼び出し
        response = clusters_api.list_clusters(**api_dataset.VALID_GET_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert results is not None

        instance_uuids = []
        for result in results:
            if (
                result.vm_instance_uuid is not None
                and result.vm_instance_uuid not in instance_uuids
            ):
                instance_uuids.append(result.vm_instance_uuid)
        # １件のクラスタのみ返却されることをチェック
        # assert len(results) == 1
        assert len(instance_uuids) == 1

        # レスポンスデータがスキーマに適合していることを存在チェック
        for result in results:
            assert isinstance(result, ClusterResponseSchema)

        # 期待した値を返していることをチェック
        for result, expected_result in zip(
            results, api_dataset.EXPECTED_SINGLE_VM_SNAPSHOTS
        ):
            assert result.name == expected_result["name"]
            assert result.status == expected_result["status"]
            assert result.hosts == expected_result["hosts"]
            assert result.vcenter == expected_result["vcenter"]

        print(f"✅ クラスタ取得テスト成功")

    def test_get_cluster_not_found_with_invalid_cluster(self, clusters_api):
        """存在しないクラスタ取得のテスト"""
        try:
            # 存在しないクラスタ名でAPIを呼び出し
            response = clusters_api.list_clusters(
                **api_dataset.INVALID_GET_PARAMETERS_VM_INSTANCE_UUID
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないクラスタ取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(
                    "✅ 存在しないクラスタ取得テスト成功: 404エラーが正しく返されました"
                )
            else:
                pytest.fail(
                    f"存在しないクラスタ取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_get_vm_not_found_with_invalid_vcenter(self, clusters_api):
        """存在しないvCenterを指定し、クラスタ取得のテスト"""
        try:
            # 存在しないVMのインスタンスUUIDでAPIを呼び出し
            response = clusters_api.list_clusters(
                **api_dataset.INVALID_GET_PARAMETERS_VCENTER
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないVM取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(
                    f"✅ 存在しないクラスタ取得テスト成功: 500エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"存在しないクラスタ取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_clusters_success(self, clusters_api):
        """クラスタリスト取得の成功テスト"""
        # APIを呼び出し
        response = clusters_api.list_clusters(**api_dataset.VALID_LIST_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(
            api_dataset.EXPECTED_MULTI_VM_SNAPSHOT_LIST["results"]
        )

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, ClusterResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            api_dataset.EXPECTED_MULTI_VM_SNAPSHOT_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.status == expected_result["status"]
            assert result.hosts == expected_result["hosts"]
            assert result.vcenter == expected_result["vcenter"]

        print(
            f"✅ クラスタリスト取得テスト成功: {len(response.results)}件のクラスタが見つかりました"
        )

    def test_list_vcenters_with_invalid_max_results(self, clusters_api):
        """クラスタリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""

        # max_resultsに制限（<=1000)を超える値を指定してAPIを呼び出し
        try:
            response = clusters_api.list_vcenters(
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
            response = clusters_api.list_clusters(
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

    def test_list_clusters_with_invalid_offset(self, clusters_api):
        """クラスタリスト取得のテスト（パラメータ制限が有効であることを確認）"""
        # offsetに制限を超える値をを指定してAPIを呼び出し
        try:
            response = clusters_api.list_clusters(
                **api_dataset.INVALID_LIST_PARAMETERS_OFFSET
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"offsetに制限を超える値を指定したテストでエラーが発生しました")

        except pydantic.ValidationError as e:
            print(
                f"✅ offsetに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}"
            )

    def test_list_clusters_with_pagination(self, clusters_api):
        """ページネーション付きクラスタリスト取得のテスト"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = clusters_api.list_clusters(**api_dataset.VALID_LIST_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        assert isinstance(response.results, list)

        # ページネーション情報のチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        expected_pagination = api_dataset.EXPECTED_MULTI_VM_SNAPSHOT_LIST["pagination"]
        assert pagination.total_count == expected_pagination["totalCount"]
        assert pagination.offset == expected_pagination["offset"]
        assert pagination.limit == expected_pagination["limit"]
        assert pagination.has_next == expected_pagination["hasNext"]
        assert pagination.has_previous == expected_pagination["hasPrevious"]

        # データ件数のチェック（per_page以下であることを確認）
        assert len(response.results) <= 100

        print(
            f"✅ ページネーション付きVMスナップショットリスト取得テスト成功: ページ1, 1ページあたり100件"
        )

    def test_list_clusters_empty_result(self, clusters_api):
        """空の結果を返すフィルターのテスト"""
        try:
            # 存在しない条件でフィルタリング。例外が発生することを期待する。
            response = clusters_api.list_vm_snapshots(
                **api_dataset.INVALID_LIST_PARAMETERS_VM_FOLDERS
            )

        except Exception as e:
            # HTTPステータス404が例外として投げられる
            if "404" in str(e):
                print(
                    f"✅ 空の結果フィルターテスト成功: 404エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"空の結果フィルターテストで予期しないエラーが発生しました: {str(e)}"
                )
