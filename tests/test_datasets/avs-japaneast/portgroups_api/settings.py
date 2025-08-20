# coding: utf-8

import json

"""
PORTGROUPS APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "avs-japaneast01"
VALID_TAG_CATEGORY = "system_id"
VALID_TAGS = ["devel"]
VALID_TAGS_MULTI = ["devel", "home"]
INVALID_VCENTER = "non-existent-vcenter"
INVALID_TAG_CATEGORY = "non-existent-tag-category"
INVALID_TAGS = ["non-existent-tag1", "non-existent-tag2"]


# PORTGROUPSリストのパラメータ(正常, 全vCenter)
VALID_LIST_PARAMETERS = {
    "tag_category": VALID_TAG_CATEGORY,
    "tags": VALID_TAGS,
    "offset": 0,
    "max_results": 100,
}

# PORTGROUPSリストのパラメータ(正常, 全vCenter, 複数タグ)
VALID_LIST_PARAMETERS_MULTI_TAGS = {
    "tag_category": VALID_TAG_CATEGORY,
    "tags": VALID_TAGS_MULTI,
    "offset": 0,
    "max_results": 100,
}

# PORTGROUPSリストのパラメータ(正常, 指定vCenter)
VALID_LIST_PARAMETERS_VCENTER = {
    "tag_category": VALID_TAG_CATEGORY,
    "tags": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# PORTGROUPSリストのパラメータ(tag_categoryが存在しない)
INVALID_LIST_PARAMETERS_TAG_CATEGORY = {
    "tag_category": INVALID_TAG_CATEGORY,
    "tags": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# PORTGROUPSリストのパラメータ(tagsが存在しない)
INVALID_LIST_PARAMETERS_TAGS = {
    "tag_category": VALID_TAG_CATEGORY,
    "tags": INVALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# PORTGROUPSリストのパラメータ(vCenterが存在しない)
INVALID_LIST_PARAMETERS_VCENTER = {
    "tag_category": VALID_TAG_CATEGORY,
    "tags": VALID_TAGS,
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# PORTGROUPSリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "tag_category": VALID_TAG_CATEGORY,
    "tags": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# PORTGROUPSリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "tag_category": VALID_TAG_CATEGORY,
    "tags": VALID_TAGS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# PORTGROUPSリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "tag_category": VALID_TAG_CATEGORY,
    "tags": VALID_TAGS,
    "offset": -1,  # offset > 0
    "max_results": 100,
}

# PORTGROUPSリストのレスポンス例
EXPECTED_PORTGROUPS_LIST = json.loads(
    """
{
    "results": [
    {
      "name": "mng-net",
      "vcenter": "devel",
      "tag_category": "system-id",
      "tags": [
        "devel"
      ],
      "hosts": []
    },
    {
      "name": "nested-net",
      "vcenter": "devel",
      "tag_category": "system-id",
      "tags": [
        "devel"
      ],
      "hosts": []
    }
  ],
  "success": true,
  "message": "2件のポートグループ情報を取得しました。",
  "pagination": {
    "totalCount": 2,
    "offset": 0,
    "limit": 100,
    "hasNext": false,
    "hasPrevious": false
  }
}
"""
)

# PORTGROUPSリストのレスポンス例
EXPECTED_PORTGROUPS_LIST_MULTI_TAGS = json.loads(
    """
{
    "results": [
    {
      "name": "mng-net",
      "vcenter": "devel",
      "tag_category": "system-id",
      "tags": [
        "devel"
      ],
      "hosts": []
    },
    {
      "name": "nested-net",
      "vcenter": "devel",
      "tag_category": "system-id",
      "tags": [
        "devel"
      ],
      "hosts": []
    },
    {
      "name": "VM Network",
      "vcenter": "devel",
      "tag_category": "system-id",
      "tags": [
        "home"
      ],
      "hosts": [
        "mini5.moriyama.internal"
      ]
    }
  ],
  "success": true,
  "message": "3件のポートグループ情報を取得しました。",
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
