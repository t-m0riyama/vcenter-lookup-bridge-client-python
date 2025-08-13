# coding: utf-8

import json

"""
VM関連APIのテストで使用する期待するレスポンスデータ
"""

VALID_INSTANCE_UUID = "525eab7a-d9f1-06b8-7e82-e1c6c42028b7"
VALID_VCENTER = "simulator02"
VALID_VM_FOLDERS = ["devel3"]
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
EXPECTED_VM = json.loads(
    """
{
    "name": "vcenter8-01",
    "uuid": "564d8a63-b9bc-63e2-7302-f520e56a2009",
    "instanceUuid": "525eab7a-d9f1-06b8-7e82-e1c6c42028b7",
    "vcenter": "simulator02",
    "datacenter": "KanagawaDC",
    "cluster": "cluster-99",
    "esxiHostname": "mini5.moriyama.internal",
    "powerState": "poweredOn",
    "numCpu": 4,
    "memorySizeMB": 16384,
    "diskDevices": [
      {
        "label": "VCSIM Simulator Label",
        "datastore": "VCSIM Simulator Datastore",
        "sizeGB": 100
      }
    ],
    "networkDevices": [
      {
        "label": "VCSIM Simulator Label",
        "macAddress": "00:11:22:33:44:55",
        "portgroup": "VCSIM Simulator PortGroup",
        "connected": true,
        "startConnected": true
      }
    ],
    "vmFolder": "devel3",
    "vmPathName": "[vmware-ds01] vcenter8-01/vcenter8-01.vmx",
    "guestFullName": "Other 3.x or later Linux (64-bit)",
    "hostname": null,
    "ipAddress": null,
    "template": false,
    "hwVersion": "vmx-10"
}
"""
)

