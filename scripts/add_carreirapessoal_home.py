from pathlib import Path
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]


def feature_re(name: str) -> re.Pattern[str]:
    return re.compile(
        rf'<article class="feature-case[^>]*>(?:(?!</article>).)*?<h3>\s*{re.escape(name)}\s*</h3>(?:(?!</article>).)*?</article>',
        re.S,
    )


def remove_feature(text: str, name: str) -> str:
    match = feature_re(name).search(text)
    if not match:
        return text
    return text[:match.start()] + text[match.end():]


def append_archive(text: str, entries: list[tuple[str, str]]) -> str:
    missing = [block for marker, block in entries if marker not in text]
    if not missing:
        return text
    empty = text.find('<p class="empty-state"')
    if empty < 0:
        raise RuntimeError('archive empty-state marker missing')
    close = text.rfind('</div>', 0, empty)
    if close < 0:
        raise RuntimeError('archive list closing tag missing')
    insertion = '\n        '.join(missing) + '\n      '
    return text[:close] + insertion + text[close:]


def renumber_archive(text: str) -> str:
    start = text.find('<section class="archive" id="archive">')
    end = text.find('<section class="journey">', start)
    if start < 0 or end < 0:
        raise RuntimeError('archive boundaries missing')
    block = text[start:end]
    counter = 5

    def repl(match: re.Match[str]) -> str:
        nonlocal counter
        value = f'{counter:02d}'
        counter += 1
        return f'{match.group(1)}{value}{match.group(3)}'

    block = re.sub(r'(<span class="archive-number">)([^<]+)(</span>)', repl, block)
    return text[:start] + block + text[end:]


PT_CAREER_ARCHIVE = '<article class="archive-row persp-architecture persp-agents persp-process" data-project="carreira-pessoal-archive" data-search="carreira pessoal fastapi react typescript tauri evidenceguard qa"><span class="archive-number">05</span><div class="archive-name"><h3>CarreiraPessoal</h3><p>Ferramenta pessoal para reunir oportunidades, entender requisitos e organizar candidaturas.</p></div><div class="archive-state"><span class="status status--public">USO PESSOAL</span><small>busca de vagas e currículos em um só lugar</small></div><div class="archive-stack">FastAPI · React/TypeScript · Tauri/Rust</div><a class="archive-open" href="cases/carreira-pessoal/" aria-label="Abrir CarreiraPessoal">↗</a></article>'
PT_PROD_ARCHIVE = '<article class="archive-row persp-process persp-automation persp-architecture" data-project="producao-operacional-archive" data-search="producao operacional python pyside6 sqlite windows nas"><span class="archive-number">06</span><div class="archive-name"><h3>Produção Operacional</h3><p>Aplicação Windows implantada no escritório e na fábrica para organizar OPs e visão coletiva.</p></div><div class="archive-state"><span class="status status--production">EM PRODUÇÃO</span><small>acompanhamento compartilhado entre equipes</small></div><div class="archive-stack">Python · PySide6 · SQLite · Windows</div><a class="archive-open" href="cases/producao-operacional/" aria-label="Abrir Produção Operacional">↗</a></article>'
PT_CATALOG_ARCHIVE = '<article class="archive-row persp-process persp-architecture" data-project="catalogo-operacional-archive" data-search="catalogo operacional compras fastapi sqlite fts5 dados"><span class="archive-number">07</span><div class="archive-name"><h3>Catálogo Operacional de Compras</h3><p>Busca operacional com histórico, integridade de dados e controle de edição.</p></div><div class="archive-state"><span class="status status--internal">USO INTERNO DIÁRIO</span><small>consulta e atualização de dados operacionais</small></div><div class="archive-stack">FastAPI · Python · SQLite FTS5</div><a class="archive-open" href="cases/catalogo-operacional-compras/" aria-label="Abrir Catálogo Operacional">↗</a></article>'
PT_CENTRAL = '<article class="archive-row persp-process persp-automation persp-architecture" data-project="central-iso" data-search="central iso qualidade fastapi n8n docker tauri rastreabilidade"><span class="archive-number">18</span><div class="archive-name"><h3>Central ISO</h3><p>Piloto técnico criado com requisitos reais da Qualidade, verificações determinísticas, documentos somente leitura e revisão humana.</p></div><div class="archive-state"><span class="status status--pilot">PILOTO TÉCNICO</span><small>não apresentado como conformidade certificada</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="cases/central-iso/" aria-label="Abrir Central ISO">↗</a></article>'
PT_PORTAL = '<article class="archive-row persp-architecture persp-process persp-integration" data-project="portal-archive" data-search="portal business operating platform fastapi react postgresql rls outbox arquitetura"><span class="archive-number">19</span><div class="archive-name"><h3>Portal</h3><p>Plataforma autoral para processos governados, integrações e objetos empresariais compartilhados.</p></div><div class="archive-state"><span class="status status--pilot">EM DESENVOLVIMENTO</span><small>case baseado em uma edição pública simplificada</small></div><div class="archive-stack">React · TypeScript · FastAPI · PostgreSQL</div><a class="archive-open" href="cases/portal/" aria-label="Abrir arquitetura e estado do Portal">↗</a></article>'

