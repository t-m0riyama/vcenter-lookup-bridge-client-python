"""i18n モジュールのテスト"""

import os
import pytest

from vcenter_lookup_bridge_client.cli.i18n import _detect_locale, _, LazyString


@pytest.mark.unit
class TestDetectLocale:
    def test_vlb_lang_ja(self, monkeypatch):
        """VLB_LANG=ja → 'ja' を返す"""
        monkeypatch.setenv("VLB_LANG", "ja")
        monkeypatch.delenv("LANG", raising=False)
        monkeypatch.delenv("LC_ALL", raising=False)
        monkeypatch.delenv("LC_MESSAGES", raising=False)
        assert _detect_locale() == "ja"

    def test_vlb_lang_en(self, monkeypatch):
        """VLB_LANG=en → 'en' を返す"""
        monkeypatch.setenv("VLB_LANG", "en")
        assert _detect_locale() == "en"

    def test_vlb_lang_takes_priority_over_lang(self, monkeypatch):
        """VLB_LANG が LANG より優先される"""
        monkeypatch.setenv("VLB_LANG", "en")
        monkeypatch.setenv("LANG", "ja_JP.UTF-8")
        assert _detect_locale() == "en"

    def test_lang_env_ja(self, monkeypatch):
        """LANG=ja_JP.UTF-8 → 'ja' を返す"""
        monkeypatch.delenv("VLB_LANG", raising=False)
        monkeypatch.setenv("LANG", "ja_JP.UTF-8")
        monkeypatch.delenv("LC_ALL", raising=False)
        monkeypatch.delenv("LC_MESSAGES", raising=False)
        assert _detect_locale() == "ja"

    def test_lc_all_env_ja(self, monkeypatch):
        """LC_ALL=ja_JP.UTF-8 → 'ja' を返す"""
        monkeypatch.delenv("VLB_LANG", raising=False)
        monkeypatch.delenv("LANG", raising=False)
        monkeypatch.setenv("LC_ALL", "ja_JP.UTF-8")
        monkeypatch.delenv("LC_MESSAGES", raising=False)
        assert _detect_locale() == "ja"

    def test_fallback_en(self, monkeypatch):
        """サポート外の言語 → 'en' にフォールバックする"""
        monkeypatch.setenv("VLB_LANG", "fr")
        monkeypatch.delenv("LANG", raising=False)
        monkeypatch.delenv("LC_ALL", raising=False)
        monkeypatch.delenv("LC_MESSAGES", raising=False)
        assert _detect_locale() == "en"


@pytest.mark.unit
class TestLazyString:
    def test_str_en(self, monkeypatch):
        """英語ロケールで str() が英語メッセージを返す"""
        monkeypatch.setenv("VLB_LANG", "en")
        s = _("Virtual Machine (VM) operations")
        assert str(s) == "Virtual Machine (VM) operations"

    def test_str_ja(self, monkeypatch):
        """日本語ロケールで str() が日本語翻訳を返す"""
        monkeypatch.setenv("VLB_LANG", "ja")
        s = _("Virtual Machine (VM) operations")
        assert str(s) == "仮想マシン (VM) 操作"

    def test_format_method(self, monkeypatch):
        """LazyString.format() が正しく動作する"""
        monkeypatch.setenv("VLB_LANG", "en")
        s = _("Error {status}: {reason}")
        result = s.format(status=404, reason="Not Found")
        assert result == "Error 404: Not Found"

    def test_format_method_ja(self, monkeypatch):
        """日本語ロケールで LazyString.format() が日本語翻訳を使う"""
        monkeypatch.setenv("VLB_LANG", "ja")
        s = _("Error {status}: {reason}")
        result = s.format(status=404, reason="Not Found")
        assert result == "エラー 404: Not Found"

    def test_len(self, monkeypatch):
        """len() が翻訳後の文字列長を返す"""
        monkeypatch.setenv("VLB_LANG", "en")
        s = _("Cluster operations")
        assert len(s) == len("Cluster operations")

    def test_repr(self):
        """repr() が msgid を含む文字列を返す"""
        s = _("Cluster operations")
        assert "Cluster operations" in repr(s)

    def test_click_help_integration(self, monkeypatch):
        """Click の help= に渡して str() 変換されること"""
        monkeypatch.setenv("VLB_LANG", "ja")
        from vcenter_lookup_bridge_client.cli.vms import vms
        # Click は help を str() で評価するため LazyString が日本語に変換される
        help_text = str(vms.help)
        assert "仮想マシン" in help_text
