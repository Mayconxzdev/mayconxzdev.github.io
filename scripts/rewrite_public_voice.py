from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PT_REPLACEMENTS = {
    "PROVAS EM CONTEXTO": "RESULTADOS EM USO",
    "Números ligados a sistemas em uso - não a marketing.": "Alguns números da minha atuação atual.",
    "Números que apontam para sistemas em uso — não para marketing.": "Alguns números da minha atuação atual.",
    "Cada indicador pertence ao sistema ou ambiente que o sustenta. Valores operacionais podem evoluir com o uso.": "Os números abaixo vêm de sistemas e rotinas que desenvolvi ou administro. Eles podem evoluir conforme o uso.",
    "Cada indicador é contextualizado no case correspondente. Valores operacionais podem evoluir com o uso.": "Cada número está ligado ao projeto correspondente e pode evoluir conforme o uso.",
    "SISTEMAS PRIORITÁRIOS": "PROJETOS PRINCIPAIS",
    "Seis entregas para entender meu valor em poucos minutos.": "Projetos que mostram diferentes partes do meu trabalho.",
    "A seleção equilibra evidência operacional e amplitude técnica. Cada case declara estado real, resultado, limitações e tipo de prova.": "Reuni projetos de automação, sistemas internos, integrações, IA e arquitetura. Em cada um, explico o que fiz, o resultado e o estado atual.",
    "COMPETÊNCIAS DEMONSTRADAS": "COMPETÊNCIAS E EXPERIÊNCIA PRÁTICA",
    "Automação, IA, dados e governança com evidência.": "Automação, IA, dados e governança aplicados em projetos reais.",
    "As competências abaixo estão ligadas a sistemas em produção, uso interno, pilotos, referências arquiteturais e protótipos privados. O estado de cada entrega é declarado para não confundir implementação, teste, sandbox, piloto e produção.": "Abaixo estão as tecnologias e práticas que aplico em sistemas internos, automações, projetos públicos e produtos em desenvolvimento. Em cada case, informo o estado atual e os limites da entrega.",
    "PROVA OPERACIONAL": "ONDE APLIQUEI NA ROTINA",
    "PROVA DE AMPLITUDE": "OUTROS CONTEXTOS",
    "Principais evidências:": "Alguns resultados:",
    "Para uma avaliação rápida, baixe o currículo. Para aprofundar, abra um dos cases e use o GitHub como evidência técnica.": "O currículo resume minha experiência, e os cases mostram com mais detalhes como desenvolvi cada solução.",
    "Portfólio bilíngue projetado para avaliação rápida de RH e exploração técnica profunda, sem missões fictícias ou métricas inventadas.": "Portfólio bilíngue que reúne meus principais projetos, resultados, decisões técnicas e limites atuais.",
    "Leitura rápida para recrutadores": "Visão geral",
    "Resumo para avaliação técnica": "Visão técnica",
    "Caminho de revisão em cinco minutos": "Pontos principais",
    "O que este projeto demonstra": "O que desenvolvi",
    "O que este repositório comprova": "O que aprendi e desenvolvi",
    "Competências demonstradas": "Competências e tecnologias",
    "Como avaliar sem depender de dados reais": "Roteiro de uso",
    "Evidências atualmente confirmadas": "Resultados atuais",
    "Projetos recomendados para avaliação": "Projetos principais",
    "Critérios de evidência": "Como mantenho as informações atualizadas",
    "Qualidade publicada": "Qualidade e validação",
    "evidência operacional e amplitude técnica": "uso real e variedade técnica",
    "evidência técnica": "detalhes técnicos",
    "tipo de prova": "forma de validação",
    "com regras, evidência e sustentação": "com regras claras, revisão humana e sustentação",
    "apoiado por métricas públicas e revisão humana": "com acompanhamento de uso, revisão humana e melhoria contínua",
    "Meu cargo formal aparece sem alteração. O escopo funcional é demonstrado por sistemas implantados, usuários, treinamento e sustentação.": "Na prática, trabalho diretamente com gestão e usuários, desde o levantamento até a implantação, treinamento e sustentação.",
    "Responsabilidade técnica com contato direto com a operação.": "Atuação próxima da operação, do levantamento à sustentação.",
    "Inglês técnico para leitura; escrita e conversação básicas": "Inglês básico; leitura independente de documentação técnica, escrita e conversação básicas",
    "Text-to-video": "Geração de mídia",
    "text-to-video": "geração de mídia",
}

