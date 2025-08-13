# HealthcheckResponseSchema

ヘルスチェックのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**pagination** | [**PaginationInfo**](PaginationInfo.md) |  | [optional] 
**request_id** | **str** |  | [optional] 
**results** | [**HealthcheckSchema**](HealthcheckSchema.md) | 実際のデータ | 
**success** | **bool** | 処理成功フラグ (true|false) | 
**timestamp** | **str** | レスポンス生成時刻 | 
**vcenter_ws_sessions** | **object** |  | [optional] 

## Example

```python
from vcenter_lookup_bridge_client.models.healthcheck_response_schema import HealthcheckResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HealthcheckResponseSchema from a JSON string
healthcheck_response_schema_instance = HealthcheckResponseSchema.from_json(json)
# print the JSON string representation of the object
print(HealthcheckResponseSchema.to_json())

# convert the object into a dict
healthcheck_response_schema_dict = healthcheck_response_schema_instance.to_dict()
# create an instance of HealthcheckResponseSchema from a dict
healthcheck_response_schema_from_dict = HealthcheckResponseSchema.from_dict(healthcheck_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


