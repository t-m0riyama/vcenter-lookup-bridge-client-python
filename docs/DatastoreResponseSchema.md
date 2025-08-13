# DatastoreResponseSchema

データストア情報のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_gb** | **int** | データストアの容量(GB)を示します。 | 
**free_space_gb** | **int** | データストアの空き容量(GB)を示します。 | 
**hosts** | **List[str]** | データストアをマウント済みのESXiホストを示します。 | 
**name** | **str** | データストアの名前を示します。 | 
**tag_category** | **str** |  | 
**tags** | **List[str]** |  | 
**type** | **str** | データストアのタイプ（VMFS, NFS, ...）を示します。 | 
**vcenter** | **str** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.datastore_response_schema import DatastoreResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DatastoreResponseSchema from a JSON string
datastore_response_schema_instance = DatastoreResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DatastoreResponseSchema.to_json())

# convert the object into a dict
datastore_response_schema_dict = datastore_response_schema_instance.to_dict()
# create an instance of DatastoreResponseSchema from a dict
datastore_response_schema_from_dict = DatastoreResponseSchema.from_dict(datastore_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