EN_REPLACEMENTS = {
    "EVIDENCE IN CONTEXT": "RESULTS IN USE",
    "Numbers tied to systems in use - not marketing.": "A few numbers from my current work.",
    "Numbers that point to systems in use — not marketing.": "A few numbers from my current work.",
    "Each indicator belongs to the system or environment that supports it. Operational values may evolve with usage.": "The numbers below come from systems and routines I built or administer. They may change as usage grows.",
    "Each indicator is contextualized in its corresponding case. Operational values may evolve with usage.": "Each number is linked to its project and may change as usage grows.",
    "PRIORITY SYSTEMS": "MAIN PROJECTS",
    "Six deliveries that show my value in a few minutes.": "Projects that show different parts of my work.",
    "The selection balances operational evidence and technical breadth. Every case states its real status, outcome, limitations and evidence type.": "I selected projects across automation, internal systems, integrations, AI and architecture. Each case explains what I built, the result and its current state.",
    "DEMONSTRATED SKILLS": "SKILLS AND PRACTICAL EXPERIENCE",
    "Automation, AI, data and governance with evidence.": "Automation, AI, data and governance applied in real projects.",
    "The skills below are connected to production systems, internal use, pilots, architectural references and private prototypes. Each delivery state is declared to distinguish implementation, testing, sandbox, pilot and production.": "Below are technologies and practices I use across internal systems, automations, public projects and products in development. Each case states its current status and limits.",
    "OPERATIONAL EVIDENCE": "WHERE I USE IT IN PRACTICE",
    "BREADTH EVIDENCE": "OTHER CONTEXTS",
    "Main evidence:": "A few results:",
    "For a quick evaluation, download the resume. To go deeper, open a case and use GitHub as technical evidence.": "The resume summarizes my experience, while the cases show how I built each solution in more detail.",
    "Bilingual portfolio designed for quick HR evaluation and deep technical exploration, without fictional missions or invented metrics.": "Bilingual portfolio bringing together my main projects, results, technical decisions and current limits.",
    "Recruiter overview": "Overview",
    "Technical review summary": "Technical overview",
    "Five-minute review path": "Main areas",
    "What this project demonstrates": "What I built",
    "What this repository demonstrates": "What I learned and built",
    "Skills demonstrated": "Skills and technologies",
    "Two-minute evaluation": "Try the application",
    "Currently verified evidence": "Current results",
    "Projects recommended for evaluation": "Main projects",
    "Evidence criteria": "How I keep the information current",
    "Published quality": "Quality and validation",
    "technical evidence": "technical details",
    "evidence type": "validation method",
    "with explicit rules, evidence and support": "with clear rules, human review and support",
    "backed by public metrics and human review": "with usage monitoring, human review and continuous improvement",
    "My formal role is shown unchanged. Functional scope is demonstrated through deployed systems, users, training and support.": "In practice, I work directly with management and users from discovery through deployment, training and support.",
    "Technical ownership with direct contact with operations.": "Close involvement with operations, from discovery through support.",
    "Technical English for reading; basic writing and conversation": "Basic English; independent technical-documentation reading, basic writing and conversation",
    "Text-to-video": "Media generation",
    "text-to-video": "media generation",
}


def apply(path: Path, replacements: dict[str, str]) -> None:
    text = path.read_text(encoding="utf-8")
    original = text
    for old, new in replacements.items():
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"public voice updated: {path.relative_to(ROOT)}")
    else:
        print(f"public voice already current: {path.relative_to(ROOT)}")


def main() -> None:
    for path in sorted(ROOT.rglob("*.html")):
        relative = path.relative_to(ROOT)
        if "artifacts" in relative.parts:
            continue
        apply(path, EN_REPLACEMENTS if relative.parts and relative.parts[0] == "en" else PT_REPLACEMENTS)


if __name__ == "__main__":
    main()
