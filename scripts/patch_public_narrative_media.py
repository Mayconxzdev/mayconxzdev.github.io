from __future__ import annotations

from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FRAGMENTS = ROOT / "scripts" / "fragments"


def fragment(name: str) -> str:
    return (FRAGMENTS / name).read_text(encoding="utf-8").strip()


def replace_main(path: Path, value: str) -> None:
    text = path.read_text(encoding="utf-8")
    text, count = re.subn(r"<main\b[^>]*>.*?</main>", value, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"{path.relative_to(ROOT)}: expected one main")
    path.write_text(text, encoding="utf-8", newline="")


def set_metadata(path: Path, *, title: str, description: str, canonical: str) -> None:
    text = path.read_text(encoding="utf-8")
    absolute = f"https://mayconxzdev.github.io/{canonical}/"
    replacements = [
        (r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{escape(description, quote=True)}">'),
        (r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{escape(title, quote=True)}">'),
        (r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{escape(description, quote=True)}">'),
        (r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{absolute}">'),
        (r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{absolute}">'),
        (r'<title>.*?</title>', f'<title>{escape(title)}</title>'),
    ]
    for pattern, value in replacements:
        text, count = re.subn(pattern, lambda _match, value=value: value, text, count=1, flags=re.S)
        if count != 1:
            raise RuntimeError(f"{path.relative_to(ROOT)}: metadata missing: {pattern}")
    for language, value in (
        ("pt-BR", "cases/compras-e-cotacoes"),
        ("en", "en/cases/purchasing-and-quotes"),
        ("x-default", "cases/compras-e-cotacoes"),
    ):
        url = f"https://mayconxzdev.github.io/{value}/"
        pattern = rf'<link rel="alternate" hreflang="{re.escape(language)}" href="[^"]*">'
        text, count = re.subn(pattern, f'<link rel="alternate" hreflang="{language}" href="{url}">', text, count=1)
        if count == 0 and language == "en":
            pt = '<link rel="alternate" hreflang="pt-BR" href="https://mayconxzdev.github.io/cases/compras-e-cotacoes/">'
            if pt not in text:
                raise RuntimeError(f"{path.relative_to(ROOT)}: Portuguese alternate missing")
            text = text.replace(pt, pt + f'<link rel="alternate" hreflang="en" href="{url}">', 1)
        elif count != 1:
            raise RuntimeError(f"{path.relative_to(ROOT)}: alternate {language} missing")
    path.write_text(text, encoding="utf-8", newline="")


def add_gallery(path: Path, name: str) -> None:
    text = path.read_text(encoding="utf-8")
    block = fragment(name)
    if block.split('src="', 1)[1].split('"', 1)[0] in text:
        return
    match = re.search(r'<section class="case-facts".*?</section>', text, flags=re.S)
    if not match:
        raise RuntimeError(f"{path.relative_to(ROOT)}: case facts section missing")
    text = text[:match.end()] + "\n" + block + text[match.end():]
    path.write_text(text, encoding="utf-8", newline="")


def main() -> None:
    cases = [
        (ROOT / "cases/compras-e-cotacoes/index.html", "scripts/fragments/purchasing_pt.main.fragment", "Compras e Cotações | Maycon Ferreira", "Aplicação desktop para organizar pedidos de compra, cotações e respostas de fornecedores.", "cases/compras-e-cotacoes"),
        (ROOT / "en/cases/purchasing-and-quotes/index.html", "scripts/fragments/purchasing_en.main.fragment", "Purchasing and Quotes | Maycon Ferreira", "A desktop application that organizes purchase requests, supplier quotes and replies.", "en/cases/purchasing-and-quotes"),
    ]
    for path, source, title, description, canonical in cases:
        replace_main(path, fragment(Path(source).name))
        set_metadata(path, title=title, description=description, canonical=canonical)

    for path, source in [
        (ROOT / "cases/proposta-comercial/index.html", "proposal_gallery_pt.fragment"),
        (ROOT / "en/cases/commercial-proposal/index.html", "proposal_gallery_en.fragment"),
        (ROOT / "cases/tradutor-documental/index.html", "translator_gallery_pt.fragment"),
        (ROOT / "en/cases/offline-document-translator/index.html", "translator_gallery_en.fragment"),
    ]:
        add_gallery(path, source)

    for path, english in [
        (ROOT / "cases/proposta-comercial/index.html", False),
        (ROOT / "en/cases/commercial-proposal/index.html", True),
    ]:
        text = path.read_text(encoding="utf-8")
        text = text.replace("without showing internal screens or data.", "without exposing company data or documents.")
        text = text.replace("sem mostrar dados ou telas internas.", "sem expor dados empresariais ou documentos.")
        path.write_text(text, encoding="utf-8", newline="")

    for path, english in [
        (ROOT / "cases/tradutor-documental/index.html", False),
        (ROOT / "en/cases/offline-document-translator/index.html", True),
    ]:
        text = path.read_text(encoding="utf-8")
        text = text.replace("tradutor-documental-ui.png", "tradutor-interface-bilingue.png")
        if english:
            text = text.replace(
                'alt="Real Translator screen with a demonstration document ready for processing."',
                'alt="The translator showing a completed demonstration document and bilingual output."',
            )
        else:
            text = text.replace(
                'alt="Tela real do Tradutor com um documento de demonstração pronto para processamento."',
                'alt="O tradutor exibindo um documento demonstrativo traduzido e pronto para revisão."',
            )
        path.write_text(text, encoding="utf-8", newline="")

    for path in [ROOT / "index.html", ROOT / "en/index.html"]:
        text = path.read_text(encoding="utf-8").replace("tradutor-documental-ui.png", "tradutor-interface-bilingue.png")
        path.write_text(text, encoding="utf-8", newline="")

    print("Human project names and public screenshots applied to the site source.")


if __name__ == "__main__":
    main()
