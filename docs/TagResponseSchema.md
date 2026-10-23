# TagResponseSchema

タグのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | タグの説明を示します。 | 
**name** | **str** | タグの名前を示します。 | 
**object_id** | **str** | タグが割り当てられたオブジェクトのIDを示します。仮想マシンはインスタンスUUID、それ以外はmoRef IDです。割り当ての問い合わせ時のみ値が入ります。 | [optional] 
**object_name** | **str** | タグが割り当てられたオブジェクトの名前を示します。割り当ての問い合わせ時のみ値が入ります。 | [optional] 
**tag_category** | **str** | タグのカテゴリを示します。 | 
**vcenter** | **str** | vCenter名を示します。 | 

## Example

```python
from vcenter_lookup_bridge_client.models.tag_response_schema import TagResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TagResponseSchema from a JSON string
tag_response_schema_instance = TagResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TagResponseSchema.to_json())

# convert the object into a dict
tag_response_schema_dict = tag_response_schema_instance.to_dict()
# create an instance of TagResponseSchema from a dict
tag_response_schema_from_dict = TagResponseSchema.from_dict(tag_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


