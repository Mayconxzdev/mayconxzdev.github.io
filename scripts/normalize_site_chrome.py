from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PT_RESUME = "/assets/cv/Maycon_Ferreira_Analista_Automacao_IA_Integracoes.pdf"
EN_RESUME = "/assets/cv/Maycon_Ferreira_AI_Automation_Integrations_Analyst.pdf"
THEME_INIT = """<script>(function(){try{var t=localStorage.getItem('mf-theme');document.documentElement.dataset.theme=t==='dark'?'dark':'light';}catch(e){document.documentElement.dataset.theme='light';}}())</script>"""

ALIASES = {
    "cases/compass-automation/index.html",
    "cases/portal-vesper/index.html",
    "cases/procureflow/index.html",
    "en/cases/compass-automation/index.html",
    "en/cases/portal-vesper/index.html",
    "en/cases/procureflow/index.html",
}

CASE_EN_SLUG = {
    "carreira-pessoal": "career-personal",
    "catalogo-operacional-compras": "operational-procurement-catalog",
}
CASE_PT_SLUG = {v: k for k, v in CASE_EN_SLUG.items()}


def route_for(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[:-10]
    return "/" + rel


def lang_target(route: str, english: bool) -> str:
    if english:
        if route == "/en/":
            return "/"
        if route == "/en/skills/":
            return "/competencias/"
        if route == "/en/credentials/":
            return "/competencias/credenciais/"
        match = re.fullmatch(r"/en/cases/([^/]+)/", route)
        if match:
            slug = CASE_PT_SLUG.get(match.group(1), match.group(1))
            return f"/cases/{slug}/"
        return route.removeprefix("/en") or "/"

    if route == "/":
        return "/en/"
    if route == "/404.html":
        return "/en/"
    if route == "/competencias/":
        return "/en/skills/"
    if route == "/competencias/credenciais/":
        return "/en/credentials/"
    match = re.fullmatch(r"/cases/([^/]+)/", route)
    if match:
        slug = CASE_EN_SLUG.get(match.group(1), match.group(1))
        return f"/en/cases/{slug}/"
    return "/en" + route


def global_header(english: bool, lang_href: str) -> str:
    if english:
        labels = [
            ("/en/#overview", "Overview"),
            ("/en/#systems", "Projects"),
            ("/en/#experience", "Experience"),
            ("/en/#evidence", "Results"),
            ("/en/skills/", "Skills"),
            ("/en/#contact", "Contact"),
        ]
        resume = EN_RESUME
        resume_label = "Resume"
        lang_label = "PT"
        nav_label = "Primary navigation"
        theme_label = "Switch to dark theme"
        sr_theme = "Toggle theme"
        brand_home = "/en/"
        brand_subtitle = "Automation · AI · Integrations"
    else:
        labels = [
            ("/#overview", "Visão geral"),
            ("/#systems", "Projetos"),
            ("/#experience", "Experiência"),
            ("/#evidence", "Resultados"),
            ("/competencias/", "Competências"),
            ("/#contact", "Contato"),
        ]
        resume = PT_RESUME
        resume_label = "Currículo"
        lang_label = "EN"
        nav_label = "Navegação principal"
        theme_label = "Ativar tema escuro"
        sr_theme = "Alternar tema"
        brand_home = "/"
        brand_subtitle = "Automação · IA · Integrações"

    links = "".join(f'<a href="{href}">{label}</a>' for href, label in labels)
    return (
        '<header class="site-header" data-global-chrome="2026-08">'
        f'<a class="brand" href="{brand_home}" aria-label="Maycon Ferreira">'
        '<span class="brand-mark">MF</span>'
        '<span class="brand-copy"><strong>Maycon Ferreira</strong>'
        f'<small>{brand_subtitle}</small></span></a>'
        '<button class="menu-button" type="button" aria-expanded="false" aria-controls="main-nav">'
        '<span></span><span></span><span></span><span class="sr-only">Menu</span></button>'
        f'<nav id="main-nav" aria-label="{nav_label}">{links}'
        f'<a class="nav-cv" href="{resume}">{resume_label}</a>'
        f'<a class="lang-link" href="{lang_href}">{lang_label}</a></nav>'
        f'<button class="theme-toggle" type="button" aria-pressed="false" aria-label="{theme_label}" title="{sr_theme}">'
        f'<span class="theme-toggle__icon" aria-hidden="true">◐</span><span class="sr-only">{sr_theme}</span></button>'
        '</header>'
    )


def global_footer(english: bool) -> str:
    if english:
        subtitle = "Automation, applied AI, integrations and internal systems."
        email = "Email"
        resume_label = "Resume"
        resume = EN_RESUME
    else:
        subtitle = "Automação, IA aplicada, integrações e sistemas internos."
        email = "E-mail"
        resume_label = "Currículo"
        resume = PT_RESUME
    return (
        '<footer class="site-footer" data-global-footer="2026-08">'
        f'<div><strong>Maycon Ferreira</strong><p>{subtitle}</p></div>'
        '<div class="footer-links">'
        f'<a href="mailto:mayconxz00dev@gmail.com">{email}</a>'
        '<a href="https://www.linkedin.com/in/maycon-ferreira-7bb870231/">LinkedIn</a>'
        '<a href="https://github.com/Mayconxzdev">GitHub</a>'
        f'<a href="{resume}">{resume_label}</a>'
        '</div></footer>'
    )


def ensure_head(text: str, route: str, english: bool) -> str:
    additions = []
    if 'name="theme-color"' not in text:
        additions.append('<meta name="theme-color" content="#ffffff">')
    if 'rel="icon"' not in text:
        additions.append('<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">')
    if 'layout-safety.css' not in text:
        additions.append('<link rel="stylesheet" href="/css/layout-safety.css">')
    if '/js/site.js' not in text and 'js/site.js' not in text:
        additions.append('<script defer src="/js/site.js"></script>')
    if "localStorage.getItem('mf-theme')" not in text and 'localStorage.getItem("mf-theme")' not in text:
        additions.append(THEME_INIT)

    if 'rel="canonical"' not in text:
        additions.append(f'<link rel="canonical" href="https://mayconxzdev.github.io{route}">')
    if 'hreflang="pt-BR"' not in text and 'hreflang="en"' not in text:
        pt = lang_target(route, True) if english else route
        en = route if english else lang_target(route, False)
        additions.extend([
            f'<link rel="alternate" hreflang="pt-BR" href="https://mayconxzdev.github.io{pt}">',
            f'<link rel="alternate" hreflang="en" href="https://mayconxzdev.github.io{en}">',
            f'<link rel="alternate" hreflang="x-default" href="https://mayconxzdev.github.io{pt}">',
        ])
    if additions:
        text = text.replace('</head>', ''.join(additions) + '</head>', 1)
    return text


def ensure_main_and_skip(text: str, route: str) -> str:
    if '<a class="skip-link"' not in text:
        label = "Skip to content" if route.startswith("/en/") else "Pular para o conteúdo"
        text = re.sub(r'(<body\b[^>]*>)', rf'\1<a class="skip-link" href="#main">{label}</a>', text, count=1, flags=re.I)
    if not re.search(r'<main\b[^>]*\bid=["\']main["\']', text, flags=re.I):
        text = re.sub(r'<main\b', '<main id="main"', text, count=1, flags=re.I)
    return text


def ensure_case_body_class(text: str, route: str) -> str:
    match = re.fullmatch(r"/(?:en/)?cases/([^/]+)/", route)
    if not match:
        return text
    slug = match.group(1)
    body = re.search(r'<body\b([^>]*)>', text, flags=re.I)
    if not body:
        return text
    attrs = body.group(1)
    class_match = re.search(r'class=(["\'])(.*?)\1', attrs, flags=re.I | re.S)
    needed = ["case-body", f"case-body--{slug}"]
    if class_match:
        classes = class_match.group(2).split()
        changed = False
        for item in needed:
            if item not in classes:
                classes.append(item)
                changed = True
        if changed:
            new_attrs = attrs[:class_match.start()] + f'class="{" ".join(classes)}"' + attrs[class_match.end():]
            text = text[:body.start()] + "<body" + new_attrs + ">" + text[body.end():]
    else:
        text = text[:body.start()] + f'<body class="{" ".join(needed)}"' + attrs + ">" + text[body.end():]
    return text


def normalize_page(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    if rel in ALIASES:
        return
    text = path.read_text(encoding="utf-8")
    route = route_for(path)
    english = route.startswith("/en/")
    text = ensure_head(text, route, english)
    text = ensure_main_and_skip(text, route)
    text = ensure_case_body_class(text, route)

    header = global_header(english, lang_target(route, english))
    header_pattern = r'<header\b[^>]*class=["\'][^"\']*\bsite-header\b[^"\']*["\'][^>]*>.*?</header>'
    if re.search(header_pattern, text, flags=re.I | re.S):
        text = re.sub(header_pattern, header, text, count=1, flags=re.I | re.S)
    else:
        body_end = re.search(r'<body\b[^>]*>', text, flags=re.I)
        if body_end:
            insert_at = body_end.end()
            skip = re.match(r'<a class="skip-link".*?</a>', text[insert_at:], flags=re.S)
            if skip:
                insert_at += skip.end()
            text = text[:insert_at] + header + text[insert_at:]

    footer = global_footer(english)
    footer_pattern = r'<footer\b[^>]*class=["\'][^"\']*\bsite-footer\b[^"\']*["\'][^>]*>.*?</footer>'
    if re.search(footer_pattern, text, flags=re.I | re.S):
        text = re.sub(footer_pattern, footer, text, count=1, flags=re.I | re.S)
    elif '</body>' in text:
        text = text.replace('</body>', footer + '</body>', 1)

    path.write_text(text, encoding="utf-8")


for path in ROOT.rglob("*.html"):
    if any(part in {".git", ".github", "node_modules", "artifacts", ".site"} for part in path.parts):
        continue
    normalize_page(path)

print("Global navigation, theme support, language routing and footer normalized across canonical pages.")