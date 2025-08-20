# coding: utf-8

import json

"""
VM関連APIのテストで使用する期待するレスポンスデータ
"""

VALID_INSTANCE_UUID = "502c8a03-0533-dae6-1e75-fbfefeaa452f"
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
EXPECTED_VM = json.loads(
    """
    {
      "name": "D-V2044JMC013",
      "uuid": "422c2fc0-9356-8ad5-f502-65dfce15b09f",
      "instanceUuid": "502c8a03-0533-dae6-1e75-fbfefeaa452f",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx03-r04.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 2,
      "memorySizeMB": 4096,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 260
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:eb:69",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:0b:19",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] 44027864-3808-835f-8e93-b8599fb147b4/D-V2044JMC013.vmx",
      "guestFullName": "Microsoft Windows Server 2022 (64-bit)",
      "hostname": "JMC-ESS01A",
      "ipAddress": "172.22.2.171",
      "template": false,
      "hwVersion": "vmx-19"
    }
"""
)

# VMリストのレスポンス例
EXPECTED_VM_LIST = json.loads(
    """
{
  "results": [
    {
      "name": "D-V2044JMC009",
      "uuid": "422c81de-fb08-8253-1168-8bd0554f1d80",
      "instanceUuid": "502c231e-5de6-fd9d-1c50-a6edf4bd939d",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx09-r08.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 1,
      "memorySizeMB": 8192,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 60
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:d0:c6",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:b1:f5",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] db007864-643b-1a4f-dbf9-b8599fb147b4/D-V2044JMC009.vmx",
      "guestFullName": "Microsoft Windows Server 2022 (64-bit)",
      "hostname": "JMC-END01A",
      "ipAddress": "172.22.2.169",
      "template": false,
      "hwVersion": "vmx-19"
    },
    {
      "name": "D-V2044JMC002",
      "uuid": "422cbd93-10a7-535f-39b8-b6fc0c0fb0e8",
      "instanceUuid": "502c3379-7fb0-91a3-501d-0756c0ae8f96",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx09-r08.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 4,
      "memorySizeMB": 16384,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 150
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:45:7b",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:77:a7",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] 9a4e3e64-2432-89e3-e1fb-b8599fb147b4/D-V2044JMC002.vmx",
      "guestFullName": "Microsoft Windows Server 2022 (64-bit)",
      "hostname": "JMC-FVM01A.ad-jgranz-dc.jp",
      "ipAddress": "172.22.2.164",
      "template": false,
      "hwVersion": "vmx-19"
    },
    {
      "name": "D-V2044JMC010",
      "uuid": "422c1eca-92b6-088c-68d7-7df9103a75d9",
      "instanceUuid": "502cef2a-2cf9-f4f0-000b-f709ef331421",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx11-r03.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 2,
      "memorySizeMB": 2048,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 2
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:07:bf",
          "portgroup": null,
          "connected": true,
          "startConnected": false
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:08:04",
          "portgroup": null,
          "connected": false,
          "startConnected": false
        },
        {
          "label": "Network adapter 3",
          "macAddress": "00:50:56:ac:6e:64",
          "portgroup": null,
          "connected": false,
          "startConnected": false
        },
        {
          "label": "Network adapter 4",
          "macAddress": "00:50:56:ac:04:59",
          "portgroup": null,
          "connected": false,
          "startConnected": false
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] 51967a64-0e28-89b7-4356-b8599fb147b4/D-V2044JMC010.vmx",
      "guestFullName": "Other 3.x or later Linux (32-bit)",
      "hostname": "jmc-rad01a",
      "ipAddress": "133.190.225.16",
      "template": false,
      "hwVersion": "vmx-10"
    },
    {
      "name": "D-V2044JMC011",
      "uuid": "422c47a8-270e-35bc-d5b4-dba4f3d4903e",
      "instanceUuid": "502cc10d-7fba-a4f7-af90-73f83667ea71",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx09-r08.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 4,
      "memorySizeMB": 8192,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 40
        },
        {
          "label": "Hard disk 2",
          "datastore": "vsanDatastore",
          "sizeGB": 36
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:32:cc",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] ad39ae64-2a91-b9f9-25bb-b8599fb147b4/D-V2044JMC011.vmx",
      "guestFullName": "CentOS 7 (64-bit)",
      "hostname": "jmc-sys01a",
      "ipAddress": "133.190.225.20",
      "template": false,
      "hwVersion": "vmx-13"
    },
    {
      "name": "D-V2044JMC003",
      "uuid": "422c1ad0-5558-4d3d-1398-4a753b7d9419",
      "instanceUuid": "502c64c3-8879-b599-a12d-d948162a9773",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx11-r03.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 8,
      "memorySizeMB": 16384,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 8
        },
        {
          "label": "Hard disk 2",
          "datastore": "vsanDatastore",
          "sizeGB": 50
        }
      ],
      "networkDevices": [],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] c2503f64-6628-9573-6732-b8599fb147b4/D-V2044JMC003.vmx",
      "guestFullName": "Other (64-bit)",
      "hostname": "JMC-NLD01A",
      "ipAddress": "133.190.225.18",
      "template": false,
      "hwVersion": "vmx-11"
    },
    {
      "name": "D-V2044JMC004",
      "uuid": "422cceb6-7f0b-4dbe-dc63-ee8789ed0b90",
      "instanceUuid": "502ca6ba-32ec-bdd5-bc85-b95e7ce936e1",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx09-r08.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 4,
      "memorySizeMB": 16384,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 100
        },
        {
          "label": "Hard disk 2",
          "datastore": "vsanDatastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:3f:a9",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:f9:ac",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] c1ad3f64-bc1c-19c4-f7a4-b8599fcbccd8/D-V2044JMC004.vmx",
      "guestFullName": "Microsoft Windows Server 2022 (64-bit)",
      "hostname": "JMC-SDP01A",
      "ipAddress": "172.22.2.166",
      "template": false,
      "hwVersion": "vmx-19"
    },
    {
      "name": "D-V2044JMC008",
      "uuid": "422c250a-5516-09a5-6bda-8b3ea616fc13",
      "instanceUuid": "502cceb0-ebfc-234a-2b9c-7ff1e41f2e5d",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx11-r03.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 4,
      "memorySizeMB": 6144,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 40
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:79:34",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:42:c2",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] 33007864-22fa-619e-d5a3-b8599fb147b4/D-V2044JMC008.vmx",
      "guestFullName": "Microsoft Windows Server 2022 (64-bit)",
      "hostname": "JMC-DNS01A.ad-jgranz-dc.jp",
      "ipAddress": "172.22.2.168",
      "template": false,
      "hwVersion": "vmx-19"
    },
    {
      "name": "D-V2044JMC018",
      "uuid": "422c8e56-ea29-1e07-9f2f-e9684158fb11",
      "instanceUuid": "502c50f8-8ea4-5fa4-8392-e53a88903b9b",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx05-r17.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 4,
      "memorySizeMB": 16384,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 100
        },
        {
          "label": "Hard disk 2",
          "datastore": "vsanDatastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:62:bf",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:2f:53",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] 58ff9268-7e41-609c-c3d0-e8ebd366edea/D-V2044JMC018.vmx",
      "guestFullName": "Microsoft Windows Server 2022 (64-bit)",
      "hostname": "JMC-SDP01A-TEST",
      "ipAddress": "172.22.2.163",
      "template": false,
      "hwVersion": "vmx-21"
    },
    {
      "name": "D-V2044JMC016",
      "uuid": "422c3b74-dfab-0636-69a1-bda008193736",
      "instanceUuid": "502c4d02-56b7-9c69-a187-c054ede8430c",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx04-r14.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 2,
      "memorySizeMB": 12288,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 40
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:5f:57",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] 317aea66-0ef3-3ee0-5d16-b8599fb14c24/D-V2044JMC016.vmx",
      "guestFullName": "Ubuntu Linux (64-bit)",
      "hostname": "jmc-trf02a",
      "ipAddress": "133.190.225.15",
      "template": false,
      "hwVersion": "vmx-19"
    },
    {
      "name": "D-V2044JMC007",
      "uuid": "422c0cd7-7e0c-4a53-a6f7-de8b1ee77780",
      "instanceUuid": "502caf6e-498d-27ae-1327-ab0f6264828e",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx11-r06.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 4,
      "memorySizeMB": 16384,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 40
        },
        {
          "label": "Hard disk 2",
          "datastore": "vsanDatastore",
          "sizeGB": 50
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:2f:4c",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:42:63",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] acff7764-a404-9ac6-05c2-b8599fb147b4/D-V2044JMC007.vmx",
      "guestFullName": "Microsoft Windows Server 2022 (64-bit)",
      "hostname": "JMC-HCO01A",
      "ipAddress": "172.22.2.167",
      "template": false,
      "hwVersion": "vmx-19"
    },
    {
      "name": "D-V2044JMC013",
      "uuid": "422c2fc0-9356-8ad5-f502-65dfce15b09f",
      "instanceUuid": "502c8a03-0533-dae6-1e75-fbfefeaa452f",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx03-r04.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 2,
      "memorySizeMB": 4096,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 260
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:eb:69",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:0b:19",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] 44027864-3808-835f-8e93-b8599fb147b4/D-V2044JMC013.vmx",
      "guestFullName": "Microsoft Windows Server 2022 (64-bit)",
      "hostname": "JMC-ESS01A",
      "ipAddress": "172.22.2.171",
      "template": false,
      "hwVersion": "vmx-19"
    },
    {
      "name": "D-V2044JMC017",
      "uuid": "422c9f6d-6ba5-2a0e-5c96-ee792e5aaa85",
      "instanceUuid": "502ce608-b08a-467d-23ea-f37fe3fac1a8",
      "vcenter": "avs-japaneast01",
      "datacenter": "SDDC-Datacenter",
      "cluster": "Cluster-1",
      "esxiHostname": "esx05-r17.p03.2389a0898727466ca2347b.japaneast.avs.azure.com",
      "powerState": "poweredOn",
      "numCpu": 4,
      "memorySizeMB": 8192,
      "diskDevices": [
        {
          "label": "Hard disk 1",
          "datastore": "vsanDatastore",
          "sizeGB": 100
        }
      ],
      "networkDevices": [
        {
          "label": "Network adapter 1",
          "macAddress": "00:50:56:ac:ce:11",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        },
        {
          "label": "Network adapter 2",
          "macAddress": "00:50:56:ac:1f:b0",
          "portgroup": null,
          "connected": true,
          "startConnected": true
        }
      ],
      "vmFolder": "D-V2044JMC",
      "vmPathName": "[vsanDatastore] f299f366-4cb2-fa8a-a053-b8599fb147b4/D-V2044JMC017.vmx",
      "guestFullName": "Ubuntu Linux (64-bit)",
      "hostname": "jmc-sys02a",
      "ipAddress": "133.190.225.21",
      "template": false,
      "hwVersion": "vmx-19"
    }
  ],
  "success": true,
  "message": "12件の仮想マシンを取得しました。",
  "pagination": {
    "totalCount": 12,
    "offset": 0,
    "limit": 100,
    "hasNext": false,
    "hasPrevious": false
  },
  "vcenterWsSessions": {
    "avs-japaneast01": "alive"
  },
  "timestamp": "2025-08-20T06:11:19.700461+00:00",
  "requestId": "f3bfb791-0eb9-471e-8779-ab666aa9e0f0"
}
"""
)

