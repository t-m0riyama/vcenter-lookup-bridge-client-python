# VmSnapshotResponseSchema

仮想マシンスナップショットのレスポンススキーマ

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **str** | スナップショットの作成日時を示します。 | 
**datacenter** | **str** | 仮想マシンのデータセンターを示します。 | 
**description** | **str** |  | 
**has_child** | **bool** | このスナップショットを元とした子スナップショットが存在する場合はTrue、存在しない場合はFalseがセットされます。 | 
**id** | **int** |  | 
**name** | **str** | スナップショットの名前を示します。 | 
**parent_id** | **int** |  | 
**vcenter** | **str** |  | 
**vm_folder** | **str** |  | 
**vm_instance_uuid** | **str** | 仮想マシンのインスタンスUUIDを示します。 | 
**vm_name** | **str** | 仮想マシンの名前を示します。 | 

## Example

```python
from vcenter_lookup_bridge_client.models.vm_snapshot_response_schema import VmSnapshotResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of VmSnapshotResponseSchema from a JSON string
vm_snapshot_response_schema_instance = VmSnapshotResponseSchema.from_json(json)
# print the JSON string representation of the object
print(VmSnapshotResponseSchema.to_json())

# convert the object into a dict
vm_snapshot_response_schema_dict = vm_snapshot_response_schema_instance.to_dict()
# create an instance of VmSnapshotResponseSchema from a dict
vm_snapshot_response_schema_from_dict = VmSnapshotResponseSchema.from_dict(vm_snapshot_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


