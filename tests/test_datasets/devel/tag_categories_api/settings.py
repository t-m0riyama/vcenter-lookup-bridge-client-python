# coding: utf-8

import json

"""
TAG CATEGORIES APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "devel"
INVALID_VCENTER = "non-existent-vcenter"


# タグカテゴリリストのパラメータ(正常, 指定vCenter)
VALID_LIST_PARAMETERS = {
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# タグカテゴリリストのパラメータ(正常, ページング)
VALID_LIST_PARAMETERS_PAGINATION = {
    "vcenter": VALID_VCENTER,
    "offset": 1,
    "max_results": 1,
}

# タグカテゴリリストのパラメータ(異常, vCenterが存在しない)
INVALID_LIST_PARAMETERS_VCENTER = {
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# タグカテゴリリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# タグカテゴリリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# タグカテゴリリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "offset": -1,  # offset >= 0
    "max_results": 100,
}

# 期待するタグカテゴリリスト
EXPECTED_TAG_CATEGORY_LIST = json.loads(
    """
{
  "results": [
    {
      "name": "scheduled-deletion",
      "description": "",
      "cardinality": "SINGLE",
      "associableTypes": [
        "ClusterComputeResource",
        "Datacenter",
        "Datastore",
        "DistributedVirtualPortgroup",
        "DistributedVirtualSwitch",
        "Folder",
        "HostNetwork",
        "HostSystem",
        "Network",
        "OpaqueNetwork",
        "ResourcePool",
        "StoragePod",
        "VirtualApp",
        "VirtualMachine",
        "VmwareDistributedVirtualSwitch",
        "com.vmware.content.Library",
        "com.vmware.content.library.Item"
      ],
      "vcenter": "devel"
    },
    {
      "name": "system-id",
      "description": "",
      "cardinality": "MULTIPLE",
      "associableTypes": [],
      "vcenter": "devel"
    }
  ]
}
"""
)
