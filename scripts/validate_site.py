from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
CURRENT_CVS = {
    "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
}
LEGACY_REDIRECTS = {
    "cases/procureflow/index.html": "../catalogo-operacional-compras/",
    "en/cases/procureflow/index.html": "../operational-procurement-catalog/",
    "cases/portal-vesper/index.html": "../portal/",
    "en/cases/portal-vesper/index.html": "../portal/",
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.refs: list[str] = []
        self.pdf_refs: list[str] = []
        self.html_lang = ""
        self.has_title = False
        self.has_description = False
        self.has_canonical = False
        self.has_hreflang = False
        self.has_theme_toggle = False
        self.metric_links = 0
        self.images_without_alt: list[str] = []
        self.classes: set[str] = set()
        self._in_title = False
        self._title_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if tag == "html":
            self.html_lang = data.get("lang") or ""
        if tag == "title":
            self._in_title = True
        if value := data.get("id"):
            self.ids.append(value)
        if value := data.get("class"):
            self.classes.update(value.split())
        if tag == "a" and "metric-link" in (data.get("class") or "").split():
            self.metric_links += 1
        if tag == "meta" and data.get("name") == "description" and (data.get("content") or "").strip():
            self.has_description = True
        if tag == "link" and "canonical" in (data.get("rel") or "").split():
            self.has_canonical = True
        if tag == "link" and data.get("hreflang"):
            self.has_hreflang = True
        if tag == "button" and "theme-toggle" in (data.get("class") or "").split() and data.get("aria-label") and data.get("aria-pressed") is not None:
            self.has_theme_toggle = True
        if tag == "img" and not (data.get("alt") or "").strip():
            self.images_without_alt.append(data.get("src") or "[missing src]")
        attr = "href" if tag in {"a", "link"} else "src" if tag in {"img", "script"} else None
        if attr and (value := data.get(attr)):
            self.refs.append(value)
            if tag == "a" and urlparse(value).path.lower().endswith(".pdf"):
                self.pdf_refs.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.has_title = bool("".join(self._title_text).strip())

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_text.append(data)


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def parse(relative: str) -> PageParser:
    parser = PageParser()
    parser.feed(read(relative))
    return parser


def resolve_reference(page: Path, value: str) -> Path | None:
    if not value or value == "/" or value.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
        return None
    parsed = urlparse(value)
    if parsed.scheme in {"http", "https"}:
        return None
    target = (page.parent / unquote(parsed.path)).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"reference leaves repository root: {value}") from exc
    if parsed.path.endswith("/"):
        target = target / "index.html"
    return target


def require_text(content: str, required: list[str], label: str, errors: list[str]) -> None:
    for phrase in required:
        if phrase not in content:
            errors.append(f"{label}: required verified text missing: {phrase}")


def forbid_text(content: str, forbidden: list[str], label: str, errors: list[str]) -> None:
    for phrase in forbidden:
        if phrase in content:
            errors.append(f"{label}: stale, ambiguous or unsupported text found: {phrase}")


