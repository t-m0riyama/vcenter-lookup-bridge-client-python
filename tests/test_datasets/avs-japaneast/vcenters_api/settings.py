# coding: utf-8

import json

"""
VCENTERS APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "avs-japaneast01"
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
      "name": "avs-japaneast01",
      "hostName": "vc.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "port": 443,
      "description": "vCenter(Azure東日本 AVS)"
}
"""
)

# VCENTERリストのレスポンス例
EXPECTED_VCENTER_LIST = json.loads(
    """
{
  "results": [
    {
      "name": "avs-japaneast01",
      "hostName": "vc.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "port": 443,
      "description": "vCenter(Azure東日本 AVS)"
    }
  ],
  "success": true,
  "message": "接続先のvCenter一覧を取得しました。",
  "pagination": null,
  "vcenterWsSessions": {
    "avs-japaneast01": "alive"
  },
  "timestamp": "2025-08-20T07:21:59.262384+00:00",
  "requestId": "f1d8c7d5-6eec-431d-8c34-8f734759b32e"
}
"""
)

