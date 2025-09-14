# vcenter_lookup_bridge_client.EventsApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_events**](EventsApi.md#list_events) | **GET** /events/ | List Events


# **list_events**
> EventListResponseSchema list_events(begin_time=begin_time, end_time=end_time, days_ago_begin=days_ago_begin, days_ago_end=days_ago_end, hours_ago_begin=hours_ago_begin, hours_ago_end=hours_ago_end, event_types=event_types, event_sources=event_sources, user_names=user_names, ip_addresses=ip_addresses, offset=offset, max_results=max_results, vcenter=vcenter)

List Events

イベント一覧を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.event_list_response_schema import EventListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.EventsApi(api_client)
    begin_time = 'begin_time_example' # str | イベントが発生したと思われる時間帯の開始時間を指定します。(指定しない場合は7日前からのイベントを取得します。) \\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    end_time = 'end_time_example' # str | イベントが発生したと思われる時間帯の終了時間を指定します。(指定しない場合は現在までのイベントを取得します。) \\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    days_ago_begin = 56 # int | n日前以降に発生したイベントを取得します。指定した日数の過去日付で、イベントが発生したと思われる時間帯の開始日を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    days_ago_end = 56 # int | n日前以前に発生したイベントを取得します。指定した日数の過去日付で、イベントが発生したと思われる時間帯の終了日を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    hours_ago_begin = 56 # int | n時間前以降に発生したイベントを取得します。指定した時間数の過去で、イベントが発生したと思われる時間帯の開始時間を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    hours_ago_end = 56 # int | n時間前以前に発生したイベントを取得します。指定した時間数の過去で、イベントが発生したと思われる時間帯の終了時間を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    event_types = ['event_types_example'] # List[str] | イベントの種類を指定します。(参考. https://files.hypervisor.fr/vcEvents.html) (optional)
    event_sources = ['event_sources_example'] # List[str] | イベントのソースを指定します。 (optional)
    user_names = ['user_names_example'] # List[str] | イベントを発生させたユーザー名を指定します。 (optional)
    ip_addresses = ['ip_addresses_example'] # List[str] | イベントを発生させたIPアドレスを指定します。 (optional)
    offset = 0 # int | イベントを取得する際の開始位置を指定します。 (optional) (default to 0)
    max_results = 100 # int | イベントを取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter_example' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Events
        api_response = api_instance.list_events(begin_time=begin_time, end_time=end_time, days_ago_begin=days_ago_begin, days_ago_end=days_ago_end, hours_ago_begin=hours_ago_begin, hours_ago_end=hours_ago_end, event_types=event_types, event_sources=event_sources, user_names=user_names, ip_addresses=ip_addresses, offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of EventsApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_time** | **str**| イベントが発生したと思われる時間帯の開始時間を指定します。(指定しない場合は7日前からのイベントを取得します。) \\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **end_time** | **str**| イベントが発生したと思われる時間帯の終了時間を指定します。(指定しない場合は現在までのイベントを取得します。) \\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **days_ago_begin** | **int**| n日前以降に発生したイベントを取得します。指定した日数の過去日付で、イベントが発生したと思われる時間帯の開始日を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **days_ago_end** | **int**| n日前以前に発生したイベントを取得します。指定した日数の過去日付で、イベントが発生したと思われる時間帯の終了日を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **hours_ago_begin** | **int**| n時間前以降に発生したイベントを取得します。指定した時間数の過去で、イベントが発生したと思われる時間帯の開始時間を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **hours_ago_end** | **int**| n時間前以前に発生したイベントを取得します。指定した時間数の過去で、イベントが発生したと思われる時間帯の終了時間を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **event_types** | [**List[str]**](str.md)| イベントの種類を指定します。(参考. https://files.hypervisor.fr/vcEvents.html) | [optional] 
 **event_sources** | [**List[str]**](str.md)| イベントのソースを指定します。 | [optional] 
 **user_names** | [**List[str]**](str.md)| イベントを発生させたユーザー名を指定します。 | [optional] 
 **ip_addresses** | [**List[str]**](str.md)| イベントを発生させたIPアドレスを指定します。 | [optional] 
 **offset** | **int**| イベントを取得する際の開始位置を指定します。 | [optional] [default to 0]
 **max_results** | **int**| イベントを取得する際の最大件数を指定します。 | [optional] [default to 100]
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**EventListResponseSchema**](EventListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定した条件のイベントが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | イベント情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

