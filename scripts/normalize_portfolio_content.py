from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_CATALOG_ROUTE = "cases/catalogo-operacional-compras/"
EN_CATALOG_ROUTE = "cases/operational-procurement-catalog/"
PT_PORTAL_ROUTE = "cases/portal/"
EN_PORTAL_ROUTE = "cases/portal/"

PT_CATALOG_CARD = f'''<article class="feature-case feature-case--procureflow feature-case--reverse">
  <div class="feature-case__copy">
    <div class="case-index"><span>04</span><span class="status status--internal">USO INTERNO DIÁRIO</span></div>
    <p class="case-category">Backend, busca e integridade de dados</p>
    <h3>Catálogo Operacional de Compras</h3>
    <p class="case-summary">Sistema interno para localizar materiais, fornecedores, preços e histórico por código, nome ou fornecedor, sem depender da navegação manual em planilhas.</p>
    <div class="case-impact"><small>Resultado observado</small><strong>Base histórica com 24 categorias e 480+ códigos, usada diariamente por 3 usuários e consultada pela gestão.</strong></div>
    <p class="case-stack">FastAPI · Python · SQLite FTS5 · JavaScript · OCR · controle por revisão</p>
    <div class="project-links"><a class="text-link" href="{PT_CATALOG_ROUTE}">Abrir case completo<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/CatalogoOperacional">Ver repositório<span aria-hidden="true">↗</span></a></div>
  </div>
  <div class="feature-case__visual"><div class="visual visual--portal"><div class="portal-core"><span>FONTE VERSIONADA</span><b>Catálogo de Compras</b><small>FastAPI · JSON · SQLite FTS5</small></div><div class="module-grid"><span>24 categorias</span><span>480+ códigos</span><span>Fornecedor</span><span>Histórico</span><span>Revision</span><span>Backup</span><span>OCR</span></div><div class="executor-line"><span>Edição concorrente</span><i>→</i><b>Conflito explícito</b><small>sem sobrescrita silenciosa</small></div></div></div>
</article>'''

EN_CATALOG_CARD = f'''<article class="feature-case feature-case--procureflow feature-case--reverse">
  <div class="feature-case__copy">
    <div class="case-index"><span>04</span><span class="status status--internal">DAILY INTERNAL USE</span></div>
    <p class="case-category">Backend, search and data integrity</p>
    <h3>Operational Procurement Catalog</h3>
    <p class="case-summary">Internal system to find materials, suppliers, prices and history by code, name or supplier without manually navigating spreadsheets.</p>
    <div class="case-impact"><small>Observed result</small><strong>Historical base with 24 categories and 480+ material codes, used daily by 3 users and consulted by management.</strong></div>
    <p class="case-stack">FastAPI · Python · SQLite FTS5 · JavaScript · OCR · revision control</p>
    <div class="project-links"><a class="text-link" href="{EN_CATALOG_ROUTE}">Open full case<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/CatalogoOperacional">View repository<span aria-hidden="true">↗</span></a></div>
  </div>
  <div class="feature-case__visual"><div class="visual visual--portal"><div class="portal-core"><span>VERSIONED SOURCE</span><b>Procurement Catalog</b><small>FastAPI · JSON · SQLite FTS5</small></div><div class="module-grid"><span>24 categories</span><span>480+ codes</span><span>Supplier</span><span>History</span><span>Revision</span><span>Backup</span><span>OCR</span></div><div class="executor-line"><span>Concurrent edit</span><i>→</i><b>Explicit conflict</b><small>no silent overwrite</small></div></div></div>
</article>'''

