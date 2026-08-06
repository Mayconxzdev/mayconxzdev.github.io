from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATCHES = {
    "competencias/index.html": [
        (
            "A instância n8n que administro ultrapassou 10 mil execuções em produção.",
            "A instância n8n que administro ultrapassou 10 mil execuções de workflows em produção.",
        ),
    ],
    "en/skills/index.html": [
        (
            "The n8n environment I administer has surpassed 10,000 production executions.",
            "The n8n environment I administer has surpassed 10,000 workflow executions in production.",
        ),
    ],
}


def main() -> None:
    for relative, replacements in PATCHES.items():
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        for old, new in replacements:
            if old in text:
                text = text.replace(old, new)
            elif new not in text:
                raise RuntimeError(f"{relative}: expected wording not found: {old}")
        path.write_text(text, encoding="utf-8")
        print(f"final wording current: {relative}")


if __name__ == "__main__":
    main()
