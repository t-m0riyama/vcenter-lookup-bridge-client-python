# coding: utf-8

"""
vCenter Lookup Bridge API - VM SNAPSHOTS APIテスト
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
api_dataset = importlib.import_module(f"{dataset_name}.vm_snapshots_api.settings")

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.configuration import Configuration
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.vm_snapshot_response_schema import (
    VmSnapshotResponseSchema,
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
def vm_snapshots_api(api_client):
    """VMs APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.VmSnapshotsApi(api_client)


class TestVmSnapshotsApi:
    """VMs API unit test"""

    def test_get_vm_success(self, vm_snapshots_api):
        """単一VMスナップショット取得の成功テスト"""
        # APIを呼び出し
        response = vm_snapshots_api.get_vm_snapshots(**api_dataset.VALID_GET_PARAMETERS)

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
        # １件の仮想マシンスナップショットのみ返却されることをチェック
        # assert len(results) == 1
        assert len(instance_uuids) == 1

        # レスポンスデータがスキーマに適合していることを存在チェック
        for result in results:
            assert isinstance(result, VmSnapshotResponseSchema)

        # 期待した値を返していることをチェック
        for result, expected_result in zip(
            results, api_dataset.EXPECTED_SINGLE_VM_SNAPSHOTS
        ):
            assert result.name == expected_result["name"]
            assert result.description == expected_result["description"]
            assert result.id == expected_result["id"]
            assert result.has_child == expected_result["hasChild"]
            assert result.parent_id == expected_result["parentId"]
            assert result.create_time == expected_result["createTime"]
            assert result.vm_name == expected_result["vmName"]
            assert result.vm_instance_uuid == expected_result["vmInstanceUuid"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]
            assert result.vm_folder == expected_result["vmFolder"]

        print(f"✅ VMスナップショット取得テスト成功")

    def test_get_vm_snapshots_not_found_with_invalid_vm_instance_uuid(
        self, vm_snapshots_api
    ):
        """存在しないVMスナップショット取得のテスト"""
        try:
            # 存在しないVMのインスタンスUUIDでAPIを呼び出し
            response = vm_snapshots_api.get_vm_snapshots(
                **api_dataset.INVALID_GET_PARAMETERS_VM_INSTANCE_UUID
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないVM取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print("✅ 存在しないVM取得テスト成功: 404エラーが正しく返されました")
            else:
                pytest.fail(
                    f"存在しないVM取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_get_vm_snapshot_not_found_with_invalid_vcenter(self, vm_snapshots_api):
        """存在しないVM取得のテスト"""
        try:
            # 存在しないVMのインスタンスUUIDでAPIを呼び出し
            response = vm_snapshots_api.get_vm_snapshots(
                **api_dataset.INVALID_GET_PARAMETERS_VCENTER
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないVM取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 500エラーは例外として投げられる可能性がある
            if "500" in str(e):
                print(
                    f"✅ 存在しないVM取得テスト成功: 500エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"存在しないVM取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_vm_snapshots_success(self, vm_snapshots_api):
        """VMスナップショットリスト取得の成功テスト"""
        # APIを呼び出し
        response = vm_snapshots_api.list_vm_snapshots(
            **api_dataset.VALID_LIST_PARAMETERS
        )

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数の仮想マシンが返却されることをチェック
        assert len(results) == len(
            api_dataset.EXPECTED_MULTI_VM_SNAPSHOT_LIST["results"]
        )

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, VmSnapshotResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            api_dataset.EXPECTED_MULTI_VM_SNAPSHOT_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.description == expected_result["description"]
            assert result.id == expected_result["id"]
            assert result.has_child == expected_result["hasChild"]
            assert result.parent_id == expected_result["parentId"]
            assert result.create_time == expected_result["createTime"]
            assert result.vm_name == expected_result["vmName"]
            assert result.vm_instance_uuid == expected_result["vmInstanceUuid"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]
            assert result.vmFolder == expected_result["vmFolder"]

        print(
            f"✅ VMスナップショットリスト取得テスト成功: {len(response.results)}件のVMスナップショットが見つかりました"
        )

    def test_list_vm_snapshots_with_invalid_max_results(self, vm_snapshots_api):
        """VMスナップショットリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""

        # max_resultsに制限（<=1000)を超える値を指定してAPIを呼び出し
        try:
            response = vm_snapshots_api.list_vm_snapshots(
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
            response = vm_snapshots_api.list_vm_snapshots(
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

    def test_list_vm_snapshots_with_invalid_offset(self, vm_snapshots_api):
        """VMスナップショットリスト取得のテスト（パラメータ制限が有効であることを確認）"""
        # offsetに制限を超える値をを指定してAPIを呼び出し
        try:
            response = vm_snapshots_api.list_vm_snapshots(
                **api_dataset.INVALID_LIST_PARAMETERS_OFFSET
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"offsetに制限を超える値を指定したテストでエラーが発生しました")

        except pydantic.ValidationError as e:
            print(
                f"✅ offsetに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}"
            )

    def test_list_vm_snapshots_with_pagination(self, vm_snapshots_api):
        """ページネーション付きVMスナップショットリスト取得のテスト"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = vm_snapshots_api.list_vm_snapshots(
            **api_dataset.VALID_LIST_PARAMETERS
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

    def test_list_vms_empty_result(self, vm_snapshots_api):
        """空の結果を返すフィルターのテスト"""
        try:
            # 存在しない条件でフィルタリング。例外が発生することを期待する。
            response = vm_snapshots_api.list_vm_snapshots(
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
