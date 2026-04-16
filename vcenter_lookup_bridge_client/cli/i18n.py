"""CLI メッセージの国際化 (i18n) モジュール

優先順位: VLB_LANG > LANG > LC_ALL > LC_MESSAGES > OS デフォルト > "en"
サポート言語: "en", "ja"
"""
from __future__ import annotations

import gettext
import os
from pathlib import Path

_LOCALE_DIR = Path(__file__).parent.parent / "locale"
_SUPPORTED_LANGUAGES = {"en", "ja"}
_DOMAIN = "vlb"


def _detect_locale() -> str:
    """環境変数・OS locale から言語コードを検出して返す。"""
    for env_var in ("VLB_LANG", "LANG", "LC_ALL", "LC_MESSAGES"):
        val = os.environ.get(env_var, "")
        if val:
            lang = val.split("_")[0].split(".")[0].lower()
            if lang in _SUPPORTED_LANGUAGES:
                return lang

    # OS のデフォルト locale を試みる
    try:
        import locale as _locale
        lang_code, _ = _locale.getlocale()
        if lang_code:
            lang = lang_code.split("_")[0].lower()
            if lang in _SUPPORTED_LANGUAGES:
                return lang
    except Exception:
        pass

    return "en"


def _make_translation(lang: str) -> gettext.NullTranslations:
    try:
        return gettext.translation(
            _DOMAIN,
            localedir=str(_LOCALE_DIR),
            languages=[lang],
        )
    except FileNotFoundError:
        return gettext.NullTranslations()


class LazyString:
    """翻訳を遅延評価する文字列ラッパー。

    Click の help= パラメーター（import 時評価）に渡しても、
    実際に str() に変換されるまで翻訳が行われない。
    未実装の str メソッドは __getattr__ で委譲する。
    """

    __slots__ = ("_msgid",)

    def __init__(self, msgid: str) -> None:
        self._msgid = msgid

    def _translate(self) -> str:
        lang = _detect_locale()
        t = _make_translation(lang)
        return t.gettext(self._msgid)

    def __str__(self) -> str:
        return self._translate()

    def __repr__(self) -> str:
        return f"LazyString({self._msgid!r})"

    def __len__(self) -> int:
        return len(self._translate())

    def __bool__(self) -> bool:
        return bool(self._msgid)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, LazyString):
            return self._msgid == other._msgid
        return self._translate() == other

    def __hash__(self) -> int:
        return hash(self._msgid)

    def __add__(self, other: str) -> str:
        return self._translate() + other

    def __radd__(self, other: str) -> str:
        return other + self._translate()

    def __mod__(self, args: object) -> str:
        return self._translate() % args

    def __format__(self, format_spec: str) -> str:
        return format(self._translate(), format_spec)

    def __getattr__(self, name: str):
        """未実装の str メソッドを翻訳済み文字列に委譲する。"""
        return getattr(self._translate(), name)

    def format(self, *args: object, **kwargs: object) -> str:
        return self._translate().format(*args, **kwargs)


def _(msgid: str) -> LazyString:
    """翻訳可能文字列を返す。Click の help= に直接渡せる。"""
    return LazyString(msgid)
