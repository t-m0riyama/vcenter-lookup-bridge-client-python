# coding: utf-8

"""
vCenter Lookup Bridge API - HOSTS APIテスト
"""

import pydantic
import pytest
from typing import Dict, Any

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.host_response_schema import HostResponseSchema
from vcenter_lookup_bridge_client.models.host_detail_response_schema import HostDetailResponseSchema


@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "hosts_api"


@pytest.fixture
def api_instance(api_client):
    """Hosts APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.HostsApi(api_client)


class TestHostsApi:
    """Hosts API unit test"""

    def test_get_host_success(self, api_instance, test_dataset):
        """単一ホスト取得の成功テスト"""
        # APIを呼び出し
        response = api_instance.get_host(**test_dataset.VALID_GET_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert results is not None

        # レスポンスデータがスキーマに適合していることを存在チェック
        assert isinstance(results, HostDetailResponseSchema)

        # 期待した値を返していることをチェック
        assert results.name == test_dataset.EXPECTED_HOST["name"]
        assert results.uuid == test_dataset.EXPECTED_HOST["uuid"]
        assert results.status == test_dataset.EXPECTED_HOST["status"]
        assert results.esxi_version == test_dataset.EXPECTED_HOST["esxiVersion"]
        assert results.esxi_version_full == test_dataset.EXPECTED_HOST["esxiVersionFull"]
        assert results.vcenter == test_dataset.EXPECTED_HOST["vcenter"]
        assert results.datacenter == test_dataset.EXPECTED_HOST["datacenter"]
        assert results.cluster == test_dataset.EXPECTED_HOST["cluster"]
        assert results.hardware_vendor == test_dataset.EXPECTED_HOST["hardwareVendor"]
        assert results.hardware_model == test_dataset.EXPECTED_HOST["hardwareModel"]
        assert results.power_state == test_dataset.EXPECTED_HOST["powerState"]
        assert results.cpu_model == test_dataset.EXPECTED_HOST["cpuModel"]
        assert results.num_cpu_sockets == test_dataset.EXPECTED_HOST["numCpuSockets"]
        assert results.num_cpu_cores == test_dataset.EXPECTED_HOST["numCpuCores"]
        assert results.num_cpu_threads == test_dataset.EXPECTED_HOST["numCpuThreads"]
        assert results.memory_size_mb == test_dataset.EXPECTED_HOST["memorySizeMB"]
        assert results.datastores == test_dataset.EXPECTED_HOST["datastores"]
        assert results.portgroups == test_dataset.EXPECTED_HOST["portgroups"]
        assert results.vswitches == test_dataset.EXPECTED_HOST["vswitches"]
        assert results.ip_address == test_dataset.EXPECTED_HOST["ipAddress"]

        print(f"✅ ホスト取得テスト成功")

    def test_get_host_not_found_with_invalid_host(self, api_instance, test_dataset):
        """存在しないホスト取得のテスト"""
        try:
            # 存在しないホスト名でAPIを呼び出し
            response = api_instance.get_host(**test_dataset.INVALID_GET_PARAMETERS_HOST_UUID)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"存在しないホスト取得テストでエラーが発生しました。想定される例外が発生しませんでした。")

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print("✅ 存在しないホスト取得テスト成功: 404エラーが正しく返されました")
            else:
                pytest.fail(f"存在しないホスト取得テストで予期しないエラーが発生しました: {str(e)}")

    def test_get_host_not_found_with_invalid_vcenter(self, api_instance, test_dataset):
        """存在しないvCenterを指定し、ホスト取得のテスト"""
        try:
            # 存在しないvCenterでAPIを呼び出し
            response = api_instance.get_host(**test_dataset.INVALID_GET_PARAMETERS_VCENTER)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"存在しないホスト取得テストでエラーが発生しました。想定される例外が発生しませんでした。")

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(f"✅ 存在しないホスト取得テスト成功: 404エラーが正しく返されました: {str(e)}")
            else:
                pytest.fail(f"存在しないホスト取得テストで予期しないエラーが発生しました: {str(e)}")

    def test_list_hosts_success(self, api_instance, test_dataset):
        """ホストリスト取得の成功テスト"""
        # APIを呼び出し
        response = api_instance.list_hosts(**test_dataset.VALID_LIST_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_HOST_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, HostResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_HOST_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.uuid == expected_result["uuid"]
            assert result.status == expected_result["status"]
            assert result.esxi_version == expected_result["esxiVersion"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]
            assert result.num_cpu_sockets == expected_result["numCpuSockets"]
            assert result.num_cpu_cores == expected_result["numCpuCores"]
            assert result.num_cpu_threads == expected_result["numCpuThreads"]
            assert result.memory_size_mb == expected_result["memorySizeMB"]

        print(f"✅ ホストリスト取得テスト成功: {len(response.results)}件のホストが見つかりました")

    def test_list_vcenters_with_invalid_max_results(self, api_instance, test_dataset):
        """ホストリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""

        # max_resultsに制限（<=1000)を超える値を指定してAPIを呼び出し
        try:
            response = api_instance.list_hosts(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"max_resultsに制限を超える値(>1000, {test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS['max_results']})を指定したテストでエラーが発生しました"
            )

        except pydantic.ValidationError as e:
            print(f"✅ max_resultsに制限を超える値(>1000)を指定した場合、正しくエラーが返却されました: {e}")

        # max_resultsに制限（>=1)を超える値を指定してAPIを呼び出し
        try:
            response = api_instance.list_hosts(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"max_resultsに制限を超える値(<0, {test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2['max_results']})を指定したテストでエラーが発生しました"
            )

        except pydantic.ValidationError as e:
            print(f"✅ max_resultsに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}")

    def test_list_hosts_with_invalid_offset(self, api_instance, test_dataset):
        """ホストリスト取得のテスト（パラメータ制限が有効であることを確認）"""
        # offsetに制限を超える値をを指定してAPIを呼び出し
        try:
            response = api_instance.list_hosts(**test_dataset.INVALID_LIST_PARAMETERS_OFFSET)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"offsetに制限を超える値を指定したテストでエラーが発生しました")

        except pydantic.ValidationError as e:
            print(f"✅ offsetに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}")

    def test_list_hosts_with_pagination(self, api_instance, test_dataset):
        """ページネーション付きホストリスト取得のテスト"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = api_instance.list_hosts(**test_dataset.VALID_LIST_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        assert isinstance(response.results, list)

        # ページネーション情報のチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # データ件数のチェック（per_page以下であることを確認）
        assert len(response.results) <= 100

        print(f"✅ ページネーション付きホストリスト取得テスト成功: ページ1, 1ページあたり100件")
