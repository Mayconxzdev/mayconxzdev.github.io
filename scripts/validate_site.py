from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
CURRENT_CVS = {
    "Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf",
    "Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf",
}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.refs: list[str] = []
        self.pdf_refs: list[str] = []
        self.has_title = False
        self.html_lang = ""
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
            self.images_without_alt.append(data.get("src") or "[sem src]")
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

    for page in html_pages:
        parser = PageParser()
        content = page.read_text(encoding="utf-8")
        parser.feed(content)
        rel = page.relative_to(ROOT)
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
        if not parser.has_theme_toggle:
            errors.append(f"{rel}: accessible theme toggle missing")
        if parser.images_without_alt:
            errors.append(f"{rel}: images without alt: {parser.images_without_alt}")
        if "cases" in rel.parts and not ({"case-showcase", "case-proof-card"} & parser.classes):
            errors.append(f"{rel}: case lacks primary visual evidence")
        if "cases" in rel.parts and not {"case-gallery-section", "case-evidence-index", "evidence-label"}.issubset(parser.classes):
            errors.append(f"{rel}: case lacks traceable gallery/evidence labels")

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

    if len(html_pages) != 41:
        errors.append(f"unexpected HTML page count: {len(html_pages)} (expected 41)")
    pt_cases = len(list((ROOT / "cases").glob("*/index.html")))
    en_cases = len(list((ROOT / "en/cases").glob("*/index.html")))
    if pt_cases != 18 or en_cases != 18:
        errors.append(f"unexpected case count: PT={pt_cases}, EN={en_cases}")
    for case in (ROOT / "cases").glob("*/index.html"):
        if not (ROOT / "en" / case.relative_to(ROOT)).exists():
            errors.append(f"case lacks English counterpart: {case.relative_to(ROOT)}")

    pt_home = (ROOT / "index.html").read_text(encoding="utf-8")
    en_home = (ROOT / "en/index.html").read_text(encoding="utf-8")
    pt_skills = (ROOT / "competencias/index.html").read_text(encoding="utf-8")
    en_skills = (ROOT / "en/skills/index.html").read_text(encoding="utf-8")
    pt_catalog = (ROOT / "cases/procureflow/index.html").read_text(encoding="utf-8")
    en_catalog = (ROOT / "en/cases/procureflow/index.html").read_text(encoding="utf-8")
    pt_portal = (ROOT / "cases/portal-vesper/index.html").read_text(encoding="utf-8")
    en_portal = (ROOT / "en/cases/portal-vesper/index.html").read_text(encoding="utf-8")

    for home in (ROOT / "index.html", ROOT / "en/index.html"):
        parser = PageParser()
        parser.feed(home.read_text(encoding="utf-8"))
        if parser.metric_links != 6:
            errors.append(f"{home.relative_to(ROOT)}: expected 6 linked metrics, found {parser.metric_links}")

    require_text(pt_home, [
        "Analista de Automação, IA e Integrações", "2 workflows públicos", "Catálogo Operacional de Compras",
        "Usado diariamente por 3 usuários operacionais e consultado pela gestão", "58 nós no workflow de ações",
        "Portal", "Procurement e sourcing validados em sandbox", "tenant/RLS", "Action Envelope",
        '<a href="competencias/">Competências</a>', "DIO · 4h / 4 cursos",
    ], "index.html", errors)
    require_text(en_home, [
        "AI Automation &amp; Integrations Analyst", "2 public workflows", "Operational Procurement Catalog",
        "Used daily by 3 operational users and consulted by management", "58 nodes in Actions",
        "Procurement and sourcing validated in sandbox", "tenant/RLS", "Action Envelope",
        '<a href="skills/">Skills</a>', "DIO · 4h / 4 courses",
    ], "en/index.html", errors)

    require_text(pt_skills, [
        "automação low-code/no-code", "OpenAI, Gemini, Ollama, OpenRouter e Codex", "SQLite e FTS5",
        "Action Envelope", "Catálogo Operacional de Compras", "Procurement do Portal validado em sandbox",
    ], "competencias/index.html", errors)
    require_text(en_skills, [
        "low-code/no-code automation", "OpenAI, Gemini, Ollama, OpenRouter and Codex", "SQLite and FTS5",
        "Action Envelopes", "Operational Procurement Catalog", "Portal Procurement validated in sandbox",
    ], "en/skills/index.html", errors)

    require_text(pt_catalog, [
        "Catálogo Operacional de Compras", "USO INTERNO DIÁRIO", "três usuários operacionais", "SQLite FTS5",
        "controle de revisão", "aproximadamente dois anos", "Conflito por revisão",
    ], "cases/procureflow/index.html", errors)
    require_text(en_catalog, [
        "Operational Procurement Catalog", "DAILY INTERNAL USE", "three operational users", "SQLite FTS5",
        "revision", "approximately two years", "Revision conflict",
    ], "en/cases/procureflow/index.html", errors)

    require_text(pt_portal, [
        "Business Operating Platform multiempresa", "EM DESENVOLVIMENTO · PRÉ-PILOTO", "produto autoral",
        "tenant/RLS", "Action Envelope", "Procurement Intake e sourcing", "em preparação para piloto interno",
        "ainda não está comprovado", "referência pública anterior",
    ], "cases/portal-vesper/index.html", errors)
    require_text(en_portal, [
        "Multi-tenant Business Operating Platform", "IN DEVELOPMENT · PRE-PILOT", "Author-built product",
        "tenant/RLS", "Action Envelopes", "Procurement Intake and sourcing", "prepared for an internal pilot",
        "not yet demonstrated", "previous public reference",
    ], "en/cases/portal-vesper/index.html", errors)

    strategic = pt_home + en_home + pt_skills + en_skills + pt_catalog + en_catalog + pt_portal + en_portal
    forbid_text(strategic, [
        "5 workflows publicados", "5 published workflows", "5 workflows/158", "3 workflows/58",
        "Portal Vesper", ">ProcureFlow<", "REFERENCE ARCHITECTURE</span><h1>Portal",
        "RAG/grounding", "FastAPI/Flask", "REGISTRO DE SISTEMAS EM OPERAÇÃO · 2026",
    ], "strategic pages", errors)

    actual_cvs = {path.name for path in (ROOT / "assets/cv").glob("*.pdf")}
    if actual_cvs != CURRENT_CVS:
        errors.append(f"assets/cv inventory differs from current resumes: {sorted(actual_cvs)}")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if sitemap.count("<url>") != 40:
        errors.append(f"sitemap URL count is {sitemap.count('<url>')}, expected 40")
    for route in ("https://mayconxzdev.github.io/competencias/", "https://mayconxzdev.github.io/en/skills/"):
        if route not in sitemap:
            errors.append(f"sitemap missing strategic route: {route}")

    print(f"HTML: {len(html_pages)} | local refs: {refs_checked} | resume links: {pdf_links_checked} | cases PT/EN: {pt_cases}/{en_cases}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Portfolio content, evidence, links and hygiene validation completed without errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
