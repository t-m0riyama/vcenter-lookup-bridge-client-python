# Plan: vCenter Lookup Bridge CLI (TDD)

## TL;DR
既存の `vcenter_lookup_bridge_client` パッケージ内に `cli/` サブパッケージを追加し、clickベースのCLIを `vlb` コマンドとして提供する。全12 APIをサブコマンドとしてカバーし、テーブル/JSON出力、環境変数+CLIオプションによる接続情報指定をサポートする。

**TDD方針**: 各ステップで「RED（失敗テスト作成）→ GREEN（最小実装で通す）→ REFACTOR」のサイクルを回す。APIコールは `unittest.mock.patch` でモックし、実サーバ不要でテスト可能にする。テストには `click.testing.CliRunner` を使用する。

## テスト方針

- **テスト配置**: `tests/cli/` ディレクトリに配置（既存の統合テストとは分離）
- **モック戦略**: 各APIクラスのメソッドを `unittest.mock.patch` でモックし、固定のレスポンスオブジェクト（pydanticモデルインスタンス）を返す
- **CLIテスト手法**: `click.testing.CliRunner` で `cli` グループを `invoke()` し、`result.exit_code` と `result.output` を検証
- **テストマーカー**: `@pytest.mark.unit` を付与（既存のmarkers設定に合致）
- **共通フィクスチャ**: `tests/cli/conftest.py` にモックレスポンスファクトリと `CliRunner` フィクスチャを定義

## Steps

### Phase 1: テスト基盤とパッケージング設定

1. **パッケージング設定を更新**
   - `setup.py`: `REQUIRES` に `click>=8.0` と `tabulate>=0.9` を追加、`entry_points` に `console_scripts: vlb = vcenter_lookup_bridge_client.cli.main:cli` を追加
   - `pyproject.toml`: `dependencies` に `click (>=8.0)` と `tabulate (>=0.9)` を追加、`[project.scripts]` セクションに `vlb` エントリポイントを追加
   - `requirements.txt`: `click>=8.0` と `tabulate>=0.9` を追加

2. **テスト基盤を作成**
   - `tests/cli/__init__.py` — 空ファイル
   - `tests/cli/conftest.py` — 共通フィクスチャ:
     - `cli_runner` — `click.testing.CliRunner` インスタンス
     - `mock_api_client` — `ApiClient` のモック（`Configuration` 含む）
     - 各APIレスポンスのファクトリ関数（`make_vm_list_response()` 等）
   - `vcenter_lookup_bridge_client/cli/__init__.py` — 空ファイル（importエラー回避のため先行作成）

### Phase 2: CLI骨格 — RED → GREEN → REFACTOR

3. **RED: `tests/cli/test_main.py`** — メインCLIグループのテストを先に書く
   - `test_cli_help` — `vlb --help` が exit_code=0 で、サブコマンド一覧を含む出力を返す
   - `test_cli_version` — `vlb --version` が正しいバージョンを返す
   - `test_cli_missing_host_shows_error` — `--host` も `VLB_HOST` も未設定時にエラー

4. **GREEN: `vcenter_lookup_bridge_client/cli/main.py`** — テストを通す最小実装
   - click グループ定義、グローバルオプション（`--host`, `--username`, `--password`, `--format`, `--no-verify-ssl`）
   - 環境変数（`VLB_HOST`, `VLB_USERNAME`, `VLB_PASSWORD`）からのデフォルト値読み込み
   - `click.Context.obj` 経由で `ApiClient` を全サブコマンドに共有

5. **RED: `tests/cli/test_formatters.py`** — フォーマッタのテストを先に書く
   - `test_output_json_single_result` — 単一結果のJSON出力
   - `test_output_json_list_results` — リスト結果のJSON出力
   - `test_output_table_list_results` — リスト結果のテーブル出力（ヘッダ、行数）
   - `test_output_table_empty_results` — 空結果のテーブル出力

6. **GREEN: `vcenter_lookup_bridge_client/cli/formatters.py`** — テストを通す実装
   - `output_json(data, file=sys.stdout)` — pydanticモデルを `.model_dump()` → `json.dumps()`
   - `output_table(data, columns, file=sys.stdout)` — `tabulate` でテーブル整形

### Phase 3: サブコマンド実装 — 各API毎に RED → GREEN

各サブコマンドは以下のTDDサイクルで実装する。テストファイル → 実装ファイルの順。

