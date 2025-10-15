# coding: utf-8

import json

"""
ESXiホスト関連APIのテストで使用する期待するレスポンスデータ
"""

VALID_HOST_UUID = "1bc44b00-9306-11ee-b50e-4fdb31f95200"
VALID_VCENTER = "devel"
INVALID_HOST_UUID = "99999999-9999-9999-9999-999999999999"
INVALID_VCENTER = "non-existent-vcenter"


# ESXiホスト取得のパラメータ(正常)
VALID_GET_PARAMETERS = {
    "host_uuid": VALID_HOST_UUID,
    "vcenter": VALID_VCENTER,
}

# ESXiホスト取得のパラメータ(存在しないvcenterを指定)
INVALID_GET_PARAMETERS_VCENTER = {
    "host_uuid": VALID_HOST_UUID,
    "vcenter": INVALID_VCENTER,
}

# ESXiホスト取得のパラメータ(存在しないhost_uuidを指定)
INVALID_GET_PARAMETERS_HOST_UUID = {
    "host_uuid": INVALID_HOST_UUID,
    "vcenter": VALID_VCENTER,
}

# ESXiホストリストのパラメータ(正常)
VALID_LIST_PARAMETERS = {
    "vcenter": VALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# ESXiホストリストのパラメータ(存在しないvcenterを指定)
INVALID_LIST_PARAMETERS_VCENTER = {
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 100,
}

# ESXiホストリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# ESXiホストリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "vcenter": INVALID_VCENTER,
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# ESXiホストリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "vcenter": INVALID_VCENTER,
    "offset": -1,  # offset > 0
    "max_results": 100,
}


# 単一ESXiホストのレスポンス例
EXPECTED_HOST = json.loads(
    """
{
  "name": "mini5.moriyama.internal",
  "uuid": "1bc44b00-9306-11ee-b50e-4fdb31f95200",
  "status": "red",
  "esxiVersion": "8.0.3",
  "esxiVersionFull": "VMware ESXi 8.0.3 build-24262298",
  "vcenter": "devel",
  "datacenter": "KanagawaDC",
  "cluster": "cluster-99",
  "hardwareVendor": "Micro Computer (HK) Tech Limited",
  "hardwareModel": "UM690",
  "powerState": "poweredOn",
  "cpuModel": "AMD Ryzen 9 6900HX with Radeon Graphics        ",
  "numCpuSockets": 1,
  "numCpuCores": 8,
  "numCpuThreads": 16,
  "memorySizeMB": 64248,
  "datastores": [
    {
      "name": "vmware-ds02",
      "status": "green",
      "type": "NFS41",
      "capacityGB": 5436,
      "freeSpaceGB": 2639
    },
    {
      "name": "datastore1",
      "status": "green",
      "type": "VMFS",
      "capacityGB": 825,
      "freeSpaceGB": 526
    },
    {
      "name": "vmware-ds01",
      "status": "green",
      "type": "NFS41",
      "capacityGB": 5436,
      "freeSpaceGB": 2639
    }
  ],
  "portgroups": [
    {
      "name": "VM Network"
    }
  ],
  "vswitches": [
    {
      "name": "vSwitch0"
    }
  ],
  "ipAddress": "10.1.1.159"
}
"""
)

# ESXiホストリストのレスポンス例
EXPECTED_HOST_LIST = json.loads(
    """
{
    "results": [
    {
      "name": "mini5.moriyama.internal",
      "uuid": "1bc44b00-9306-11ee-b50e-4fdb31f95200",
      "status": "red",
      "esxiVersion": "8.0.3",
      "vcenter": "devel",
      "datacenter": "KanagawaDC",
      "numCpuSockets": 1,
      "numCpuCores": 8,
      "numCpuThreads": 16,
      "memorySizeMB": 64248
    }
  ],
  "success": true,
  "message": "1件のESXiホストを取得しました。",
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
