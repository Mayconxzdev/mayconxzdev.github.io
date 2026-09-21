from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "competencias/index.html": [
        ('href="../cases/procureflow/"', 'href="../cases/catalogo-operacional-compras/"'),
        ('href="../cases/portal-vesper/"', 'href="../cases/portal/"'),
    ],
    "en/skills/index.html": [
        ('href="../../cases/procureflow/"', 'href="../cases/operational-procurement-catalog/"'),
        ('href="../../cases/portal-vesper/"', 'href="../cases/portal/"'),
    ],
    "cases/compras-vesper/index.html": [
        ('href="../../cases/procureflow/">ProcureFlow', 'href="../catalogo-operacional-compras/">Catálogo Operacional de Compras'),
    ],
    "en/cases/compras-vesper/index.html": [
        ('href="../../../en/cases/procureflow/">ProcureFlow', 'href="../operational-procurement-catalog/">Operational Procurement Catalog'),
    ],
    "cases/postagem-redes/index.html": [
        ('href="../../cases/portal-vesper/">Portal Vesper', 'href="../portal/">Portal'),
    ],
    "en/cases/postagem-redes/index.html": [
        ('href="../../../en/cases/portal-vesper/">Portal Vesper', 'href="../portal/">Portal'),
    ],
}

SITEMAP_REPLACEMENTS = [
    ("https://mayconxzdev.github.io/cases/procureflow/", "https://mayconxzdev.github.io/cases/catalogo-operacional-compras/"),
    ("https://mayconxzdev.github.io/en/cases/procureflow/", "https://mayconxzdev.github.io/en/cases/operational-procurement-catalog/"),
    ("https://mayconxzdev.github.io/cases/portal-vesper/", "https://mayconxzdev.github.io/cases/portal/"),
    ("https://mayconxzdev.github.io/en/cases/portal-vesper/", "https://mayconxzdev.github.io/en/cases/portal/"),
]


def update_file(relative: str, replacements: list[tuple[str, str]]) -> None:
    path = ROOT / relative
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
        elif new not in text:
            raise RuntimeError(f"{relative}: neither old nor canonical text was found: {old}")
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"canonicalized: {relative}")
    else:
        print(f"canonical: {relative}")


def main() -> None:
    for relative, replacements in REPLACEMENTS.items():
        update_file(relative, replacements)
    update_file("sitemap.xml", SITEMAP_REPLACEMENTS)


if __name__ == "__main__":
    main()
