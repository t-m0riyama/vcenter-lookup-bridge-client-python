# HealthcheckSchema

ヘルスチェックのスキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | サービスのステータスを示します。(ok|ng) | 
**vcenter_service_instances** | **str** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.healthcheck_schema import HealthcheckSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HealthcheckSchema from a JSON string
healthcheck_schema_instance = HealthcheckSchema.from_json(json)
# print the JSON string representation of the object
print(HealthcheckSchema.to_json())

# convert the object into a dict
healthcheck_schema_dict = healthcheck_schema_instance.to_dict()
# create an instance of HealthcheckSchema from a dict
healthcheck_schema_from_dict = HealthcheckSchema.from_dict(healthcheck_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


