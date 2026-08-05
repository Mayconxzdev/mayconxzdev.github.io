from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    ROOT / "index.html": {
        '<meta name="description" content="Automação, IA e integrações que saíram da ideia e entraram na rotina. Cases reais de n8n, Python, APIs, sistemas internos e IA aplicada.">':
            '<meta name="description" content="Analista de Automação, IA e Integrações. Cases reais de n8n, Python, APIs REST, IA generativa, agentes, sistemas internos e resultados mensuráveis.">',
        '<meta property="og:description" content="Automação, IA e integrações que saíram da ideia e entraram na rotina. Cases reais de n8n, Python, APIs, sistemas internos e IA aplicada.">':
            '<meta property="og:description" content="Analista de Automação, IA e Integrações. Cases reais de n8n, Python, APIs REST, IA generativa, agentes, sistemas internos e resultados mensuráveis.">',
        '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Person", "name": "Maycon da Silva Ferreira", "jobTitle": "Automation, AI and Integrations Analyst", "url": "https://mayconxzdev.github.io/", "sameAs": ["https://github.com/Mayconxzdev", "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"], "knowsAbout": ["n8n", "Python", "REST APIs", "Process Automation", "Applied AI", "Systems Integration"]}</script>':
            '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Maycon da Silva Ferreira","jobTitle":"Analista de Automação, IA e Integrações","url":"https://mayconxzdev.github.io/","sameAs":["https://github.com/Mayconxzdev","https://www.linkedin.com/in/maycon-ferreira-7bb870231/"],"knowsAbout":["n8n","Automação low-code","Automação de processos","Mapeamento de processos","AS-IS/TO-BE","IA generativa","Agentes de IA","Codex","Engenharia de prompts","Recuperação de contexto","Grounding","JSON Schema","IA multimodal","Text-to-video","Integração de sistemas","APIs REST","Webhooks","Python","JavaScript","TypeScript","Node.js","Express","FastAPI","PostgreSQL","Docker","CI/CD","Idempotência"]}</script>',
        '    <a href="#evidence">Evidências</a>\n    <a href="#contact">Contato</a>':
            '    <a href="#evidence">Evidências</a>\n    <a href="competencias/">Competências</a>\n    <a href="#contact">Contato</a>',
        '<p class="eyebrow">REGISTRO DE SISTEMAS EM OPERAÇÃO · 2026</p>':
            '<p class="eyebrow">ANALISTA DE AUTOMAÇÃO, IA E INTEGRAÇÕES · 2026</p>',
        '<p class="hero-statement">Automação, IA e integrações que deixam de ser ideia e passam a fazer parte do trabalho.</p>':
            '<p class="hero-statement">Automação de processos, IA generativa e integrações que entram na rotina com regras, evidência e sustentação.</p>',
        '<p class="hero-body">Transformo necessidades operacionais em automações, integrações e sistemas internos usados de verdade. Trabalho do entendimento do processo à implantação, documentação, monitoramento e sustentação.</p>':
            '<p class="hero-body">Transformo necessidades operacionais em automações e sistemas internos em produção. Atuo do levantamento à sustentação com n8n, Python, APIs REST e IA generativa, apoiado por métricas públicas e revisão humana.</p>',
        '<dl class="profile-direction"><div><dt>Atuação atual</dt><dd>Automação, IA e integrações em sistemas internos</dd></div><div><dt>Prática</dt><dd>n8n · Python · APIs REST · FastAPI · SQL · Docker</dd></div>':
            '<dl class="profile-direction"><div><dt>Posicionamento</dt><dd>Analista de Automação, IA e Integrações</dd></div><div><dt>Prática</dt><dd>n8n · Python · APIs REST · SQL · Docker · IA generativa</dd></div>',
        '<strong>Automação de Processos por RPA</strong><span>ENAP · 25h</span>':
            '<strong>Automação de Processos através da RPA</strong><span>ENAP · 25h</span>',
        '<strong>Mapeamento e Automação de Processos</strong><span>ENAP · 20h</span>':
            '<strong>Fundamentos da Transformação Digital: Mapeamento e Automação de Processos</strong><span>ENAP · 20h</span>',
        '<strong>Trilha n8n e Workflows</strong><span>DIO · 8h / 4 cursos</span>':
            '<strong>Trilha n8n e Workflows</strong><span>DIO · 4h / 4 cursos</span>',
    },
    ROOT / "en" / "index.html": {
        '<meta name="description" content="Automation, AI and integrations that moved from an idea into daily operations. Real cases involving n8n, Python, APIs, internal systems and applied AI.">':
            '<meta name="description" content="AI Automation and Integrations Analyst. Real cases involving n8n, Python, REST APIs, generative AI, agents, internal systems and measurable outcomes.">',
        '<meta property="og:description" content="Automation, AI and integrations that moved from an idea into daily operations. Real cases involving n8n, Python, APIs, internal systems and applied AI.">':
            '<meta property="og:description" content="AI Automation and Integrations Analyst. Real cases involving n8n, Python, REST APIs, generative AI, agents, internal systems and measurable outcomes.">',
        '<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Person", "name": "Maycon da Silva Ferreira", "jobTitle": "Automation, AI and Integrations Analyst", "url": "https://mayconxzdev.github.io/", "sameAs": ["https://github.com/Mayconxzdev", "https://www.linkedin.com/in/maycon-ferreira-7bb870231/"], "knowsAbout": ["n8n", "Python", "REST APIs", "Process Automation", "Applied AI", "Systems Integration"]}</script>':
            '<script type="application/ld+json">{"@context":"https://schema.org","@type":"Person","name":"Maycon da Silva Ferreira","jobTitle":"AI Automation & Integrations Analyst","url":"https://mayconxzdev.github.io/","sameAs":["https://github.com/Mayconxzdev","https://www.linkedin.com/in/maycon-ferreira-7bb870231/"],"knowsAbout":["n8n","Low-code automation","Process automation","Process mapping","AS-IS/TO-BE","Generative AI","AI agents","Codex","Prompt engineering","Context retrieval","Grounding","JSON Schema","Multimodal AI","Text-to-video","Systems integration","REST APIs","Webhooks","Python","JavaScript","TypeScript","Node.js","Express","FastAPI","PostgreSQL","Docker","CI/CD","Idempotency"]}</script>',
        '    <a href="#evidence">Evidence</a>\n    <a href="#contact">Contact</a>':
            '    <a href="#evidence">Evidence</a>\n    <a href="skills/">Skills</a>\n    <a href="#contact">Contact</a>',
        '<p class="eyebrow">SYSTEMS IN OPERATION · 2026</p>':
            '<p class="eyebrow">AI AUTOMATION &amp; INTEGRATIONS ANALYST · 2026</p>',
        '<p class="hero-statement">Automation, AI and integrations that moved from an idea into daily operations.</p>':
            '<p class="hero-statement">Process automation, generative AI and integrations built for real operations, with explicit rules, evidence and support.</p>',
        '<p class="hero-body">I turn operational needs into automations, integrations and internal systems people actually use. I own the complete technical cycle: requirements, architecture, development, deployment, documentation, training, monitoring and support.</p>':
            '<p class="hero-body">I turn operational needs into production automations and internal systems. I work from discovery through support with n8n, Python, REST APIs and generative AI, backed by public metrics and human review.</p>',
        '<dl class="profile-direction"><div><dt>Current focus</dt><dd>Automation, AI and integrations for internal systems</dd></div><div><dt>Practice</dt><dd>n8n · Python · REST APIs · FastAPI · SQL · Docker</dd></div>':
            '<dl class="profile-direction"><div><dt>Positioning</dt><dd>AI Automation &amp; Integrations Analyst</dd></div><div><dt>Practice</dt><dd>n8n · Python · REST APIs · SQL · Docker · Generative AI</dd></div>',
        '<strong>Ferramentas de IA: Agentes e Automações</strong><span>FIRJAN SENAI · 40h</span>':
            '<strong>AI Tools: Agents and Automations</strong><span>FIRJAN SENAI · 40h</span>',
        '<strong>Automação de Processos por RPA</strong><span>ENAP · 25h</span>':
            '<strong>Process Automation through RPA</strong><span>ENAP · 25h</span>',
        '<strong>Mapeamento e Automação de Processos</strong><span>ENAP · 20h</span>':
            '<strong>Digital Transformation Fundamentals: Process Mapping and Automation</strong><span>ENAP · 20h</span>',
        '<strong>IA no Contexto do Serviço Público</strong><span>ENAP · 20h</span>':
            '<strong>AI in the Public Service Context</strong><span>ENAP · 20h</span>',
        '<strong>Introdução à LGPD</strong><span>ENAP · 10h</span>':
            '<strong>Introduction to Brazil\'s Data Protection Law</strong><span>ENAP · 10h</span>',
        '<strong>Trilha n8n e Workflows</strong><span>DIO · 8h / 4 cursos</span>':
            '<strong>n8n and Workflows Learning Path</strong><span>DIO · 4h / 4 courses</span>',
    },
}


def normalize(path: Path, replacements: dict[str, str]) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in replacements.items():
        if old in text:
            text = text.replace(old, new)
        elif new not in text:
            raise RuntimeError(f"Expected portfolio text not found in {path.relative_to(ROOT)}: {old}")
    if text == original:
        print(f"unchanged: {path.relative_to(ROOT)}")
        return False
    path.write_text(text, encoding="utf-8")
    print(f"normalized: {path.relative_to(ROOT)}")
    return True


def main() -> None:
    for path, replacements in REPLACEMENTS.items():
        normalize(path, replacements)


if __name__ == "__main__":
    main()
