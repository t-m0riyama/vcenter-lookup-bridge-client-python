# vcenter_lookup_bridge_client.PortgroupsApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_portgroups**](PortgroupsApi.md#list_portgroups) | **GET** /portgroups/ | List Portgroups


# **list_portgroups**
> PortgroupListResponseSchema list_portgroups(tag_category, tags, offset=offset, max_results=max_results, vcenter=vcenter)

List Portgroups

タグを指定して、同タグが付与されたポートグループ一覧を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.portgroup_list_response_schema import PortgroupListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.PortgroupsApi(api_client)
    tag_category = 'cat1' # str | タグのカテゴリを指定します。
    tags = ['[tag1]'] # List[str] | タグの名前を指定します。
    offset = 56 # int | ポートグループ一覧を取得する際の開始位置を指定します。 (optional)
    max_results = 56 # int | ポートグループ一覧を取得する際の最大件数を指定します。 (optional)
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Portgroups
        api_response = api_instance.list_portgroups(tag_category, tags, offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of PortgroupsApi->list_portgroups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PortgroupsApi->list_portgroups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_category** | **str**| タグのカテゴリを指定します。 | 
 **tags** | [**List[str]**](str.md)| タグの名前を指定します。 | 
 **offset** | **int**| ポートグループ一覧を取得する際の開始位置を指定します。 | [optional] 
 **max_results** | **int**| ポートグループ一覧を取得する際の最大件数を指定します。 | [optional] 
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**PortgroupListResponseSchema**](PortgroupListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定したタグを持つポートグループが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | ポートグループ情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

