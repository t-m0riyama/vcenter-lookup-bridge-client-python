# ClusterResponseSchema

クラスタのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** | クラスタに所属するホストの名前を示します。 | 
**name** | **str** | 仮想マシンフォルダの名前を示します。 | 
**status** | **str** | クラスタのステータスを示します。 | 
**vcenter** | **str** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.cluster_response_schema import ClusterResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResponseSchema from a JSON string
cluster_response_schema_instance = ClusterResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ClusterResponseSchema.to_json())

# convert the object into a dict
cluster_response_schema_dict = cluster_response_schema_instance.to_dict()
# create an instance of ClusterResponseSchema from a dict
cluster_response_schema_from_dict = ClusterResponseSchema.from_dict(cluster_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


