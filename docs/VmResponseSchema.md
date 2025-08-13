# VmResponseSchema

仮想マシンのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster** | **str** |  | 
**datacenter** | **str** | 仮想マシンのデータセンターを示します。 | 
**disk_devices** | **List[object]** |  | 
**esxi_hostname** | **str** |  | 
**guest_full_name** | **str** | 仮想マシンのゲストOSの種別をフルネームを示します。 | 
**hostname** | **str** |  | 
**hw_version** | **str** | 仮想マシンのハードウェアバージョンを示します。 | 
**instance_uuid** | **str** | 仮想マシンのインスタンスUUIDを示します。 | 
**ip_address** | **str** |  | 
**memory_size_mb** | **int** | 仮想マシンのメモリサイズ(MB)を示します。 | 
**name** | **str** | 仮想マシンの名前を示します。 | 
**network_devices** | **List[object]** |  | 
**num_cpu** | **int** | 仮想マシンのCPU数を示します。 | 
**power_state** | **str** | 仮想マシンの電源の状態を示します。 | 
**template** | **bool** | 仮想マシンがテンプレートかどうかを示します。 | 
**uuid** | **str** | 仮想マシンのUUIDを示します。 | 
**vcenter** | **str** |  | 
**vm_folder** | **str** |  | 
**vm_path_name** | **str** | 仮想マシンのVMXファイルのパスを示します。 | 

## Example

```python
from vcenter_lookup_bridge_client.models.vm_response_schema import VmResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VmResponseSchema from a JSON string
vm_response_schema_instance = VmResponseSchema.from_json(json)
# print the JSON string representation of the object
print(VmResponseSchema.to_json())

# convert the object into a dict
vm_response_schema_dict = vm_response_schema_instance.to_dict()
# create an instance of VmResponseSchema from a dict
vm_response_schema_from_dict = VmResponseSchema.from_dict(vm_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


