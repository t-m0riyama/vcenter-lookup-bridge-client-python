# ThreadPoolResponseSchema

スレッド枠の状態確認のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**partial_failure** | **bool** | 部分失敗フラグ (true\|false) | 
**request_id** | **str** |  | [optional] 
**results** | [**ThreadPoolSchema**](ThreadPoolSchema.md) | 実際のデータ | 
**success** | **bool** | 処理成功フラグ (true\|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**truncated** | **bool** | 取得上限に達したvCenterがあり、結果と総件数が上限までの範囲に限られているか (true\|false) | [optional] [default to False]
**vcenter_ws_sessions** | **Dict[str, object]** |  | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.thread_pool_response_schema import ThreadPoolResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadPoolResponseSchema from a JSON string
thread_pool_response_schema_instance = ThreadPoolResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ThreadPoolResponseSchema.to_json())

# convert the object into a dict
thread_pool_response_schema_dict = thread_pool_response_schema_instance.to_dict()
# create an instance of ThreadPoolResponseSchema from a dict
thread_pool_response_schema_from_dict = ThreadPoolResponseSchema.from_dict(thread_pool_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