7. **VMs** (`vlb vms list` / `vlb vms get`)
   - RED: `tests/cli/test_vms.py`
     - `test_vms_list_success` — モックAPI → テーブル出力に期待カラム含む、exit_code=0
     - `test_vms_list_json_format` — `--format json` → JSON出力
     - `test_vms_list_missing_vm_folders` — `--vm-folders` 省略時エラー
     - `test_vms_get_success` — UUIDと`--vcenter`指定 → 詳細テーブル出力
     - `test_vms_get_api_error` — API例外発生時 → エラーメッセージ、exit_code=1
   - GREEN: `vcenter_lookup_bridge_client/cli/vms.py`
   - 利用API: `VmsApi.list_vms()`, `VmsApi.get_vm()`

8. **Hosts** (`vlb hosts list` / `vlb hosts get`)
   - RED: `tests/cli/test_hosts.py`
     - `test_hosts_list_success` / `test_hosts_list_json` / `test_hosts_get_success` / `test_hosts_get_api_error`
   - GREEN: `vcenter_lookup_bridge_client/cli/hosts.py`
   - 利用API: `HostsApi.list_hosts()`, `HostsApi.get_host()`

9. **Clusters** (`vlb clusters list`)
   - RED: `tests/cli/test_clusters.py`
     - `test_clusters_list_success` / `test_clusters_list_json` / `test_clusters_list_with_filter`
   - GREEN: `vcenter_lookup_bridge_client/cli/clusters.py`
   - 利用API: `ClustersApi.list_clusters()`

10. **Datastores** (`vlb datastores list`)
    - RED: `tests/cli/test_datastores.py`
      - `test_datastores_list_success` / `test_datastores_list_missing_tag_category` / `test_datastores_list_missing_tags`
    - GREEN: `vcenter_lookup_bridge_client/cli/datastores.py`
    - 利用API: `DatastoresApi.list_datastores()`

11. **Portgroups** (`vlb portgroups list`)
    - RED: `tests/cli/test_portgroups.py`
      - `test_portgroups_list_success` / `test_portgroups_list_json` / `test_portgroups_list_missing_required`
    - GREEN: `vcenter_lookup_bridge_client/cli/portgroups.py`
    - 利用API: `PortgroupsApi.list_portgroups()`

12. **VM Folders** (`vlb vm-folders list`)
    - RED: `tests/cli/test_vm_folders.py`
      - `test_vm_folders_list_success` / `test_vm_folders_list_json`
    - GREEN: `vcenter_lookup_bridge_client/cli/vm_folders.py`
    - 利用API: `VmFoldersApi.list_vm_folders()`

13. **VM Snapshots** (`vlb vm-snapshots list` / `vlb vm-snapshots get`)
    - RED: `tests/cli/test_vm_snapshots.py`
      - `test_vm_snapshots_list_success` / `test_vm_snapshots_get_success` / `test_vm_snapshots_list_missing_vm_folders`
    - GREEN: `vcenter_lookup_bridge_client/cli/vm_snapshots.py`
    - 利用API: `VmSnapshotsApi.list_vm_snapshots()`, `VmSnapshotsApi.get_vm_snapshots()`

14. **Events** (`vlb events list`)
    - RED: `tests/cli/test_events.py`
      - `test_events_list_with_days_ago` / `test_events_list_with_time_range` / `test_events_list_json` / `test_events_list_with_filters`
    - GREEN: `vcenter_lookup_bridge_client/cli/events.py`
    - 利用API: `EventsApi.list_events()`

15. **Alarms** (`vlb alarms list`)
    - RED: `tests/cli/test_alarms.py`
      - `test_alarms_list_with_days_ago` / `test_alarms_list_json` / `test_alarms_list_with_status_filter`
    - GREEN: `vcenter_lookup_bridge_client/cli/alarms.py`
    - 利用API: `AlarmsApi.list_alarms()`

16. **Vcenters** (`vlb vcenters list`)
    - RED: `tests/cli/test_vcenters.py`
      - `test_vcenters_list_success` / `test_vcenters_list_json`
    - GREEN: `vcenter_lookup_bridge_client/cli/vcenters.py`
    - 利用API: `VcentersApi.list_vcenters()`

17. **Admins** (`vlb admins flush-caches` / `vlb admins reset-ws-session`)
    - RED: `tests/cli/test_admins.py`
      - `test_flush_caches_success` / `test_reset_ws_session_success` / `test_flush_caches_api_error`
    - GREEN: `vcenter_lookup_bridge_client/cli/admins.py`
    - 利用API: `AdminsApi.flush_caches()`, `AdminsApi.reset_ws_session()`

