# coding: utf-8

import json

"""
ADMINS APIのテストで使用する期待するレスポンスデータ
"""


# キャッシュクリアのレスポンス例
EXPECTED_FLUSH_CACHE = json.loads(
    """
{
  "results": [],
  "success": true,
  "message": "キャッシュをクリアしました。",
  "pagination": null
}
"""
)

# Web Service Sessionリセットのレスポンス例
EXPECTED_RESET_WS_SESSION = json.loads(
    """
{
  "results": [],
  "success": true,
  "message": "全てのvCenterのダウンマークをクリアしました。",
  "pagination": null
}
"""
)
