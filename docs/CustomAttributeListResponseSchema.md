# CustomAttributeListResponseSchema

カスタム属性一覧のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | メッセージ | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) | ページネーション情報 | [optional] 
**partial_failure** | **bool** | 部分失敗フラグ (true|false) | 
**request_id** | **str** | リクエストID | [optional] 
**results** | [**List[CustomAttributeResponseSchema]**](CustomAttributeResponseSchema.md) | 実際のデータ | 
**success** | **bool** | 処理成功フラグ (true|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**truncated** | **bool** | 取得上限に達したvCenterがあり、結果と総件数が上限までの範囲に限られているか (true|false) | [optional] [default to False]
**vcenter_ws_sessions** | **object** | vCenterの接続状況 | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.custom_attribute_list_response_schema import CustomAttributeListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeListResponseSchema from a JSON string
custom_attribute_list_response_schema_instance = CustomAttributeListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeListResponseSchema.to_json())

# convert the object into a dict
custom_attribute_list_response_schema_dict = custom_attribute_list_response_schema_instance.to_dict()
# create an instance of CustomAttributeListResponseSchema from a dict
custom_attribute_list_response_schema_from_dict = CustomAttributeListResponseSchema.from_dict(custom_attribute_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


