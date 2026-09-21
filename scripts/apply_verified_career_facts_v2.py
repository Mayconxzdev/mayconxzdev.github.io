from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_PROOF = '''<section class="proof-strip" aria-labelledby="proof-title">
          <div class="section-heading section-heading--compact"><p>PROVAS EM CONTEXTO</p><h2 id="proof-title">Números ligados a sistemas em uso - não a marketing.</h2><span>Cada indicador pertence ao sistema ou ambiente que o sustenta. Valores operacionais podem evoluir com o uso.</span></div>
          <ol class="metric-list"><li><a class="metric-link" href="competencias/" aria-label="Abrir competências: mais de 10 mil execuções na instância n8n"><strong>10 mil+</strong><span>execuções na instância n8n</span><small>múltiplas automações em produção · abrir evidências ↗</small></a></li><li><a class="metric-link" href="cases/helpdesk/" aria-label="Abrir HelpDesk: 11 usuários"><strong>11</strong><span>usuários no HelpDesk</span><small>uso interno real · abrir case ↗</small></a></li><li><a class="metric-link" href="cases/producao-operacional/" aria-label="Abrir Produção Operacional: 20 profissionais"><strong>20+</strong><span>profissionais apoiados na produção</span><small>10+ PCs · 1 TV · 9 setores · abrir case ↗</small></a></li><li><a class="metric-link" href="cases/mala-direta/" aria-label="Abrir Mala Direta: seis campanhas"><strong>6</strong><span>campanhas operacionais</span><small>base de 1.020 contatos · uma com 900+ ↗</small></a></li><li><a class="metric-link" href="cases/vesper-propostas/" aria-label="Abrir Vesper Propostas: menos de 30 segundos"><strong>&lt; 30s</strong><span>em propostas simples</span><small>antes: 2 a 4 minutos · abrir case ↗</small></a></li><li><a class="metric-link" href="cases/catalogo-operacional-compras/" aria-label="Abrir Catálogo: mais de 480 códigos"><strong>480+</strong><span>códigos no Catálogo Operacional</span><small>24 categorias · uso diário · abrir case ↗</small></a></li></ol>
        </section>'''

EN_PROOF = '''<section class="proof-strip" aria-labelledby="proof-title">
          <div class="section-heading section-heading--compact"><p>EVIDENCE IN CONTEXT</p><h2 id="proof-title">Numbers tied to systems in use - not marketing.</h2><span>Each indicator belongs to the system or environment that supports it. Operational values may evolve with usage.</span></div>
          <ol class="metric-list"><li><a class="metric-link" href="skills/" aria-label="Open skills evidence: 10 thousand executions in n8n"><strong>10k+</strong><span>executions in the n8n environment</span><small>multiple production automations · open evidence ↗</small></a></li><li><a class="metric-link" href="cases/helpdesk/" aria-label="Open HelpDesk: 11 users"><strong>11</strong><span>HelpDesk users</span><small>real internal use · open case ↗</small></a></li><li><a class="metric-link" href="cases/producao-operacional/" aria-label="Open Production Operations: 20 professionals"><strong>20+</strong><span>professionals supported in production</span><small>10+ PCs · 1 TV · 9 areas · open case ↗</small></a></li><li><a class="metric-link" href="cases/mala-direta/" aria-label="Open Mala Direta: six campaigns"><strong>6</strong><span>operational campaigns</span><small>1,020-contact base · one with 900+ ↗</small></a></li><li><a class="metric-link" href="cases/vesper-propostas/" aria-label="Open proposals: under 30 seconds"><strong>&lt; 30s</strong><span>for simple proposals</span><small>before: 2 to 4 minutes · open case ↗</small></a></li><li><a class="metric-link" href="cases/operational-procurement-catalog/" aria-label="Open catalog: 480 codes"><strong>480+</strong><span>codes in the procurement catalog</span><small>24 categories · daily use · open case ↗</small></a></li></ol>
        </section>'''

