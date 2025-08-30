# vcenter_lookup_bridge_client.HostsApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_host**](HostsApi.md#get_host) | **GET** /hosts/{host_uuid} | Get Host
[**list_hosts**](HostsApi.md#list_hosts) | **GET** /hosts/ | List Hosts


# **get_host**
> HostGetResponseSchema get_host(host_uuid, vcenter)

Get Host

ESXiホストのUUIDを指定して、単一のESXiホストの情報を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.host_get_response_schema import HostGetResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.HostsApi(api_client)
    host_uuid = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # str | ホストUUIDを指定します。
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。

    try:
        # Get Host
        api_response = api_instance.get_host(host_uuid, vcenter)
        print("The response of HostsApi->get_host:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->get_host: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_uuid** | **str**| ホストUUIDを指定します。 | 
 **vcenter** | **str**| vCenterの名前を指定します。 | 

### Return type

[**HostGetResponseSchema**](HostGetResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定したESXiホストUUIDを持つESXiホストが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | ESXiホスト情報を取得中にエラーが発生した場合に返されます |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hosts**
> HostListResponseSchema list_hosts(offset=offset, max_results=max_results, vcenter=vcenter)

List Hosts

ESXiホスト一覧を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.host_list_response_schema import HostListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.HostsApi(api_client)
    offset = 0 # int | ESXiホスト一覧を取得する際の開始位置を指定します。 (optional) (default to 0)
    max_results = 100 # int | ESXiホスト一覧を取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Hosts
        api_response = api_instance.list_hosts(offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of HostsApi->list_hosts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HostsApi->list_hosts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| ESXiホスト一覧を取得する際の開始位置を指定します。 | [optional] [default to 0]
 **max_results** | **int**| ESXiホスト一覧を取得する際の最大件数を指定します。 | [optional] [default to 100]
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**HostListResponseSchema**](HostListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | ESXiホストが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | ESXiホスト情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

