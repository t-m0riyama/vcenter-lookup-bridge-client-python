# coding: utf-8

"""
vCenter Lookup Bridge API - TAG CATEGORIES APIテスト
"""

import pydantic
import pytest

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.tag_category_response_schema import TagCategoryResponseSchema


@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "tag_categories_api"


@pytest.fixture
def api_instance(api_client):
    """Tag Categories APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.TagCategoriesApi(api_client)


class TestTagCategoriesApi:
    """Tag Categories API unit test"""

    def test_list_tag_categories_success(self, api_instance, test_dataset):
        """タグカテゴリリスト取得の成功テスト"""
        response = api_instance.list_tag_categories(**test_dataset.VALID_LIST_PARAMETERS)

        assert response is not None
        assert response.success is True
        assert response.truncated is False
        assert isinstance(response.pagination, PaginationInfo)

        expected_results = test_dataset.EXPECTED_TAG_CATEGORY_LIST["results"]
        assert len(response.results) == len(expected_results)
        for result, expected_result in zip(
            sorted(response.results, key=lambda r: r.name),
            sorted(expected_results, key=lambda r: r["name"]),
        ):
            assert isinstance(result, TagCategoryResponseSchema)
            assert result.name == expected_result["name"]
            assert result.description == expected_result["description"]
            assert result.cardinality == expected_result["cardinality"]
            assert sorted(result.associable_types) == sorted(expected_result["associableTypes"])
            assert result.vcenter == expected_result["vcenter"]

        print(f"✅ タグカテゴリリスト取得テスト成功: {len(response.results)}件のタグカテゴリが見つかりました")

    def test_list_tag_categories_with_pagination(self, api_instance, test_dataset):
        """ページネーション付きタグカテゴリリスト取得のテスト"""
        response = api_instance.list_tag_categories(**test_dataset.VALID_LIST_PARAMETERS_PAGINATION)

        assert response.success is True
        assert len(response.results) <= test_dataset.VALID_LIST_PARAMETERS_PAGINATION["max_results"]
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)
        assert pagination.offset == test_dataset.VALID_LIST_PARAMETERS_PAGINATION["offset"]
        assert pagination.has_previous is True

        print(f"✅ ページネーション付きタグカテゴリリスト取得テスト成功")

    def test_list_tag_categories_not_found_with_invalid_vcenter(self, api_instance, test_dataset):
        """存在しないvCenterのタグカテゴリ取得のテスト"""
        try:
            api_instance.list_tag_categories(**test_dataset.INVALID_LIST_PARAMETERS_VCENTER)
            pytest.fail("存在しないvCenterのタグカテゴリ取得テストで、想定される例外が発生しませんでした。")
        except Exception as e:
            if "404" in str(e):
                print(f"✅ 存在しないvCenterのタグカテゴリ取得テスト成功: 404エラーが正しく返されました")
            else:
                pytest.fail(f"存在しないvCenterのタグカテゴリ取得テストで予期しないエラーが発生しました: {str(e)}")

    def test_list_tag_categories_with_invalid_max_results(self, api_instance, test_dataset):
        """タグカテゴリリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_tag_categories(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS)
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_tag_categories(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2)

    def test_list_tag_categories_with_invalid_offset(self, api_instance, test_dataset):
        """タグカテゴリリスト取得のテスト（offsetパラメータの制限が有効であることを確認）"""
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_tag_categories(**test_dataset.INVALID_LIST_PARAMETERS_OFFSET)