EN_CAREER_ARCHIVE = '<article class="archive-row persp-architecture persp-agents persp-process" data-project="carreira-pessoal-archive" data-search="career personal fastapi react typescript tauri evidenceguard qa"><span class="archive-number">05</span><div class="archive-name"><h3>CarreiraPessoal</h3><p>A personal tool for collecting opportunities, understanding requirements and organizing applications.</p></div><div class="archive-state"><span class="status status--public">PERSONAL USE</span><small>job search and resumes in one place</small></div><div class="archive-stack">FastAPI · React/TypeScript · Tauri/Rust</div><a class="archive-open" href="cases/career-personal/" aria-label="Open CarreiraPessoal">↗</a></article>'
EN_PROD_ARCHIVE = '<article class="archive-row persp-process persp-automation persp-architecture" data-project="producao-operacional-archive" data-search="production operations python pyside6 sqlite windows nas"><span class="archive-number">06</span><div class="archive-name"><h3>Production Operations</h3><p>Windows application deployed across office and factory to organize production orders and shared visibility.</p></div><div class="archive-state"><span class="status status--production">IN PRODUCTION</span><small>shared tracking across teams</small></div><div class="archive-stack">Python · PySide6 · SQLite · Windows</div><a class="archive-open" href="cases/producao-operacional/" aria-label="Open Production Operations">↗</a></article>'
EN_CATALOG_ARCHIVE = '<article class="archive-row persp-process persp-architecture" data-project="catalogo-operacional-archive" data-search="operational procurement catalog fastapi sqlite fts5 data"><span class="archive-number">07</span><div class="archive-name"><h3>Operational Procurement Catalog</h3><p>Operational search with history, data integrity and revision control.</p></div><div class="archive-state"><span class="status status--internal">DAILY INTERNAL USE</span><small>search and update operational data</small></div><div class="archive-stack">FastAPI · Python · SQLite FTS5</div><a class="archive-open" href="cases/operational-procurement-catalog/" aria-label="Open Operational Procurement Catalog">↗</a></article>'
EN_CENTRAL = '<article class="archive-row persp-process persp-automation persp-architecture" data-project="central-iso" data-search="central iso quality fastapi n8n docker tauri traceability"><span class="archive-number">18</span><div class="archive-name"><h3>Central ISO</h3><p>Technical pilot based on real Quality requirements, deterministic checks, read-only documents and human review.</p></div><div class="archive-state"><span class="status status--pilot">TECHNICAL PILOT</span><small>not presented as certified compliance</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="cases/central-iso/" aria-label="Open Central ISO">↗</a></article>'
EN_PORTAL = '<article class="archive-row persp-architecture persp-process persp-integration" data-project="portal-archive" data-search="portal business operating platform fastapi react postgresql rls outbox architecture"><span class="archive-number">19</span><div class="archive-name"><h3>Portal</h3><p>Author-led business platform for governed processes, integrations and shared business objects.</p></div><div class="archive-state"><span class="status status--pilot">IN DEVELOPMENT</span><small>case based on a simplified public edition</small></div><div class="archive-stack">React · TypeScript · FastAPI · PostgreSQL</div><a class="archive-open" href="cases/portal/" aria-label="Open Portal architecture and status">↗</a></article>'


for rel, english in [('index.html', False), ('en/index.html', True)]:
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')

    # Homepage features four projects; the archive keeps the rest.
    for name in (
        'CarreiraPessoal',
        'Produção Operacional' if not english else 'Production Operations',
        'Catálogo Operacional de Compras' if not english else 'Operational Procurement Catalog',
        'Portal',
    ):
        text = remove_feature(text, name)

    if english:
        entries = [
            ('data-project="carreira-pessoal-archive"', EN_CAREER_ARCHIVE),
            ('data-project="producao-operacional-archive"', EN_PROD_ARCHIVE),
            ('data-project="catalogo-operacional-archive"', EN_CATALOG_ARCHIVE),
            ('data-project="central-iso"', EN_CENTRAL),
            ('data-project="portal-archive"', EN_PORTAL),
        ]
    else:
        entries = [
            ('data-project="carreira-pessoal-archive"', PT_CAREER_ARCHIVE),
            ('data-project="producao-operacional-archive"', PT_PROD_ARCHIVE),
            ('data-project="catalogo-operacional-archive"', PT_CATALOG_ARCHIVE),
            ('data-project="central-iso"', PT_CENTRAL),
            ('data-project="portal-archive"', PT_PORTAL),
        ]

    text = append_archive(text, entries)
    text = renumber_archive(text)
    path.write_text(text, encoding='utf-8')

runpy.run_path(str(ROOT / 'scripts' / 'patch_maintenance_case.py'), run_name='__main__')
runpy.run_path(str(ROOT / 'scripts' / 'patch_proposal_case_pt.py'), run_name='__main__')
print('Homepage keeps four featured projects; remaining cases preserved in the archive.')
