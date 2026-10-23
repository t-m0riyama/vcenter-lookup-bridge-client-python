# vcenter_lookup_bridge_client.EventsApi

All URIs are relative to *http://localhost/vcenter-lookup-bridge/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_events**](EventsApi.md#list_events) | **GET** /events/ | List Events


# **list_events**
> EventListResponseSchema list_events(begin_time=begin_time, end_time=end_time, days_ago_begin=days_ago_begin, days_ago_end=days_ago_end, hours_ago_begin=hours_ago_begin, hours_ago_end=hours_ago_end, event_types=event_types, event_sources=event_sources, user_names=user_names, ip_addresses=ip_addresses, offset=offset, cursor=cursor, max_results=max_results, vcenter=vcenter)

List Events

イベント一覧を、発生時刻の新しい順に取得します。(同じ時刻の場合はvCenter名の順、さらに新しく記録された順)続きのページは、pagination.nextCursorをcursorに指定し、1ページ目と同じ検索条件で取得してください。cursorを使うと、時間帯は1ページ目で決めたものに固定され、ページを順に読む間にイベントが増えても、それによる抜けや重複は起きません。1回の取得では、vCenterごとに、新しいもの(cursorを指定した場合はcursorより古いもの)から環境変数VLB_MAX_RETRIEVE_EVENTS_PER_VCENTERの件数(既定1000件)までを読みます。上限はevent_sources・ip_addressesで絞り込む前の件数に適用します。上限に達したvCenterがある場合はtruncatedをtrueにし、totalCountも上限までの範囲の件数になります。このとき、上限に達したvCenterで読んだ範囲までを返すため、件数がmax_resultsに満たないページや、空のページになることがあります。その場合もnextCursorで続きを取得でき、ページを進めると上限より古いイベントにも届きます。続きを読んだ結果、該当するイベントがなかった場合は、空の結果とhasNext=falseを返します。cursorで取得したページのtotalCountは、cursorより後に読んだ件数です。partialFailureがtrueのページがあった場合、取得に失敗したvCenterの、そのページの範囲の分は続きのページでも返りません。取り直すときは1ページ目から読み直してください。(レスポンスのキャッシュの有効期間中は、同じ条件の1ページ目は同じ内容になります。)offsetでページを指定した場合は、上限より古いイベントは対象外で、ページを順に読む間にイベントが増えると、ページ間で結果がずれ、抜けや重複が起きることがあります。

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
    offset = 0 # int | イベントを取得する際の開始位置を指定します。(結果は発生時刻の新しい順に並びます。) cursorと同時には指定できません。 (optional) (default to 0)
    max_results = 100 # int | イベントを取得する際の最大件数を指定します。 (optional) (default to 100)
    vcenter = 'vcenter_example' # str | vCenterの名前を指定します。 (optional)
    cursor = 'cursor_example' # str | 前のページのpagination.nextCursorを指定すると、その続きを取得します。1ページ目と同じ検索条件と一緒に指定してください。(max_resultsは変えても構いません。) (optional)

    try:
        # List Events
        api_response = api_instance.list_events(begin_time=begin_time, end_time=end_time, days_ago_begin=days_ago_begin, days_ago_end=days_ago_end, hours_ago_begin=hours_ago_begin, hours_ago_end=hours_ago_end, event_types=event_types, event_sources=event_sources, user_names=user_names, ip_addresses=ip_addresses, offset=offset, max_results=max_results, vcenter=vcenter, cursor=cursor)
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
 **offset** | **int**| イベントを取得する際の開始位置を指定します。(結果は発生時刻の新しい順に並びます。) cursorと同時には指定できません。 | [optional] [default to 0]
 **cursor** | **str**| 前のページのpagination.nextCursorを指定すると、その続きを取得します。1ページ目と同じ検索条件と一緒に指定してください。(max_resultsは変えても構いません。) | [optional] 
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
**404** | 指定した条件のイベントが見つからない場合に返されます。offsetを指定し、上限に達したvCenterがある場合は、その旨をdetailに書きます。(上限より古いイベントは対象外のため) |  -  |
**422** | Validation Error |  -  |
**500** | イベント情報の一覧を取得中にエラーが発生した場合に返されます。 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

