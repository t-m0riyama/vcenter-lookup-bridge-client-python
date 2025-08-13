# APIクライアントテスト実行ガイド

## 📋 概要

このプロジェクトでは、vCenter Lookup Bridge APIのクライアントのテストを実装しています。モックを使わずに実際のAPIを呼び出してテストを行います。

## 🏗️ 実装内容

### 1. テストデータの分離

リクエストパラメータと期待するレスポンスデータは `tests/test_dataset/${DATA_SET}/*/settings.py` に分離されています：

VMS APIであれば、以下のような変数を環境に応じて調整します。
- `EXPECTED_VM_RESPONSE`: 単一VMのレスポンス例
- `EXPECTED_VM_LIST_RESPONSE`: VMリストのレスポンス例
- `EXPECTED_ERROR_RESPONSE`: エラーレスポンス例
- `EXPECTED_EMPTY_VM_LIST_RESPONSE`: 空のVMリストレスポンス例
- `EXPECTED_FILTERED_VM_LIST_RESPONSE`: フィルタリングされたVMリストレスポンス例

### 2. テストファイル

#### メインテストファイル
- `test/test_vms_api.py`: 完全なVM APIテスト（pytest使用）
- `test_vm_api_simple.py`: シンプルなVM APIテスト（unittest使用）

#### テストデータ
- `test/test_data/__init__.py`: テストデータパッケージ
- `test/test_data/vm_responses.py`: VM関連レスポンスデータ

### 3. テスト実行スクリプト
- `run_vm_tests.py`: pyenvを使用したテスト実行スクリプト

## 🚀 テスト実行方法

### 方法1: シンプルなテスト実行

```bash
# シンプルなテストを実行
python test_vm_api_simple.py
```

### 方法2: pyenvを使用したテスト実行

```bash
# pyenv環境を設定してテストを実行
pyenv shell vcenter-lookup-bridge-client
python -m pytest test/test_vms_api.py -v
```

### 方法3: テスト実行スクリプトを使用

```bash
# 自動化されたテスト実行
python run_vm_tests.py
```

## 📊 テストケース

### 実装済みテストケース

1. **API接続テスト**
   - サーバーへの接続確認
   - ヘルスチェックエンドポイントの確認

2. **VM取得テスト**
   - 単一VM取得の成功テスト
   - 存在しないVM取得のエラーテスト

3. **VMリスト取得テスト**
   - 全VMリスト取得の成功テスト
   - ページネーション付きVMリスト取得テスト
   - フィルター付きVMリスト取得テスト
   - 空の結果フィルターテスト

4. **データ構造テスト**
   - 期待するレスポンスデータの構造確認
   - VMリストレスポンスの構造確認

### テストの特徴

- **モック不使用**: 実際のAPIを呼び出してテスト
- **エラーハンドリング**: 接続エラーやAPIエラーの適切な処理
- **データ検証**: レスポンスの構造とデータ型の検証
- **フィルタリング**: 各種フィルターパラメータのテスト

## ⚙️ 設定

### APIサーバー設定

テストは以下の設定でAPIサーバーに接続します：

```python
Configuration(
    host="http://localhost:8000"
)
```

### テスト用データ

テストで使用するVM UUID：
- 正常テスト用: `421d0f07-b177-f71b-9723-123456789abc`
- エラーテスト用: `99999999-9999-9999-9999-999999999999`

## 🔧 必要な依存関係

```bash
# 基本的な依存関係
pip install requests pytest

# 開発用依存関係
pip install pytest-cov flake8 mypy
```

## 📝 テスト実行時の注意事項

1. **APIサーバーの起動**: テスト実行前にAPIサーバーが起動していることを確認
2. **ネットワーク接続**: localhost:8000への接続が可能であることを確認
3. **pyenv環境**: pyenvを使用する場合は適切な環境が設定されていることを確認

## 🐛 トラブルシューティング

### よくある問題

1. **接続エラー**
   ```
   APIサーバーに接続できません。サーバーが起動していることを確認してください。
   ```
   → APIサーバーが起動していることを確認

2. **pyenv環境エラー**
   ```
   pyenv: shell integration not enabled
   ```
   → pyenvの初期化が必要

3. **インポートエラー**
   ```
   ModuleNotFoundError: No module named 'vcenter_lookup_bridge_client'
   ```
   → Pythonパスが正しく設定されていることを確認

### 解決方法

1. **APIサーバーの起動確認**
   ```bash
   curl http://localhost:8000/healthcheck
   ```

2. **pyenv環境の確認**
   ```bash
   pyenv versions
   pyenv local vcenter-lookup-bridge-client
   ```

3. **Pythonパスの確認**
   ```bash
   python -c "import sys; print(sys.path)"
   ```

## 📈 テスト結果の解釈

### 成功パターン
- ✅ すべてのテストが成功
- 期待するレスポンス構造と一致
- API接続が正常

### 失敗パターン
- ❌ 接続エラー: APIサーバーが起動していない
- ❌ 構造エラー: レスポンス構造が期待と異なる
- ❌ データエラー: レスポンスデータが期待と異なる

## 🔄 継続的改善

今後の改善点：

1. **より詳細なテストケース追加**
   - エッジケースのテスト
   - パフォーマンステスト

2. **テストカバレッジの向上**
   - より多くのAPIエンドポイントのテスト
   - エラーケースの充実

3. **自動化の強化**
   - CI/CDパイプラインへの統合
   - 自動テスト実行の設定 