PT_EXPERIENCE = '''<section class="experience" id="experience">
          <div class="section-heading"><p>EXPERIÊNCIA</p><h2>Responsabilidade técnica com contato direto com a operação.</h2><span>Meu cargo formal aparece sem alteração. O escopo funcional é demonstrado por sistemas implantados, usuários, treinamento e sustentação.</span></div>
          <div class="experience-list">
            <article><div class="experience-date">dez. 2025 - atual</div><div><h3>Grupo Vesper - Vesper Equipamentos EX e Vent Rio Equipamentos</h3><p class="experience-role">Técnico Júnior em Automação de Processos <span>cargo formal</span></p><p>Responsável técnico pelo ciclo ponta a ponta de soluções internas, em contato direto com gestão e usuários: requisitos, arquitetura, desenvolvimento, implantação, monitoramento e sustentação. Treinei e orientei 30+ pessoas em escritório, fábrica e acesso remoto.</p></div></article>
            <article><div class="experience-date">out. 2024 - mar. 2025</div><div><h3>Compass UOL</h3><p class="experience-role">Programa de Bolsas em Engenharia de Dados</p><p>Dez sprints práticas com Python, SQL, Docker e AWS, incluindo ingestão CSV/API TMDB, S3, Lambda/boto3, Glue/PySpark, Parquet, camadas Raw/Trusted/Refined, Athena e QuickSight.</p></div></article>
          </div>
        </section>'''

EN_EXPERIENCE = '''<section class="experience" id="experience">
          <div class="section-heading"><p>EXPERIENCE</p><h2>Technical ownership with direct contact with operations.</h2><span>My formal role is shown unchanged. Functional scope is demonstrated through deployed systems, users, training and support.</span></div>
          <div class="experience-list">
            <article><div class="experience-date">Dec. 2025 - present</div><div><h3>Grupo Vesper - Vesper Equipamentos EX e Vent Rio Equipamentos</h3><p class="experience-role">Junior Process Automation Technician <span>official title</span></p><p>Technical owner of the end-to-end lifecycle of internal solutions, working directly with management and users across requirements, architecture, development, deployment, monitoring and support. Trained and guided 30+ people in office, factory and remote settings.</p></div></article>
            <article><div class="experience-date">Oct. 2024 - Mar. 2025</div><div><h3>Compass UOL</h3><p class="experience-role">Data Engineering Scholarship Program</p><p>Ten practical sprints with Python, SQL, Docker and AWS, including CSV/TMDB API ingestion, S3, Lambda/boto3, Glue/PySpark, Parquet, Raw/Trusted/Refined layers, Athena and QuickSight.</p></div></article>
          </div>
        </section>'''


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def write(relative: str, text: str) -> None:
    path = ROOT / relative
    original = path.read_text(encoding="utf-8")
    if original != text:
        path.write_text(text, encoding="utf-8")
        print(f"updated: {relative}")
    else:
        print(f"current: {relative}")


def replace_section(text: str, class_name: str, replacement: str) -> str:
    result, count = re.subn(rf'<section class="{re.escape(class_name)}"[^>]*>.*?</section>', replacement, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f"missing section: {class_name}")
    return result


def apply_pairs(text: str, pairs: list[tuple[str, str]]) -> str:
    for old, new in pairs:
        if old in text:
            text = text.replace(old, new)
    return text


def update_home(relative: str, english: bool) -> None:
    text = read(relative)
    text = replace_section(text, "proof-strip", EN_PROOF if english else PT_PROOF)
    text = replace_section(text, "experience", EN_EXPERIENCE if english else PT_EXPERIENCE)
    pairs = [
        ("First campaign with more than 900 recipients.", "6 campaigns over a 1,020-contact base, including one for 900+ recipients."),
        ("Primeira campanha com mais de 900 destinatários.", "6 campanhas sobre uma base de 1.020 contatos, incluindo uma para 900+ destinatários."),
        ('<div class="visual-facts"><span>158 nodes</span><span>9 Data Tables</span><span>900+ recipients</span></div>', '<div class="visual-facts"><span>6 campaigns</span><span>1,020 contacts</span><span>158 nodes in the main flow</span></div>'),
        ('<div class="visual-facts"><span>158 nós</span><span>9 Data Tables</span><span>900+ destinatários</span></div>', '<div class="visual-facts"><span>6 campanhas</span><span>1.020 contatos</span><span>158 nós no principal</span></div>'),
        ("Deployed on 11 office computers and the factory TV.", "Deployed on 10+ computers and 1 factory TV, supporting 20+ professionals across 9 production areas."),
        ("Implantado em 11 computadores do escritório e na TV da fábrica.", "Implantado em 10+ computadores e 1 TV, apoiando 20+ profissionais em 9 setores produtivos."),
        ('<div class="node"><small>11</small><b>Stations</b><span>office</span></div>', '<div class="node"><small>10+</small><b>Stations</b><span>office</span></div>'),
        ('<div class="node"><small>11</small><b>Estações</b><span>escritório</span></div>', '<div class="node"><small>10+</small><b>Estações</b><span>escritório</span></div>'),
        ("Multi-image Facebook publication confirmed.", "Facebook and Instagram exercised in testing; external constraints are documented per channel."),
        ("Publicação multi-imagem confirmada no Facebook.", "Facebook e Instagram exercitados em teste; limites externos documentados por canal."),
        ("Technical English for reading; basic writing and conversation", "Basic English; independent technical-documentation reading, basic writing and conversation"),
        ("Inglês técnico para leitura; escrita e conversação básicas", "Inglês básico; leitura independente de documentação técnica, escrita e conversação básicas"),
        ('"Text-to-video",', '"Media generation","AWS","PySpark",'),
        ('"Text-to-video"', '"Media generation","AWS","PySpark"'),
    ]
    text = apply_pairs(text, pairs)
    text = re.sub(r'<article class="archive-row[^\"]*"[^>]*>.*?href="(?:cases/)?compass-automation/".*?</article>', "", text, count=1, flags=re.S)
    write(relative, text)


