# coding: utf-8

import json

"""
VM FOLDERS APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "avs-japaneast01"
VALID_VM_FOLDERS = ["D-V2044JMC"]
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
      "name": "D-V2044JMC",
      "vcenter": "avs-japaneast01"
}
"""
)

# VM FOLDERリストのレスポンス例
EXPECTED_VM_FOLDER_LIST = json.loads(
    """
{
  "results": [
    {
      "name": "D-V2002ADREP",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2007KSFZGRAN",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012JTEC-GENRN",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2031FO",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006DNS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2044JMC",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006AFS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2044JMCBOM",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2002ASSETVIEW",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012WQ",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2002BI",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2002LIFEPIMS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2044JMCECN",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2031FS3",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006OTRDGW",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2008JFEWPEDI",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006ABTIB7CS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006TMA",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012TECDC2",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2050JIRBM",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2040AD",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012JTECWSUS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2039LOG",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2010INTINF",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2017FUSEIBOUSHI",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012DENGON",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2041FILE",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006OT",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012UC",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2041SHIKKOU",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2004MDEV",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2005SKYSEA",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006APKYOYO",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2022FILE",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012TECVWNAS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006ITOT",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2007KSFZSAP",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2010TPM",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2041KYUUYO",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2002FJ",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2040FILE",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012JTECNYUTAI",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2017GETPCLOG",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006RADIUS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2050DESKNETS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2010KS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2017AD",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2022AX",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006OUTSYSTEMS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2002FILESV",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006UKKSK",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012PSCAN",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2010UEM",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006CLOUD",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2041SALES",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012HIBUN",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012ITDM",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2040DB",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2020SCJG",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2015XOBLOS",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012QANAT",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2039NWM",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006MSTR",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2002FSB",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2041AD",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012SEP",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006ZTNST",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006EAM",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012WF",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012PCLEAR",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012FC",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012LOG",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012TECDC1",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006BLABO",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2020SCAVYAK01",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V1001AOSMQ",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2010ISDEPT",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012SUG",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2010LOGAF",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012MAIL",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006HDHOTLINE",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2006VDI",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2008FUSIONXP",
      "vcenter": "avs-japaneast01"
    },
    {
      "name": "D-V2012AD2",
      "vcenter": "avs-japaneast01"
    }
  ],
  "success": true,
  "message": "84件の仮想マシンフォルダを取得しました。",
  "pagination": {
    "totalCount": 84,
    "offset": 0,
    "limit": 100,
    "hasNext": false,
    "hasPrevious": false
  },
  "vcenterWsSessions": {
    "avs-japaneast01": "alive"
  },
  "timestamp": "2025-08-20T07:10:39.508037+00:00",
  "requestId": "3dbde86b-b159-474f-b264-791de91ab92d"
}
"""
)

