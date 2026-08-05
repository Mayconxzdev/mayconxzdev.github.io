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
        if (
            tag == "button"
            and "theme-toggle" in (data.get("class") or "").split()
            and data.get("aria-label")
            and data.get("aria-pressed") is not None
        ):
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
        raise ValueError(f"referência sai da raiz: {value}") from exc
    if parsed.path.endswith("/"):
        target = target / "index.html"
    return target


def require_text(content: str, required: list[str], label: str, errors: list[str]) -> None:
    for phrase in required:
        if phrase not in content:
            errors.append(f"{label}: texto verificado ausente: {phrase}")


def forbid_text(content: str, forbidden: list[str], label: str, errors: list[str]) -> None:
    for phrase in forbidden:
        if phrase in content:
            errors.append(f"{label}: conteúdo antigo ou não sustentado encontrado: {phrase}")


def validate_cv_inventory(errors: list[str]) -> None:
    cv_dir = ROOT / "assets" / "cv"
    actual = {path.name for path in cv_dir.glob("*.pdf")}
    missing = CURRENT_CVS - actual
    legacy = actual - CURRENT_CVS
    if missing:
        errors.append(f"currículos atuais ausentes: {sorted(missing)}")
    if legacy:
        errors.append(f"PDFs antigos ainda presentes em assets/cv: {sorted(legacy)}")


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
            errors.append(f"{rel}: IDs duplicados: {duplicates}")
        if not parser.has_title:
            errors.append(f"{rel}: título ausente")
        if not parser.html_lang:
            errors.append(f"{rel}: atributo lang ausente")
        if not parser.has_description:
            errors.append(f"{rel}: meta description ausente")
        if not parser.has_canonical:
            errors.append(f"{rel}: canonical ausente")
        if rel.name != "404.html" and not parser.has_hreflang:
            errors.append(f"{rel}: hreflang ausente")
        if not parser.has_theme_toggle:
            errors.append(f"{rel}: controle de tema acessível ausente")
        if parser.images_without_alt:
            errors.append(f"{rel}: imagens sem alt: {parser.images_without_alt}")
        if "cases" in rel.parts and not ({"case-showcase", "case-proof-card"} & parser.classes):
            errors.append(f"{rel}: case sem prova visual principal")
        if "cases" in rel.parts and not {"case-gallery-section", "case-evidence-index", "evidence-label"}.issubset(parser.classes):
            errors.append(f"{rel}: case sem galeria visual rastreável")

        for pdf_ref in parser.pdf_refs:
            pdf_links_checked += 1
            filename = Path(urlparse(pdf_ref).path).name
            if filename not in CURRENT_CVS:
                errors.append(f"{rel}: link aponta para currículo antigo ou inesperado: {pdf_ref}")

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
                errors.append(f"{rel}: referência inexistente: {value}")

    if len(html_pages) != 41:
        errors.append(f"quantidade de páginas HTML inesperada: {len(html_pages)} (esperado: 41)")

    pt_cases = len(list((ROOT / "cases").glob("*/index.html")))
    en_cases = len(list((ROOT / "en/cases").glob("*/index.html")))
    if pt_cases != 18 or en_cases != 18:
        errors.append(f"quantidade de cases inesperada: PT={pt_cases}, EN={en_cases}")
    for case in (ROOT / "cases").glob("*/index.html"):
        translated = ROOT / "en" / case.relative_to(ROOT)
        if not translated.exists():
            errors.append(f"case sem equivalente em inglês: {case.relative_to(ROOT)}")

    for home in (ROOT / "index.html", ROOT / "en" / "index.html"):
        parser = PageParser()
        parser.feed(home.read_text(encoding="utf-8"))
        if parser.metric_links != 6:
            errors.append(f"{home.relative_to(ROOT)}: esperado 6 indicadores com links para cases, encontrado {parser.metric_links}")

    pt_home = (ROOT / "index.html").read_text(encoding="utf-8")
    en_home = (ROOT / "en" / "index.html").read_text(encoding="utf-8")
    pt_skills = (ROOT / "competencias" / "index.html").read_text(encoding="utf-8")
    en_skills = (ROOT / "en" / "skills" / "index.html").read_text(encoding="utf-8")

    require_text(
        pt_home,
        [
            "Analista de Automação, IA e Integrações. Cases reais de n8n, Python, APIs REST, IA generativa, agentes, sistemas internos e resultados mensuráveis.",
            "ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES · 2026",
            "<dt>Posicionamento</dt><dd>Analista de Automação, IA e Integrações</dd>",
            '<a href="competencias/">Competências</a>',
            '"Automação low-code"',
            '"Codex"',
            "Automação de Processos através da RPA",
            "Fundamentos da Transformação Digital: Mapeamento e Automação de Processos",
            "DIO · 4h / 4 cursos",
        ],
        "index.html",
        errors,
    )
    require_text(
        en_home,
        [
            "AI Automation and Integrations Analyst. Real cases involving n8n, Python, REST APIs, generative AI, agents, internal systems and measurable outcomes.",
            "AI AUTOMATION &amp; INTEGRATIONS ANALYST · 2026",
            "<dt>Positioning</dt><dd>AI Automation &amp; Integrations Analyst</dd>",
            '<a href="skills/">Skills</a>',
            '"Low-code automation"',
            '"Codex"',
            "AI Tools: Agents and Automations",
            "Process Automation through RPA",
            "Digital Transformation Fundamentals: Process Mapping and Automation",
            "AI in the Public Service Context",
            "Introduction to Brazil's Data Protection Law",
            "n8n and Workflows Learning Path",
            "DIO · 4h / 4 courses",
        ],
        "en/index.html",
        errors,
    )
    require_text(
        pt_skills,
        [
            "automação low-code/no-code",
            "OpenAI, Gemini, Ollama, OpenRouter e Codex",
            "geração de texto, imagem e vídeo (text-to-video)",
            "Node.js/Express",
            "mais de 10 mil execuções de workflows em produção",
            "Protótipos funcionais privados",
        ],
        "competencias/index.html",
        errors,
    )
    require_text(
        en_skills,
        [
            "low-code/no-code automation",
            "OpenAI, Gemini, Ollama, OpenRouter and Codex",
            "text, image and video generation (text-to-video)",
            "Node.js/Express",
            "more than 10,000 production workflow executions",
            "Private functional prototypes",
        ],
        "en/skills/index.html",
        errors,
    )

    forbid_text(
        pt_home + en_home + pt_skills + en_skills,
        [
            "DIO · 8h / 4 cursos",
            "RAG/grounding",
            "FastAPI/Flask",
            '"Applied AI"',
            "REGISTRO DE SISTEMAS EM OPERAÇÃO · 2026",
            "SYSTEMS IN OPERATION · 2026",
        ],
        "home/skills",
        errors,
    )
    if "10 mil+" in en_home or "out. 2024 — mar. 2025" in en_home:
        errors.append("en/index.html: conteúdo de localidade PT-BR no resumo em inglês")

    validate_cv_inventory(errors)

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if sitemap.count("<url>") != 40:
        errors.append(f"sitemap.xml: quantidade inesperada de URLs ({sitemap.count('<url>')}, esperado: 40)")
    for route in (
        "https://mayconxzdev.github.io/competencias/",
        "https://mayconxzdev.github.io/en/skills/",
    ):
        if route not in sitemap:
            errors.append(f"sitemap.xml: rota estratégica ausente: {route}")

    css = (ROOT / "css/styles.css").read_text(encoding="utf-8")
    if "[hidden]" not in css:
        errors.append("CSS não preserva o atributo hidden")

    print(
        f"HTML: {len(html_pages)} páginas | referências locais: {refs_checked} | "
        f"links de currículo: {pdf_links_checked} | cases: PT {pt_cases} / EN {en_cases}"
    )
    if errors:
        for error in errors:
            print(f"ERRO: {error}")
        return 1
    print("Validação de conteúdo, posicionamento, referências e higiene concluída sem erros.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