def update_skills(relative: str, english: bool) -> None:
    text = read(relative)
    pairs = [
        ("OpenAI, Gemini, Ollama, OpenRouter and Codex; LLM APIs, prompt engineering, context retrieval/grounding, JSON Schema, multi-stage pipelines, multimodal AI, text, image and video generation (text-to-video), fallback, auditing and human review.", "OpenAI, Gemini, Ollama, OpenRouter and Codex; LLM APIs, prompt engineering, context retrieval/grounding, JSON Schema, multi-stage pipelines, multimodal AI and media generation across text, image, audio and video, with fallback, auditing and human review."),
        ("OpenAI, Gemini, Ollama, OpenRouter e Codex; APIs de LLM, engenharia de prompts, recuperação de contexto/grounding, JSON Schema, pipelines multiestágio, IA multimodal, geração de texto, imagem e vídeo (text-to-video), fallback, auditoria e revisão humana.", "OpenAI, Gemini, Ollama, OpenRouter e Codex; APIs de LLM, engenharia de prompts, recuperação de contexto/grounding, JSON Schema, pipelines multiestágio, IA multimodal e geração de mídia em texto, imagem, áudio e vídeo, com fallback, auditoria e revisão humana."),
        ("FastAPI, Python, SQL, PostgreSQL, SQLite and FTS5; versioned sources, derived indexes, optimistic revision control, backups, migrations and explicit conflict handling.", "FastAPI, Python, SQL, PostgreSQL, SQLite and FTS5; AWS S3, EC2, Lambda, Glue/PySpark, Athena and QuickSight; versioned sources, derived indexes, revision control, backups, migrations and explicit conflict handling."),
        ("FastAPI, Python, SQL, PostgreSQL, SQLite e FTS5; fontes versionadas, índices derivados, controle otimista por revisão, backups, migrações e tratamento explícito de conflitos.", "FastAPI, Python, SQL, PostgreSQL, SQLite e FTS5; AWS S3, EC2, Lambda, Glue/PySpark, Athena e QuickSight; fontes versionadas, índices derivados, controle por revisão, backups, migrações e tratamento explícito de conflitos."),
        ("Mala Direta, Produção Operacional, Vesper Propostas, HelpDesk and the Operational Procurement Catalog demonstrate scale, adoption, deployment and business routines.", "Mala Direta, Produção Operacional, Vesper Propostas, HelpDesk and the Operational Procurement Catalog demonstrate recurring use, adoption, deployment, training and business routines."),
        ("Mala Direta, Produção Operacional, Vesper Propostas, HelpDesk e Catálogo Operacional de Compras comprovam escala, adoção, implantação e rotinas empresariais.", "Mala Direta, Produção Operacional, Vesper Propostas, HelpDesk e Catálogo Operacional de Compras comprovam uso recorrente, adoção, implantação, treinamento e rotinas empresariais."),
        ("Postagem Redes demonstrates AI and external APIs. Portal, still in development, demonstrates multi-tenant foundations, governance, sandbox Procurement and full-stack architecture without being presented as production.", "Postagem Redes demonstrates generative AI and external APIs. Portal demonstrates multi-tenant foundations and governance, with Procurement implemented in sandbox and current-head revalidation before a pilot."),
        ("Postagem Redes demonstra IA e APIs externas. Portal, ainda em desenvolvimento, demonstra fundação multiempresa, governança, Procurement em sandbox e arquitetura full-stack sem ser apresentado como produção.", "Postagem Redes demonstra IA generativa e APIs externas. Portal demonstra fundação multiempresa e governança, com Procurement implementado em sandbox e revalidação do head atual antes do piloto."),
        ("more than 10,000 production workflow executions; a campaign for more than 900 recipients; deployment to 11 workstations and a factory TV; HelpDesk with 11 users; proposals reduced from 2-4 minutes to under 30 seconds; a catalog used daily by three operational users; and Portal Procurement validated in sandbox.", "10,000+ executions across the production n8n environment; six campaigns over a 1,020-contact base; Produção Operacional on 10+ computers and one TV supporting 20+ professionals across nine areas; HelpDesk used by 11 users; proposals reduced from 2-4 minutes to under 30 seconds; a catalog with 24 categories and 480+ codes used daily by three users; and Portal Procurement under pre-pilot technical revalidation."),
        ("mais de 10 mil execuções de workflows em produção; campanha para mais de 900 destinatários; implantação em 11 computadores e uma TV; HelpDesk com 11 usuários; propostas de 2-4 minutos para menos de 30 segundos; catálogo usado diariamente por três usuários operacionais; e Procurement do Portal validado em sandbox.", "10 mil+ execuções na instância n8n de produção; seis campanhas sobre base de 1.020 contatos; Produção Operacional em 10+ computadores e uma TV, apoiando 20+ profissionais em nove setores; HelpDesk utilizado por 11 usuários; propostas de 2-4 minutos para menos de 30 segundos; catálogo com 24 categorias e 480+ códigos, usado diariamente por três usuários; e Procurement do Portal em revalidação técnica pré-piloto."),
        ('"Text-to-video",', '"Media generation","AWS","PySpark",'),
        ('"Text-to-video"', '"Media generation","AWS","PySpark"'),
    ]
    write(relative, apply_pairs(text, pairs))


