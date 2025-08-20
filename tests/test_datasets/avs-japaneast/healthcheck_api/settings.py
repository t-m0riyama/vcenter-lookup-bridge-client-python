# coding: utf-8

import json

"""
HEALTHCHECK APIのテストで使用する期待するレスポンスデータ
"""

# HEALTHCHECKのレスポンス例
EXPECTED_HEALTHCHECK_STATUS = json.loads(
    """
{
  "results": {
    "status": "ok",
    "vcenter_service_instances": "ok"
  },
  "success": true,
  "message": "サービスのステータスを取得しました",
  "pagination": null
}
"""
)
