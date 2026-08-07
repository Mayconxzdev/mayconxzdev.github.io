from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
CURRENT_RESUMES = {
    "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
}
REDIRECT_ROUTES = {
    "cases/procureflow/index.html",
    "en/cases/procureflow/index.html",
    "cases/portal-vesper/index.html",
    "en/cases/portal-vesper/index.html",
    "cases/compass-automation/index.html",
    "en/cases/compass-automation/index.html",
}
IGNORED_HTML_PARTS = {
    ".git",
    ".venv",
    "artifacts",
    "node_modules",
}


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.lang = ""
        self.ids: list[str] = []
        self.refs: list[str] = []
        self.pdf_refs: list[str] = []
        self.classes: set[str] = set()
        self.has_title = False
        self.has_description = False
        self.has_canonical = False
        self.has_hreflang = False
        self.has_theme_toggle = False
        self.images_without_alt: list[str] = []
        self._in_title = False
        self._title: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "html":
            self.lang = data.get("lang") or ""
        if tag == "title":
            self._in_title = True
        if value := data.get("id"):
            self.ids.append(value)
        if value := data.get("class"):
            self.classes.update(value.split())
        if tag == "meta" and data.get("name") == "description" and (data.get("content") or "").strip():
            self.has_description = True
        if tag == "link" and "canonical" in (data.get("rel") or "").split():
            self.has_canonical = True
        if tag == "link" and data.get("hreflang"):
            self.has_hreflang = True
        if tag == "button" and "theme-toggle" in (data.get("class") or "").split():
            self.has_theme_toggle = bool(data.get("aria-label")) and data.get("aria-pressed") is not None
        if tag == "img" and data.get("alt") is None:
            self.images_without_alt.append(data.get("src") or "[missing src]")
        attribute = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script"} else None
        if attribute and (value := data.get(attribute)):
            self.refs.append(value)
            if tag == "a" and urlparse(value).path.lower().endswith(".pdf"):
                self.pdf_refs.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.has_title = bool("".join(self._title).strip())

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title.append(data)


def parse(path: Path) -> Parser:
    parser = Parser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def local_target(page: Path, reference: str) -> Path | None:
    if not reference or reference == "/" or reference.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    parsed = urlparse(reference)
    if parsed.scheme in {"http", "https"}:
        return None
    target = (page.parent / unquote(parsed.path)).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"reference leaves repository root: {reference}") from exc
    if parsed.path.endswith("/"):
        target /= "index.html"
    return target


def is_public_html(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    return not any(part in IGNORED_HTML_PARTS for part in relative.parts)


def main() -> int:
    errors: list[str] = []
    html_files = sorted(path for path in ROOT.rglob("*.html") if is_public_html(path))
    local_references = 0
    resume_links = 0
    pt_cases = 0
    en_cases = 0

    for page in html_files:
        relative = page.relative_to(ROOT)
        relative_str = relative.as_posix()
        parser = parse(page)
        is_redirect = relative_str in REDIRECT_ROUTES or "redirect-page" in parser.classes
        is_case = "cases" in relative.parts and not is_redirect
        if is_case:
            if relative.parts[0] == "cases":
                pt_cases += 1
            elif relative.parts[0] == "en":
                en_cases += 1

        duplicates = sorted({item for item in parser.ids if parser.ids.count(item) > 1})
        if duplicates:
            errors.append(f"{relative}: duplicate IDs: {duplicates}")
        if not parser.lang:
            errors.append(f"{relative}: html lang missing")
        if not parser.has_title:
            errors.append(f"{relative}: title missing")
        if not parser.has_description:
            errors.append(f"{relative}: meta description missing")
        if not parser.has_canonical:
            errors.append(f"{relative}: canonical link missing")
        if relative.name != "404.html" and not parser.has_hreflang:
            errors.append(f"{relative}: hreflang link missing")
        if not is_redirect and not parser.has_theme_toggle:
            errors.append(f"{relative}: accessible theme toggle missing")
        if parser.images_without_alt:
            errors.append(f"{relative}: images without alt attribute: {parser.images_without_alt}")

        for pdf in parser.pdf_refs:
            resume_links += 1
            if Path(urlparse(pdf).path).name not in CURRENT_RESUMES:
                errors.append(f"{relative}: old or unknown resume link: {pdf}")

        for reference in parser.refs:
            try:
                target = local_target(page, reference)
            except ValueError as exc:
                errors.append(f"{relative}: {exc}")
                continue
            if target is None:
                continue
            local_references += 1
            if not target.exists():
                errors.append(f"{relative}: missing local reference: {reference}")

    if len(html_files) != 45:
        errors.append(f"unexpected HTML inventory: {len(html_files)} files, expected 45")
    if pt_cases != 17 or en_cases != 17:
        errors.append(f"unexpected active case inventory: PT={pt_cases}, EN={en_cases}, expected 17/17")
    if not REDIRECT_ROUTES.issubset({path.relative_to(ROOT).as_posix() for path in html_files}):
        errors.append("one or more compatibility redirect pages are missing")

    cv_files = {path.name for path in (ROOT / "assets" / "cv").glob("*.pdf")}
    if cv_files != CURRENT_RESUMES:
        errors.append(f"resume inventory differs from the two current PDFs: {sorted(cv_files)}")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    required_routes = [
        "https://mayconxzdev.github.io/",
        "https://mayconxzdev.github.io/en/",
        "https://mayconxzdev.github.io/competencias/",
        "https://mayconxzdev.github.io/en/skills/",
        "https://mayconxzdev.github.io/cases/catalogo-operacional-compras/",
        "https://mayconxzdev.github.io/en/cases/operational-procurement-catalog/",
        "https://mayconxzdev.github.io/cases/portal/",
        "https://mayconxzdev.github.io/en/cases/portal/",
        "https://mayconxzdev.github.io/cases/compass/",
        "https://mayconxzdev.github.io/en/cases/compass/",
    ]
    for route in required_routes:
        if route not in sitemap:
            errors.append(f"sitemap missing canonical route: {route}")
    for route in REDIRECT_ROUTES:
        url = "https://mayconxzdev.github.io/" + route.removesuffix("index.html")
        if url in sitemap:
            errors.append(f"redirect route must not appear in sitemap: {url}")

    print(
        f"HTML={len(html_files)} | active cases PT/EN={pt_cases}/{en_cases} | "
        f"local refs={local_references} | resume links={resume_links}"
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Portfolio structure, references, canonical routes and resume inventory validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
