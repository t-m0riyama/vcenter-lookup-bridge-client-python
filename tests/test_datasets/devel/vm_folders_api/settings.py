# coding: utf-8

import json

"""
VM FOLDERS APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "simulator02"
VALID_VM_FOLDERS = ["devel3"]
INVALID_VCENTER = "non-existent-vcenter"
INVALID_VM_FOLDERS = ["non-existent-vm-folder"]


# VM FOLDERリストのパラメータ(正常, 全vCenter)
VALID_LIST_PARAMETERS = {
    "offset": 0,
    "max_results": 100,
}

# VM FOLDERリストのパラメータ(正常, 指定vCenter)
VALID_LIST_PARAMETERS_VCENTER = {
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# VM FOLDERリストのパラメータ(正常, 指定vm_folders)
VALID_LIST_PARAMETERS_VM_FOLDERS = {
    "vm_folders": VALID_VM_FOLDERS,
    "offset": 0,
    "max_results": 100,
}

# VM FOLDERリストのパラメータ(正常, 指定vCenter, 指定vm_folders)
VALID_LIST_PARAMETERS_VCENTER_VM_FOLDERS = {
    "vm_folders": VALID_VM_FOLDERS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# VM FOLDERリストのパラメータ(vm_foldersが存在しない)
INVALID_LIST_PARAMETERS_VM_FOLDERS = {
    "vm_folders": INVALID_VM_FOLDERS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# VM FOLDERリストのパラメータ(vCenterが存在しない)
INVALID_LIST_PARAMETERS_VCENTER = {
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# VMリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "vm_folders": VALID_VM_FOLDERS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# VM FOLDERリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "vm_folders": VALID_VM_FOLDERS,
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# VM FOLDERリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "vm_folders": VALID_VM_FOLDERS,
    "offset": -1,  # offset > 0
    "max_results": 100,
}


# 単一VM FOLDERのレスポンス例
EXPECTED_VM_FOLDER = json.loads(
    """
{
      "name": "devel3",
      "vcenter": "simulator02"
}
"""
)

# VM FOLDERリストのレスポンス例
EXPECTED_VM_FOLDER_LIST = json.loads(
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
