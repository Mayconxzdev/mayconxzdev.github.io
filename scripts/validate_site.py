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
        self._in_title = False
        self._title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "html": self.html_lang = data.get("lang") or ""
        if tag == "title": self._in_title = True
        if value := data.get("id"): self.ids.append(value)
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
        for value in parser.refs:
            try: target = resolve_reference(page, value)
            except ValueError as exc: errors.append(f"{rel}: {exc}"); continue
            if target is None: continue
            refs_checked += 1
            if not target.exists(): errors.append(f"{rel}: referência inexistente: {value}")
    pt_cases = len(list((ROOT / "cases").glob("*/index.html")))
    en_cases = len(list((ROOT / "en/cases").glob("*/index.html")))
    if pt_cases != 18 or en_cases != 18: errors.append(f"quantidade de cases inesperada: PT={pt_cases}, EN={en_cases}")
    if not (ROOT / "assets/cv/Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf").exists(): errors.append("currículo PDF ausente")
    css = (ROOT / "css/styles.css").read_text(encoding="utf-8")
    if "[hidden]" not in css: errors.append("CSS não preserva o atributo hidden")
    print(f"HTML: {len(html_pages)} páginas | referências locais: {refs_checked} | cases: PT {pt_cases} / EN {en_cases}")
    if errors:
        for error in errors: print(f"ERRO: {error}")
        return 1
    print("Validação concluída sem erros.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
