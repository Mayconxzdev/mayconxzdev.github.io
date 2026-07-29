from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]

class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.refs: list[str] = []
        self.has_title = False
        self.html_lang = ""
        self.has_description = False
        self.has_canonical = False
        self.has_hreflang = False
        self.has_theme_toggle = False
        self.images_without_alt: list[str] = []
        self.classes: set[str] = set()
        self._in_title = False
        self._title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "html": self.html_lang = data.get("lang") or ""
        if tag == "title": self._in_title = True
        if value := data.get("id"): self.ids.append(value)
        if value := data.get("class"): self.classes.update(value.split())
        if tag == "meta" and data.get("name") == "description" and (data.get("content") or "").strip(): self.has_description = True
        if tag == "link" and "canonical" in (data.get("rel") or "").split(): self.has_canonical = True
        if tag == "link" and data.get("hreflang"): self.has_hreflang = True
        if tag == "button" and "theme-toggle" in (data.get("class") or "").split() and data.get("aria-label") and data.get("aria-pressed") is not None: self.has_theme_toggle = True
        if tag == "img" and not (data.get("alt") or "").strip(): self.images_without_alt.append(data.get("src") or "[sem src]")
        attr = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script"} else None
        if attr and (value := data.get(attr)): self.refs.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.has_title = bool("".join(self._title_text).strip())

    def handle_data(self, data: str) -> None:
        if self._in_title: self._title_text.append(data)


def resolve_reference(page: Path, value: str) -> Path | None:
    if not value or value == "/" or value.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    parsed = urlparse(value)
    if parsed.scheme in {"http", "https"}: return None
    target = (page.parent / unquote(parsed.path)).resolve()
    try: target.relative_to(ROOT)
    except ValueError as exc: raise ValueError(f"referência sai da raiz: {value}") from exc
    if parsed.path.endswith("/"): target = target / "index.html"
    return target


def main() -> int:
    errors: list[str] = []
    html_pages = sorted(ROOT.rglob("*.html"))
    refs_checked = 0
    for page in html_pages:
        parser = PageParser(); parser.feed(page.read_text(encoding="utf-8")); rel = page.relative_to(ROOT)
        duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
        if duplicates: errors.append(f"{rel}: IDs duplicados: {duplicates}")
        if not parser.has_title: errors.append(f"{rel}: título ausente")
        if not parser.html_lang: errors.append(f"{rel}: atributo lang ausente")
        if not parser.has_description: errors.append(f"{rel}: meta description ausente")
        if not parser.has_canonical: errors.append(f"{rel}: canonical ausente")
        if rel.name != "404.html" and not parser.has_hreflang: errors.append(f"{rel}: hreflang ausente")
        if not parser.has_theme_toggle: errors.append(f"{rel}: controle de tema acessível ausente")
        if parser.images_without_alt: errors.append(f"{rel}: imagens sem alt: {parser.images_without_alt}")
        if "cases" in rel.parts and not ({"case-showcase", "case-proof-card"} & parser.classes): errors.append(f"{rel}: case sem prova visual principal")
        for value in parser.refs:
            try: target = resolve_reference(page, value)
            except ValueError as exc: errors.append(f"{rel}: {exc}"); continue
            if target is None: continue
            refs_checked += 1
            if not target.exists(): errors.append(f"{rel}: referência inexistente: {value}")
    pt_cases = len(list((ROOT / "cases").glob("*/index.html")))
    en_cases = len(list((ROOT / "en/cases").glob("*/index.html")))
    if pt_cases != 18 or en_cases != 18: errors.append(f"quantidade de cases inesperada: PT={pt_cases}, EN={en_cases}")
    for case in (ROOT / "cases").glob("*/index.html"):
        translated = ROOT / "en" / case.relative_to(ROOT)
        if not translated.exists(): errors.append(f"case sem equivalente em inglês: {case.relative_to(ROOT)}")
    if not (ROOT / "assets/cv/Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf").exists(): errors.append("currículo PDF ausente")
    if not (ROOT / "assets/cv/Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf").exists(): errors.append("resume em inglês ausente")
    css = (ROOT / "css/styles.css").read_text(encoding="utf-8")
    if "[hidden]" not in css: errors.append("CSS não preserva o atributo hidden")
    print(f"HTML: {len(html_pages)} páginas | referências locais: {refs_checked} | cases: PT {pt_cases} / EN {en_cases}")
    if errors:
        for error in errors: print(f"ERRO: {error}")
        return 1
    print("Validação concluída sem erros.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
