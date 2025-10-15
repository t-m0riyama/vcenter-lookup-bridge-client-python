# coding: utf-8

import json

"""
EVENTS APIのテストで使用する期待するレスポンスデータ
"""

# シミュレータを利用する場合は、 過去のイベントは削除されるため、
# 直近の起動直後の日付に変更してテストすること。

VALID_VCENTER = "simulator02"
VALID_BEGIN_TIME = "2025-10-15T00:00:00+09:00"
VALID_END_TIME = "2025-10-17T23:59:59+09:00"
VALID_BEGIN_TIME2 = "2025-10-15"
VALID_END_TIME2 = "2025-10-17"
VALID_DAYS_AGO_BEGIN = 3650
VALID_DAYS_AGO_END = 0
VALID_HOURS_AGO_BEGIN = VALID_DAYS_AGO_BEGIN * 24
VALID_HOURS_AGO_END = VALID_DAYS_AGO_END * 24

INVALID_VCENTER = "non-existent-vcenter"
# begin_time, end_timeのフォーマットは、以下のいずれかの形式でなければならない。
# 2025-08-15T08:53:00+09:00, 2025-08-15T08:53:00, 2025-08-15
INVALID_BEGIN_TIME = "2025/10/15T9"
INVALID_END_TIME = "2025/10/17T9"
INVALID_BEGIN_TIME2 = "2025/10/15"
INVALID_END_TIME2 = "2025/10/17"
INVALID_DAYS_AGO_BEGIN = 0  # days_ago_begin >= 1
INVALID_DAYS_AGO_END = -1  # days_ago_end >= 0
INVALID_HOURS_AGO_BEGIN = 0  # hours_ago_begin >= 1
INVALID_HOURS_AGO_END = -1  # hours_ago_end >= 0


# イベントリストのパラメータ(正常/絶対日付指定/タイムゾーン付き)
VALID_LIST_PARAMETERS_BEGIN_TIME = {
    "begin_time": VALID_BEGIN_TIME,
    "end_time": VALID_END_TIME,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(正常/絶対日付指定/タイムゾーンなし)
VALID_LIST_PARAMETERS_BEGIN_TIME2 = {
    "begin_time": VALID_BEGIN_TIME2,
    "end_time": VALID_END_TIME2,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(正常/相対日付指定/日数)
VALID_LIST_PARAMETERS_DAYS_AGO = {
    "days_ago_begin": VALID_DAYS_AGO_BEGIN,
    "days_ago_end": VALID_DAYS_AGO_END,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(正常/相対日付指定/時間数)
VALID_LIST_PARAMETERS_HOURS_AGO = {
    "hours_ago_begin": VALID_HOURS_AGO_BEGIN,
    "hours_ago_end": VALID_HOURS_AGO_END,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(異常/絶対日付指定/タイムゾーン付き)
INVALID_LIST_PARAMETERS_BEGIN_TIME = {
    "begin_time": INVALID_BEGIN_TIME,
    "end_time": INVALID_END_TIME,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(異常/絶対日付指定/タイムゾーンなし)
INVALID_LIST_PARAMETERS_BEGIN_TIME2 = {
    "begin_time": INVALID_BEGIN_TIME2,
    "end_time": INVALID_END_TIME2,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(異常/相対日付指定/日数)
INVALID_LIST_PARAMETERS_DAYS_AGO = {
    "days_ago_begin": INVALID_DAYS_AGO_BEGIN,
    "days_ago_end": INVALID_DAYS_AGO_END,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(異常/相対日付指定/時間数)
INVALID_LIST_PARAMETERS_HOURS_AGO = {
    "hours_ago_begin": INVALID_HOURS_AGO_BEGIN,
    "hours_ago_end": INVALID_HOURS_AGO_END,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(異常/vCenter指定)
INVALID_LIST_PARAMETERS_VCENTER = {
    "begin_time": VALID_BEGIN_TIME,
    "end_time": VALID_END_TIME,
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# イベントリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "days_ago_begin": VALID_DAYS_AGO_BEGIN,
    "days_ago_end": VALID_DAYS_AGO_END,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# イベントリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "days_ago_begin": VALID_DAYS_AGO_BEGIN,
    "days_ago_end": VALID_DAYS_AGO_END,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# イベントリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "days_ago_begin": VALID_DAYS_AGO_BEGIN,
    "days_ago_end": VALID_DAYS_AGO_END,
    "vcenter": VALID_VCENTER,
    "offset": -1,  # offset > 0
    "max_results": 100,
}


# イベントリストのレスポンス例
EXPECTED_EVENT_LIST = json.loads(
    """
{
  "results": [
    {
      "message": "User {userName}@{ipAddress} logged in as {userAgent}",
      "createdTime": "2025-10-15T17:33:28.604974+00:00",
      "eventType": "UserLoginSessionEvent",
      "eventSource": null,
      "userName": "ansible01@vsphere.local",
      "ipAddress": "192.168.65.1",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC"
    }
  ],
  "success": true,
  "message": "1件のイベントを取得しました。",
  "pagination": {
    "totalCount": 1,
    "offset": 0,
    "limit": 100,
    "hasNext": false,
    "hasPrevious": false
  }
}
"""
)
