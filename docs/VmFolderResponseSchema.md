# VmFolderResponseSchema

仮想マシンフォルダのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 仮想マシンフォルダの名前を示します。 | 
**vcenter** | **str** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.vm_folder_response_schema import VmFolderResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VmFolderResponseSchema from a JSON string
vm_folder_response_schema_instance = VmFolderResponseSchema.from_json(json)
# print the JSON string representation of the object
print(VmFolderResponseSchema.to_json())

# convert the object into a dict
vm_folder_response_schema_dict = vm_folder_response_schema_instance.to_dict()
# create an instance of VmFolderResponseSchema from a dict
vm_folder_response_schema_from_dict = VmFolderResponseSchema.from_dict(vm_folder_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


