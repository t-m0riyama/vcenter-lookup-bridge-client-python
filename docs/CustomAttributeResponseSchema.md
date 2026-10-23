# CustomAttributeResponseSchema

カスタム属性のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | カスタム属性の名前を示します。 | 
**object_id** | **str** | カスタム属性の値が設定されたオブジェクトのIDを示します。仮想マシンはインスタンスUUID、それ以外はmoRef IDです。割り当ての問い合わせ時のみ値が入ります。 | [optional] 
**object_name** | **str** | カスタム属性の値が設定されたオブジェクトの名前を示します。割り当ての問い合わせ時のみ値が入ります。 | [optional] 
**object_type** | **str** | カスタム属性を設定できるオブジェクトの種別を示します。グローバル属性の場合はGlobalです。 | 
**type** | **str** | カスタム属性の値の型を示します。 | 
**value** | **str** | オブジェクトに設定されたカスタム属性の値を示します。割り当ての問い合わせ時のみ値が入ります。 | [optional] 
**vcenter** | **str** | vCenter名を示します。 | 

## Example

```python
from vcenter_lookup_bridge_client.models.custom_attribute_response_schema import CustomAttributeResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CustomAttributeResponseSchema from a JSON string
custom_attribute_response_schema_instance = CustomAttributeResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CustomAttributeResponseSchema.to_json())

# convert the object into a dict
custom_attribute_response_schema_dict = custom_attribute_response_schema_instance.to_dict()
# create an instance of CustomAttributeResponseSchema from a dict
custom_attribute_response_schema_from_dict = CustomAttributeResponseSchema.from_dict(custom_attribute_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


