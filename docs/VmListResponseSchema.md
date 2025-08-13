# VmListResponseSchema

仮想マシン一覧のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**request_id** | **str** |  | [optional] 
**results** | [**List[VmResponseSchema]**](VmResponseSchema.md) | 実際のデータ | 
**success** | **bool** | 処理成功フラグ (true|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**vcenter_ws_sessions** | **object** |  | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.vm_list_response_schema import VmListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VmListResponseSchema from a JSON string
vm_list_response_schema_instance = VmListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(VmListResponseSchema.to_json())

# convert the object into a dict
vm_list_response_schema_dict = vm_list_response_schema_instance.to_dict()
# create an instance of VmListResponseSchema from a dict
vm_list_response_schema_from_dict = VmListResponseSchema.from_dict(vm_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


