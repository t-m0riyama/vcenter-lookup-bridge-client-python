# coding: utf-8

"""
vCenter Lookup Bridge API - PORTGROUPS APIテスト
"""

import pydantic
import pytest
from typing import Dict, Any

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.portgroup_response_schema import (
    PortgroupResponseSchema,
)


@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "portgroups_api"


@pytest.fixture
def api_instance(api_client):
    """PORTGROUPS APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.PortgroupsApi(api_client)


class TestPortgroupsApi:
    """PORTGROUPS API unit test"""

    def test_list_portgroups_success(self, api_instance, api_dataset):
        """データストアリスト取得の成功テスト"""
        # APIを呼び出し
        response = api_instance.list_portgroups(
            **api_dataset.VALID_LIST_PARAMETERS
        )

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数の仮想マシンが返却されることをチェック
        assert len(results) == len(api_dataset.EXPECTED_PORTGROUPS_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, PortgroupResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            api_dataset.EXPECTED_PORTGROUPS_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.vcenter == expected_result["vcenter"]

        print(
            f"✅ データストアリスト取得テスト成功: {len(response.results)}件のデータストアが見つかりました"
        )
        
    def test_list_portgroups_success_multi_tags(self, api_instance, api_dataset):
        """ポートグループリスト取得の成功テスト"""
        # APIを呼び出し
        response = api_instance.list_portgroups(
            **api_dataset.VALID_LIST_PARAMETERS_MULTI_TAGS
        )

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数の仮想マシンが返却されることをチェック
        assert len(results) == len(api_dataset.EXPECTED_PORTGROUPS_LIST_MULTI_TAGS["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, PortgroupResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            api_dataset.EXPECTED_PORTGROUPS_LIST_MULTI_TAGS["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.vcenter == expected_result["vcenter"]

        print(
            f"✅ ポートグループリスト取得テスト(複数タグ指定)成功: {len(response.results)}件のポートグループが見つかりました"
        )

    def test_list_portgroup_not_found_with_invalid_tag_category(self, api_instance, api_dataset):
        """付与されていないタグカテゴリを指定してのポートグループ取得のテスト(tags指定)"""
        try:
            # 付与されていないタグ名で  S APIを呼び出し
            response = api_instance.list_portgroups(
                **api_dataset.INVALID_LIST_PARAMETERS_TAG_CATEGORY
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"付与されていないタグカテゴリを指定してのポートグループ取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(
                    "✅ 付与されていないタグカテゴリを指定してのポートグループ取得テスト成功: 404エラーが正しく返されました"
                )
            else:
                pytest.fail(
                    f"付与されていないタグカテゴリを指定してのポートグループ取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_portgroup_not_found_with_invalid_tag(self, api_instance, api_dataset):
        """付与されていないタグを指定してのポートグループ取得のテスト(tags指定)"""
        try:
            # 付与されていないタグ名で  S APIを呼び出し
            response = api_instance.list_portgroups(
                **api_dataset.INVALID_LIST_PARAMETERS_TAGS
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"付与されていないタグを指定してのポートグループ取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(
                    "✅ 付与されていないタグを指定してのポートグループ取得テスト成功: 404エラーが正しく返されました"
                )
            else:
                pytest.fail(
                    f"付与されていないタグを指定してのポートグループ取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_portgroup_not_found_with_invalid_vcenter(self, api_instance, api_dataset):
        """存在しないvCenterを指定してのポートグループ取得のテスト(vCenter指定)"""
        try:
            # 存在しないvCenterでAPIを呼び出し
            response = api_instance.list_portgroups(
                **api_dataset.INVALID_LIST_PARAMETERS_VCENTER
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないvCenterを指定してのデータストア取得テストでエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 500エラーは例外として投げられる可能性がある
            if "500" in str(e):
                print(
                    f"✅ 存在しないvCenterを指定してのデータストア取得テスト成功: 500エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"存在しないvCenterを指定してのデータストア取得テストで予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_portgroups_with_invalid_max_results(self, api_instance, api_dataset):
        """ポートグループリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""

        # max_resultsに制限（<=1000)を超える値を指定してAPIを呼び出し
        try:
            response = api_instance.list_portgroups(
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
            response = api_instance.list_portgroups(
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

    def test_list_portgroups_with_invalid_offset(self, api_instance, api_dataset):
        """ポートグループリスト取得のテスト（パラメータ制限が有効であることを確認）"""
        # offsetに制限を超える値をを指定してAPIを呼び出し
        try:
            response = api_instance.list_portgroups(
                **api_dataset.INVALID_LIST_PARAMETERS_OFFSET
            )

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"offsetに制限を超える値を指定したテストでエラーが発生しました")

        except pydantic.ValidationError as e:
            print(
                f"✅ offsetに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}"
            )

    def test_list_portgroups_with_pagination(self, api_instance, api_dataset):
        """ページネーション付きポートグループリスト取得のテスト"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = api_instance.list_portgroups(
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
        expected_pagination = api_dataset.EXPECTED_PORTGROUPS_LIST["pagination"]
        assert pagination.total_count == expected_pagination["totalCount"]
        assert pagination.offset == expected_pagination["offset"]
        assert pagination.limit == expected_pagination["limit"]
        assert pagination.has_next == expected_pagination["hasNext"]
        assert pagination.has_previous == expected_pagination["hasPrevious"]

        # データ件数のチェック（per_page以下であることを確認）
        assert len(response.results) <= 100

        print(
            f"✅ ページネーション付きポートグループリスト取得テスト成功: ページ1, 1ページあたり100件"
        )
