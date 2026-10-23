# coding: utf-8

"""
vCenter Lookup Bridge API - TAGS APIテスト
"""

import pydantic
import pytest

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.tag_response_schema import TagResponseSchema


@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "tags_api"


@pytest.fixture
def api_instance(api_client):
    """Tags APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.TagsApi(api_client)


def _assert_tags(results, expected_results):
    """タグリストが期待結果と一致することをチェック"""
    assert len(results) == len(expected_results)
    for result, expected_result in zip(
        sorted(results, key=lambda r: (r.tag_category, r.name)),
        sorted(expected_results, key=lambda r: (r["tag_category"], r["name"])),
    ):
        assert isinstance(result, TagResponseSchema)
        assert result.name == expected_result["name"]
        assert result.tag_category == expected_result["tag_category"]
        assert result.description == expected_result["description"]
        assert result.vcenter == expected_result["vcenter"]
        assert result.object_name == expected_result["objectName"]
        assert result.object_id == expected_result["objectId"]


class TestTagsApi:
    """Tags API unit test"""

    def test_list_tags_success(self, api_instance, test_dataset):
        """タグリスト取得の成功テスト(全vCenter)"""
        response = api_instance.list_tags(**test_dataset.VALID_LIST_PARAMETERS)

        assert response is not None
        assert response.success is True
        assert response.truncated is False
        assert isinstance(response.results, list)
        assert len(response.results) > 0
        for result in response.results:
            assert isinstance(result, TagResponseSchema)
            # 割り当ての問い合わせでない場合は、オブジェクトの情報は入らない
            assert result.object_name is None
            assert result.object_id is None
        assert isinstance(response.pagination, PaginationInfo)
        assert response.pagination.total_count == len(response.results)

        print(f"✅ タグリスト取得テスト成功: {len(response.results)}件のタグが見つかりました")

    def test_list_tags_success_with_tag_category(self, api_instance, test_dataset):
        """タグリスト取得の成功テスト(カテゴリ指定)"""
        response = api_instance.list_tags(**test_dataset.VALID_LIST_PARAMETERS_TAG_CATEGORY)

        assert response.success is True
        _assert_tags(response.results, test_dataset.EXPECTED_TAG_LIST_TAG_CATEGORY["results"])

        print(f"✅ タグリスト取得テスト(カテゴリ指定)成功: {len(response.results)}件のタグが見つかりました")

    def test_list_tags_success_with_object(self, api_instance, test_dataset):
        """オブジェクトに割り当てられたタグの取得の成功テスト"""
        response = api_instance.list_tags(**test_dataset.VALID_LIST_PARAMETERS_OBJECT)

        assert response.success is True
        _assert_tags(response.results, test_dataset.EXPECTED_TAG_LIST_OBJECT["results"])

        print(f"✅ オブジェクトに割り当てられたタグの取得テスト成功: {len(response.results)}件のタグが見つかりました")

    def test_list_tags_with_pagination(self, api_instance, test_dataset):
        """ページネーション付きタグリスト取得のテスト"""
        response = api_instance.list_tags(**test_dataset.VALID_LIST_PARAMETERS_PAGINATION)

        assert response.success is True
        assert len(response.results) <= test_dataset.VALID_LIST_PARAMETERS_PAGINATION["max_results"]
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)
        assert pagination.offset == test_dataset.VALID_LIST_PARAMETERS_PAGINATION["offset"]
        assert pagination.has_previous is True

        print(f"✅ ページネーション付きタグリスト取得テスト成功")

    def test_list_tags_not_found_with_invalid_tag_category(self, api_instance, test_dataset):
        """存在しないカテゴリのタグ取得のテスト"""
        try:
            api_instance.list_tags(**test_dataset.INVALID_LIST_PARAMETERS_TAG_CATEGORY)
            pytest.fail("存在しないカテゴリのタグ取得テストで、想定される例外が発生しませんでした。")
        except Exception as e:
            if "404" in str(e):
                print(f"✅ 存在しないカテゴリのタグ取得テスト成功: 404エラーが正しく返されました")
            else:
                pytest.fail(f"存在しないカテゴリのタグ取得テストで予期しないエラーが発生しました: {str(e)}")

    def test_list_tags_not_found_with_invalid_vcenter(self, api_instance, test_dataset):
        """存在しないvCenterのタグ取得のテスト"""
        try:
            api_instance.list_tags(**test_dataset.INVALID_LIST_PARAMETERS_VCENTER)
            pytest.fail("存在しないvCenterのタグ取得テストで、想定される例外が発生しませんでした。")
        except Exception as e:
            if "404" in str(e):
                print(f"✅ 存在しないvCenterのタグ取得テスト成功: 404エラーが正しく返されました")
            else:
                pytest.fail(f"存在しないvCenterのタグ取得テストで予期しないエラーが発生しました: {str(e)}")

    def test_list_tags_with_invalid_object_type(self, api_instance, test_dataset):
        """サポート外のオブジェクトの種別を指定したテスト"""
        try:
            api_instance.list_tags(**test_dataset.INVALID_LIST_PARAMETERS_OBJECT_TYPE)
            pytest.fail("サポート外のオブジェクトの種別を指定したテストで、想定される例外が発生しませんでした。")
        except Exception as e:
            if "422" in str(e):
                print(f"✅ サポート外のオブジェクトの種別を指定したテスト成功: 422エラーが正しく返されました")
            else:
                pytest.fail(f"サポート外のオブジェクトの種別を指定したテストで予期しないエラーが発生しました: {str(e)}")

    def test_list_tags_with_invalid_object_id(self, api_instance, test_dataset):
        """仮想マシン以外にobject_idを指定したテスト"""
        try:
            api_instance.list_tags(**test_dataset.INVALID_LIST_PARAMETERS_OBJECT_ID)
            pytest.fail("仮想マシン以外にobject_idを指定したテストで、想定される例外が発生しませんでした。")
        except Exception as e:
            if "422" in str(e):
                print(f"✅ 仮想マシン以外にobject_idを指定したテスト成功: 422エラーが正しく返されました")
            else:
                pytest.fail(f"仮想マシン以外にobject_idを指定したテストで予期しないエラーが発生しました: {str(e)}")

    def test_list_tags_with_invalid_max_results(self, api_instance, test_dataset):
        """タグリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_tags(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS)
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_tags(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2)

    def test_list_tags_with_invalid_offset(self, api_instance, test_dataset):
        """タグリスト取得のテスト（offsetパラメータの制限が有効であることを確認）"""
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_tags(**test_dataset.INVALID_LIST_PARAMETERS_OFFSET)