def update_case(relative: str, pairs: list[tuple[str, str]]) -> None:
    write(relative, apply_pairs(read(relative), pairs))


def main() -> None:
    update_home("index.html", False)
    update_home("en/index.html", True)
    update_skills("competencias/index.html", False)
    update_skills("en/skills/index.html", True)

    update_case("cases/mala-direta/index.html", [
        ("<li>Primeira campanha com mais de 900 destinatários.</li><li>158 nós no workflow público principal.</li><li>Cancelamento corrigido para revalidar cada destinatário.</li>", "<li>Seis campanhas executadas sobre uma base de 1.020 contatos; uma delas com 900+ destinatários.</li><li>Dois workflows públicos, com 158 nós no principal e nove Data Tables de domínio.</li><li>Cancelamento corrigido para revalidar cada destinatário.</li>"),
        ("A evidência pública não contém credenciais, dados pessoais ou informações internas sensíveis.", "A instância n8n que hospeda esta e outras automações ultrapassou 10 mil execuções em produção; esse volume não é atribuído exclusivamente à Mala Direta. A evidência pública não contém credenciais ou dados pessoais."),
    ])
    update_case("en/cases/mala-direta/index.html", [
        ("<li>First campaign with more than 900 recipients.</li><li>158 nodes in the main public workflow.</li><li>Cancellation corrected to revalidate each recipient.</li>", "<li>Six campaigns executed over a 1,020-contact base; one included 900+ recipients.</li><li>Two public workflows, with 158 nodes in the main flow and nine domain Data Tables.</li><li>Cancellation corrected to revalidate each recipient.</li>"),
        ("The public evidence contains no credentials, personal data or sensitive internal information.", "The n8n environment hosting this and other automations has surpassed 10,000 production executions; that volume is not attributed exclusively to Mala Direta. The public evidence contains no credentials or personal data."),
    ])
    update_case("cases/producao-operacional/index.html", [
        ("<li>Implantado em 11 computadores do escritório e na TV da fábrica.</li><li>Modos Escritório, TV/Foco e Demonstração isolada.</li><li>Integração não move, renomeia nem apaga arquivos do NAS.</li>", "<li>Implantado em 10+ computadores e uma TV, apoiando 20+ profissionais em nove setores produtivos.</li><li>Modos Escritório, TV/Foco e Demonstração isolada, com treinamento e orientação aos usuários.</li><li>Integração agendada consulta novas OPs no NAS em modo somente leitura e não move, renomeia ou apaga arquivos.</li>"),
    ])
    update_case("en/cases/producao-operacional/index.html", [
        ("<li>Deployed on 11 office computers and the factory TV.</li><li>Office, TV/Focus and isolated Demonstration modes.</li><li>The integration does not move, rename or delete NAS files.</li>", "<li>Deployed on 10+ computers and one factory TV, supporting 20+ professionals across nine production areas.</li><li>Office, TV/Focus and isolated Demonstration modes, with user training and guidance.</li><li>Scheduled integration checks new orders on the NAS in read-only mode and does not move, rename or delete files.</li>"),
    ])
    update_case("cases/catalogo-operacional-compras/index.html", [
        ("Sistema interno usado diariamente por três usuários operacionais e consultado pela gestão para localizar materiais, fornecedores, preços e histórico sem depender da navegação manual entre abas e famílias de uma planilha.", "Sistema interno usado diariamente por três usuários operacionais e consultado pela gestão, construído sobre uma base histórica com 24 categorias e mais de 480 códigos de materiais."),
        ("https://github.com/Mayconxzdev/PlanilhaCompras", "https://github.com/Mayconxzdev/CatalogoOperacional"),
        ("A base interna foi construída a partir de uma planilha cultivada por aproximadamente dois anos, mas volumes, valores e fornecedores não são publicados.", "A base interna foi cultivada por aproximadamente dois anos. O portfólio publica apenas a escala estrutural - 24 categorias e 480+ códigos - sem divulgar valores, fornecedores ou históricos empresariais."),
        ("<li>Uso diário por três usuários operacionais e consulta pela gestão.</li><li>Busca rápida por código, nome ou fornecedor.</li><li>Conflito de edição, backups e testes reproduzíveis na versão pública.</li>", "<li>Base histórica com 24 categorias e 480+ códigos, usada diariamente por três usuários e consultada pela gestão.</li><li>Busca rápida por código, nome, especificação ou fornecedor.</li><li>Conflito de edição, backups e testes reproduzíveis na versão pública.</li>"),
    ])
    update_case("en/cases/operational-procurement-catalog/index.html", [
        ("Internal system used daily by three operational users and consulted by management to find materials, suppliers, prices and history without manually navigating spreadsheet tabs and product families.", "Internal system used daily by three operational users and consulted by management, built from a historical base with 24 categories and more than 480 material codes."),
        ("https://github.com/Mayconxzdev/PlanilhaCompras", "https://github.com/Mayconxzdev/CatalogoOperacional"),
        ("The internal base originated from a spreadsheet maintained for approximately two years, but volumes, values and suppliers are not published.", "The internal base was maintained for approximately two years. The portfolio publishes only its structural scale - 24 categories and 480+ codes - without company values, suppliers or purchasing history."),
        ("<li>Daily use by three operational users and management consultation.</li><li>Fast search by code, name or supplier.</li><li>Edit conflicts, backups and reproducible tests in the public release.</li>", "<li>Historical base with 24 categories and 480+ codes, used daily by three users and consulted by management.</li><li>Fast search by code, name, specification or supplier.</li><li>Edit conflicts, backups and reproducible tests in the public release.</li>"),
    ])
    update_case("cases/portal/index.html", [
        ("<p class=\"eyebrow\">O que já está comprovado na nova fundação</p><p>Tenancy e RLS no primeiro capability pack, Action Envelope versionado, aprovações imutáveis, idempotência, timeline, auditoria, outbox, RFQ, ofertas e comparação de fornecedores em sandbox.</p>", "<p class=\"eyebrow\">O que já foi implementado e exercitado</p><p>Tenancy e RLS no primeiro capability pack, Action Envelope versionado, aprovações imutáveis, idempotência, timeline, auditoria, outbox, RFQ, ofertas e comparação de fornecedores em sandbox. O head atual está em revalidação.</p>"),
        ("<li>Procurement Intake e sourcing implementados e validados em sandbox.</li>", "<li>Procurement Intake e sourcing implementados e exercitados anteriormente em sandbox; revalidação do head atual em andamento.</li>"),
        ("Em preparação para piloto interno; ainda não apresentado como produção multiempresa.", "Piloto interno condicionado à conclusão da revalidação técnica; ainda não apresentado como produção multiempresa."),
    ])
    update_case("en/cases/portal/index.html", [
        ("<p class=\"eyebrow\">What is already demonstrated in the new foundation</p><p>Tenancy and RLS in the first capability pack, versioned Action Envelopes, immutable approvals, idempotency, timeline, auditing, outbox, RFQs, offers and supplier comparison in sandbox.</p>", "<p class=\"eyebrow\">What has been implemented and exercised</p><p>Tenancy and RLS in the first capability pack, versioned Action Envelopes, immutable approvals, idempotency, timeline, auditing, outbox, RFQs, offers and supplier comparison in sandbox. The current head is being revalidated.</p>"),
        ("<li>Procurement Intake and sourcing implemented and validated in sandbox.</li>", "<li>Procurement Intake and sourcing implemented and previously exercised in sandbox; current-head revalidation is underway.</li>"),
        ("Being prepared for an internal pilot; not presented as multi-tenant production.", "The internal pilot depends on completing technical revalidation; the product is not presented as multi-tenant production."),
    ])
    update_case("cases/compass/index.html", [
        ("<article><span>01</span><h2>Contexto e problema</h2><p>Construir base prática em dados, automação, nuvem e documentação.</p></article>", "<article><span>01</span><h2>Contexto e objetivo</h2><p>Programa de seis meses e dez sprints para evoluir dos fundamentos de Git, Linux e SQL até um pipeline analítico completo em AWS.</p></article>"),
        ("<article><span>02</span><h2>O que eu fiz</h2><p>Execução das sprints, projetos, documentação e repositório público solicitado pelo programa.</p></article>", "<article><span>02</span><h2>O que eu fiz</h2><p>Implementei exercícios e desafios com Python, Pandas/Polars, SQL, Docker, boto3, ingestão de arquivos e API TMDB, além de documentação e evidências por sprint.</p></article>"),
        ("<article><span>03</span><h2>Como construí</h2><p>Python, SQL, Docker, AWS S3/EC2/Lambda/Glue/Athena e pipelines de dados.</p></article>", "<article><span>03</span><h2>Como construí</h2><p>Dados passaram por Raw, Trusted e Refined no S3; Lambda/boto3 cuidaram da ingestão, Glue/PySpark transformou CSV e JSON em Parquet, Athena consultou e QuickSight apresentou os resultados.</p></article>"),
        ("<article><span>04</span><h2>O que ficou comprovado</h2><ul><li>Programa concluído com 10 sprints.</li></ul></article>", "<article><span>04</span><h2>O que ficou comprovado</h2><ul><li>Dez sprints concluídas entre out. 2024 e mar. 2025.</li><li>Pipeline público com ingestão CSV/API, S3, Lambda, Glue/PySpark, Parquet, Athena e QuickSight.</li><li>Experiência histórica de formação, não apresentada como ambiente de produção.</li></ul></article>"),
    ])
    update_case("en/cases/compass/index.html", [
        ("<article><span>01</span><h2>Context and problem</h2><p>Build a practical foundation in data, automation, cloud and documentation.</p></article>", "<article><span>01</span><h2>Context and objective</h2><p>A six-month, ten-sprint program progressing from Git, Linux and SQL fundamentals to a complete analytical pipeline on AWS.</p></article>"),
        ("<article><span>02</span><h2>What I did</h2><p>Sprint execution, projects, documentation and the public repository required by the program.</p></article>", "<article><span>02</span><h2>What I did</h2><p>Implemented exercises and challenges with Python, Pandas/Polars, SQL, Docker, boto3, file and TMDB API ingestion, plus documentation and evidence for each sprint.</p></article>"),
        ("<article><span>03</span><h2>How I built it</h2><p>Python, SQL, Docker, AWS S3/EC2/Lambda/Glue/Athena and data pipelines.</p></article>", "<article><span>03</span><h2>How I built it</h2><p>Data moved through Raw, Trusted and Refined layers in S3; Lambda/boto3 handled ingestion, Glue/PySpark transformed CSV and JSON into Parquet, Athena queried it and QuickSight presented the results.</p></article>"),
        ("<article><span>04</span><h2>What is demonstrated</h2><ul><li>Program completed with 10 sprints.</li></ul></article>", "<article><span>04</span><h2>What is demonstrated</h2><ul><li>Ten sprints completed between Oct. 2024 and Mar. 2025.</li><li>Public pipeline with CSV/API ingestion, S3, Lambda, Glue/PySpark, Parquet, Athena and QuickSight.</li><li>Historical learning experience, not presented as a production environment.</li></ul></article>"),
    ])
    update_case("cases/helpdesk/index.html", [("Portal Vesper", "Portal")])
    update_case("en/cases/helpdesk/index.html", [("Portal Vesper", "Portal")])


if __name__ == "__main__":
    main()
