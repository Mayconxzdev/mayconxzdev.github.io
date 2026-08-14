from pathlib import Path
import re
import runpy

ROOT = Path(__file__).resolve().parents[1]


def feature_re(name: str) -> re.Pattern[str]:
    # Keep every operation inside one feature-card boundary. A plain `.*?` here
    # can start at an earlier article and accidentally consume several cards.
    return re.compile(
        rf'<article class="feature-case[^>]*>(?:(?!</article>).)*?<h3>\s*{re.escape(name)}\s*</h3>(?:(?!</article>).)*?</article>',
        re.S,
    )


def get_feature(text: str, name: str) -> re.Match[str]:
    match = feature_re(name).search(text)
    if not match:
        raise RuntimeError(f'featured project missing: {name}')
    return match


def renumber(text: str, name: str, number: str) -> str:
    match = get_feature(text, name)
    block = re.sub(
        r'(<div class="case-index"><span>)\d+(</span>)',
        rf'\g<1>{number}\g<2>',
        match.group(0),
        count=1,
    )
    return text[:match.start()] + block + text[match.end():]


def insert_before(text: str, name: str, block: str) -> str:
    match = get_feature(text, name)
    return text[:match.start()] + block + '\n\n        ' + text[match.start():]


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


def copy_sync(text: str, english: bool) -> str:
    if english:
        pairs = [
            (
                'I work from process discovery and business rules through architecture, development, deployment, training, monitoring and support. My main stack includes self-hosted n8n, Python, REST APIs, databases and generative AI with human review.',
                'I work from process discovery and business rules through architecture, development, deployment, training, monitoring and support. My core is self-hosted n8n, Python, FastAPI, REST APIs, SQL/PostgreSQL and Docker, with applied AI, RAG/grounding and human review when they add value.',
            ),
            (
                '<div><dt>Practice</dt><dd>n8n · Python · REST APIs · SQL · Docker · Generative AI</dd></div>',
                '<div><dt>Practice</dt><dd>n8n · Python · FastAPI · REST APIs · SQL/PostgreSQL · Docker · applied AI</dd></div>',
            ),
            (
                '<div><dt>Applied AI</dt><dd>Postagem Redes · StudioCad · Vesper Maintenance · Hubora</dd></div>',
                '<div><dt>Applied AI</dt><dd>Postagem Redes · CarreiraPessoal · StudioCad · RAG/grounding</dd></div>',
            ),
            (
                '<div><dt>Architecture</dt><dd>Modular monolith · tenant/RLS · Action Envelope · outbox</dd></div>',
                '<div><dt>Architecture</dt><dd>FastAPI · React/TypeScript · Tauri · modular monolith · APIs/contracts</dd></div>',
            ),
        ]
        old_ld = '"knowsAbout":["n8n","Process automation","Low-code","AS-IS/TO-BE process mapping","Generative AI","AI agents","Prompt engineering","Grounding","JSON Schema","Multimodal AI","Media generation","REST APIs","Webhooks","Python","JavaScript","TypeScript","FastAPI","PostgreSQL","SQLite FTS5","Docker","AWS","PySpark","CI/CD","Idempotency","RLS","Transactional outbox"]'
        new_ld = '"knowsAbout":["n8n","Process automation","BPMN","AS-IS/TO-BE process mapping","Requirements discovery","Applied AI","Generative AI","RAG/grounding","AI agents","Human-in-the-loop","REST APIs","Webhooks","OAuth 2.0","Python","FastAPI","JavaScript","TypeScript","SQL","PostgreSQL","SQLite FTS5","Docker","GitHub Actions","CI/CD","Traceability","Monitoring","Retries","Idempotency"]'
    else:
        pairs = [
            (
                'Trabalho desde o levantamento do processo e das regras de negócio até arquitetura, desenvolvimento, implantação, treinamento, monitoramento e sustentação. Minha base principal é n8n self-hosted, Python, APIs REST, bancos de dados e IA generativa com revisão humana.',
                'Trabalho desde o levantamento do processo e das regras de negócio até arquitetura, desenvolvimento, implantação, treinamento, monitoramento e sustentação. Meu núcleo é n8n self-hosted, Python, FastAPI, APIs REST, SQL/PostgreSQL e Docker, com IA aplicada, RAG/grounding e revisão humana quando agregam valor.',
            ),
            (
                '<div><dt>Prática</dt><dd>n8n · Python · APIs REST · SQL · Docker · IA generativa</dd></div>',
                '<div><dt>Prática</dt><dd>n8n · Python · FastAPI · APIs REST · SQL/PostgreSQL · Docker · IA aplicada</dd></div>',
            ),
            (
                '<div><dt>IA aplicada</dt><dd>Postagem Redes · StudioCad · Vesper Manutenção · Hubora</dd></div>',
                '<div><dt>IA aplicada</dt><dd>Postagem Redes · CarreiraPessoal · StudioCad · RAG/grounding</dd></div>',
            ),
            (
                '<div><dt>Arquitetura</dt><dd>Monólito modular · tenant/RLS · Action Envelope · outbox</dd></div>',
                '<div><dt>Arquitetura</dt><dd>FastAPI · React/TypeScript · Tauri · monólito modular · APIs/contratos</dd></div>',
            ),
        ]
        old_ld = '"knowsAbout":["n8n","Automação de processos","Low-code","Mapeamento AS-IS/TO-BE","IA generativa","Agentes de IA","Engenharia de prompts","Grounding","JSON Schema","IA multimodal","Geração de mídia","APIs REST","Webhooks","Python","JavaScript","TypeScript","FastAPI","PostgreSQL","SQLite FTS5","Docker","AWS","PySpark","CI/CD","Idempotência","RLS","Transactional outbox"]'
        new_ld = '"knowsAbout":["n8n","Automação de processos","BPMN","Mapeamento AS-IS/TO-BE","Levantamento de requisitos","IA aplicada","IA generativa","RAG/grounding","Agentes de IA","Human-in-the-loop","APIs REST","Webhooks","OAuth 2.0","Python","FastAPI","JavaScript","TypeScript","SQL","PostgreSQL","SQLite FTS5","Docker","GitHub Actions","CI/CD","Rastreabilidade","Monitoramento","Retries","Idempotência"]'

    for old, new in pairs:
        if old in text:
            text = text.replace(old, new, 1)
    if old_ld in text:
        text = text.replace(old_ld, new_ld, 1)
    return text


