# coding: utf-8

"""
vCenter Lookup Bridge API - ALARMS APIテスト
"""

import pydantic
import pytest
from datetime import datetime
from typing import Dict, Any
from unittest.mock import MagicMock

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.alarm_response_schema import AlarmResponseSchema
from vcenter_lookup_bridge_client.models.alarm_list_response_schema import AlarmListResponseSchema


@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "alarms_api"


@pytest.fixture
def api_instance(api_client):
    """Alarms APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.AlarmsApi(api_client)


class TestAlarmsApi:
    """Alarms API unit test"""

    def test_list_alarms_success_begin_time(self, api_instance, test_dataset):
        """アラームリスト取得の成功テスト 絶対日付指定/タイムゾーン付き"""
        # APIを呼び出し
        response = api_instance.list_alarms(**test_dataset.VALID_LIST_PARAMETERS_BEGIN_TIME)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_ALARM_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, AlarmResponseSchema)
            assert isinstance(result.key, str)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_ALARM_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.description == expected_result["description"]
            assert result.alarm_source == expected_result["alarmSource"]
            assert result.status == expected_result["status"]
            assert result.created_time == expected_result["createdTime"]
            assert result.acknowledged == expected_result["acknowledged"]
            assert result.acknowledged_time == expected_result["acknowledgedTime"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]

        print(
            f"✅ アラームリスト取得テスト(絶対日付指定/タイムゾーン付き)成功: {len(response.results)}件のアラームが見つかりました"
        )

    def test_list_alarms_success_begin_time2(self, api_instance, test_dataset):
        """アラームリスト取得の成功テスト 絶対日付指定/タイムゾーンなし"""
        # APIを呼び出し
        response = api_instance.list_alarms(**test_dataset.VALID_LIST_PARAMETERS_BEGIN_TIME2)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_ALARM_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, AlarmResponseSchema)
            assert isinstance(result.key, str)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_ALARM_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.description == expected_result["description"]
            assert result.alarm_source == expected_result["alarmSource"]
            assert result.status == expected_result["status"]
            assert result.created_time == expected_result["createdTime"]
            assert result.acknowledged == expected_result["acknowledged"]
            assert result.acknowledged_time == expected_result["acknowledgedTime"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]

        print(
            f"✅ アラームリスト取得テスト(絶対日付指定/タイムゾーンなし)成功: {len(response.results)}件のアラームが見つかりました"
        )

    def test_list_alarms_success_days_ago(self, api_instance, test_dataset):
        """アラームリスト取得の成功テスト 相対日付指定/日数"""
        # APIを呼び出し
        response = api_instance.list_alarms(**test_dataset.VALID_LIST_PARAMETERS_DAYS_AGO)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_ALARM_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, AlarmResponseSchema)
            assert isinstance(result.key, str)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_ALARM_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.description == expected_result["description"]
            assert result.alarm_source == expected_result["alarmSource"]
            assert result.status == expected_result["status"]
            assert result.created_time == expected_result["createdTime"]
            assert result.acknowledged == expected_result["acknowledged"]
            assert result.acknowledged_time == expected_result["acknowledgedTime"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]

        print(
            f"✅ アラームリスト取得テスト(相対日付指定/日数)成功: {len(response.results)}件のアラームが見つかりました"
        )

    def test_list_alarms_success_hours_ago(self, api_instance, test_dataset):
        """アラームリスト取得の成功テスト 相対日付指定/時間数"""
        # APIを呼び出し
        response = api_instance.list_alarms(**test_dataset.VALID_LIST_PARAMETERS_HOURS_AGO)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        results = response.results
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_ALARM_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, AlarmResponseSchema)
            assert isinstance(result.key, str)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_ALARM_LIST["results"],
        ):
            assert result.name == expected_result["name"]
            assert result.description == expected_result["description"]
            assert result.alarm_source == expected_result["alarmSource"]
            assert result.status == expected_result["status"]
            assert result.created_time == expected_result["createdTime"]
            assert result.acknowledged == expected_result["acknowledged"]
            assert result.acknowledged_time == expected_result["acknowledgedTime"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]

        print(
            f"✅ アラームリスト取得テスト(相対日付指定/時間数)成功: {len(response.results)}件のアラームが見つかりました"
        )

    def test_list_alarms_with_invalid_begin_time(self, api_instance, test_dataset):
        """不正な書式の時間を指定したアラーム取得のテスト(begin_time, end_timeパラメータの制限が有効であることを確認）"""
        try:
            # 不正な書式のbegin_time, end_timeでAPIを呼び出し
            response = api_instance.list_alarms(**test_dataset.INVALID_LIST_PARAMETERS_BEGIN_TIME)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"不正な書式の時間を指定したアラーム取得テスト(begin_time, end_time)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 422エラーは例外として投げられる可能性がある
            if "422" in str(e):
                print(
                    f"✅ 不正な書式の時間を指定したアラーム取得テスト(begin_time, end_time): 422エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"不正な書式の時間を指定したアラーム取得テスト(begin_time, end_time)で予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_alarms_with_invalid_begin_time2(self, api_instance, test_dataset):
        """不正な書式の時間を指定したアラーム取得のテスト2(begin_time, end_timeパラメータの制限が有効であることを確認）"""
        try:
            # 不正な書式のbegin_time, end_timeでAPIを呼び出し
            response = api_instance.list_alarms(**test_dataset.INVALID_LIST_PARAMETERS_BEGIN_TIME2)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"不正な書式の時間を指定したアラーム取得テスト2(begin_time, end_time)でエラーが発生しました。想定される例外が発生しませんでした。"
            )
        except Exception as e:
            # 422エラーは例外として投げられる可能性がある
            if "422" in str(e):
                print(
                    f"✅ 不正な書式の時間を指定したアラーム取得テスト2(begin_time, end_time): 422エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"不正な書式の時間を指定したアラーム取得テスト2(begin_time, end_time)で予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_alarms_with_invalid_days_ago(self, api_instance, test_dataset):
        """日付指定に対して制限を超える値を指定したアラーム取得のテスト(days_ago_begin, days_ago_endパラメータの制限が有効であることを確認）"""
        try:
            # 不正な書式のdays_ago_begin, days_ago_endでAPIを呼び出し
            response = api_instance.list_alarms(**test_dataset.INVALID_LIST_PARAMETERS_DAYS_AGO)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"日付指定に対して制限を超える値を指定したアラーム取得テスト(days_ago_begin, days_ago_end)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except pydantic.ValidationError as e:
            print(
                f"✅ 日付指定に対して制限を超える値を指定したアラーム取得テスト(days_ago_begin, days_ago_end)成功: 正しくエラーが返されました: {str(e)}"
            )
        except Exception as e:
            pytest.fail(
                f"日付指定に対して制限を超える値を指定したアラーム取得テスト(days_ago_begin, days_ago_end)で予期しないエラーが発生しました: {str(e)}"
            )

    def test_list_alarms_with_invalid_hours_ago(self, api_instance, test_dataset):
        """時間指定に対して制限を超える値を指定したアラーム取得のテスト(hours_ago_begin, hours_ago_endパラメータの制限が有効であることを確認）"""
        try:
            # 不正な書式のhours_ago_begin, hours_ago_endでAPIを呼び出し
            response = api_instance.list_alarms(**test_dataset.INVALID_LIST_PARAMETERS_HOURS_AGO)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"時間指定に対して制限を超える値を指定したアラーム取得テスト(hours_ago_begin, hours_ago_end)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except pydantic.ValidationError as e:
            print(
                f"✅ 時間指定に対して制限を超える値を指定したアラーム取得テスト(hours_ago_begin, hours_ago_end)成功: 正しくエラーが正しく返されました: {str(e)}"
            )
        except Exception as e:
            pytest.fail(
                f"時間指定に対して制限を超える値を指定したアラーム取得テスト(hours_ago_begin, hours_ago_end)で予期しないエラーが発生しました: {str(e)}"
            )

    def test_list_alarms_not_found_with_invalid_vcenter(self, api_instance, test_dataset):
        """存在しないアラーム取得のテスト(vCenter指定)"""
        try:
            # 存在しないvCenterでAPIを呼び出し
            response = api_instance.list_alarms(**test_dataset.INVALID_LIST_PARAMETERS_VCENTER)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないアラーム取得テスト(vCenter)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(f"✅ 存在しないアラーム取得テスト(vCenter)成功: 404エラーが正しく返されました: {str(e)}")
            else:
                pytest.fail(f"存在しないアラーム取得テスト(vCenter)で予期しないエラーが発生しました: {str(e)}")

    def test_list_alarms_with_invalid_max_results(self, api_instance, test_dataset):
        """アラームリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""

        # max_resultsに制限（<=1000)を超える値を指定してAPIを呼び出し
        try:
            response = api_instance.list_alarms(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"max_resultsに制限を超える値(>1000, {test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS['max_results']})を指定したテストでエラーが発生しました"
            )

        except pydantic.ValidationError as e:
            print(f"✅ max_resultsに制限を超える値(>1000)を指定した場合、正しくエラーが返却されました: {e}")

        # max_resultsに制限（>=1)を超える値を指定してAPIを呼び出し
        try:
            response = api_instance.list_alarms(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"max_resultsに制限を超える値(<0, {test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2['max_results']})を指定したテストでエラーが発生しました"
            )

        except pydantic.ValidationError as e:
            print(f"✅ max_resultsに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}")

    def test_list_alarms_with_invalid_offset(self, api_instance, test_dataset):
        """アラームリスト取得のテスト（パラメータ制限が有効であることを確認）"""
        # offsetに制限を超える値をを指定してAPIを呼び出し
        try:
            response = api_instance.list_alarms(**test_dataset.INVALID_LIST_PARAMETERS_OFFSET)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"offsetに制限を超える値を指定したテストでエラーが発生しました")

        except pydantic.ValidationError as e:
            print(f"✅ offsetに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}")

    def test_list_alarms_with_pagination(self, api_instance, test_dataset):
        """ページネーション付きクラスタリスト取得のテスト"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = api_instance.list_alarms(**test_dataset.VALID_LIST_PARAMETERS_BEGIN_TIME)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        assert isinstance(response.results, list)

        # ページネーション情報のチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # データ件数のチェック（per_page以下であることを確認）
        assert len(response.results) <= 100

        print(f"✅ ページネーション付きアラームリスト取得テスト成功: ページ1, 1ページあたり100件")

    def test_list_alarms_with_cursor_paging(self, api_instance, test_dataset):
        """カーソル方式のページングで、続きのページが重複なく取得できることのテスト"""
        params = test_dataset.VALID_LIST_PARAMETERS_CURSOR
        page1 = api_instance.list_alarms(**params)
        assert page1.success is True
        assert isinstance(page1.pagination, PaginationInfo)
        if not page1.pagination.next_cursor:
            pytest.skip("次のページがあるだけのデータがないため、カーソル方式のページングを確認できません")
        assert page1.pagination.has_next is True

        # 1ページ目と同じ検索条件にcursorを加えて、続きのページを取得する
        page2 = api_instance.list_alarms(**params, cursor=page1.pagination.next_cursor)
        assert page2.success is True
        if not page2.results:
            # 読む間にアラームが解除された場合などは、続きのページが空の結果になることがある
            pytest.skip("続きのページが空のため、ページ間の重複と並び順を確認できません")

        # 同じvCenterのkeyが重複しないこと
        keys1 = {(r.vcenter, r.key) for r in page1.results}
        keys2 = {(r.vcenter, r.key) for r in page2.results}
        assert keys1.isdisjoint(keys2)

        # 結果はトリガーされた時刻の新しい順に並ぶため、続きのページは1ページ目の最後より新しくならないこと
        assert datetime.fromisoformat(page2.results[0].created_time) <= datetime.fromisoformat(page1.results[-1].created_time)

        print(f"✅ カーソル方式のページングのテスト成功: 1ページ目{len(page1.results)}件, 2ページ目{len(page2.results)}件")


@pytest.mark.unit
class TestAlarmsApiSignature:
    """ALARMS APIの引数の互換性テスト(APIサーバ不要)"""

    @pytest.fixture
    def mock_api_instance(self):
        """call_apiをモックしたALARMS APIのフィクスチャ"""
        api_client = vcenter_lookup_bridge_client.ApiClient()
        api_client.call_api = MagicMock()
        api_client.response_deserialize = MagicMock()
        return vcenter_lookup_bridge_client.AlarmsApi(api_client)

    def test_list_alarms_positional_request_timeout(self, mock_api_instance):
        """13番目の位置引数が従来どおり_request_timeoutとして扱われることを確認"""
        mock_api_instance.list_alarms("2026-01-01", "2026-01-31", None, None, None, None, None, None, None, 0, 100, "vcenter01", 30.0)

        args, kwargs = mock_api_instance.api_client.call_api.call_args
        assert kwargs["_request_timeout"] == 30.0
        assert "cursor" not in args[1]

    def test_list_alarms_cursor_keyword(self, mock_api_instance):
        """cursorをキーワード引数で指定するとクエリに付与されることを確認"""
        mock_api_instance.list_alarms(cursor="abc", max_results=10)

        args, _ = mock_api_instance.api_client.call_api.call_args
        assert "cursor=abc" in args[1]
        assert "max_results=10" in args[1]


@pytest.mark.unit
class TestAlarmListResponseSchemaModel:
    """ALARMSのレスポンスモデルのテスト(APIサーバ不要)"""

    def _response(self, result, **kwargs):
        return {
            "results": [result],
            "success": True,
            "partialFailure": False,
            "timestamp": "2026-01-01T00:00:00+00:00",
            **kwargs,
        }

    def test_key_and_next_cursor(self):
        """key・truncated・pagination.nextCursorが読み込まれることを確認"""
        response = AlarmListResponseSchema.from_dict(
            self._response(
                {"key": "alarm-7.host-21", "name": "a", "description": "d", "alarmSource": None, "status": "red", "createdTime": "2026-01-01T00:00:00+00:00", "acknowledged": False, "acknowledgedTime": None, "vcenter": "vcenter01", "datacenter": None},
                truncated=True,
                pagination={"totalCount": 2, "offset": 0, "limit": 1, "hasNext": True, "hasPrevious": False, "nextCursor": "abc"},
            )
        )
        assert isinstance(response.results[0].key, str)
        assert response.truncated is True
        assert response.pagination.next_cursor == "abc"
        assert response.to_dict()["pagination"]["nextCursor"] == "abc"

    def test_truncated_default_false(self):
        """truncatedがない場合はFalse、nextCursorがない場合はNoneになることを確認"""
        response = AlarmListResponseSchema.from_dict(
            self._response(
                {"key": "alarm-7.host-21", "name": "a", "description": "d", "alarmSource": None, "status": "red", "createdTime": "2026-01-01T00:00:00+00:00", "acknowledged": False, "acknowledgedTime": None, "vcenter": "vcenter01", "datacenter": None},
                pagination={"totalCount": 1, "offset": 0, "limit": 100, "hasNext": False, "hasPrevious": False},
            )
        )
        assert response.truncated is False
        assert response.pagination.next_cursor is None

    def test_key_required(self):
        """keyは必須のため、keyのない結果は検証エラーになることを確認"""
        with pytest.raises(pydantic.ValidationError):
            AlarmListResponseSchema.from_dict(self._response({"name": "a", "description": "d", "alarmSource": None, "status": "red", "createdTime": "2026-01-01T00:00:00+00:00", "acknowledged": False, "acknowledgedTime": None, "vcenter": "vcenter01", "datacenter": None}))
