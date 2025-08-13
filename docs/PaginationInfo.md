# PaginationInfo

ページネーション情報

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_next** | **bool** | 次のページが存在するか | 
**has_previous** | **bool** | 前のページが存在するか | 
**limit** | **int** | 取得件数制限 | 
**offset** | **int** | 現在のオフセット | 
**total_count** | **int** | 総件数 | 

## Example

```python
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationInfo from a JSON string
pagination_info_instance = PaginationInfo.from_json(json)
# print the JSON string representation of the object
print(PaginationInfo.to_json())

# convert the object into a dict
pagination_info_dict = pagination_info_instance.to_dict()
# create an instance of PaginationInfo from a dict
pagination_info_from_dict = PaginationInfo.from_dict(pagination_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


