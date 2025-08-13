# AdminResponseSchema

ポートグループ一覧のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**request_id** | **str** |  | [optional] 
**results** | **object** |  | 
**success** | **bool** | 処理成功フラグ (true|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**vcenter_ws_sessions** | **object** |  | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.admin_response_schema import AdminResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AdminResponseSchema from a JSON string
admin_response_schema_instance = AdminResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AdminResponseSchema.to_json())

# convert the object into a dict
admin_response_schema_dict = admin_response_schema_instance.to_dict()
# create an instance of AdminResponseSchema from a dict
admin_response_schema_from_dict = AdminResponseSchema.from_dict(admin_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


