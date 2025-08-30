# AlarmResponseSchema

アラームのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged** | **bool** | アラームが確認済みかどうかを示します。 | 
**acknowledged_time** | **str** |  | 
**alarm_source** | **str** |  | 
**created_time** | **str** | アラームの作成時間を示します。（ISO 8601形式） | 
**datacenter** | **str** |  | 
**description** | **str** | アラームの説明を示します。 | 
**name** | **str** |  | 
**status** | **str** | アラームのステータスを示します。 | 
**vcenter** | **str** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.alarm_response_schema import AlarmResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmResponseSchema from a JSON string
alarm_response_schema_instance = AlarmResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AlarmResponseSchema.to_json())

# convert the object into a dict
alarm_response_schema_dict = alarm_response_schema_instance.to_dict()
# create an instance of AlarmResponseSchema from a dict
alarm_response_schema_from_dict = AlarmResponseSchema.from_dict(alarm_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


