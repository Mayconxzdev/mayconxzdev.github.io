from pathlib import Path
import re
import runpy

root = Path(__file__).resolve().parents[1]


def article_pattern(name: str) -> re.Pattern[str]:
    return re.compile(
        rf'<article class="feature-case[^>]*>.*?<h3>{re.escape(name)}</h3>.*?</article>',
        re.S,
    )


def renumber_feature(text: str, name: str, number: str) -> str:
    pattern = article_pattern(name)
    match = pattern.search(text)
    if not match:
        raise RuntimeError(f'featured project missing: {name}')
    block = match.group(0)
    updated = re.sub(
        r'(<div class="case-index"><span>)\d+(</span>)',
        rf'\g<1>{number}\g<2>',
        block,
        count=1,
    )
    return text[:match.start()] + updated + text[match.end():]


def remove_feature(text: str, name: str) -> str:
    pattern = article_pattern(name)
    match = pattern.search(text)
    if not match:
        return text
    return text[:match.start()] + text[match.end():]


def insert_before_feature(text: str, name: str, block: str) -> str:
    pattern = article_pattern(name)
    match = pattern.search(text)
    if not match:
        raise RuntimeError(f'cannot find insertion target: {name}')
    return text[:match.start()] + block + '\n\n        ' + text[match.start():]


def append_archive_rows(text: str, rows: list[str]) -> str:
    marker = '</div>\n      <p class="empty-state"'
    if marker not in text:
        raise RuntimeError('archive end marker missing')
    missing = [row for key, row in rows if key not in text]
    if not missing:
        return text
    return text.replace(marker, '\n        '.join(missing) + '\n      </div>\n      <p class="empty-state"', 1)


