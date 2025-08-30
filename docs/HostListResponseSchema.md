# HostListResponseSchema

ESXiホスト一覧のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**request_id** | **str** |  | [optional] 
**results** | [**List[HostResponseSchema]**](HostResponseSchema.md) | 実際のデータ | 
**success** | **bool** | 処理成功フラグ (true|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**vcenter_ws_sessions** | **object** |  | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.host_list_response_schema import HostListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HostListResponseSchema from a JSON string
host_list_response_schema_instance = HostListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(HostListResponseSchema.to_json())

# convert the object into a dict
host_list_response_schema_dict = host_list_response_schema_instance.to_dict()
# create an instance of HostListResponseSchema from a dict
host_list_response_schema_from_dict = HostListResponseSchema.from_dict(host_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


