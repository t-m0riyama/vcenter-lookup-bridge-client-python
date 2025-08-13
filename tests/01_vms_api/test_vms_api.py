# coding: utf-8

"""
vCenter Lookup Bridge API - VMs APIテスト
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
api_dataset = importlib.import_module(f"{dataset_name}.vms_api.settings")

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.configuration import Configuration
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.vm_response_schema import VmResponseSchema


@pytest.fixture
def api_config():
    """API設定のフィクスチャ"""
    return Configuration(**api_server_settings.VALID_API_SERVER_SETTINGS)


@pytest.fixture
def api_client(api_config):
    """APIクライアントのフィクスチャ"""
    return vcenter_lookup_bridge_client.ApiClient(api_config)


@pytest.fixture
def vms_api(api_client):
    """VMs APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.VmsApi(api_client)


class TestVmsApi:
    """VMs API unit test"""

    def test_get_vm_success(self, vms_api):
        """単一VM取得の成功テスト"""
        # APIを呼び出し
        response = vms_api.get_vm(**api_dataset.VALID_GET_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert results is not None

        # １件の仮想マシンのみ返却されることをチェック
        assert len(results) == 1

        # レスポンスデータがスキーマに適合していることを存在チェック
        assert isinstance(results[0], VmResponseSchema)

        # 期待した値を返していることをチェック
        assert results[0].name == api_dataset.EXPECTED_VM["name"]
        assert results[0].uuid == api_dataset.EXPECTED_VM["uuid"]
        assert results[0].instance_uuid == api_dataset.EXPECTED_VM["instanceUuid"]
        assert results[0].vcenter == api_dataset.EXPECTED_VM["vcenter"]
        assert results[0].datacenter == api_dataset.EXPECTED_VM["datacenter"]
        assert results[0].cluster == api_dataset.EXPECTED_VM["cluster"]
        assert results[0].esxi_hostname == api_dataset.EXPECTED_VM["esxiHostname"]
        assert results[0].power_state == api_dataset.EXPECTED_VM["powerState"]
        assert results[0].num_cpu == api_dataset.EXPECTED_VM["numCpu"]
        assert results[0].memory_size_mb == api_dataset.EXPECTED_VM["memorySizeMB"]
        assert results[0].vm_path_name == api_dataset.EXPECTED_VM["vmPathName"]
        assert results[0].guest_full_name == api_dataset.EXPECTED_VM["guestFullName"]
        assert results[0].hostname == api_dataset.EXPECTED_VM["hostname"]
        assert results[0].ip_address == api_dataset.EXPECTED_VM["ipAddress"]
        assert results[0].template == api_dataset.EXPECTED_VM["template"]
        assert results[0].hw_version == api_dataset.EXPECTED_VM["hwVersion"]
        assert results[0].disk_devices == api_dataset.EXPECTED_VM["diskDevices"]
        assert results[0].network_devices == api_dataset.EXPECTED_VM["networkDevices"]
        # vm_folderはNoneであることをチェック
        assert results[0].vm_folder is None

        print(f"✅ VM取得テスト成功: {results[0].name}")

    def test_get_vm_not_found_with_invalid_vm_instance_uuid(self, vms_api):
        """存在しないVM取得のテスト"""
        try:
            # 存在しないVMのインスタンスUUIDでAPIを呼び出し
            response = vms_api.get_vm(
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

    def test_get_vm_not_found_with_invalid_vcenter(self, vms_api):
        """存在しないVM取得のテスト"""
        try:
            # 存在しないVMのインスタンスUUIDでAPIを呼び出し
            response = vms_api.get_vm(**api_dataset.INVALID_GET_PARAMETERS_VCENTER)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないVM取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(
                    f"✅ 存在しないVM取得テスト成功: 404エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"存在しないVM取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_vms_success(self, vms_api):
        """VMリスト取得の成功テスト"""
        # APIを呼び出し
        response = vms_api.list_vms(**api_dataset.VALID_LIST_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数の仮想マシンが返却されることをチェック
        assert len(results) == len(api_dataset.EXPECTED_VM_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, VmResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results, api_dataset.EXPECTED_VM_LIST["results"]
        ):
            assert result.name == expected_result["name"]
            assert result.uuid == expected_result["uuid"]
            assert result.instance_uuid == expected_result["instanceUuid"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]
            assert result.cluster == expected_result["cluster"]
            assert result.esxi_hostname == expected_result["esxiHostname"]
            assert result.power_state == expected_result["powerState"]
            assert result.num_cpu == expected_result["numCpu"]
            assert result.memory_size_mb == expected_result["memorySizeMB"]
            assert result.vm_path_name == expected_result["vmPathName"]
            assert result.guest_full_name == expected_result["guestFullName"]
            assert result.hostname == expected_result["hostname"]
            assert result.ip_address == expected_result["ipAddress"]
            assert result.template == expected_result["template"]
            assert result.hw_version == expected_result["hwVersion"]
            assert result.disk_devices == expected_result["diskDevices"]
            assert result.network_devices == expected_result["networkDevices"]

        print(
            f"✅ VMリスト取得テスト成功: {len(response.results)}件のVMが見つかりました"
        )

    def test_list_vms_with_invalid_max_results(self, vms_api):
        """VMリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""

        # max_resultsに制限（<=1000)を超える値を指定してAPIを呼び出し
        try:
            response = vms_api.list_vms(
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
            response = vms_api.list_vms(
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

    def test_list_vms_with_invalid_offset(self, vms_api):
        """VMリスト取得のテスト（パラメータ制限が有効であることを確認）"""
        # offsetに制限を超える値をを指定してAPIを呼び出し
        try:
            response = vms_api.list_vms(**api_dataset.INVALID_LIST_PARAMETERS_OFFSET)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"offsetに制限を超える値を指定したテストでエラーが発生しました")

        except pydantic.ValidationError as e:
            print(
                f"✅ offsetに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}"
            )

    def test_list_vms_with_pagination(self, vms_api):
        """ページネーション付きVMリスト取得のテスト"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = vms_api.list_vms(**api_dataset.VALID_LIST_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        assert isinstance(response.results, list)

        # ページネーション情報のチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        expected_pagination = api_dataset.EXPECTED_VM_LIST["pagination"]
        assert pagination.total_count == expected_pagination["totalCount"]
        assert pagination.offset == expected_pagination["offset"]
        assert pagination.limit == expected_pagination["limit"]
        assert pagination.has_next == expected_pagination["hasNext"]
        assert pagination.has_previous == expected_pagination["hasPrevious"]

        # データ件数のチェック（per_page以下であることを確認）
        assert len(response.results) <= 100

        print(
            f"✅ ページネーション付きVMリスト取得テスト成功: ページ1, 1ページあたり100件"
        )

    def test_list_vms_empty_result(self, vms_api):
        """空の結果を返すフィルターのテスト"""
        try:
            # 存在しない条件でフィルタリング。例外が発生することを期待する。
            response = vms_api.list_vms(
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
