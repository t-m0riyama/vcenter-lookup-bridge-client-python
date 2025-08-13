# PortgroupResponseSchema

ポートグループのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** |  | 
**name** | **str** | ポートグループの名前を示します。 | 
**tag_category** | **str** |  | 
**tags** | **List[str]** |  | 
**vcenter** | **str** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.portgroup_response_schema import PortgroupResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PortgroupResponseSchema from a JSON string
portgroup_response_schema_instance = PortgroupResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PortgroupResponseSchema.to_json())

# convert the object into a dict
portgroup_response_schema_dict = portgroup_response_schema_instance.to_dict()
# create an instance of PortgroupResponseSchema from a dict
portgroup_response_schema_from_dict = PortgroupResponseSchema.from_dict(portgroup_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