PT_CAREER = '''<article class="feature-case feature-case--portal-vesper feature-case--reverse" data-project="carreira-pessoal"><div class="feature-case__copy"><div class="case-index"><span>04</span><span class="status status--public">PRODUTO PESSOAL EM USO</span></div><p class="case-category">Produto Windows, evidências e QA</p><h3>CarreiraPessoal</h3><p class="case-summary">Criei este produto para unificar descoberta de vagas, deduplicação, direção de carreira, evidências e roteamento de currículo sem tornar IA ou auto-submit obrigatórios.</p><div class="case-impact"><small>Evidência de engenharia</small><strong>v12.5.2 com 283 testes Python aprovados, 102 famílias ATS/plataformas e 11 coletores diretos.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5 · IA opcional</p><div class="project-links"><a class="text-link" href="cases/carreira-pessoal/">Abrir case<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/CarreiraPessoal">Ver código<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><figure class="portfolio-proof"><img src="assets/evidence/carreira-overview.webp" alt="Telas reais do CarreiraPessoal" loading="lazy" decoding="async"><figcaption>Telas reais da v12.5.2.</figcaption></figure></div></article>'''
EN_CAREER = '''<article class="feature-case feature-case--portal-vesper feature-case--reverse" data-project="carreira-pessoal"><div class="feature-case__copy"><div class="case-index"><span>04</span><span class="status status--public">PERSONAL PRODUCT IN USE</span></div><p class="case-category">Windows product, evidence and QA</p><h3>CarreiraPessoal</h3><p class="case-summary">I built this product to unify job discovery, deduplication, career-goal checks, evidence and resume routing without making AI or auto-submit mandatory.</p><div class="case-impact"><small>Engineering evidence</small><strong>v12.5.2 with 283 passing Python tests, 102 ATS/career-platform families and 11 direct collectors.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5 · optional AI</p><div class="project-links"><a class="text-link" href="cases/career-personal/">Open case<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/CarreiraPessoal">View code<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><figure class="portfolio-proof"><img src="../assets/evidence/carreira-overview.webp" alt="Real CarreiraPessoal screens" loading="lazy" decoding="async"><figcaption>Real v12.5.2 product screens.</figcaption></figure></div></article>'''

