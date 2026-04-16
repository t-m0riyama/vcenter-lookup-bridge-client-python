import json
import sys
from typing import Any, List

import click
from tabulate import tabulate


def output_json(data: Any, file=None) -> None:
    """pydantic モデルまたはその他のデータを JSON 形式で出力する"""
    if file is None:
        file = sys.stdout
    if hasattr(data, "model_dump"):
        serialized = data.model_dump(by_alias=False)
    elif isinstance(data, list):
        serialized = [
            item.model_dump(by_alias=False) if hasattr(item, "model_dump") else item
            for item in data
        ]
    else:
        serialized = data
    click.echo(json.dumps(serialized, indent=2, default=str), file=file)


def output_table(data: List[Any], columns: List[str], file=None) -> None:
    """データをテーブル形式で出力する"""
    if file is None:
        file = sys.stdout
    rows = []
    for item in data:
        row = [str(getattr(item, col, "") or "") for col in columns]
        rows.append(row)
    click.echo(tabulate(rows, headers=columns, tablefmt="simple"), file=file)
