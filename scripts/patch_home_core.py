from pathlib import Path

root = Path(__file__).resolve().parents[1]

def patch(path, pairs):
    p = root / path
    text = p.read_text(encoding='utf-8')
    for old, new in pairs:
        if old not in text:
            raise RuntimeError(f'{path}: source phrase missing: {old[:80]}')
        text = text.replace(old, new, 1)
    p.write_text(text, encoding='utf-8')

patch('index.html', [
    ('AUTOMAÇÃO · IA · INTEGRAÇÕES · 2026', 'AUTOMAÇÃO · IA APLICADA · INTEGRAÇÕES · PROCESSOS'),
    ('Transformo necessidades operacionais em automações, integrações e sistemas internos que as pessoas conseguem usar no dia a dia.', 'Transformo necessidades operacionais em automações, integrações e sistemas internos rastreáveis, utilizáveis e sustentáveis.'),
    ('Trabalho desde o levantamento do processo e das regras de negócio até arquitetura, desenvolvimento, implantação, treinamento, monitoramento e sustentação. Minha base principal é n8n self-hosted, Python, APIs REST, bancos de dados e IA generativa com revisão humana.', 'Atuo desde a conversa com usuários e stakeholders, mapeamento AS-IS/TO-BE e regras de negócio até arquitetura, desenvolvimento, testes, implantação, treinamento, monitoramento e sustentação. Minha base é n8n self-hosted, Python, FastAPI, APIs REST, bancos de dados, Docker e IA aplicada com revisão humana.'),
    ('<div><dt>Prática</dt><dd>n8n · Python · APIs REST · SQL · Docker · IA generativa</dd></div><div><dt>Forma de trabalho</dt><dd>Revisão humana, regras claras, histórico e melhoria contínua</dd></div>', '<div><dt>Núcleo técnico</dt><dd>n8n · Python · APIs REST · PostgreSQL · Docker · IA aplicada</dd></div><div><dt>Forma de trabalho</dt><dd>Requisitos · rastreabilidade · revisão humana · sustentação</dd></div>'),
    ('<li><a class="metric-link" href="cases/helpdesk/" aria-label="Abrir HelpDesk: 11 usuários"><strong>11</strong><span>usuários no HelpDesk</span><small>uso interno diário · abrir case ↗</small></a></li>', '<li><a class="metric-link" href="cases/vesper-manutencao/" aria-label="Abrir Vesper Manutenção: mais de 40 ativos"><strong>40+</strong><span>ativos acompanhados em manutenção</span><small>histórico, evidências e Qualidade · abrir ↗</small></a></li>'),
    ('<h3>Vesper Propostas</h3><p class="case-summary">Reuni dados do pedido, seleção de modelos, geração ODT/PDF, revisão e preparação de e-mail em um fluxo único.</p>', '<h3>Proposta Comercial</h3><p class="case-summary">Evoluí o Vesper Propostas para reunir pedido, cliente, modelo, ODT/PDF, revisão, aprovação, preparação de e-mail e histórico em um fluxo controlado.</p>'),
    ('<div class="section-heading"><p>EXPERIÊNCIA PROFISSIONAL</p><h2>Atuação próxima da operação, do levantamento à sustentação.</h2><span>Na prática, trabalho diretamente com gestão e usuários, transformando necessidades em sistemas, automações e melhorias acompanhadas no uso real.</span></div>', '<div class="section-heading"><p>EXPERIÊNCIA PROFISSIONAL</p><h2>Automação próxima da operação, da Qualidade e da gestão.</h2><span>Trabalho diretamente com usuários e stakeholders, transformando problemas operacionais em sistemas rastreáveis, implantados e sustentados no uso real.</span></div>'),
    ('Sou responsável pelo ciclo ponta a ponta de soluções internas: requisitos, mapeamento AS-IS/TO-BE, arquitetura, desenvolvimento, implantação, treinamento, monitoramento e sustentação. Já treinei e orientei 30+ pessoas em escritório, fábrica e acesso remoto.', 'Levanto requisitos diretamente com usuários, Produção, Qualidade e gestão em ambiente industrial com requisitos de qualidade/Ex, transformando rotinas de planilhas, papel, e-mail e pastas de rede em automações e sistemas com aprovações, versionamento, histórico e auditoria. Desenvolvo, testo, implanto, documento, treino e sustento as soluções; já treinei/orientei 30+ pessoas em escritório, fábrica e acesso remoto.'),
    ('Concluí dez sprints práticas com Python, SQL, Docker e AWS, incluindo ingestão CSV/API TMDB, S3, Lambda/boto3, Glue/PySpark, Parquet, camadas Raw/Trusted/Refined, Athena e QuickSight.', 'Concluí dez sprints práticas com Linux, Git, Python, SQL e Docker, incluindo ETL/Data Lake em AWS, ingestão CSV/API TMDB, S3, Lambda/boto3, Glue/PySpark, Parquet, camadas Raw/Trusted/Refined, Athena e QuickSight.'),
    ('<div><dt>Backend e dados</dt><dd>FastAPI · PostgreSQL · SQLite FTS5 · AWS · PySpark</dd></div>', '<div><dt>Backend e dados</dt><dd>Python · FastAPI · PostgreSQL · SQLite FTS5 · ETL/Data Lake · AWS/PySpark</dd></div>'),
    ('<div><dt>IA aplicada</dt><dd>Postagem Redes · StudioCad · Vesper Manutenção · Hubora</dd></div>', '<div><dt>IA aplicada</dt><dd>RAG/grounding · LangChain · Postagem Redes · CarreiraPessoal · revisão humana</dd></div>'),
    ('<div><dt>Confiabilidade</dt><dd>Filas · retries · idempotência · logs · alertas · backups</dd></div>', '<div><dt>Rastreabilidade e Qualidade</dt><dd>histórico · evidências · aprovações · auditoria · controle de mudanças</dd></div><div><dt>Confiabilidade</dt><dd>monitoramento · filas · retries · idempotência · logs · alertas · backups</dd></div>'),
    ('Piscine 42 Rio · programa intensivo concluído em jul. 2025', 'Piscine 42 Rio · programa intensivo em ambiente Linux/C concluído em jul. 2025'),
    ('Inglês básico · leitura independente de documentação técnica', 'Inglês · leitura técnica independente; escrita e conversação básicas'),
])

