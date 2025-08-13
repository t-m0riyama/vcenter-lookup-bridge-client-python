# VCenterResponseSchema

vCenterのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_name** | **str** | vCenterのホスト名を示します。 | 
**name** | **str** |  | 
**port** | **int** | vCenterのポート番号を示します。 | 

## Example

```python
from vcenter_lookup_bridge_client.models.v_center_response_schema import VCenterResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VCenterResponseSchema from a JSON string
v_center_response_schema_instance = VCenterResponseSchema.from_json(json)
# print the JSON string representation of the object
print(VCenterResponseSchema.to_json())

# convert the object into a dict
v_center_response_schema_dict = v_center_response_schema_instance.to_dict()
# create an instance of VCenterResponseSchema from a dict
v_center_response_schema_from_dict = VCenterResponseSchema.from_dict(v_center_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