def apply_copy_sync(text: str, *, english: bool) -> str:
    if english:
        replacements = [
            (
                'I work from process discovery and business rules through architecture, development, deployment, training, monitoring and support. My main stack includes self-hosted n8n, Python, REST APIs, databases and generative AI with human review.',
                'I work from process discovery and business rules through architecture, development, deployment, training, monitoring and support. My core is self-hosted n8n, Python, FastAPI, REST APIs, SQL/PostgreSQL and Docker, with applied AI, RAG/grounding and human review when they add value.',
            ),
            (
                '<div><dt>Practice</dt><dd>n8n · Python · REST APIs · SQL · Docker · Generative AI</dd></div>',
                '<div><dt>Practice</dt><dd>n8n · Python · FastAPI · REST APIs · SQL/PostgreSQL · Docker · applied AI</dd></div>',
            ),
            (
                '<div><dt>Applied AI</dt><dd>Social Publishing · StudioCad · Vesper Maintenance · Hubora</dd></div>',
                '<div><dt>Applied AI</dt><dd>Social Publishing · CarreiraPessoal · StudioCad · RAG/grounding</dd></div>',
            ),
            (
                '<div><dt>Architecture</dt><dd>Modular monolith · tenant/RLS · Action Envelope · outbox</dd></div>',
                '<div><dt>Architecture</dt><dd>FastAPI · React/TypeScript · Tauri · modular monolith · APIs/contracts</dd></div>',
            ),
        ]
        old_ld = '"knowsAbout":["n8n","Process automation","Low-code","AS-IS/TO-BE process mapping","Generative AI","AI agents","Prompt engineering","Grounding","JSON Schema","Multimodal AI","Media generation","REST APIs","Webhooks","Python","JavaScript","TypeScript","FastAPI","PostgreSQL","SQLite FTS5","Docker","AWS","PySpark","CI/CD","Idempotency","RLS","Transactional outbox"]'
        new_ld = '"knowsAbout":["n8n","Process automation","BPMN","AS-IS/TO-BE process mapping","Requirements discovery","Applied AI","Generative AI","RAG/grounding","AI agents","Human-in-the-loop","REST APIs","Webhooks","OAuth 2.0","Python","FastAPI","JavaScript","TypeScript","SQL","PostgreSQL","SQLite FTS5","Docker","GitHub Actions","CI/CD","Traceability","Monitoring","Retries","Idempotency"]'
    else:
        replacements = [
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

    for old, new in replacements:
        if old in text:
            text = text.replace(old, new, 1)
    if old_ld in text:
        text = text.replace(old_ld, new_ld, 1)
    return text


for rel, lang in [('index.html', 'pt'), ('en/index.html', 'en')]:
    p = root / rel
    text = p.read_text(encoding='utf-8')
    english = lang == 'en'

    if english:
        catalog_name = 'Operational Procurement Catalog'
        social_name = 'Social Publishing'
        portal_name = 'Portal'
        career_card = '''<article class="feature-case feature-case--portal-vesper feature-case--reverse" data-project="carreira-pessoal"><div class="feature-case__copy"><div class="case-index"><span>04</span><span class="status status--public">PERSONAL PRODUCT IN USE</span></div><p class="case-category">Windows product, evidence and QA</p><h3>CarreiraPessoal</h3><p class="case-summary">I built this product to unify job discovery, deduplication, career-goal checks, evidence and resume routing without making AI or auto-submit mandatory.</p><div class="case-impact"><small>Engineering evidence</small><strong>v12.5.2 with 283 passing Python tests, 102 ATS/career-platform families and 11 direct collectors.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5 · optional AI</p><div class="project-links"><a class="text-link" href="cases/career-personal/">Open case<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/CarreiraPessoal">View code<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><figure class="portfolio-proof"><img src="../assets/evidence/carreira-overview.webp" alt="Real CarreiraPessoal screens" loading="lazy" decoding="async"><figcaption>Real v12.5.2 product screens.</figcaption></figure></div></article>'''
        central_row = '<article class="archive-row persp-process persp-automation persp-architecture" data-project="central-iso" data-search="central iso quality fastapi n8n docker tauri traceability"><span class="archive-number">18</span><div class="archive-name"><h3>Central ISO</h3><p>Technical pilot based on real Quality requirements, deterministic checks, read-only documents and human review.</p></div><div class="archive-state"><span class="status status--pilot">TECHNICAL PILOT</span><small>not presented as certified compliance</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="cases/central-iso/" aria-label="Open Central ISO">↗</a></article>'
        portal_row = '<article class="archive-row persp-architecture persp-process persp-integration" data-project="portal-archive" data-search="portal business operating platform fastapi react postgresql rls outbox architecture"><span class="archive-number">19</span><div class="archive-name"><h3>Portal</h3><p>Author-led business platform for governed processes, integrations and shared business objects.</p></div><div class="archive-state"><span class="status status--pilot">DEVELOPMENT / REVALIDATION</span><small>public repository is an earlier sanitized architecture reference</small></div><div class="archive-stack">React · TypeScript · FastAPI · PostgreSQL</div><a class="archive-open" href="cases/portal/" aria-label="Open Portal architecture and status">↗</a></article>'
    else:
        catalog_name = 'Catálogo Operacional de Compras'
        social_name = 'Postagem Redes'
        portal_name = 'Portal'
        career_card = '''<article class="feature-case feature-case--portal-vesper feature-case--reverse" data-project="carreira-pessoal"><div class="feature-case__copy"><div class="case-index"><span>04</span><span class="status status--public">PRODUTO PESSOAL EM USO</span></div><p class="case-category">Produto Windows, evidências e QA</p><h3>CarreiraPessoal</h3><p class="case-summary">Criei este produto para unificar descoberta de vagas, deduplicação, direção de carreira, evidências e roteamento de currículo sem tornar IA ou auto-submit obrigatórios.</p><div class="case-impact"><small>Evidência de engenharia</small><strong>v12.5.2 com 283 testes Python aprovados, 102 famílias ATS/plataformas e 11 coletores diretos.</strong></div><p class="case-stack">FastAPI · React/TypeScript · Tauri/Rust · SQLite/FTS5 · IA opcional</p><div class="project-links"><a class="text-link" href="cases/carreira-pessoal/">Abrir case<span aria-hidden="true">↗</span></a><a class="text-link text-link--muted" href="https://github.com/Mayconxzdev/CarreiraPessoal">Ver código<span aria-hidden="true">↗</span></a></div></div><div class="feature-case__visual"><figure class="portfolio-proof"><img src="assets/evidence/carreira-overview.webp" alt="Telas reais do CarreiraPessoal" loading="lazy" decoding="async"><figcaption>Telas reais da v12.5.2.</figcaption></figure></div></article>'''
        central_row = '<article class="archive-row persp-process persp-automation persp-architecture" data-project="central-iso" data-search="central iso qualidade fastapi n8n docker tauri rastreabilidade"><span class="archive-number">18</span><div class="archive-name"><h3>Central ISO</h3><p>Piloto técnico criado com requisitos reais da Qualidade, verificações determinísticas, documentos somente leitura e revisão humana.</p></div><div class="archive-state"><span class="status status--pilot">PILOTO TÉCNICO</span><small>não apresentado como conformidade certificada</small></div><div class="archive-stack">FastAPI · n8n · Docker · Tauri</div><a class="archive-open" href="cases/central-iso/" aria-label="Abrir Central ISO">↗</a></article>'
        portal_row = '<article class="archive-row persp-architecture persp-process persp-integration" data-project="portal-archive" data-search="portal business operating platform fastapi react postgresql rls outbox arquitetura"><span class="archive-number">19</span><div class="archive-name"><h3>Portal</h3><p>Plataforma autoral para processos governados, integrações e objetos empresariais compartilhados.</p></div><div class="archive-state"><span class="status status--pilot">DESENVOLVIMENTO / REVALIDAÇÃO</span><small>repositório público é referência sanitizada de arquitetura anterior</small></div><div class="archive-stack">React · TypeScript · FastAPI · PostgreSQL</div><a class="archive-open" href="cases/portal/" aria-label="Abrir arquitetura e estado do Portal">↗</a></article>'

    if 'data-project="carreira-pessoal"' not in text:
        text = insert_before_feature(text, catalog_name, career_card)

    text = renumber_feature(text, catalog_name, '05')
    text = renumber_feature(text, social_name, '06')
    text = remove_feature(text, portal_name)

    rows = [
        ('data-project="central-iso"', central_row),
        ('data-project="portal-archive"', portal_row),
    ]
    text = append_archive_rows(text, rows)
    text = apply_copy_sync(text, english=english)
    p.write_text(text, encoding='utf-8')

runpy.run_path(str(root / 'scripts' / 'patch_maintenance_case.py'), run_name='__main__')
runpy.run_path(str(root / 'scripts' / 'patch_proposal_case_pt.py'), run_name='__main__')
print('Flagship order, portfolio copy and archive status synchronized with current career evidence.')
