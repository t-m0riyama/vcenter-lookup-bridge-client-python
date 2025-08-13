# vcenter_lookup_bridge_client.VcentersApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_vcenters**](VcentersApi.md#list_vcenters) | **GET** /vcenters/ | List Vcenters


# **list_vcenters**
> VCenterListResponseSchema list_vcenters(offset=offset, max_results=max_results, vcenter=vcenter)

List Vcenters

接続先のvCenter一覧を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.v_center_list_response_schema import VCenterListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.VcentersApi(api_client)
    offset = 0 # int | vCenterを取得する際の開始位置を指定します。 (optional) (default to 0)
    max_results = 100 # int | vCenterを取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Vcenters
        api_response = api_instance.list_vcenters(offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of VcentersApi->list_vcenters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VcentersApi->list_vcenters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| vCenterを取得する際の開始位置を指定します。 | [optional] [default to 0]
 **max_results** | **int**| vCenterを取得する際の最大件数を指定します。 | [optional] [default to 100]
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**VCenterListResponseSchema**](VCenterListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定した条件のvCenterが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | vCenter情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

