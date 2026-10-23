# TagCategoryResponseSchema

タグカテゴリのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associable_types** | **List[str]** | タグを割り当てられるオブジェクトの種別を示します。空の場合は全ての種別に割り当てられます。 | 
**cardinality** | **str** | 1つのオブジェクトに割り当てられるタグの数(SINGLE: 1つのみ, MULTIPLE: 複数)を示します。 | 
**description** | **str** | タグカテゴリの説明を示します。 | 
**name** | **str** | タグカテゴリの名前を示します。 | 
**vcenter** | **str** | vCenter名を示します。 | 

## Example

```python
from vcenter_lookup_bridge_client.models.tag_category_response_schema import TagCategoryResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TagCategoryResponseSchema from a JSON string
tag_category_response_schema_instance = TagCategoryResponseSchema.from_json(json)
# print the JSON string representation of the object
print(TagCategoryResponseSchema.to_json())

# convert the object into a dict
tag_category_response_schema_dict = tag_category_response_schema_instance.to_dict()
# create an instance of TagCategoryResponseSchema from a dict
tag_category_response_schema_from_dict = TagCategoryResponseSchema.from_dict(tag_category_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


