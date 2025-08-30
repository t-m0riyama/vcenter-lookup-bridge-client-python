# EventResponseSchema

イベントのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_time** | **str** | イベントの作成時間を示します。（ISO 8601形式） | 
**datacenter** | **str** |  | 
**event_source** | **str** |  | 
**ip_address** | **str** |  | 
**message** | **str** | イベントのメッセージを示します。 | 
**user_name** | **str** |  | 
**vcenter** | **str** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.event_response_schema import EventResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponseSchema from a JSON string
event_response_schema_instance = EventResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EventResponseSchema.to_json())

# convert the object into a dict
event_response_schema_dict = event_response_schema_instance.to_dict()
# create an instance of EventResponseSchema from a dict
event_response_schema_from_dict = EventResponseSchema.from_dict(event_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


