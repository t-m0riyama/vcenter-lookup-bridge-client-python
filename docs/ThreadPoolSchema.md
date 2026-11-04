# ThreadPoolSchema

応答したワーカーのAnyIO既定スレッド枠の状態

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | スレッド枠の状態。(ok\|saturated) | 
**process_id** | **int** | 応答したワーカープロセスのPID | 
**total_tokens** | **int** | スレッド枠の総数 | 
**borrowed_tokens** | **int** | 使用中のスレッド枠数 | 
**available_tokens** | **int** | 空いているスレッド枠数 | 
**tasks_waiting** | **int** | スレッド枠の取得を待つタスク数。HTTPリクエスト数とは異なります。 | 

## Example

```python
from vcenter_lookup_bridge_client.models.thread_pool_schema import ThreadPoolSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadPoolSchema from a JSON string
thread_pool_schema_instance = ThreadPoolSchema.from_json(json)
# print the JSON string representation of the object
print(ThreadPoolSchema.to_json())

# convert the object into a dict
thread_pool_schema_dict = thread_pool_schema_instance.to_dict()
# create an instance of ThreadPoolSchema from a dict
thread_pool_schema_from_dict = ThreadPoolSchema.from_dict(thread_pool_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
