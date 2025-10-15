# HostDetailResponseSchema

ESXiホストの詳細情報のレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** |  | 
**cpu_model** | **str** | ESXiホストのCPUモデルを示します。 | 
**datacenter** | **str** | ESXiホストのデータセンターを示します。 | 
**datastores** | **List[object]** |  | 
**esxi_version** | **str** | ESXiホストのバージョンを示します。 | 
**esxi_version_full** | **str** | ESXiホストのビルド番号を含む、バージョンを示します。 | 
**hardware_model** | **str** | ESXiホストのハードウェアモデルを示します。 | 
**hardware_vendor** | **str** | ESXiホストのハードウェアベンダーを示します。 | 
**ip_address** | **str** |  | 
**memory_size_mb** | **int** | ESXiホストのメモリサイズ(MB)を示します。 | 
**name** | **str** | ESXiホストの名前(ホスト名)を示します。 | 
**num_cpu_cores** | **int** | ESXiホストのCPUコア数を示します。 | 
**num_cpu_sockets** | **int** | ESXiホストのCPUソケット数を示します。 | 
**num_cpu_threads** | **int** | ESXiホストのCPUスレッド数を示します。 | 
**portgroups** | **List[object]** |  | 
**power_state** | **str** | ESXiホストの電源の状態を示します。 | 
**status** | **str** | ESXiホストのステータスを示します。 | 
**uuid** | **str** | ESXiホストのUUIDを示します。 | 
**vcenter** | **str** |  | 
**vswitches** | **List[object]** |  | 

## Example

```python
from vcenter_lookup_bridge_client.models.host_detail_response_schema import HostDetailResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HostDetailResponseSchema from a JSON string
host_detail_response_schema_instance = HostDetailResponseSchema.from_json(json)
# print the JSON string representation of the object
print(HostDetailResponseSchema.to_json())

# convert the object into a dict
host_detail_response_schema_dict = host_detail_response_schema_instance.to_dict()
# create an instance of HostDetailResponseSchema from a dict
host_detail_response_schema_from_dict = HostDetailResponseSchema.from_dict(host_detail_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


