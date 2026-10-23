# vcenter_lookup_bridge_client.CustomAttributesApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_custom_attributes**](CustomAttributesApi.md#list_custom_attributes) | **GET** /custom_attributes/ | List Custom Attributes


# **list_custom_attributes**
> CustomAttributeListResponseSchema list_custom_attributes(object_type=object_type, object_name=object_name, object_id=object_id, offset=offset, max_results=max_results, vcenter=vcenter)

List Custom Attributes

カスタム属性の定義一覧を取得します。object_typeとobject_name(仮想マシンはobject_idも可)を指定した場合は、そのオブジェクトに値が設定されたカスタム属性のみを値と合わせて取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.custom_attribute_list_response_schema import CustomAttributeListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.CustomAttributesApi(api_client)
    object_type = 'VirtualMachine' # str | オブジェクトの種別を指定します。単独で指定した場合は、その種別のカスタム属性の定義のみを取得します(完全一致。グローバル属性はGlobal)。object_nameまたはobject_idと合わせて指定した場合は、割り当てを問い合わせるオブジェクトの種別(VirtualMachine, HostSystem, Datastore, ClusterComputeResource, Network)になります。 (optional)
    object_name = 'vm01' # str | 割り当てを問い合わせるオブジェクトの名前を指定します。指定すると、そのオブジェクトに値が設定されたカスタム属性のみを値と合わせて取得します。同じ名前のオブジェクトが複数ある場合は、全てのオブジェクトの割り当てを取得します。 (optional)
    object_id = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' # str | 割り当てを問い合わせる仮想マシンのインスタンスUUIDを指定します。object_typeがVirtualMachineの場合のみ指定できます。 (optional)
    offset = 0 # int | カスタム属性一覧を取得する際の開始位置を指定します。 (optional) (default to 0)
    max_results = 100 # int | カスタム属性一覧を取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter01' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Custom Attributes
        api_response = api_instance.list_custom_attributes(object_type=object_type, object_name=object_name, object_id=object_id, offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of CustomAttributesApi->list_custom_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributesApi->list_custom_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_type** | **str**| オブジェクトの種別を指定します。単独で指定した場合は、その種別のカスタム属性の定義のみを取得します(完全一致。グローバル属性はGlobal)。object_nameまたはobject_idと合わせて指定した場合は、割り当てを問い合わせるオブジェクトの種別(VirtualMachine, HostSystem, Datastore, ClusterComputeResource, Network)になります。 | [optional] 
 **object_name** | **str**| 割り当てを問い合わせるオブジェクトの名前を指定します。指定すると、そのオブジェクトに値が設定されたカスタム属性のみを値と合わせて取得します。同じ名前のオブジェクトが複数ある場合は、全てのオブジェクトの割り当てを取得します。 | [optional] 
 **object_id** | **str**| 割り当てを問い合わせる仮想マシンのインスタンスUUIDを指定します。object_typeがVirtualMachineの場合のみ指定できます。 | [optional] 
 **offset** | **int**| カスタム属性一覧を取得する際の開始位置を指定します。 | [optional] [default to 0]
 **max_results** | **int**| カスタム属性一覧を取得する際の最大件数を指定します。 | [optional] [default to 100]
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**CustomAttributeListResponseSchema**](CustomAttributeListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定した条件のカスタム属性が見つからない場合に返されます。 |  -  |
**500** | カスタム属性情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