PT_PORTAL_CARD = f'''<article class="feature-case feature-case--portal-vesper feature-case--reverse">
  <div class="feature-case__copy">
    <div class="case-index"><span>06</span><span class="status status--pilot">EM DESENVOLVIMENTO</span></div>
    <p class="case-category">Produto autoral multiempresa</p>
    <h3>Portal</h3>
    <p class="case-summary">Business Operating Platform para conectar pessoas, processos, dados, aprovações, integrações, automações e agentes governados em torno dos mesmos objetos empresariais.</p>
    <div class="case-impact"><small>Estado atual</small><strong>Procurement implementado em sandbox; revalidação técnica do head atual antes do piloto interno.</strong></div>
    <p class="case-stack">React · TypeScript · FastAPI · PostgreSQL · tenant/RLS · Action Envelope · outbox</p>
    <div class="project-links"><a class="text-link" href="{PT_PORTAL_ROUTE}">Abrir estado e arquitetura<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/Portal">Referência pública anterior<span aria-hidden="true">↗</span></a></div>
  </div>
  <div class="feature-case__visual"><div class="visual visual--portal"><div class="portal-core"><span>BUSINESS OPERATING PLATFORM</span><b>Portal</b><small>FastAPI · PostgreSQL · tenancy · RLS</small></div><div class="module-grid"><span>Organizations</span><span>Action Envelope</span><span>Approvals</span><span>Procurement</span><span>RFQ</span><span>Offers</span><span>Timeline</span><span>Audit</span><span>Outbox</span></div><div class="executor-line"><span>estado atual</span><i>→</i><b>Sandbox / revalidação</b><small>não apresentado como produção</small></div></div></div>
</article>'''

EN_PORTAL_CARD = f'''<article class="feature-case feature-case--portal-vesper feature-case--reverse">
  <div class="feature-case__copy">
    <div class="case-index"><span>06</span><span class="status status--pilot">IN DEVELOPMENT</span></div>
    <p class="case-category">Author-built multi-tenant product</p>
    <h3>Portal</h3>
    <p class="case-summary">Business Operating Platform connecting people, processes, data, approvals, integrations, automations and governed agents around shared business objects.</p>
    <div class="case-impact"><small>Current state</small><strong>Procurement implemented in sandbox; technical revalidation of the current head before an internal pilot.</strong></div>
    <p class="case-stack">React · TypeScript · FastAPI · PostgreSQL · tenant/RLS · Action Envelope · outbox</p>
    <div class="project-links"><a class="text-link" href="{EN_PORTAL_ROUTE}">Open status and architecture<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/Portal">Previous public reference<span aria-hidden="true">↗</span></a></div>
  </div>
  <div class="feature-case__visual"><div class="visual visual--portal"><div class="portal-core"><span>BUSINESS OPERATING PLATFORM</span><b>Portal</b><small>FastAPI · PostgreSQL · tenancy · RLS</small></div><div class="module-grid"><span>Organizations</span><span>Action Envelope</span><span>Approvals</span><span>Procurement</span><span>RFQ</span><span>Offers</span><span>Timeline</span><span>Audit</span><span>Outbox</span></div><div class="executor-line"><span>current state</span><i>→</i><b>Sandbox / revalidation</b><small>not presented as production</small></div></div></div>
</article>'''

PT_CATALOG_ARCHIVE = f'''<article class="archive-row persp-process persp-automation persp-integration persp-architecture" data-search="catálogo operacional de compras uso interno diário fastapi sqlite fts5 24 categorias 480 códigos busca código nome fornecedor histórico revisão concorrência backups ocr">
  <span class="archive-number">08</span>
  <div class="archive-name"><h3>Catálogo Operacional de Compras</h3><p>Base histórica com 24 categorias e 480+ códigos, pesquisável sem sobrescrita silenciosa entre computadores.</p></div>
  <div class="archive-state"><span class="status status--internal">USO INTERNO DIÁRIO</span><small>3 usuários operacionais · consulta pela gestão</small></div>
  <div class="archive-stack">FastAPI · Python · SQLite FTS5 · JavaScript · OCR</div>
  <a class="archive-open" href="{PT_CATALOG_ROUTE}" aria-label="Abrir: Catálogo Operacional de Compras">↗</a>
</article>'''

EN_CATALOG_ARCHIVE = f'''<article class="archive-row persp-process persp-automation persp-integration persp-architecture" data-search="operational procurement catalog daily internal use fastapi sqlite fts5 24 categories 480 codes search supplier history revision concurrency backups ocr">
  <span class="archive-number">08</span>
  <div class="archive-name"><h3>Operational Procurement Catalog</h3><p>Historical base with 24 categories and 480+ codes, searchable without silent overwrites between computers.</p></div>
  <div class="archive-state"><span class="status status--internal">DAILY INTERNAL USE</span><small>3 operational users · management consultation</small></div>
  <div class="archive-stack">FastAPI · Python · SQLite FTS5 · JavaScript · OCR</div>
  <a class="archive-open" href="{EN_CATALOG_ROUTE}" aria-label="Open: Operational Procurement Catalog">↗</a>
</article>'''

