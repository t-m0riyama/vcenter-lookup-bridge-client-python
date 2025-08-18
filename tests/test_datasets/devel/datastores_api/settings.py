# coding: utf-8

import json

"""
DATASTORES APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "simulator02"
VALID_TAG_CATEGORY = "system_id"
VALID_TAGS = ["devel"]
INVALID_VCENTER = "non-existent-vcenter"
INVALID_TAG_CATEGORY = "non-existent-tag-category"
INVALID_TAGS = ["non-existent-tag-name"]


# DATASTOREリストのパラメータ(正常, 全vCenter)
VALID_LIST_PARAMETERS = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "offset": 0,
    "max_results": 100,
}

# DATASTOREリストのパラメータ(正常, 指定vCenter)
VALID_LIST_PARAMETERS_VCENTER = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# DATASTOREリストのパラメータ(正常, 指定datastores)
VALID_LIST_PARAMETERS_DATASTORES = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "offset": 0,
    "max_results": 100,
}

# DATASTOREリストのパラメータ(正常, 指定vCenter, 指定datastores)
VALID_LIST_PARAMETERS_VCENTER_DATASTORES = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# DATASTOREリストのパラメータ(datastoresが存在しない)
INVALID_LIST_PARAMETERS_DATASTORES = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# DATASTOREリストのパラメータ(vCenterが存在しない)
INVALID_LIST_PARAMETERS_VCENTER = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# DATASTOREリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# DATASTOREリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# DATASTOREリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "tag_category": VALID_TAG_CATEGORY,
    "tag_values": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": -1,  # offset > 0
    "max_results": 100,
}


# DATASTOREリストのレスポンス例
EXPECTED_DATASTORE_LIST = json.loads(
    """
{
    "results": [
    {
      "name": "devel3",
      "vcenter": "simulator02"
    },
    {
      "name": "devel2",
      "vcenter": "simulator02"
    },
    {
      "name": "devel",
      "vcenter": "simulator02"
    }
  ],
  "success": true,
  "message": "3件の仮想マシンフォルダを取得しました。",
  "pagination": {
    "totalCount": 3,
    "offset": 0,
    "limit": 100,
    "hasNext": false,
    "hasPrevious": false
  }
}
"""
)
