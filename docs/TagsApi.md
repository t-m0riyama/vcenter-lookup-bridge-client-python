# vcenter_lookup_bridge_client.TagsApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_tags**](TagsApi.md#list_tags) | **GET** /tags/ | List Tags


# **list_tags**
> TagListResponseSchema list_tags(tag_category=tag_category, object_type=object_type, object_name=object_name, object_id=object_id, offset=offset, max_results=max_results, vcenter=vcenter)

List Tags

タグ一覧を取得します。object_typeとobject_name(仮想マシンはobject_idも可)を指定した場合は、そのオブジェクトに割り当てられたタグのみを取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.tag_list_response_schema import TagListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.TagsApi(api_client)
    tag_category = 'cat1' # str | タグのカテゴリを指定します。指定したカテゴリのタグのみを取得します。 (optional)
    object_type = 'VirtualMachine' # str | 割り当てを問い合わせるオブジェクトの種別を指定します。object_nameまたはobject_idと合わせて指定すると、そのオブジェクトに割り当てられたタグのみを取得します。Networkは標準・分散ポートグループの両方が対象です。 (optional)
    object_name = 'vm01' # str | 割り当てを問い合わせるオブジェクトの名前を指定します。同じ名前のオブジェクトが複数ある場合は、全てのオブジェクトの割り当てを取得します。 (optional)
    object_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # str | 割り当てを問い合わせる仮想マシンのインスタンスUUIDを指定します。object_typeがVirtualMachineの場合のみ指定できます。 (optional)
    offset = 0 # int | タグ一覧を取得する際の開始位置を指定します。 (optional) (default to 0)
    max_results = 100 # int | タグ一覧を取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Tags
        api_response = api_instance.list_tags(tag_category=tag_category, object_type=object_type, object_name=object_name, object_id=object_id, offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of TagsApi->list_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->list_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_category** | **str**| タグのカテゴリを指定します。指定したカテゴリのタグのみを取得します。 | [optional] 
 **object_type** | **str**| 割り当てを問い合わせるオブジェクトの種別を指定します。object_nameまたはobject_idと合わせて指定すると、そのオブジェクトに割り当てられたタグのみを取得します。Networkは標準・分散ポートグループの両方が対象です。 | [optional] 
 **object_name** | **str**| 割り当てを問い合わせるオブジェクトの名前を指定します。同じ名前のオブジェクトが複数ある場合は、全てのオブジェクトの割り当てを取得します。 | [optional] 
 **object_id** | **str**| 割り当てを問い合わせる仮想マシンのインスタンスUUIDを指定します。object_typeがVirtualMachineの場合のみ指定できます。 | [optional] 
 **offset** | **int**| タグ一覧を取得する際の開始位置を指定します。 | [optional] [default to 0]
 **max_results** | **int**| タグ一覧を取得する際の最大件数を指定します。 | [optional] [default to 100]
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**TagListResponseSchema**](TagListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定した条件のタグが見つからない場合に返されます。 |  -  |
**500** | タグ情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

