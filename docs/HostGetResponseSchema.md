# HostGetResponseSchema

単一ESXiホストのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**request_id** | **str** |  | [optional] 
**results** | [**HostResponseSchema**](HostResponseSchema.md) | 実際のデータ | 
**success** | **bool** | 処理成功フラグ (true|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**vcenter_ws_sessions** | **object** |  | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.host_get_response_schema import HostGetResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HostGetResponseSchema from a JSON string
host_get_response_schema_instance = HostGetResponseSchema.from_json(json)
# print the JSON string representation of the object
print(HostGetResponseSchema.to_json())

# convert the object into a dict
host_get_response_schema_dict = host_get_response_schema_instance.to_dict()
# create an instance of HostGetResponseSchema from a dict
host_get_response_schema_from_dict = HostGetResponseSchema.from_dict(host_get_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