18. **Healthcheck** (`vlb healthcheck`)
    - RED: `tests/cli/test_healthcheck.py`
      - `test_healthcheck_success` / `test_healthcheck_json` / `test_healthcheck_api_error`
    - GREEN: `vcenter_lookup_bridge_client/cli/healthcheck.py`
    - 利用API: `HealthcheckApi.get_service_status()`

### Phase 4: 統合・エラーハンドリング — RED → GREEN → REFACTOR

19. **RED: `tests/cli/test_error_handling.py`** — エラーハンドリングの横断テスト
    - `test_api_exception_shows_status_and_message` — `ApiException(status=404)` → "Error 404: ..." メッセージ
    - `test_connection_error_shows_message` — 接続エラー → "Connection failed: ..." メッセージ
    - `test_invalid_credentials_exit_code` — 401エラー → exit_code=1

20. **GREEN: エラーハンドリング実装** — `main.py` または共通デコレータで `ApiException` をキャッチし、ユーザーフレンドリーなエラーメッセージを表示し、適切な終了コードで終了

21. **REFACTOR** — 全テスト通過後、コード整理
    - 重複パターンの共通化（サブコマンド間の共通ページングオプション等）
    - テストフィクスチャの整理

## サブコマンド仕様まとめ

| サブコマンド | アクション | 必須パラメータ | オプションパラメータ |
|---|---|---|---|
| `vlb vms list` | VM一覧 | `--vm-folders` | `--offset`, `--max-results`, `--vcenter` |
| `vlb vms get <uuid>` | VM詳細 | `<uuid>`, `--vcenter` | — |
| `vlb hosts list` | ホスト一覧 | — | `--offset`, `--max-results`, `--vcenter` |
| `vlb hosts get <uuid>` | ホスト詳細 | `<uuid>`, `--vcenter` | — |
| `vlb clusters list` | クラスタ一覧 | — | `--clusters`, `--offset`, `--max-results`, `--vcenter` |
| `vlb datastores list` | データストア一覧 | `--tag-category`, `--tags` | `--offset`, `--max-results`, `--vcenter` |
| `vlb portgroups list` | ポートグループ一覧 | `--tag-category`, `--tags` | `--offset`, `--max-results`, `--vcenter` |
| `vlb vm-folders list` | VMフォルダ一覧 | — | `--vm-folders`, `--offset`, `--max-results`, `--vcenter` |
| `vlb vm-snapshots list` | スナップショット一覧 | `--vm-folders` | `--offset`, `--max-results`, `--vcenter` |
| `vlb vm-snapshots get <uuid>` | VM別スナップショット | `<uuid>`, `--vcenter` | `--offset`, `--max-results` |
| `vlb events list` | イベント一覧 | — | 時間範囲(3種排他), フィルタ群, ページング |
| `vlb alarms list` | アラーム一覧 | — | 時間範囲(3種排他), フィルタ群, ページング |
| `vlb vcenters list` | vCenter一覧 | — | `--offset`, `--max-results`, `--vcenter` |
| `vlb admins flush-caches` | キャッシュクリア | — | — |
| `vlb admins reset-ws-session` | WSセッションリセット | — | — |
| `vlb healthcheck` | ヘルスチェック | — | — |

全サブコマンド共通グローバルオプション: `--host`, `--username`, `--password`, `--format [table|json]`, `--no-verify-ssl`

## Relevant files

### 新規作成（テスト — 先に作成）
- `tests/cli/__init__.py` — 空ファイル
- `tests/cli/conftest.py` — 共通フィクスチャ（`cli_runner`, `mock_api_client`, レスポンスファクトリ）
- `tests/cli/test_main.py` — メインCLIグループのテスト
- `tests/cli/test_formatters.py` — フォーマッタのテスト
- `tests/cli/test_vms.py` — VMsサブコマンドのテスト
- `tests/cli/test_hosts.py` — Hostsサブコマンドのテスト
- `tests/cli/test_clusters.py` — Clustersサブコマンドのテスト
- `tests/cli/test_datastores.py` — Datastoresサブコマンドのテスト
- `tests/cli/test_portgroups.py` — Portgroupsサブコマンドのテスト
- `tests/cli/test_vm_folders.py` — VmFoldersサブコマンドのテスト
- `tests/cli/test_vm_snapshots.py` — VmSnapshotsサブコマンドのテスト
- `tests/cli/test_events.py` — Eventsサブコマンドのテスト
- `tests/cli/test_alarms.py` — Alarmsサブコマンドのテスト
- `tests/cli/test_vcenters.py` — Vcentersサブコマンドのテスト
- `tests/cli/test_admins.py` — Adminsサブコマンドのテスト
- `tests/cli/test_healthcheck.py` — Healthcheckサブコマンドのテスト
- `tests/cli/test_error_handling.py` — エラーハンドリング横断テスト

