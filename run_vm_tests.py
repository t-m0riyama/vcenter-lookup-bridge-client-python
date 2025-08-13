#!/usr/bin/env python3
# coding: utf-8
"""
VM関連APIのテスト実行スクリプト
pyenvを使用して環境を切り替えてテストを実行します。
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(command: str, description: str) -> bool:
    """コマンドを実行し、結果を表示する"""
    print(f"\n🔧 {description}")
    print(f"実行コマンド: {command}")
    print("-" * 50)

    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            cwd=Path(__file__).parent,
        )
        print("✅ 成功")
        if result.stdout:
            print("出力:")
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print("❌ 失敗")
        print(f"エラーコード: {e.returncode}")
        if e.stdout:
            print("標準出力:")
            print(e.stdout)
        if e.stderr:
            print("エラー出力:")
            print(e.stderr)
        return False


def main():
    """メイン関数"""
    print("🚀 VM関連APIテスト実行スクリプト")
    print("=" * 50)

    # 現在のディレクトリを確認
    current_dir = Path.cwd()
    print(f"現在のディレクトリ: {current_dir}")

    # pyenv環境の確認
    print("\n📋 pyenv環境の確認")
    pyenv_version = subprocess.run(
        "pyenv version", shell=True, capture_output=True, text=True
    )
    print(f"現在のpyenv環境: {pyenv_version.stdout.strip()}")

    # 必要な環境変数を設定
    env_vars = {"PYTHONPATH": str(current_dir), "PYTHONUNBUFFERED": "1"}

    # テスト実行の準備
    test_commands = [
        # 単体テストの実行
        {
            "command": "python -m pytest test/test_vms_api.py -v",
            "description": "VM関連APIの単体テスト実行",
        },
        # カバレッジ付きテストの実行
        {
            "command": "python -m pytest test/test_vms_api.py --cov=vcenter_lookup_bridge_client.api.vms_api --cov-report=term-missing -v",
            "description": "VM関連APIのカバレッジ付きテスト実行",
        },
        # 特定のテストメソッドの実行
        {
            "command": "python -m pytest test/test_vms_api.py::TestVmsApi::test_api_connection -v",
            "description": "API接続テストのみ実行",
        },
    ]

    # 各テストコマンドを実行
    success_count = 0
    total_count = len(test_commands)

    for i, test_cmd in enumerate(test_commands, 1):
        print(f"\n📊 テスト {i}/{total_count}")

        # pyenv環境を設定してコマンドを実行
        full_command = (
            f"pyenv shell vcenter-lookup-bridge-client && {test_cmd['command']}"
        )

        if run_command(full_command, test_cmd["description"]):
            success_count += 1

    # 結果サマリー
    print("\n" + "=" * 50)
    print("📈 テスト実行結果サマリー")
    print(f"成功: {success_count}/{total_count}")
    print(f"失敗: {total_count - success_count}/{total_count}")

    if success_count == total_count:
        print("🎉 すべてのテストが成功しました！")
        return 0
    else:
        print("⚠️  一部のテストが失敗しました。")
        return 1


if __name__ == "__main__":
    sys.exit(main())
