# coding: utf-8

import json

"""
TAGS APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "devel"
VALID_TAG_CATEGORY = "system-id"
VALID_OBJECT_TYPE = "Datastore"
VALID_OBJECT_NAME = "vmware-ds01"
INVALID_VCENTER = "non-existent-vcenter"
INVALID_TAG_CATEGORY = "non-existent-tag-category"
INVALID_OBJECT_TYPE = "Folder"  # VirtualMachine, HostSystem, Datastore, ClusterComputeResource, Network以外は不可


# タグリストのパラメータ(正常, 全vCenter)
VALID_LIST_PARAMETERS = {
    "offset": 0,
    "max_results": 100,
}

# タグリストのパラメータ(正常, カテゴリ指定)
VALID_LIST_PARAMETERS_TAG_CATEGORY = {
    "tag_category": VALID_TAG_CATEGORY,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# タグリストのパラメータ(正常, オブジェクトへの割り当ての問い合わせ)
VALID_LIST_PARAMETERS_OBJECT = {
    "object_type": VALID_OBJECT_TYPE,
    "object_name": VALID_OBJECT_NAME,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# タグリストのパラメータ(正常, ページング)
VALID_LIST_PARAMETERS_PAGINATION = {
    "offset": 1,
    "max_results": 1,
}

# タグリストのパラメータ(異常, カテゴリが存在しない)
INVALID_LIST_PARAMETERS_TAG_CATEGORY = {
    "tag_category": INVALID_TAG_CATEGORY,
    "offset": 0,
    "max_results": 100,
}

# タグリストのパラメータ(異常, vCenterが存在しない)
INVALID_LIST_PARAMETERS_VCENTER = {
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# タグリストのパラメータ(異常, サポート外のオブジェクトの種別)
INVALID_LIST_PARAMETERS_OBJECT_TYPE = {
    "object_type": INVALID_OBJECT_TYPE,
    "object_name": VALID_OBJECT_NAME,
    "offset": 0,
    "max_results": 100,
}

# タグリストのパラメータ(異常, object_idはVirtualMachineの場合のみ指定可)
INVALID_LIST_PARAMETERS_OBJECT_ID = {
    "object_type": VALID_OBJECT_TYPE,
    "object_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "offset": 0,
    "max_results": 100,
}

# タグリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# タグリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# タグリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "offset": -1,  # offset >= 0
    "max_results": 100,
}

# 期待するタグリスト(カテゴリ指定)
EXPECTED_TAG_LIST_TAG_CATEGORY = json.loads(
    """
{
  "results": [
    {
      "name": "devel",
      "tag_category": "system-id",
      "description": "",
      "vcenter": "devel",
      "objectName": null,
      "objectId": null
    },
    {
      "name": "home",
      "tag_category": "system-id",
      "description": "",
      "vcenter": "devel",
      "objectName": null,
      "objectId": null
    }
  ]
}
"""
)

# 期待するタグリスト(オブジェクトへの割り当ての問い合わせ)
EXPECTED_TAG_LIST_OBJECT = json.loads(
    """
{
  "results": [
    {
      "name": "devel",
      "tag_category": "system-id",
      "description": "",
      "vcenter": "devel",
      "objectName": "vmware-ds01",
      "objectId": "datastore-15"
    },
    {
      "name": "home",
      "tag_category": "system-id",
      "description": "",
      "vcenter": "devel",
      "objectName": "vmware-ds01",
      "objectId": "datastore-15"
    }
  ]
}
"""
)