### 新規作成（実装 — テスト後に作成）
- `vcenter_lookup_bridge_client/cli/__init__.py` — 空ファイル
- `vcenter_lookup_bridge_client/cli/main.py` — click グループ定義、グローバルオプション、ApiClient生成ロジック
- `vcenter_lookup_bridge_client/cli/formatters.py` — `output_table()`, `output_json()` 共通フォーマッタ
- `vcenter_lookup_bridge_client/cli/vms.py` — VMsサブコマンド
- `vcenter_lookup_bridge_client/cli/hosts.py` — Hostsサブコマンド
- `vcenter_lookup_bridge_client/cli/clusters.py` — Clustersサブコマンド
- `vcenter_lookup_bridge_client/cli/datastores.py` — Datastoresサブコマンド
- `vcenter_lookup_bridge_client/cli/portgroups.py` — Portgroupsサブコマンド
- `vcenter_lookup_bridge_client/cli/vm_folders.py` — VmFoldersサブコマンド
- `vcenter_lookup_bridge_client/cli/vm_snapshots.py` — VmSnapshotsサブコマンド
- `vcenter_lookup_bridge_client/cli/events.py` — Eventsサブコマンド
- `vcenter_lookup_bridge_client/cli/alarms.py` — Alarmsサブコマンド
- `vcenter_lookup_bridge_client/cli/vcenters.py` — Vcentersサブコマンド
- `vcenter_lookup_bridge_client/cli/admins.py` — Adminsサブコマンド
- `vcenter_lookup_bridge_client/cli/healthcheck.py` — Healthcheckサブコマンド

### 変更
- `setup.py` — `REQUIRES` に click/tabulate 追加、`entry_points` に console_scripts 追加
- `pyproject.toml` — `dependencies` に click/tabulate 追加、`[project.scripts]` セクション追加
- `requirements.txt` — click/tabulate 追加

## テスト実行方法

```bash
# CLIテストのみ実行（unitマーカー）
pytest tests/cli/ -m unit -v

# 特定サブコマンドのテストのみ
pytest tests/cli/test_vms.py -v

# 全テスト（既存の統合テスト含む）
pytest tests/ -v
```

## Verification

1. 各Phase完了時に `pytest tests/cli/ -v` で全CLIテストがパスすることを確認
2. `pip install -e .` → `vlb --help` でヘルプ表示を確認
3. `vlb vms --help`, `vlb hosts --help` 等、各サブコマンドのヘルプ表示確認
4. `vlb healthcheck` で実サーバへの疎通確認（実サーバ接続可能な場合）
5. 環境変数 `VLB_HOST`, `VLB_USERNAME`, `VLB_PASSWORD` でのオプション省略動作確認
6. テストカバレッジの確認: `pytest tests/cli/ --cov=vcenter_lookup_bridge_client.cli --cov-report=term-missing`

## Decisions

- **TDD**: テストファイルを先に作成し、RED状態を確認してから実装（GREEN）に進む
- **モック**: `unittest.mock.patch` でAPIクラスのメソッドをモックし、実サーバ不要でテスト可能にする
- **CLIテスト**: `click.testing.CliRunner` を使用し、プロセス起動なしでコマンドをテスト
- CLIフレームワーク: **click** — 成熟したライブラリでサブコマンドグループ・環境変数サポートが標準搭載
- テーブル出力: **tabulate** ライブラリを使用（軽量で依存なし）
- コマンド名: `vlb`
- CLI コードは `vcenter_lookup_bridge_client/cli/` に配置し、パッケージに同梱
- 認証情報は環境変数（`VLB_HOST`, `VLB_USERNAME`, `VLB_PASSWORD`）をデフォルトに、CLIオプション（`--host`, `--username`, `--password`）で上書き可能
- カンマ区切りリスト引数のパース（`--vm-folders folder1,folder2`）はclick callbackで処理
- AdminsApi（flush-caches, reset-ws-session）はPOSTエンドポイントだが管理コマンドとして含める
- このリポジトリはOpenAPI Generatorで自動生成されたコードのため、cli/ ディレクトリは手動管理コードとして追加
