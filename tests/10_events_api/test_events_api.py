# coding: utf-8

"""
vCenter Lookup Bridge API - EVENTS APIテスト
"""

import pydantic
import pytest
from typing import Dict, Any

import vcenter_lookup_bridge_client
from vcenter_lookup_bridge_client.models.pagination_info import PaginationInfo
from vcenter_lookup_bridge_client.models.event_response_schema import EventResponseSchema


@pytest.fixture
def api_name():
    """API名のフィクスチャ"""
    return "events_api"


@pytest.fixture
def api_instance(api_client):
    """Events APIのフィクスチャ"""
    return vcenter_lookup_bridge_client.EventsApi(api_client)


class TestEventsApi:
    """Events API unit test"""

    def test_list_events_success_begin_time(self, api_instance, test_dataset):
        """イベントリスト取得の成功テスト 絶対日付指定/タイムゾーン付き"""
        # APIを呼び出し
        response = api_instance.list_events(**test_dataset.VALID_LIST_PARAMETERS_BEGIN_TIME)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        # 　イベントはvCenterにログインするたびに追加されるため、取得した先頭1件のみ比較する
        results = response.results[0:1]
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_EVENT_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, EventResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_EVENT_LIST["results"],
        ):
            assert result.message == expected_result["message"]
            assert result.created_time == expected_result["createdTime"]
            assert result.event_type == expected_result["eventType"]
            assert result.event_source == expected_result["eventSource"]
            assert result.user_name == expected_result["userName"]
            assert result.ip_address == expected_result["ipAddress"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]

        print(
            f"✅ イベントリスト取得テスト(絶対日付指定/タイムゾーン付き)成功: {len(response.results)}件のイベントが見つかりました"
        )

    def test_list_events_success_begin_time2(self, api_instance, test_dataset):
        """イベントリスト取得の成功テスト 絶対日付指定/タイムゾーンなし"""
        # APIを呼び出し
        response = api_instance.list_events(**test_dataset.VALID_LIST_PARAMETERS_BEGIN_TIME2)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        # 　イベントはvCenterにログインするたびに追加されるため、取得した先頭1件のみ比較する
        results = response.results[0:1]
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_EVENT_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, EventResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_EVENT_LIST["results"],
        ):
            assert result.message == expected_result["message"]
            assert result.created_time == expected_result["createdTime"]
            assert result.event_type == expected_result["eventType"]
            assert result.event_source == expected_result["eventSource"]
            assert result.user_name == expected_result["userName"]
            assert result.ip_address == expected_result["ipAddress"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]

        print(
            f"✅ イベントリスト取得テスト(絶対日付指定/タイムゾーンなし)成功: {len(response.results)}件のイベントが見つかりました"
        )

    def test_list_events_success_days_ago(self, api_instance, test_dataset):
        """イベントリスト取得の成功テスト 相対日付指定/日数"""
        # APIを呼び出し
        response = api_instance.list_events(**test_dataset.VALID_LIST_PARAMETERS_DAYS_AGO)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        # 　イベントはvCenterにログインするたびに追加されるため、取得した先頭1件のみ比較する
        results = response.results[0:1]
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_EVENT_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, EventResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_EVENT_LIST["results"],
        ):
            assert result.message == expected_result["message"]
            assert result.created_time == expected_result["createdTime"]
            assert result.event_type == expected_result["eventType"]
            assert result.event_source == expected_result["eventSource"]
            assert result.user_name == expected_result["userName"]
            assert result.ip_address == expected_result["ipAddress"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]

        print(
            f"✅ イベントリスト取得テスト(相対日付指定/日数)成功: {len(response.results)}件のイベントが見つかりました"
        )

    def test_list_events_success_hours_ago(self, api_instance, test_dataset):
        """イベントリスト取得の成功テスト 相対日付指定/時間数"""
        # APIを呼び出し
        response = api_instance.list_events(**test_dataset.VALID_LIST_PARAMETERS_HOURS_AGO)

        # レスポンスの基本チェック
        assert response is not None
        assert response.success is True

        # レスポンスデータ本体のチェック
        # 　イベントはvCenterにログインするたびに追加されるため、取得した先頭1件のみ比較する
        results = response.results[0:1]
        assert isinstance(results, list)

        # 期待した件数のクラスタが返却されることをチェック
        assert len(results) == len(test_dataset.EXPECTED_EVENT_LIST["results"])

        for result in results:
            # レスポンスデータがスキーマに適合していることをチェック
            assert isinstance(result, EventResponseSchema)

        # ページネーション情報がスキーマに適合していることをチェック
        pagination = response.pagination
        assert isinstance(pagination, PaginationInfo)

        # 期待結果との比較
        for result, expected_result in zip(
            results,
            test_dataset.EXPECTED_EVENT_LIST["results"],
        ):
            assert result.message == expected_result["message"]
            assert result.created_time == expected_result["createdTime"]
            assert result.event_type == expected_result["eventType"]
            assert result.event_source == expected_result["eventSource"]
            assert result.user_name == expected_result["userName"]
            assert result.ip_address == expected_result["ipAddress"]
            assert result.vcenter == expected_result["vcenter"]
            assert result.datacenter == expected_result["datacenter"]

        print(
            f"✅ イベントリスト取得テスト(相対日付指定/時間数)成功: {len(response.results)}件のイベントが見つかりました"
        )

    def test_list_events_with_invalid_begin_time(self, api_instance, test_dataset):
        """不正な書式の時間を指定したイベント取得のテスト(begin_time, end_time)"""
        try:
            # 不正な書式のbegin_time, end_timeでAPIを呼び出し
            response = api_instance.list_events(**test_dataset.INVALID_LIST_PARAMETERS_BEGIN_TIME)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"不正な書式の時間を指定したイベント取得テスト(begin_time, end_time)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 422エラーは例外として投げられる可能性がある
            print(str(e))
            if "422" in str(e):
                print(
                    f"✅ 不正な書式の時間を指定したイベント取得テスト(begin_time, end_time)成功: 422エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"不正な書式の時間を指定したイベント取得テスト(begin_time, end_time)で予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_events_with_invalid_begin_time2(self, api_instance, test_dataset):
        """不正な書式の時間を指定したイベント取得のテスト2(begin_time, end_time)"""
        try:
            # 不正な書式のbegin_time, end_timeでAPIを呼び出し
            response = api_instance.list_events(**test_dataset.INVALID_LIST_PARAMETERS_BEGIN_TIME2)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"不正な書式の時間を指定したイベント取得テスト2(begin_time, end_time)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 422エラーは例外として投げられる可能性がある
            if "422" in str(e):
                print(
                    f"✅ 不正な書式の時間を指定したイベント取得テスト2(begin_time, end_time): 422エラーが正しく返されました: {str(e)}"
                )
            else:
                pytest.fail(
                    f"不正な書式の時間を指定したイベント取得テスト2(begin_time, end_time)で予期しないエラーが発生しました: {str(e)}"
                )

    def test_list_events_with_invalid_days_ago(self, api_instance, test_dataset):
        """日付指定に対して制限を超える値を指定したイベント取得のテスト(days_ago_begin, days_ago_end)"""
        try:
            # 不正な書式のdays_ago_begin, days_ago_endでAPIを呼び出し
            response = api_instance.list_events(**test_dataset.INVALID_LIST_PARAMETERS_DAYS_AGO)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"日付指定に対して制限を超える値を指定したイベント取得テスト(days_ago_begin, days_ago_end)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except pydantic.ValidationError as e:
            print(
                f"✅ 日付指定に対して制限を超える値を指定したイベント取得テスト(days_ago_begin, days_ago_end)成功: 422エラーが正しく返されました: {str(e)}"
            )
        except Exception as e:
            pytest.fail(
                f"日付指定に対して制限を超える値を指定したイベント取得テスト(days_ago_begin, days_ago_end)で予期しないエラーが発生しました: {str(e)}"
            )

    def test_list_events_with_invalid_hours_ago(self, api_instance, test_dataset):
        """間指定に対して制限を超える値を指定したイベント取得のテスト(hours_ago_begin, hours_ago_end)"""
        try:
            # 不正な書式のhours_ago_begin, hours_ago_endでAPIを呼び出し
            response = api_instance.list_events(**test_dataset.INVALID_LIST_PARAMETERS_HOURS_AGO)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"間指定に対して制限を超える値を指定したイベント取得テスト(hours_ago_begin, hours_ago_end)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except pydantic.ValidationError as e:
            print(
                f"✅ 時間指定に対して制限を超える値を指定したイベント取得テスト(hours_ago_begin, hours_ago_end)成功: 正しくエラーが正しく返されました: {str(e)}"
            )
        except Exception as e:
            pytest.fail(
                f"時間指定に対して制限を超える値を指定したイベント取得テスト(hours_ago_begin, hours_ago_end)で予期しないエラーが発生しました: {str(e)}"
            )

    def test_list_events_not_found_with_invalid_vcenter(self, api_instance, test_dataset):
        """存在しないイベント取得のテスト(vCenter指定)"""
        try:
            # 存在しないvCenterでAPIを呼び出し
            response = api_instance.list_events(**test_dataset.INVALID_LIST_PARAMETERS_VCENTER)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"存在しないイベント取得テスト(vCenter)でエラーが発生しました。想定される例外が発生しませんでした。"
            )

        except Exception as e:
            # 404エラーは例外として投げられる可能性がある
            if "404" in str(e):
                print(f"✅ 存在しないイベント取得テスト(vCenter)成功: 404エラーが正しく返されました: {str(e)}")
            else:
                pytest.fail(f"存在しないイベント取得テスト(vCenter)で予期しないエラーが発生しました: {str(e)}")

    def test_list_events_with_invalid_max_results(self, api_instance, test_dataset):
        """イベントリスト取得のテスト（max_resultsパラメータの制限が有効であることを確認）"""

        # max_resultsに制限（<=1000)を超える値を指定してAPIを呼び出し
        try:
            response = api_instance.list_events(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"max_resultsに制限を超える値(>1000, {test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS['max_results']})を指定したテストでエラーが発生しました"
            )

        except pydantic.ValidationError as e:
            print(f"✅ max_resultsに制限を超える値(>1000)を指定した場合、正しくエラーが返却されました: {e}")

        # max_resultsに制限（>=1)を超える値を指定してAPIを呼び出し
        try:
            response = api_instance.list_events(**test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(
                f"max_resultsに制限を超える値(<0, {test_dataset.INVALID_LIST_PARAMETERS_MAX_RESULTS2['max_results']})を指定したテストでエラーが発生しました"
            )

        except pydantic.ValidationError as e:
            print(f"✅ max_resultsに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}")

    def test_list_events_with_invalid_offset(self, api_instance, test_dataset):
        """イベントリスト取得のテスト（パラメータ制限が有効であることを確認）"""
        # offsetに制限を超える値をを指定してAPIを呼び出し
        try:
            response = api_instance.list_events(**test_dataset.INVALID_LIST_PARAMETERS_OFFSET)

            # 例外が発生し、以降の行は実行されないことを期待する
            pytest.fail(f"offsetに制限を超える値を指定したテストでエラーが発生しました")

        except pydantic.ValidationError as e:
            print(f"✅ offsetに制限を超える値(<0)を指定した場合、正しくエラーが返却されました: {e}")

    def test_list_events_with_pagination(self, api_instance, test_dataset):
        """ページネーション付きクラスタリスト取得のテスト"""
        # ページネーションパラメータを指定してAPIを呼び出し
        response = api_instance.list_events(**test_dataset.VALID_LIST_PARAMETERS_BEGIN_TIME)

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

        print(f"✅ ページネーション付きイベントリスト取得テスト成功: ページ1, 1ページあたり100件")