PT_PORTAL_ARCHIVE = f'''<article class="archive-row persp-architecture persp-automation persp-integration persp-agents persp-process" data-search="portal desenvolvimento business operating platform multiempresa react typescript fastapi postgresql tenancy rls action envelope aprovações outbox procurement sandbox revalidação">
  <span class="archive-number">06</span>
  <div class="archive-name"><h3>Portal</h3><p>Produto autoral multiempresa que conecta processos, dados, aprovações, integrações, automações e agentes governados.</p></div>
  <div class="archive-state"><span class="status status--pilot">EM DESENVOLVIMENTO</span><small>Procurement em sandbox · revalidação pré-piloto</small></div>
  <div class="archive-stack">React · TypeScript · FastAPI · PostgreSQL · RLS · outbox</div>
  <a class="archive-open" href="{PT_PORTAL_ROUTE}" aria-label="Abrir: Portal">↗</a>
</article>'''

EN_PORTAL_ARCHIVE = f'''<article class="archive-row persp-architecture persp-automation persp-integration persp-agents persp-process" data-search="portal in development multi-tenant business operating platform react typescript fastapi postgresql tenancy rls action envelope approvals outbox procurement sandbox revalidation">
  <span class="archive-number">06</span>
  <div class="archive-name"><h3>Portal</h3><p>Author-built multi-tenant product connecting processes, data, approvals, integrations, automations and governed agents.</p></div>
  <div class="archive-state"><span class="status status--pilot">IN DEVELOPMENT</span><small>Procurement in sandbox · pre-pilot revalidation</small></div>
  <div class="archive-stack">React · TypeScript · FastAPI · PostgreSQL · RLS · outbox</div>
  <a class="archive-open" href="{EN_PORTAL_ROUTE}" aria-label="Open: Portal">↗</a>
</article>'''


def replace_feature(text: str, class_name: str, replacement: str) -> str:
    pattern = rf'<article class="feature-case {re.escape(class_name)}[^\"]*">.*?</article>'
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Expected exactly one feature block for {class_name}, found {count}")
    return updated


def replace_archive_by_number(text: str, number: str, replacement: str) -> str:
    pattern = rf'<article class="archive-row[^\"]*"[^>]*>\s*<span class="archive-number">{re.escape(number)}</span>.*?</article>'
    updated, count = re.subn(pattern, replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"Expected exactly one archive row {number}, found {count}")
    return updated


def normalize_home(path: Path, *, english: bool) -> None:
    text = path.read_text(encoding="utf-8")
    original = text

    if english:
        text = replace_feature(text, "feature-case--procureflow", EN_CATALOG_CARD)
        text = replace_feature(text, "feature-case--portal-vesper", EN_PORTAL_CARD)
        text = replace_archive_by_number(text, "06", EN_PORTAL_ARCHIVE)
        text = replace_archive_by_number(text, "08", EN_CATALOG_ARCHIVE)
        text = text.replace("ProcureFlow", "Operational Procurement Catalog")
        text = text.replace("Portal Vesper", "Portal")
    else:
        text = replace_feature(text, "feature-case--procureflow", PT_CATALOG_CARD)
        text = replace_feature(text, "feature-case--portal-vesper", PT_PORTAL_CARD)
        text = replace_archive_by_number(text, "06", PT_PORTAL_ARCHIVE)
        text = replace_archive_by_number(text, "08", PT_CATALOG_ARCHIVE)
        text = text.replace("ProcureFlow", "Catálogo Operacional de Compras")
        text = text.replace("Portal Vesper", "Portal")

    if text == original:
        print(f"unchanged: {path.relative_to(ROOT)}")
    else:
        path.write_text(text, encoding="utf-8")
        print(f"normalized: {path.relative_to(ROOT)}")


def main() -> None:
    normalize_home(ROOT / "index.html", english=False)
    normalize_home(ROOT / "en" / "index.html", english=True)


if __name__ == "__main__":
    main()