# VMリストのレスポンス例
EXPECTED_VM_LIST = json.loads(
    """
{
    "results": [
    {
      "name": "vcenter8-02",
      "uuid": "564d3d23-1b7a-c13b-a2d8-b9dcaf4851ff",
      "instanceUuid": "525e5e0e-0912-173d-fc13-0ee164000c9b",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC",
      "cluster": "cluster-99",
      "esxiHostname": "mini5.moriyama.internal",
      "powerState": "poweredOff",
      "numCpu": 2,
      "memorySizeMB": 14336,
      "diskDevices": [
        {
          "label": "VCSIM Simulator Label",
          "datastore": "VCSIM Simulator Datastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "VCSIM Simulator Label",
          "macAddress": "00:11:22:33:44:55",
          "portgroup": "VCSIM Simulator PortGroup",
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "devel3",
      "vmPathName": "[vmware-ds01] vcenter8-02/vcenter8-02.vmx",
      "guestFullName": "Other 3.x or later Linux (64-bit)",
      "hostname": "vcenter8-02.moriyama.internal",
      "ipAddress": null,
      "template": false,
      "hwVersion": "vmx-10"
    },
    {
      "name": "veeam02",
      "uuid": "42136cfc-24c8-5d92-ecb7-f0ed48bc08fc",
      "instanceUuid": "50138627-6d6a-b6de-2c77-4747455a7c33",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC",
      "cluster": "cluster-99",
      "esxiHostname": "mini5.moriyama.internal",
      "powerState": "poweredOff",
      "numCpu": 2,
      "memorySizeMB": 12288,
      "diskDevices": [
        {
          "label": "VCSIM Simulator Label",
          "datastore": "VCSIM Simulator Datastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "VCSIM Simulator Label",
          "macAddress": "00:11:22:33:44:55",
          "portgroup": "VCSIM Simulator PortGroup",
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "devel3",
      "vmPathName": "[vmware-ds11] veeam02/veeam02.vmx",
      "guestFullName": "Microsoft Windows 10 (64-bit)",
      "hostname": null,
      "ipAddress": null,
      "template": false,
      "hwVersion": "vmx-14"
    },
    {
      "name": "veeam05",
      "uuid": "4213a709-9b21-853e-f556-bdb921c1c59a",
      "instanceUuid": "5013ca47-3e5f-8e21-08fa-72133be70501",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC",
      "cluster": "cluster-99",
      "esxiHostname": "mini5.moriyama.internal",
      "powerState": "poweredOff",
      "numCpu": 2,
      "memorySizeMB": 5120,
      "diskDevices": [
        {
          "label": "VCSIM Simulator Label",
          "datastore": "VCSIM Simulator Datastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "VCSIM Simulator Label",
          "macAddress": "00:11:22:33:44:55",
          "portgroup": "VCSIM Simulator PortGroup",
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "devel3",
      "vmPathName": "[vmware-ds11] veeam05/veeam05.vmx",
      "guestFullName": "Microsoft Windows 10 (64-bit)",
      "hostname": null,
      "ipAddress": null,
      "template": false,
      "hwVersion": "vmx-14"
    },
    {
      "name": "bk-test-win01_replica",
      "uuid": "42139afd-89ca-b62a-536f-52a26efc3e2d",
      "instanceUuid": "5013f8e7-7343-4ae5-e9c8-33458e73562c",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC",
      "cluster": "cluster-99",
      "esxiHostname": "mini5.moriyama.internal",
      "powerState": "poweredOff",
      "numCpu": 2,
      "memorySizeMB": 5120,
      "diskDevices": [
        {
          "label": "VCSIM Simulator Label",
          "datastore": "VCSIM Simulator Datastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "VCSIM Simulator Label",
          "macAddress": "00:11:22:33:44:55",
          "portgroup": "VCSIM Simulator PortGroup",
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "devel3",
      "vmPathName": "[vmware-ds11] bk-test-win01_replica/bk-test-win01.vmx",
      "guestFullName": "Microsoft Windows 10 (64-bit)",
      "hostname": null,
      "ipAddress": null,
      "template": false,
      "hwVersion": "vmx-14"
    },
    {
      "name": "vcenter8-01",
      "uuid": "564d8a63-b9bc-63e2-7302-f520e56a2009",
      "instanceUuid": "525eab7a-d9f1-06b8-7e82-e1c6c42028b7",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC",
      "cluster": "cluster-99",
      "esxiHostname": "mini5.moriyama.internal",
      "powerState": "poweredOn",
      "numCpu": 4,
      "memorySizeMB": 16384,
      "diskDevices": [
        {
          "label": "VCSIM Simulator Label",
          "datastore": "VCSIM Simulator Datastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "VCSIM Simulator Label",
          "macAddress": "00:11:22:33:44:55",
          "portgroup": "VCSIM Simulator PortGroup",
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "devel3",
      "vmPathName": "[vmware-ds01] vcenter8-01/vcenter8-01.vmx",
      "guestFullName": "Other 3.x or later Linux (64-bit)",
      "hostname": null,
      "ipAddress": null,
      "template": false,
      "hwVersion": "vmx-10"
    },
    {
      "name": "veeam06",
      "uuid": "42132abc-7ea9-2e9e-19f4-8995e01f2afb",
      "instanceUuid": "50130375-75e8-79d8-8410-02c8c86977d2",
      "vcenter": "simulator02",
      "datacenter": "KanagawaDC",
      "cluster": "cluster-99",
      "esxiHostname": "mini5.moriyama.internal",
      "powerState": "poweredOff",
      "numCpu": 2,
      "memorySizeMB": 5120,
      "diskDevices": [
        {
          "label": "VCSIM Simulator Label",
          "datastore": "VCSIM Simulator Datastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "VCSIM Simulator Label",
          "macAddress": "00:11:22:33:44:55",
          "portgroup": "VCSIM Simulator PortGroup",
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "devel3",
      "vmPathName": "[vmware-ds11] veeam06/veeam06.vmx",
      "guestFullName": "Microsoft Windows 10 (64-bit)",
      "hostname": null,
      "ipAddress": null,
      "template": false,
      "hwVersion": "vmx-14"
    }
  ],
  "success": true,
  "message": "6件の仮想マシンを取得しました。",
  "pagination": {
    "totalCount": 6,
    "offset": 0,
    "limit": 100,
    "hasNext": false,
    "hasPrevious": false
  }
}
"""
)
