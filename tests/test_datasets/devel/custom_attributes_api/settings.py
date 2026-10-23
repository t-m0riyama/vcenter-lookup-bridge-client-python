# coding: utf-8

import json

"""
CUSTOM ATTRIBUTES APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "devel"
VALID_OBJECT_TYPE = "VirtualMachine"
INVALID_VCENTER = "non-existent-vcenter"
INVALID_OBJECT_TYPE = "non-existent-object-type"
INVALID_OBJECT_NAME = "non-existent-vm"


# カスタム属性リストのパラメータ(正常, 指定vCenter)
VALID_LIST_PARAMETERS = {
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# カスタム属性リストのパラメータ(正常, 種別で定義を絞り込み)
VALID_LIST_PARAMETERS_OBJECT_TYPE = {
    "object_type": VALID_OBJECT_TYPE,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# カスタム属性リストのパラメータ(正常, ページング)
VALID_LIST_PARAMETERS_PAGINATION = {
    "vcenter": VALID_VCENTER,
    "offset": 1,
    "max_results": 1,
}

# カスタム属性リストのパラメータ(異常, 該当する種別がない)
INVALID_LIST_PARAMETERS_OBJECT_TYPE = {
    "object_type": INVALID_OBJECT_TYPE,
    "offset": 0,
    "max_results": 100,
}

# カスタム属性リストのパラメータ(異常, 割り当てを問い合わせるオブジェクトが存在しない)
INVALID_LIST_PARAMETERS_OBJECT_NAME = {
    "object_type": VALID_OBJECT_TYPE,
    "object_name": INVALID_OBJECT_NAME,
    "offset": 0,
    "max_results": 100,
}

# カスタム属性リストのパラメータ(異常, vCenterが存在しない)
INVALID_LIST_PARAMETERS_VCENTER = {
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# カスタム属性リストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# カスタム属性リストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# カスタム属性リストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "offset": -1,  # offset >= 0
    "max_results": 100,
}

# 期待するカスタム属性リスト(種別で定義を絞り込み)
EXPECTED_CUSTOM_ATTRIBUTE_LIST_OBJECT_TYPE = json.loads(
    """
{
  "results": [
    {
      "name": "scheduled-deletion-date",
      "objectType": "VirtualMachine",
      "type": "string",
      "vcenter": "devel",
      "value": null,
      "objectName": null,
      "objectId": null
    }
  ]
}
"""
)
