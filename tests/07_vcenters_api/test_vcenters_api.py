# coding: utf-8

"""
vCenter Lookup Bridge API - vCenters APIテスト
"""

import pytest
from typing import Dict, Any

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.v_center_response_schema import (
    VCenterResponseSchema,
)


@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "vcenters_api"


@pytest.fixture
def api_instance(api_client):
    """vCenters APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.VcentersApi(api_client)


class TestVcentersApi:
    """vCenters API unit test"""

    def test_get_vcenter_success(self, api_instance, test_dataset):
        """単一vCenter取得(vCenter指定)の成功テスト"""
        # APIを呼び出し
        response = api_instance.list_vcenters(
            **test_dataset.VALID_LIST_PARAMETERS_VCENTER
        )

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert results is not None

        # １件のvCenterのみ返却されることをチェック
        assert len(results) == 1

        # レスポンスデータがスキーマに適合していることをチェック
        assert isinstance(results[0], VCenterResponseSchema)

        # 期待結果との比較
        assert results[0].name == test_dataset.EXPECTED_VCENTER["name"]
        assert results[0].host_name == test_dataset.EXPECTED_VCENTER["hostName"]
        assert results[0].port == test_dataset.EXPECTED_VCENTER["port"]

        print(f"✅ VCENTER取得テスト成功: {results[0].name}")

    def test_list_vcenter_not_found_with_invalid_vcenter(
        self, api_instance, test_dataset
    ):
        """存在しないVCENTER取得のテスト(vCenter指定)"""
        try:
            # 存在しないvCenterでAPIを呼び出し
            response = api_instance.list_vcenters(
                **test_dataset.INVALID_LIST_PARAMETERS_VCENTER
            )

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

    def test_list_vcenters_success(self, api_instance, test_dataset):
        """vCenterリスト取得の成功テスト"""
        # APIを呼び出し
        response = api_instance.list_vcenters(**test_dataset.VALID_LIST_PARAMETERS)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数の仮想マシンが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_VCENTER_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, VCenterResponseSchema)

        # ページネーション情報は非サポートであることをチェック
        pagination = response.pagination
        assert pagination is None

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_VCENTER_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.host_name == expected_result["hostName"]
            assert result.port == expected_result["port"]

        print(
            f"✅ VCENTERリスト取得テスト成功: {len(response.results)}件のVMが見つかりました"
        )

    def test_list_vcenters_with_pagination(self, api_instance, test_dataset):
        """ページネーション付きVMリスト取得のテスト（ページネーション機能は非サポート）"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = api_instance.list_vcenters(
            **test_dataset.VALID_LIST_PARAMETERS_VCENTER
        )

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        assert isinstance(response.results, list)

        # ページネーション情報は非サポートであることをチェック
        pagination = response.pagination
        assert pagination is None

        # データ件数のチェック（per_page以下であることを確認）
        assert len(response.results) <= 100

        print(f"✅ VCENTERリスト取得テスト成功(ページネーション機能は非サポート)")
