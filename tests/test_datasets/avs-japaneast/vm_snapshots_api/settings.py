# coding: utf-8

import json

"""
VMスナップショット関連APIのテストで使用する期待するレスポンスデータ
"""

VALID_INSTANCE_UUID = "5013f8e7-7343-4ae5-e9c8-33458e73562c"
VALID_VCENTER = "avs-japaneast01"
VALID_VM_FOLDERS = ["D-V2044JMC"]
INVALID_INSTANCE_UUID = "99999999-9999-9999-9999-999999999999"
INVALID_VCENTER = "non-existent-vcenter"
INVALID_VM_FOLDERS = ["non-existent-vm-folder"]


# VM取得のパラメータ(正常)
VALID_GET_PARAMETERS = {
    "vm_instance_uuid": VALID_INSTANCE_UUID,
    "vcenter": VALID_VCENTER,
}

# VM取得のパラメータ(vcenterが存在しない)
INVALID_GET_PARAMETERS_VCENTER = {
    "vm_instance_uuid": VALID_INSTANCE_UUID,
    "vcenter": INVALID_VCENTER,
}

# VM取得のパラメータ(vm_instance_uuidが存在しない)
INVALID_GET_PARAMETERS_VM_INSTANCE_UUID = {
    "vm_instance_uuid": INVALID_INSTANCE_UUID,
    "vcenter": VALID_VCENTER,
}

# VMリストのパラメータ(正常)
VALID_LIST_PARAMETERS = {
    "vm_folders": VALID_VM_FOLDERS,
    "offset": 0,
    "max_results": 100,
}

# VMリストのパラメータ(vm_foldersが存在しない)
INVALID_LIST_PARAMETERS_VM_FOLDERS = {
    "vm_folders": INVALID_VM_FOLDERS,
    "offset": 0,
    "max_results": 100,
}

# VMリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "vm_folders": VALID_VM_FOLDERS,
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# VMリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "vm_folders": VALID_VM_FOLDERS,
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# VMリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "vm_folders": VALID_VM_FOLDERS,
    "offset": -1,  # offset > 0
    "max_results": 100,
}


# 単一VMのレスポンス例
EXPECTED_SINGLE_VM_SNAPSHOTS = json.loads(
    """
[
    {
      "name": "Restore Point 2025-03-11 8:30:30",
      "id": 755,
      "parentId": 753,
      "description": "test snapshot07",
      "createTime": "2025/03/11 08:33:22",
      "hasChild": false,
      "vmName": "bk-test-win01_replica",
      "vmInstanceUuid": "5013f8e7-7343-4ae5-e9c8-33458e73562c",
      "vmFolder": "devel3",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC"
    }
  ]
"""
)

# VMリストのレスポンス例
EXPECTED_MULTI_VM_SNAPSHOT_LIST = json.loads(
    """
{
  "results": [
    {
      "name": "Restore Point 2024-03-11 5:30:20",
      "id": 743,
      "parentId": -1,
      "description": "test snapshot01",
      "createTime": "2025/03/11 05:33:16",
      "hasChild": true,
      "vmName": "bk-test-win01_replica",
      "vmInstanceUuid": "5013f8e7-7343-4ae5-e9c8-33458e73562c",
      "vmFolder": "devel3",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC"
    }
  ],
  "success": true,
  "message": "1件のスナップショット情報を取得しました。",
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
