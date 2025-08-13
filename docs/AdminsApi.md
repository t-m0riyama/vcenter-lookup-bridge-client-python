# vcenter_lookup_bridge_client.AdminsApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**flush_caches**](AdminsApi.md#flush_caches) | **POST** /admins/cache/flush | Flush Caches
[**reset_ws_session**](AdminsApi.md#reset_ws_session) | **POST** /admins/ws_session/reset | Reset Ws Session


# **flush_caches**
> AdminResponseSchema flush_caches()

Flush Caches

キャッシュ済みの全てのレスポンスをクリアします。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.admin_response_schema import AdminResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.AdminsApi(api_client)

    try:
        # Flush Caches
        api_response = api_instance.flush_caches()
        print("The response of AdminsApi->flush_caches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->flush_caches: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AdminResponseSchema**](AdminResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | キャッシュのクリア処理中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_ws_session**
> AdminResponseSchema reset_ws_session()

Reset Ws Session

全てのvCenterのダウンマークをクリアします。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.admin_response_schema import AdminResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.AdminsApi(api_client)

    try:
        # Reset Ws Session
        api_response = api_instance.reset_ws_session()
        print("The response of AdminsApi->reset_ws_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminsApi->reset_ws_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AdminResponseSchema**](AdminResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | vCenterのダウンマークのクリア処理中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

