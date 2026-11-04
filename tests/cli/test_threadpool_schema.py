"""ThreadPoolResponseSchema の復元テスト"""

import pytest

from vcenter_lookup_bridge_client.models.thread_pool_response_schema import (
    ThreadPoolResponseSchema,
)
from vcenter_lookup_bridge_client.models.thread_pool_schema import ThreadPoolSchema


@pytest.mark.unit
class TestThreadPoolResponseSchema:
    def test_from_json_ok(self):
        """200 応答の JSON から ThreadPoolResponseSchema を復元できる"""
        raw = (
            '{"results":{"status":"ok","process_id":1234,"total_tokens":40,'
            '"borrowed_tokens":2,"available_tokens":38,"tasks_waiting":0},'
            '"success":true,"partialFailure":false,'
            '"message":"スレッド枠の状態を取得しました",'
            '"timestamp":"2026-11-04T12:00:00.000000+09:00","requestId":"req-1"}'
        )
        response = ThreadPoolResponseSchema.from_json(raw)
        assert response is not None
        assert response.success is True
        assert isinstance(response.results, ThreadPoolSchema)
        assert response.results.status == "ok"
        assert response.results.process_id == 1234
        assert response.results.total_tokens == 40
        assert response.results.borrowed_tokens == 2
        assert response.results.available_tokens == 38
        assert response.results.tasks_waiting == 0

    def test_from_json_saturated(self):
        """503 応答と同じ形の JSON から saturated を復元できる"""
        raw = (
            '{"results":{"status":"saturated","process_id":99,"total_tokens":40,'
            '"borrowed_tokens":40,"available_tokens":0,"tasks_waiting":3},'
            '"success":false,"partialFailure":false,'
            '"message":"スレッド枠に空きがありません",'
            '"timestamp":"2026-11-04T12:00:00.000000+09:00"}'
        )
        response = ThreadPoolResponseSchema.from_json(raw)
        assert response is not None
        assert response.success is False
        assert response.results.status == "saturated"
        assert response.results.available_tokens == 0
        assert response.results.tasks_waiting == 3
