# vcenter_lookup_bridge_client.VmFoldersApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_vm_folders**](VmFoldersApi.md#list_vm_folders) | **GET** /vm_folders/ | List Vm Folders


# **list_vm_folders**
> VmFolderListResponseSchema list_vm_folders(vm_folders=vm_folders, offset=offset, max_results=max_results, vcenter=vcenter)

List Vm Folders

仮想マシンフォルダ一覧を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.vm_folder_list_response_schema import VmFolderListResponseSchema
from vcenter_lookup_bridge_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/vcenter-lookup-bridge/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = vcenter_lookup_bridge_client.Configuration(
    host = "http://localhost/vcenter-lookup-bridge/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = vcenter_lookup_bridge_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with vcenter_lookup_bridge_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vcenter_lookup_bridge_client.VmFoldersApi(api_client)
    vm_folders = ['[\"folder1\"]'] # List[str] | 仮想マシンフォルダの名前を指定します。 (optional)
    offset = 0 # int | 仮想マシンフォルダを取得する際の開始位置を指定します。 (optional) (default to 0)
    max_results = 100 # int | 仮想マシンフォルダを取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Vm Folders
        api_response = api_instance.list_vm_folders(vm_folders=vm_folders, offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of VmFoldersApi->list_vm_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VmFoldersApi->list_vm_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_folders** | [**List[str]**](str.md)| 仮想マシンフォルダの名前を指定します。 | [optional] 
 **offset** | **int**| 仮想マシンフォルダを取得する際の開始位置を指定します。 | [optional] [default to 0]
 **max_results** | **int**| 仮想マシンフォルダを取得する際の最大件数を指定します。 | [optional] [default to 100]
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**VmFolderListResponseSchema**](VmFolderListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定した条件の仮想マシンフォルダが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | 仮想マシンフォルダ情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

