# vcenter_lookup_bridge_client.AlarmsApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_alarms**](AlarmsApi.md#list_alarms) | **GET** /alarms/ | List Alarms


# **list_alarms**
> AlarmListResponseSchema list_alarms(begin_time=begin_time, end_time=end_time, days_ago_begin=days_ago_begin, days_ago_end=days_ago_end, hours_ago_begin=hours_ago_begin, hours_ago_end=hours_ago_end, statuses=statuses, alarm_sources=alarm_sources, acknowledged=acknowledged, offset=offset, max_results=max_results, vcenter=vcenter)

List Alarms

トリガー済みのアラーム一覧を取得します。

### Example

* Basic Authentication (basicAuth):

```python
import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.alarm_list_response_schema import AlarmListResponseSchema
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
    api_instance = vcenter_lookup_bridge_client.AlarmsApi(api_client)
    begin_time = 'begin_time_example' # str | アラームが発生したと思われる時間帯の開始時間を指定します。(指定しない場合は7日前からのアラームを取得します。) \\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    end_time = 'end_time_example' # str | アラームが発生したと思われる時間帯の終了時間を指定します。(指定しない場合は現在までのアラームを取得します。) \\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    days_ago_begin = 56 # int | n日前以降に発生したアラームを取得します。指定した日数の過去日付で、アラームが発生したと思われる時間帯の開始日を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    days_ago_end = 56 # int | n日前以前に発生したアラームを取得します。指定した日数の過去日付で、アラームが発生したと思われる時間帯の終了日を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    hours_ago_begin = 56 # int | n時間前以降に発生したアラームを取得します。指定した時間数の過去で、アラームが発生したと思われる時間帯の開始時間を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    hours_ago_end = 56 # int | n時間前以前に発生したアラームを取得します。指定した時間数の過去で、アラームが発生したと思われる時間帯の終了時間を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 (optional)
    statuses = ['statuses_example'] # List[Optional[str]] | アラームのステータスを指定します。 (optional)
    alarm_sources = ['alarm_sources_example'] # List[str] | アラームのソースを指定します。 (optional)
    acknowledged = True # bool | アラームが確認済みかどうかを指定します。 (optional)
    offset = 0 # int | アラームを取得する際の開始位置を指定します。 (optional) (default to 0)
    max_results = 100 # int | アラームを取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter_example' # str | vCenterの名前を指定します。 (optional)

    try:
        # List Alarms
        api_response = api_instance.list_alarms(begin_time=begin_time, end_time=end_time, days_ago_begin=days_ago_begin, days_ago_end=days_ago_end, hours_ago_begin=hours_ago_begin, hours_ago_end=hours_ago_end, statuses=statuses, alarm_sources=alarm_sources, acknowledged=acknowledged, offset=offset, max_results=max_results, vcenter=vcenter)
        print("The response of AlarmsApi->list_alarms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->list_alarms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_time** | **str**| アラームが発生したと思われる時間帯の開始時間を指定します。(指定しない場合は7日前からのアラームを取得します。) \\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **end_time** | **str**| アラームが発生したと思われる時間帯の終了時間を指定します。(指定しない場合は現在までのアラームを取得します。) \\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **days_ago_begin** | **int**| n日前以降に発生したアラームを取得します。指定した日数の過去日付で、アラームが発生したと思われる時間帯の開始日を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **days_ago_end** | **int**| n日前以前に発生したアラームを取得します。指定した日数の過去日付で、アラームが発生したと思われる時間帯の終了日を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **hours_ago_begin** | **int**| n時間前以降に発生したアラームを取得します。指定した時間数の過去で、アラームが発生したと思われる時間帯の開始時間を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **hours_ago_end** | **int**| n時間前以前に発生したアラームを取得します。指定した時間数の過去で、アラームが発生したと思われる時間帯の終了時間を指定します。\\*\\_time, days_ago\\_\\*, hours_ago\\_\\* パラメータはいずれか1種類のみを指定してください。 | [optional] 
 **statuses** | [**List[Optional[str]]**](str.md)| アラームのステータスを指定します。 | [optional] 
 **alarm_sources** | [**List[str]**](str.md)| アラームのソースを指定します。 | [optional] 
 **acknowledged** | **bool**| アラームが確認済みかどうかを指定します。 | [optional] 
 **offset** | **int**| アラームを取得する際の開始位置を指定します。 | [optional] [default to 0]
 **max_results** | **int**| アラームを取得する際の最大件数を指定します。 | [optional] [default to 100]
 **vcenter** | **str**| vCenterの名前を指定します。 | [optional] 

### Return type

[**AlarmListResponseSchema**](AlarmListResponseSchema.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | 指定した条件のトリガー済みアラームが見つからない場合に返されます。 |  -  |
**422** | Validation Error |  -  |
**500** | トリガー済みのアラーム情報を取得中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