PT_CENTRAL = '<article class="archive-row persp-process persp-automation persp-architecture" data-project="central-iso" data-search="central iso qualidade fastapi n8n docker tauri rastreabilidade"><span class="archive-number">18</span><div class="archive-name"><h3>Central ISO</h3><p>Piloto técnico criado com requisitos reais da Qualidade, verificações determinísticas, documentos somente leitura e revisão humana.</p></div><div class="archive-state"><span class="status status--pilot">PILOTO TÉCNICO</span><small>não apresentado como conformidade certificada</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="cases/central-iso/" aria-label="Abrir Central ISO">↗</a></article>'
EN_CENTRAL = '<article class="archive-row persp-process persp-automation persp-architecture" data-project="central-iso" data-search="central iso quality fastapi n8n docker tauri traceability"><span class="archive-number">18</span><div class="archive-name"><h3>Central ISO</h3><p>Technical pilot based on real Quality requirements, deterministic checks, read-only documents and human review.</p></div><div class="archive-state"><span class="status status--pilot">TECHNICAL PILOT</span><small>not presented as certified compliance</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="cases/central-iso/" aria-label="Open Central ISO">↗</a></article>'
PT_PORTAL = '<article class="archive-row persp-architecture persp-process persp-integration" data-project="portal-archive" data-search="portal business operating platform fastapi react postgresql rls outbox arquitetura"><span class="archive-number">19</span><div class="archive-name"><h3>Portal</h3><p>Plataforma autoral para processos governados, integrações e objetos empresariais compartilhados.</p></div><div class="archive-state"><span class="status status--pilot">DESENVOLVIMENTO / REVALIDAÇÃO</span><small>repositório público é referência sanitizada de arquitetura anterior</small></div><div class="archive-stack">React · TypeScript · FastAPI · PostgreSQL</div><a class="archive-open" href="cases/portal/" aria-label="Abrir arquitetura e estado do Portal">↗</a></article>'
EN_PORTAL = '<article class="archive-row persp-architecture persp-process persp-integration" data-project="portal-archive" data-search="portal business operating platform fastapi react postgresql rls outbox architecture"><span class="archive-number">19</span><div class="archive-name"><h3>Portal</h3><p>Author-led business platform for governed processes, integrations and shared business objects.</p></div><div class="archive-state"><span class="status status--pilot">DEVELOPMENT / REVALIDATION</span><small>public repository is an earlier sanitized architecture reference</small></div><div class="archive-stack">React · TypeScript · FastAPI · PostgreSQL</div><a class="archive-open" href="cases/portal/" aria-label="Open Portal architecture and status">↗</a></article>'


for rel, english in [('index.html', False), ('en/index.html', True)]:
    path = ROOT / rel
    text = path.read_text(encoding='utf-8')
    catalog = 'Operational Procurement Catalog' if english else 'Catálogo Operacional de Compras'
    social = 'Postagem Redes'

    if 'data-project="carreira-pessoal"' not in text:
        text = insert_before(text, catalog, EN_CAREER if english else PT_CAREER)
    text = renumber(text, catalog, '05')
    text = renumber(text, social, '06')
    text = remove_feature(text, 'Portal')
    text = append_archive(text, [
        ('data-project="central-iso"', EN_CENTRAL if english else PT_CENTRAL),
        ('data-project="portal-archive"', EN_PORTAL if english else PT_PORTAL),
    ])
    text = copy_sync(text, english)
    path.write_text(text, encoding='utf-8')

runpy.run_path(str(ROOT / 'scripts' / 'patch_maintenance_case.py'), run_name='__main__')
runpy.run_path(str(ROOT / 'scripts' / 'patch_proposal_case_pt.py'), run_name='__main__')
print('Flagship order, portfolio copy and archive status synchronized with current career evidence.')
