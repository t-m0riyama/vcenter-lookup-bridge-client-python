# HostResponseSchema

ESXiホストのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenter** | **str** | ESXiホストのデータセンターを示します。 | 
**esxi_version** | **str** | ESXiホストのバージョンを示します。 | 
**memory_size_mb** | **int** | ESXiホストのメモリサイズ(MB)を示します。 | 
**name** | **str** | ESXiホストの名前(ホスト名)を示します。 | 
**num_cpu_cores** | **int** | ESXiホストのCPUコア数を示します。 | 
**num_cpu_sockets** | **int** | ESXiホストのCPUソケット数を示します。 | 
**num_cpu_threads** | **int** | ESXiホストのCPUスレッド数を示します。 | 
**status** | **str** | ESXiホストのステータスを示します。 | 
**uuid** | **str** | ESXiホストのUUIDを示します。 | 
**vcenter** | **str** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.host_response_schema import HostResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HostResponseSchema from a JSON string
host_response_schema_instance = HostResponseSchema.from_json(json)
# print the JSON string representation of the object
print(HostResponseSchema.to_json())

# convert the object into a dict
host_response_schema_dict = host_response_schema_instance.to_dict()
# create an instance of HostResponseSchema from a dict
host_response_schema_from_dict = HostResponseSchema.from_dict(host_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


