# VmGetResponseSchema

単一仮想マシンのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**partial_failure** | **bool** | 部分失敗フラグ (true|false) | 
**request_id** | **str** |  | [optional] 
**results** | [**VmDetailResponseSchema**](VmDetailResponseSchema.md) | 実際のデータ | 
**success** | **bool** | 処理成功フラグ (true|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**vcenter_ws_sessions** | **object** |  | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.vm_get_response_schema import VmGetResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VmGetResponseSchema from a JSON string
vm_get_response_schema_instance = VmGetResponseSchema.from_json(json)
# print the JSON string representation of the object
print(VmGetResponseSchema.to_json())

# convert the object into a dict
vm_get_response_schema_dict = vm_get_response_schema_instance.to_dict()
# create an instance of VmGetResponseSchema from a dict
vm_get_response_schema_from_dict = VmGetResponseSchema.from_dict(vm_get_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


