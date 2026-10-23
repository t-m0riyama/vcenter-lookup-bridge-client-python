import json
import sys
from typing import Any, List, Optional

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


def output_table(data: List[Any], columns: List[str], file=None, str_columns: Optional[List[str]] = None) -> None:
    """データをテーブル形式で出力する

    str_columnsに指定した列は、数値に見える値でも文字列のまま出力する (例: アラームのkeyの"107.10"を107.1にしない)
    """
    if file is None:
        file = sys.stdout
    rows = []
    for item in data:
        row = [str(getattr(item, col, "") or "") for col in columns]
        rows.append(row)
    disable_numparse = [columns.index(col) for col in str_columns if col in columns] if str_columns else False
    click.echo(tabulate(rows, headers=columns, tablefmt="simple", disable_numparse=disable_numparse), file=file)


def output_next_cursor(pagination: Any, file=None) -> None:
    """次のページのカーソルがあれば、表を汚さないよう標準エラーに出力する"""
    from .i18n import _

    next_cursor = getattr(pagination, "next_cursor", None) if pagination is not None else None
    if isinstance(next_cursor, str) and next_cursor:
        if file is None:
            file = sys.stderr
        click.echo(_("Next cursor: {cursor}").format(cursor=next_cursor), file=file)


def _error_details(body: Any) -> List[str]:
    """APIのエラーレスポンスのdetailを、表示用の行のリストにする"""
    if not body:
        return []
    if isinstance(body, (bytes, bytearray)):
        body = body.decode("utf-8", errors="replace")
    try:
        detail = json.loads(body).get("detail")
    except (ValueError, AttributeError):
        return []
    if isinstance(detail, str):
        return [detail]
    if not isinstance(detail, list):
        return []
    lines = []
    for item in detail:
        if not isinstance(item, dict):
            lines.append(str(item))
            continue
        # pydanticのvalue_errorは"Value error, "が先頭に付くため取り除く
        msg = str(item.get("msg", "")).removeprefix("Value error, ")
        # locの先頭はquery/pathなどの場所のため、パラメータ名のみを表示する
        loc = [str(x) for x in item.get("loc", [])[1:]]
        lines.append(f"{'.'.join(loc)}: {msg}" if loc else msg)
    return lines


def output_api_error(e: Any, err: bool = False) -> None:
    """APIの例外を、ステータスとサーバが返したdetailとあわせて出力する"""
    from .i18n import _

    click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason), err=err)
    for line in _error_details(getattr(e, "body", None)):
        click.echo(f"  {line}", err=err)


def output_truncated_warning(response: Any, file=None) -> None:
    """取得上限で結果が打ち切られた場合に、サーバのメッセージを標準エラーに出力する"""
    from .i18n import _

    if getattr(response, "truncated", None) is not True:
        return
    if file is None:
        file = sys.stderr
    message = getattr(response, "message", None)
    if not (isinstance(message, str) and message):
        message = _("Some vCenters reached the retrieval limit, so the results are truncated")
    click.echo(message, file=file)
