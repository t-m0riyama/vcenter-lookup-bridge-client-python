# coding: utf-8

"""
vCenter Lookup Bridge API - CUSTOM ATTRIBUTES APIテスト
"""

import pydantic
import pytest

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.custom_attribute_response_schema import CustomAttributeResponseSchema


@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "custom_attributes_api"


@pytest.fixture
def api_instance(api_client):
    """Custom Attributes APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.CustomAttributesApi(api_client)


class TestCustomAttributesApi:
    """Custom Attributes API unit test"""

    def test_list_custom_attributes_success(self, api_instance, test_dataset):
        """カスタム属性リスト取得の成功テスト"""
        response = api_instance.list_custom_attributes(**test_dataset.VALID_LIST_PARAMETERS)

        assert response is not None
        assert response.success is True
        assert response.truncated is False
        assert isinstance(response.results, list)
        assert len(response.results) > 0
        for result in response.results:
            assert isinstance(result, CustomAttributeResponseSchema)
            assert result.vcenter == test_dataset.VALID_VCENTER
            # 割り当ての問い合わせでない場合は、値とオブジェクトの情報は入らない
            assert result.value is None
            assert result.object_name is None
            assert result.object_id is None
        assert isinstance(response.pagination, PaginationInfo)
        assert response.pagination.total_count == len(response.results)

        print(f"✅ カスタム属性リスト取得テスト成功: {len(response.results)}件のカスタム属性が見つかりました")

    def test_list_custom_attributes_success_with_object_type(self, api_instance, test_dataset):
        """カスタム属性リスト取得の成功テスト(種別で定義を絞り込み)"""
        response = api_instance.list_custom_attributes(**test_dataset.VALID_LIST_PARAMETERS_OBJECT_TYPE)

        assert response.success is True
        expected_results = test_dataset.EXPECTED_CUSTOM_ATTRIBUTE_LIST_OBJECT_TYPE["results"]
        assert len(response.results) == len(expected_results)
        for result, expected_result in zip(
            sorted(response.results, key=lambda r: r.name),
            sorted(expected_results, key=lambda r: r["name"]),
        ):
            assert result.name == expected_result["name"]
            assert result.object_type == expected_result["objectType"]
            assert result.type == expected_result["type"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.value == expected_result["value"]

        print(f"✅ カスタム属性リスト取得テスト(種別指定)成功: {len(response.results)}件のカスタム属性が見つかりました")

    def test_list_custom_attributes_with_pagination(self, api_instance, test_dataset):
        """ページネーション付きカスタム属性リスト取得のテスト"""
        response = api_instance.list_custom_attributes(**test_dataset.VALID_LIST_PARAMETERS_PAGINATION)

        assert response.success is True
        assert len(response.results) <= test_dataset.VALID_LIST_PARAMETERS_PAGINATION["max_results"]
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)
        assert pagination.offset == test_dataset.VALID_LIST_PARAMETERS_PAGINATION["offset"]
        assert pagination.has_previous is True

        print(f"✅ ページネーション付きカスタム属性リスト取得テスト成功")

    @pytest.mark.parametrize(
        "params_name",
        ["INVALID_LIST_PARAMETERS_OBJECT_TYPE", "INVALID_LIST_PARAMETERS_OBJECT_NAME", "INVALID_LIST_PARAMETERS_VCENTER"],
    )
    def test_list_custom_attributes_not_found(self, api_instance, test_dataset, params_name):
        """該当するカスタム属性がない場合のテスト(種別・オブジェクト・vCenter)"""
        try:
            api_instance.list_custom_attributes(**getattr(test_dataset, params_name))
            pytest.fail(f"該当するカスタム属性がない場合のテスト({params_name})で、想定される例外が発生しませんでした。")
        except Exception as e:
            if "404" in str(e):
                print(f"✅ 該当するカスタム属性がない場合のテスト({params_name})成功: 404エラーが正しく返されました")
            else:
                pytest.fail(f"該当するカスタム属性がない場合のテスト({params_name})で予期しないエラーが発生しました: {str(e)}")

    def test_list_custom_attributes_with_invalid_max_results(self, api_instance, test_dataset):
        """カスタム属性リスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_custom_attributes(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS)
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_custom_attributes(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2)

    def test_list_custom_attributes_with_invalid_offset(self, api_instance, test_dataset):
        """カスタム属性リスト取得のテスト（offsetパラメータの制限が有効であることを確認）"""
        with pytest.raises(pydantic.ValidationError):
            api_instance.list_custom_attributes(**test_dataset.INVALID_LIST_PARAMETERS_OFFSET)
