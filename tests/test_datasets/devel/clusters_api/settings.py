# coding: utf-8

import json

"""
CLUSTERS APIのテストで使用する期待するレスポンスデータ
"""

VALID_VCENTER = "simulator02"
VALID_CLUSTERS = ["cluster-99"]
INVALID_VCENTER = "non-existent-vcenter"
INVALID_CLUSTERS = ["non-existent-cluster"]


# クラスタ取得のパラメータ(正常)
VALID_GET_PARAMETERS = {
    "clusters": VALID_CLUSTERS,
    "vcenter": VALID_VCENTER,
}

# クラスタ取得のパラメータ(vcenterが存在しない)
INVALID_GET_PARAMETERS_VCENTER = {
    "clusters": VALID_CLUSTERS,
    "vcenter": INVALID_VCENTER,
}

# クラスタ取得のパラメータ(クラスタが存在しない)
INVALID_GET_PARAMETERS_CLUSTER = {
    "clusters": INVALID_CLUSTERS,
    "vcenter": VALID_VCENTER,
}

# クラスタリストのパラメータ(正常)
VALID_LIST_PARAMETERS = {
    "offset": 0,
    "max_results": 100,
}

# VMリストのパラメータ(max_resultsが1000を超える)
INVALID_LIST_PARAMETERS_MAX_RESULTS = {
    "cluster": VALID_CLUSTERS,
    "offset": 0,
    "max_results": 1001,  # max_results <= 1000
}

# VMリストのパラメータ(max_resultsが負の値)
INVALID_LIST_PARAMETERS_MAX_RESULTS2 = {
    "cluster": VALID_CLUSTERS,
    "offset": 0,
    "max_results": -1,  # max_results >= 1
}

# VMリストのパラメータ(offsetが負の値)
INVALID_LIST_PARAMETERS_OFFSET = {
    "cluster": VALID_CLUSTERS,
    "offset": -1,  # offset > 0
    "max_results": 100,
}


# 単一VMのレスポンス例
EXPECTED_CLUSTER = json.loads(
    """
[
  {
      "name": "cluster-99",
      "status": "green",
      "hosts": [
        "mini5.moriyama.internal",
        "mini4.moriyama.internal"
      ],
      "vcenter": "simulator02"
  }
]
"""
)

# VMリストのレスポンス例
EXPECTED_CLUSTER_LIST = json.loads(
    """
{
  "results": [
    {
      "name": "Cluster-1",
      "status": "green",
      "hosts": [
        "esx09-r02.p01.2389a0898727466ca2347b.japaneast.avs.azure.com",
        "esx01-r04.p01.2389a0898727466ca2347b.japaneast.avs.azure.com",
        "esx02-r07.p01.2389a0898727466ca2347b.japaneast.avs.azure.com",
        "esx05-r06.p01.2389a0898727466ca2347b.japaneast.avs.azure.com",
        "esx04-r21.p01.2389a0898727466ca2347b.japaneast.avs.azure.com",
        "esx11-r01.p01.2389a0898727466ca2347b.japaneast.avs.azure.com"
      ],
      "vcenter": "simulator01"
    },
    {
      "name": "cluster-99",
      "status": "green",
      "hosts": [
        "mini5.moriyama.internal",
        "mini4.moriyama.internal"
      ],
      "vcenter": "simulator02"
    }
  ],
  "success": true,
  "message": "2件のクラスタを取得しました。",
  "pagination": null
}
"""
)
