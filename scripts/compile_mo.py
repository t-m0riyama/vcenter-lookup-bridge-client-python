"""Compile .po files to .mo files (gettext binary format).

Usage: python scripts/compile_mo.py
"""
import struct
from pathlib import Path


def compile_po(po_path: Path, mo_path: Path) -> None:
    messages: dict[str, str] = {}
    msgid: str | None = None
    msgstr_lines: list[str] = []
    in_msgstr = False

    def _unquote(s: str) -> str:
        s = s.strip()
        if s.startswith('"') and s.endswith('"'):
            raw = s[1:-1]
            # unescape standard .po escape sequences
            raw = raw.replace("\\n", "\n")
            raw = raw.replace("\\t", "\t")
            raw = raw.replace('\\"', '"')
            raw = raw.replace("\\\\", "\\")
            return raw
        return ""

    with open(po_path, encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.rstrip("\n")
            if line.startswith("msgid "):
                if msgid is not None:
                    messages[msgid] = "".join(msgstr_lines)
                msgid = _unquote(line[6:])
                msgstr_lines = []
                in_msgstr = False
            elif line.startswith("msgstr "):
                in_msgstr = True
                msgstr_lines = [_unquote(line[7:])]
            elif in_msgstr and line.startswith('"'):
                msgstr_lines.append(_unquote(line))
        if msgid is not None:
            messages[msgid] = "".join(msgstr_lines)

    keys = sorted(messages.keys())
    N = len(keys)
    string_start = 28 + N * 8 + N * 8

    orig_offsets: list[tuple[int, int]] = []
    trans_offsets: list[tuple[int, int]] = []
    pos = string_start
    for k in keys:
        b = k.encode("utf-8")
        orig_offsets.append((len(b), pos))
        pos += len(b) + 1
    for k in keys:
        b = messages[k].encode("utf-8")
        trans_offsets.append((len(b), pos))
        pos += len(b) + 1

    mo_path.parent.mkdir(parents=True, exist_ok=True)
    with open(mo_path, "wb") as f:
        # magic, revision, N, offset_originals, offset_translations, hash_size, hash_offset
        f.write(struct.pack("<IIIIIII", 0x950412DE, 0, N, 28, 28 + N * 8, 0, 0))
        for length, offset in orig_offsets:
            f.write(struct.pack("<II", length, offset))
        for length, offset in trans_offsets:
            f.write(struct.pack("<II", length, offset))
        for k in keys:
            f.write(k.encode("utf-8") + b"\x00")
        for k in keys:
            f.write(messages[k].encode("utf-8") + b"\x00")

    print(f"Compiled {po_path} -> {mo_path} ({N} messages)")


if __name__ == "__main__":
    base = Path("vcenter_lookup_bridge_client/locale")
    for lang in ["en", "ja"]:
        po = base / lang / "LC_MESSAGES" / "vlb.po"
        mo = base / lang / "LC_MESSAGES" / "vlb.mo"
        compile_po(po, mo)
