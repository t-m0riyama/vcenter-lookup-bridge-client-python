# coding: utf-8

import json

"""
VCENTERS APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "simulator02"
INVALID_VCENTER = "non-existent-vcenter"


# VCENTERリストのパラメータ(正常, 全vCenter)
VALID_LIST_PARAMETERS = {
    "offset": 0,
    "max_results": 100,
}

# VCENTERリストのパラメータ(正常, 指定vCenter)
VALID_LIST_PARAMETERS_VCENTER = {
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# VCENTERリストのパラメータ(vCenterが存在しない)
INVALID_LIST_PARAMETERS_VCENTER = {
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# VMリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# VCENTERリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# VCENTERリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "offset": -1,  # offset > 0
    "max_results": 100,
}


# 単一VCENTERのレスポンス例
EXPECTED_VCENTER = json.loads(
    """
{
      "name": "simulator02",
      "hostName": "host.docker.internal",
      "port": 18989,
      "description": "vCenterシミュレータ#2"
}
"""
)

# VCENTERリストのレスポンス例
EXPECTED_VCENTER_LIST = json.loads(
    """
{
    "results": [
    {
      "name": "simulator01",
      "hostName": "host.docker.internal",
      "port": 8989,
      "description": "vCenterシミュレータ#1"
    },
    {
      "name": "simulator02",
      "hostName": "localhost",
      "port": 18989,
      "description": "vCenterシミュレータ#2"
    }
  ],
  "success": true,
  "message": "接続先のvCenter一覧を取得しました。",
  "pagination": null
}
"""
)
