from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FRAG = ROOT / "scripts" / "fragments"

def load(name: str) -> str:
    return (FRAG / name).read_text(encoding="utf-8").strip()

def replace_featured(text: str, fragment: str) -> str:
    pattern = re.compile(r'<section class="featured" id="systems">.*?</section>\s*(?=<section class="experience")', re.S)
    updated, count = pattern.subn(fragment + "\n\n    ", text, count=1)
    if count != 1:
        raise RuntimeError("featured section boundary not found")
    return updated

def replace_archive(text: str, fragment: str) -> str:
    start = text.find('<div class="archive-list" id="project-grid">')
    if start < 0:
        raise RuntimeError("archive-list start not found")
    anchors = [i for i in (
        text.find('<button class="archive-expand"', start),
        text.find('<p class="empty-state"', start),
    ) if i >= 0]
    if not anchors:
        raise RuntimeError("archive-list end anchor not found")
    end = min(anchors)
    return text[:start] + fragment + "\n      " + text[end:]

def patch_home(path: Path, featured_name: str, archive_name: str, english: bool) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_featured(text, load(featured_name))
    text = replace_archive(text, load(archive_name))
    if english:
        text = text.replace(
            "I turn operational processes into automations and AI solutions that work in the daily routine.",
            "I turn operational processes into internal systems, automations and AI solutions that work in the daily routine.",
        )
        text = text.replace(
            "Portfolio of Maycon Ferreira, Automation & AI Analyst. Internal systems, production automation, integrations and applied AI with Python, Power Automate and n8n.",
            "Portfolio of Maycon Ferreira, Automation & AI Analyst. Internal systems, production automation, integrations and applied AI with Python, Power Automate and n8n.",
        )
    else:
        text = text.replace(
            "Transformo processos manuais e rotinas operacionais em automações e soluções com IA que funcionam no dia a dia.",
            "Transformo processos e rotinas operacionais em sistemas, automações e soluções com IA que funcionam no dia a dia.",
        )
        text = text.replace(
            "Portfólio de Maycon Ferreira, Analista de Automação e IA. Sistemas internos, automação em produção, integrações e IA aplicada com Python, Power Automate e n8n.",
            "Portfólio de Maycon Ferreira, Analista de Automação e IA. Sistemas internos, automação em produção, integrações e IA aplicada com Python, Power Automate e n8n.",
        )
    path.write_text(text, encoding="utf-8")

def ensure_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    pt = '  <url><loc>https://mayconxzdev.github.io/cases/belarc-inventory/</loc><lastmod>2026-09-22</lastmod></url>'
    en = '  <url><loc>https://mayconxzdev.github.io/en/cases/belarc-inventory/</loc><lastmod>2026-09-22</lastmod></url>'
    if pt not in text:
        anchor = '  <url><loc>https://mayconxzdev.github.io/cases/vesper-propostas/</loc>'
        pos = text.find(anchor)
        if pos < 0:
            raise RuntimeError("PT sitemap insertion anchor not found")
        line_end = text.find("\n", pos)
        text = text[:line_end+1] + pt + "\n" + text[line_end+1:]
    if en not in text:
        anchor = '  <url><loc>https://mayconxzdev.github.io/en/cases/vesper-propostas/</loc>'
        pos = text.find(anchor)
        if pos < 0:
            raise RuntimeError("EN sitemap insertion anchor not found")
        line_end = text.find("\n", pos)
        text = text[:line_end+1] + en + "\n" + text[line_end+1:]
    path.write_text(text, encoding="utf-8")

patch_home(ROOT / "index.html", "featured_pt.fragment", "archive_pt.fragment", False)
patch_home(ROOT / "en" / "index.html", "featured_en.fragment", "archive_en.fragment", True)
ensure_sitemap()
print("Featured project content applied: 4 flagships, 12 secondary cases, Belarc routing and metadata.")
