# EventListResponseSchema

イベント一覧のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**partial_failure** | **bool** | 部分失敗フラグ (true|false) | 
**request_id** | **str** |  | [optional] 
**results** | [**List[EventResponseSchema]**](EventResponseSchema.md) | 実際のデータ | 
**success** | **bool** | 処理成功フラグ (true|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**vcenter_ws_sessions** | **object** |  | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.event_list_response_schema import EventListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventListResponseSchema from a JSON string
event_list_response_schema_instance = EventListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EventListResponseSchema.to_json())

# convert the object into a dict
event_list_response_schema_dict = event_list_response_schema_instance.to_dict()
# create an instance of EventListResponseSchema from a dict
event_list_response_schema_from_dict = EventListResponseSchema.from_dict(event_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