patch('en/index.html', [
    ('AUTOMATION · AI · INTEGRATIONS · 2026', 'AUTOMATION · APPLIED AI · INTEGRATIONS · PROCESSES'),
    ('I turn operational needs into automations, integrations and internal systems that people can use in their daily routines.', 'I turn operational needs into traceable, usable and supportable automations, integrations and internal systems.'),
    ('I work from process discovery and business rules through architecture, development, deployment, training, monitoring and support. My main stack includes self-hosted n8n, Python, REST APIs, databases and generative AI with human review.', 'I work from stakeholder conversations, AS-IS/TO-BE mapping and business rules through architecture, development, testing, deployment, training, monitoring and support. My core stack includes self-hosted n8n, Python, FastAPI, REST APIs, databases, Docker and applied AI with human review.'),
    ('<div><dt>Practice</dt><dd>n8n · Python · REST APIs · SQL · Docker · Generative AI</dd></div><div><dt>Working style</dt><dd>Human review, clear rules, traceable history and continuous improvement</dd></div>', '<div><dt>Core practice</dt><dd>n8n · Python · REST APIs · PostgreSQL · Docker · Applied AI</dd></div><div><dt>Working style</dt><dd>Requirements · traceability · human review · support</dd></div>'),
    ('<li><a class="metric-link" href="cases/helpdesk/" aria-label="Open HelpDesk: 11 users"><strong>11</strong><span>HelpDesk users</span><small>real internal use · open case ↗</small></a></li>', '<li><a class="metric-link" href="cases/vesper-manutencao/" aria-label="Open Vesper Maintenance: more than 40 assets"><strong>40+</strong><span>maintenance assets tracked</span><small>history, evidence and Quality · open ↗</small></a></li>'),
    ('<h3>Vesper Propostas</h3><p class="case-summary">I brought request data, template selection, ODT/PDF generation, review and email preparation into one workflow.</p>', '<h3>Proposta Comercial</h3><p class="case-summary">I evolved Vesper Propostas into a controlled workflow for request data, customer/template selection, ODT/PDF, review, approval, email preparation and history.</p>'),
])

print('Current career positioning and evidence refreshed.')