def main() -> int:
    errors: list[str] = []
    html_pages = sorted(ROOT.rglob("*.html"))
    refs_checked = 0
    pdf_links_checked = 0
    active_pt = 0
    active_en = 0
    redirects_seen: set[str] = set()

    for page in html_pages:
        parser = PageParser()
        content = page.read_text(encoding="utf-8")
        parser.feed(content)
        rel = page.relative_to(ROOT)
        rel_str = rel.as_posix()
        is_redirect = "redirect-page" in parser.classes
        is_case = "cases" in rel.parts
        is_active_case = is_case and "case-body" in parser.classes and not is_redirect

        if is_active_case:
            active_pt += int(rel.parts[0] == "cases")
            active_en += int(rel.parts[0] == "en")

        duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
        if duplicates:
            errors.append(f"{rel}: duplicate IDs: {duplicates}")
        if not parser.has_title:
            errors.append(f"{rel}: title missing")
        if not parser.html_lang:
            errors.append(f"{rel}: lang missing")
        if not parser.has_description:
            errors.append(f"{rel}: meta description missing")
        if not parser.has_canonical:
            errors.append(f"{rel}: canonical missing")
        if rel.name != "404.html" and not parser.has_hreflang:
            errors.append(f"{rel}: hreflang missing")
        if not is_redirect and not parser.has_theme_toggle:
            errors.append(f"{rel}: accessible theme toggle missing")
        if parser.images_without_alt:
            errors.append(f"{rel}: images without alt: {parser.images_without_alt}")
        if is_active_case and not ({"case-showcase", "case-proof-card"} & parser.classes):
            errors.append(f"{rel}: active case lacks primary visual evidence")
        if is_active_case and not {"case-gallery-section", "case-evidence-index", "evidence-label"}.issubset(parser.classes):
            errors.append(f"{rel}: active case lacks traceable gallery/evidence labels")

        if is_redirect:
            redirects_seen.add(rel_str)
            expected_target = LEGACY_REDIRECTS.get(rel_str)
            if expected_target is None:
                errors.append(f"{rel}: unexpected redirect page")
            elif expected_target not in content:
                errors.append(f"{rel}: redirect target is not canonical: {expected_target}")

        for pdf_ref in parser.pdf_refs:
            pdf_links_checked += 1
            if Path(urlparse(pdf_ref).path).name not in CURRENT_CVS:
                errors.append(f"{rel}: unexpected resume link: {pdf_ref}")

        for value in parser.refs:
            try:
                target = resolve_reference(page, value)
            except ValueError as exc:
                errors.append(f"{rel}: {exc}")
                continue
            if target is None:
                continue
            refs_checked += 1
            if not target.exists():
                errors.append(f"{rel}: missing local reference: {value}")

    if len(html_pages) != 45:
        errors.append(f"unexpected HTML page count: {len(html_pages)} (expected 45)")
    if active_pt != 18 or active_en != 18:
        errors.append(f"unexpected active case count: PT={active_pt}, EN={active_en}, expected 18/18")
    if redirects_seen != set(LEGACY_REDIRECTS):
        errors.append(f"legacy redirect inventory differs: {sorted(redirects_seen)}")

    for relative in (
        "cases/catalogo-operacional-compras/index.html",
        "en/cases/operational-procurement-catalog/index.html",
        "cases/portal/index.html",
        "en/cases/portal/index.html",
    ):
        if not (ROOT / relative).exists():
            errors.append(f"missing canonical strategic route: {relative}")

    pt_home = read("index.html")
    en_home = read("en/index.html")
    pt_skills = read("competencias/index.html")
    en_skills = read("en/skills/index.html")
    pt_catalog = read("cases/catalogo-operacional-compras/index.html")
    en_catalog = read("en/cases/operational-procurement-catalog/index.html")
    pt_portal = read("cases/portal/index.html")
    en_portal = read("en/cases/portal/index.html")

    if parse("index.html").metric_links != 6:
        errors.append("index.html: expected 6 linked metrics")
    if parse("en/index.html").metric_links != 6:
        errors.append("en/index.html: expected 6 linked metrics")

    require_text(pt_home, [
        "Analista de Automação, IA e Integrações", "2 workflows públicos", "Catálogo Operacional de Compras",
        "Usado diariamente por 3 usuários operacionais e consultado pela gestão", "58 nós no workflow de ações",
        "Procurement e sourcing validados em sandbox", "tenant/RLS", "Action Envelope",
        'href="cases/catalogo-operacional-compras/"', 'href="cases/portal/"',
        '<a href="competencias/">Competências</a>', "DIO · 4h / 4 cursos",
    ], "index.html", errors)
    require_text(en_home, [
        "AI Automation &amp; Integrations Analyst", "2 public workflows", "Operational Procurement Catalog",
        "Used daily by 3 operational users and consulted by management", "58 nodes in Actions",
        "Procurement and sourcing validated in sandbox", "tenant/RLS", "Action Envelope",
        'href="cases/operational-procurement-catalog/"', 'href="cases/portal/"',
        '<a href="skills/">Skills</a>', "DIO · 4h / 4 courses",
    ], "en/index.html", errors)
    if 'href="../cases/' in en_home:
        errors.append("en/index.html: English home links must remain inside /en/cases/")

    require_text(pt_skills, [
        "automação low-code/no-code", "OpenAI, Gemini, Ollama, OpenRouter e Codex", "SQLite e FTS5",
        "Action Envelope", "Catálogo Operacional de Compras", "Procurement do Portal validado em sandbox",
        'href="../cases/catalogo-operacional-compras/"', 'href="../cases/portal/"',
    ], "competencias/index.html", errors)
    require_text(en_skills, [
        "low-code/no-code automation", "OpenAI, Gemini, Ollama, OpenRouter and Codex", "SQLite and FTS5",
        "Action Envelopes", "Operational Procurement Catalog", "Portal Procurement validated in sandbox",
        'href="../cases/operational-procurement-catalog/"', 'href="../cases/portal/"',
    ], "en/skills/index.html", errors)

    require_text(pt_catalog, [
        "Catálogo Operacional de Compras", "USO INTERNO DIÁRIO", "três usuários operacionais", "SQLite FTS5",
        "controle de revisão", "aproximadamente dois anos", "Conflito por revisão",
        "https://mayconxzdev.github.io/cases/catalogo-operacional-compras/",
    ], "cases/catalogo-operacional-compras/index.html", errors)
    require_text(en_catalog, [
        "Operational Procurement Catalog", "DAILY INTERNAL USE", "three operational users", "SQLite FTS5",
        "revision", "approximately two years", "Revision conflict",
        "https://mayconxzdev.github.io/en/cases/operational-procurement-catalog/",
    ], "en/cases/operational-procurement-catalog/index.html", errors)

    require_text(pt_portal, [
        "Business Operating Platform multiempresa", "EM DESENVOLVIMENTO · PRÉ-PILOTO", "Produto autoral",
        "tenant/RLS", "Action Envelope", "Procurement Intake e sourcing", "preparada para piloto interno",
        "ainda não está comprovado", "referência pública anterior",
        "https://mayconxzdev.github.io/cases/portal/",
    ], "cases/portal/index.html", errors)
    require_text(en_portal, [
        "Multi-tenant Business Operating Platform", "IN DEVELOPMENT · PRE-PILOT", "Author-built product",
        "tenant/RLS", "Action Envelopes", "Procurement Intake and sourcing", "prepared for an internal pilot",
        "not yet demonstrated", "previous public reference",
        "https://mayconxzdev.github.io/en/cases/portal/",
    ], "en/cases/portal/index.html", errors)

    strategic = pt_home + en_home + pt_skills + en_skills + pt_catalog + en_catalog + pt_portal + en_portal
    forbid_text(strategic, [
        "5 workflows publicados", "5 published workflows", "5 workflows/158", "3 workflows/58",
        "Portal Vesper", ">ProcureFlow<", "cases/procureflow/", "cases/portal-vesper/",
        "RAG/grounding", "FastAPI/Flask", "REGISTRO DE SISTEMAS EM OPERAÇÃO · 2026",
    ], "strategic pages", errors)

    actual_cvs = {path.name for path in (ROOT / "assets/cv").glob("*.pdf")}
    if actual_cvs != CURRENT_CVS:
        errors.append(f"assets/cv inventory differs from current resumes: {sorted(actual_cvs)}")

    sitemap = read("sitemap.xml")
    if sitemap.count("<url>") != 40:
        errors.append(f"sitemap URL count is {sitemap.count('<url>')}, expected 40")
    for route in (
        "https://mayconxzdev.github.io/competencias/",
        "https://mayconxzdev.github.io/en/skills/",
        "https://mayconxzdev.github.io/cases/catalogo-operacional-compras/",
        "https://mayconxzdev.github.io/en/cases/operational-procurement-catalog/",
        "https://mayconxzdev.github.io/cases/portal/",
        "https://mayconxzdev.github.io/en/cases/portal/",
    ):
        if route not in sitemap:
            errors.append(f"sitemap missing strategic route: {route}")
    for stale in (
        "https://mayconxzdev.github.io/cases/procureflow/",
        "https://mayconxzdev.github.io/en/cases/procureflow/",
        "https://mayconxzdev.github.io/cases/portal-vesper/",
        "https://mayconxzdev.github.io/en/cases/portal-vesper/",
    ):
        if stale in sitemap:
            errors.append(f"sitemap contains legacy redirect route: {stale}")

    print(
        f"HTML: {len(html_pages)} | local refs: {refs_checked} | resume links: {pdf_links_checked} | "
        f"active cases PT/EN: {active_pt}/{active_en} | redirects: {len(redirects_seen)}"
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Portfolio content, canonical routes, redirects, links and hygiene validation completed without errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
