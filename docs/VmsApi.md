# vcenter_lookup_bridge_client.VmsApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vm**](VmsApi.md#get_vm) | **GET** /vms/{vm_instance_uuid} | Get Vm
[**list_vms**](VmsApi.md#list_vms) | **GET** /vms/ | List Vms


# **get_vm**
> VmListResponseSchema get_vm(vm_instance_uuid, vcenter)

Get Vm

インスタンスUUIDを指定して、単一の仮想マシンの情報を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.vm_list_response_schema import VmListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.VmsApi(api_client)
    vm_instance_uuid = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # str | インスタンスUUIDを指定します。※格納されている仮想マシンフォルダに関係なく、vmFolder属性はnullを返します。
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。

    try:
        # Get Vm
        api_response = api_instance.get_vm(vm_instance_uuid, vcenter)
        print("The response of VmsApi->get_vm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VmsApi->get_vm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_instance_uuid** | **str**| インスタンスUUIDを指定します。※格納されている仮想マシンフォルダに関係なく、vmFolder属性はnullを返します。 | 
 **vcenter** | **str**| vCenterの名前を指定します。 | 

### Return type

[**VmListResponseSchema**](VmListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定したインスタンスUUIDを持つ仮想マシンが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | 仮想マシン情報を取得中にエラーが発生した場合に返されます |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vms**
> VmListResponseSchema list_vms(vm_folders, offset=offset, max_results=max_results, vcenter=vcenter)

List Vms

仮想マシンフォルダを指定して、同フォルダ中の仮想マシン一覧を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.vm_list_response_schema import VmListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.VmsApi(api_client)
    vm_folders = ['[folder1]'] # List[str] | 仮想マシンフォルダの名前を指定します。
    offset = 0 # int | 仮想マシンフォルダ中の仮想マシンを取得する際の開始位置を指定します。 (optional) (default to 0)
    max_results = 100 # int | 仮想マシンフォルダ中の仮想マシンを取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Vms
        api_response = api_instance.list_vms(vm_folders, offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of VmsApi->list_vms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VmsApi->list_vms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vm_folders** | [**List[str]**](str.md)| 仮想マシンフォルダの名前を指定します。 | 
 **offset** | **int**| 仮想マシンフォルダ中の仮想マシンを取得する際の開始位置を指定します。 | [optional] [default to 0]
 **max_results** | **int**| 仮想マシンフォルダ中の仮想マシンを取得する際の最大件数を指定します。 | [optional] [default to 100]
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**VmListResponseSchema**](VmListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定した仮想マシンフォルダ中に仮想マシンが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | 仮想マシン情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

