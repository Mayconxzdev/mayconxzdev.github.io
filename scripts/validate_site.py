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
    "cases/compass-automation/index.html": "../compass/",
    "en/cases/compass-automation/index.html": "../compass/",
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
            target = LEGACY_REDIRECTS.get(rel_str)
            if target is None:
                errors.append(f"{rel}: unexpected redirect page")
            elif target not in content:
                errors.append(f"{rel}: redirect target is not canonical: {target}")

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
    if active_pt != 17 or active_en != 17:
        errors.append(f"unexpected active case count: PT={active_pt}, EN={active_en}, expected 17/17")
    if redirects_seen != set(LEGACY_REDIRECTS):
        errors.append(f"legacy redirect inventory differs: {sorted(redirects_seen)}")

    pt_home = read("index.html")
    en_home = read("en/index.html")
    pt_skills = read("competencias/index.html")
    en_skills = read("en/skills/index.html")
    pt_mala = read("cases/mala-direta/index.html")
    en_mala = read("en/cases/mala-direta/index.html")
    pt_production = read("cases/producao-operacional/index.html")
    en_production = read("en/cases/producao-operacional/index.html")
    pt_catalog = read("cases/catalogo-operacional-compras/index.html")
    en_catalog = read("en/cases/operational-procurement-catalog/index.html")
    pt_portal = read("cases/portal/index.html")
    en_portal = read("en/cases/portal/index.html")
    pt_compass = read("cases/compass/index.html")
    en_compass = read("en/cases/compass/index.html")

    if parse("index.html").metric_links != 6:
        errors.append("index.html: expected 6 linked metrics")
    if parse("en/index.html").metric_links != 6:
        errors.append("en/index.html: expected 6 linked metrics")

    require_text(pt_home, [
        "Analista de Automação, IA e Integrações", "10 mil+", "múltiplas automações em produção",
        "10+ PCs · 1 TV · 9 setores", "6 campanhas", "base de 1.020 contatos", "480+", "24 categorias",
        "treinei e orientei 30+ pessoas", "Programa de Bolsas em Engenharia de Dados",
        "Facebook e Instagram exercitados em teste", "https://github.com/Mayconxzdev/CatalogoOperacional",
        "revalidação técnica do head atual",
    ], "index.html", errors)
    require_text(en_home, [
        "AI Automation &amp; Integrations Analyst", "10k+", "multiple production automations",
        "10+ PCs · 1 TV · 9 areas", "6 campaigns", "1,020-contact base", "480+", "24 categories",
        "Trained and guided 30+ people", "Data Engineering Scholarship Program",
        "Facebook and Instagram exercised in testing", "https://github.com/Mayconxzdev/CatalogoOperacional",
        "technical revalidation of the current head",
    ], "en/index.html", errors)
    if 'href="../cases/' in en_home:
        errors.append("en/index.html: English home links must remain inside /en/cases/")

    require_text(pt_skills, [
        "automação low-code/no-code", "IA multimodal e geração de mídia em texto, imagem, áudio e vídeo",
        "AWS S3, EC2, Lambda, Glue/PySpark, Athena e QuickSight", "10 mil+ execuções na instância n8n de produção",
        "24 categorias e 480+ códigos", "revalidação técnica pré-piloto",
    ], "competencias/index.html", errors)
    require_text(en_skills, [
        "low-code/no-code automation", "multimodal AI and media generation across text, image, audio and video",
        "AWS S3, EC2, Lambda, Glue/PySpark, Athena and QuickSight", "10,000+ executions across the production n8n environment",
        "24 categories and 480+ codes", "pre-pilot technical revalidation",
    ], "en/skills/index.html", errors)

    require_text(pt_mala, ["Seis campanhas", "1.020 contatos", "158 nós no principal", "10 mil execuções em produção", "não é atribuído exclusivamente"], "cases/mala-direta/index.html", errors)
    require_text(en_mala, ["Six campaigns", "1,020-contact base", "158 nodes in the main flow", "10,000 production executions", "not attributed exclusively"], "en/cases/mala-direta/index.html", errors)
    require_text(pt_production, ["10+ computadores", "20+ profissionais", "nove setores produtivos", "treinamento e orientação", "NAS em modo somente leitura"], "cases/producao-operacional/index.html", errors)
    require_text(en_production, ["10+ computers", "20+ professionals", "nine production areas", "user training and guidance", "NAS in read-only mode"], "en/cases/producao-operacional/index.html", errors)
    require_text(pt_catalog, ["24 categorias", "mais de 480 códigos", "três usuários operacionais", "CatalogoOperacional", "Conflito por revisão"], "cases/catalogo-operacional-compras/index.html", errors)
    require_text(en_catalog, ["24 categories", "more than 480 material codes", "three operational users", "CatalogoOperacional", "Revision conflict"], "en/cases/operational-procurement-catalog/index.html", errors)
    require_text(pt_portal, ["EM DESENVOLVIMENTO · PRÉ-PILOTO", "head atual está em revalidação", "revalidação do head atual", "Piloto interno condicionado"], "cases/portal/index.html", errors)
    require_text(en_portal, ["IN DEVELOPMENT · PRE-PILOT", "current head is being revalidated", "current-head revalidation", "internal pilot depends"], "en/cases/portal/index.html", errors)
    require_text(pt_compass, ["dez sprints", "API TMDB", "Glue/PySpark", "Raw, Trusted e Refined", "QuickSight", "não apresentada como ambiente de produção"], "cases/compass/index.html", errors)
    require_text(en_compass, ["ten sprints", "TMDB API", "Glue/PySpark", "Raw, Trusted and Refined", "QuickSight", "not presented as a production environment"], "en/cases/compass/index.html", errors)

    strategic = "".join([
        pt_home, en_home, pt_skills, en_skills, pt_mala, en_mala, pt_production, en_production,
        pt_catalog, en_catalog, pt_portal, en_portal, pt_compass, en_compass,
    ])
    forbid_text(strategic, [
        "3h → 5min", "3 hours to five minutes", "três horas para cinco minutos",
        "text-to-video", "Text-to-video", "11 computadores", "11 office computers",
        "PlanilhaCompras", "Portal Vesper", "Procurement e sourcing validados em sandbox",
        "Procurement and sourcing validated in sandbox", "cases/compass-automation/",
    ], "strategic pages", errors)

    actual_cvs = {path.name for path in (ROOT / "assets/cv").glob("*.pdf")}
    if actual_cvs != CURRENT_CVS:
        errors.append(f"assets/cv inventory differs from current resumes: {sorted(actual_cvs)}")

    sitemap = read("sitemap.xml")
    if sitemap.count("<url>") != 38:
        errors.append(f"sitemap URL count is {sitemap.count('<url>')}, expected 38")
    for route in (
        "https://mayconxzdev.github.io/competencias/", "https://mayconxzdev.github.io/en/skills/",
        "https://mayconxzdev.github.io/cases/catalogo-operacional-compras/",
        "https://mayconxzdev.github.io/en/cases/operational-procurement-catalog/",
        "https://mayconxzdev.github.io/cases/portal/", "https://mayconxzdev.github.io/en/cases/portal/",
        "https://mayconxzdev.github.io/cases/compass/", "https://mayconxzdev.github.io/en/cases/compass/",
    ):
        if route not in sitemap:
            errors.append(f"sitemap missing canonical route: {route}")
    for stale in (
        "https://mayconxzdev.github.io/cases/procureflow/", "https://mayconxzdev.github.io/en/cases/procureflow/",
        "https://mayconxzdev.github.io/cases/portal-vesper/", "https://mayconxzdev.github.io/en/cases/portal-vesper/",
        "https://mayconxzdev.github.io/cases/compass-automation/", "https://mayconxzdev.github.io/en/cases/compass-automation/",
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
    print("Portfolio facts, canonical routes, redirects, links and hygiene validated without errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
