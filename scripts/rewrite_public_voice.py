from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMON = {
    "Text-to-video": "Geração de mídia",
    "text-to-video": "geração de mídia",
    "Leitura rápida para recrutadores": "Visão geral",
    "Resumo para avaliação técnica": "Visão técnica",
    "Caminho de revisão em cinco minutos": "Pontos principais",
    "Como avaliar sem depender de dados reais": "Roteiro de uso",
    "O que este projeto demonstra": "O que desenvolvi",
    "O que este repositório comprova": "O que aprendi e desenvolvi",
    "O que ficou comprovado": "Resultados e aprendizados",
    "Competências demonstradas": "Competências e tecnologias",
    "Evidências atualmente confirmadas": "Resultados atuais",
    "Projetos recomendados para avaliação": "Projetos principais",
    "Critérios de evidência": "Como mantenho as informações atualizadas",
    "Qualidade publicada": "Qualidade e validação",
    "Índice de evidências": "Índice do projeto",
    "Evidências do case": "Detalhes do projeto",
    "EVIDÊNCIAS DO CASE": "DETALHES DO PROJETO",
    "Evidências técnicas": "Detalhes técnicos",
    "evidência técnica": "detalhes técnicos",
    "evidência pública": "material público",
    "tipo de prova": "forma de validação",
    "Estado comprovado": "Estado atual",
    "PROVA OPERACIONAL": "ONDE APLIQUEI NA ROTINA",
    "PROVA DE AMPLITUDE": "OUTROS CONTEXTOS",
    "PROVAS EM CONTEXTO": "RESULTADOS EM USO",
    "SISTEMAS PRIORITÁRIOS": "PROJETOS PRINCIPAIS",
    "COMPETÊNCIAS DEMONSTRADAS": "COMPETÊNCIAS E EXPERIÊNCIA PRÁTICA",
    "COMPETÊNCIA → PROVA": "COMPETÊNCIAS NA PRÁTICA",
    "Números ligados a sistemas em uso - não a marketing.": "Alguns números da minha atuação atual.",
    "Números que apontam para sistemas em uso — não para marketing.": "Alguns números da minha atuação atual.",
    "Cada indicador pertence ao sistema ou ambiente que o sustenta. Valores operacionais podem evoluir com o uso.": "Os números vêm de sistemas e rotinas que desenvolvi ou administro e podem evoluir conforme o uso.",
    "Cada indicador é contextualizado no case correspondente. Valores operacionais podem evoluir com o uso.": "Cada número está ligado ao projeto correspondente e pode evoluir conforme o uso.",
    "Seis entregas para entender meu valor em poucos minutos.": "Projetos que mostram diferentes partes do meu trabalho.",
    "A seleção equilibra evidência operacional e amplitude técnica. Cada case declara estado real, resultado, limitações e tipo de prova.": "Reuni projetos de automação, sistemas internos, integrações, IA e arquitetura. Em cada um, explico o que fiz, o resultado e o estado atual.",
    "Automação, IA, dados e governança com evidência.": "Automação, IA, dados e governança aplicados em projetos reais.",
    "Para uma avaliação rápida, baixe o currículo. Para aprofundar, abra um dos cases e use o GitHub como evidência técnica.": "O currículo resume minha experiência, e os cases mostram com mais detalhes como desenvolvi cada solução.",
    "Portfólio bilíngue projetado para avaliação rápida de RH e exploração técnica profunda, sem missões fictícias ou métricas inventadas.": "Portfólio bilíngue que reúne meus projetos, resultados, decisões técnicas e limites atuais.",
    "Recruiter overview": "Overview",
    "Technical review summary": "Technical overview",
    "Five-minute review path": "Main areas",
    "What this project demonstrates": "What I built",
    "What this repository demonstrates": "What I learned and built",
    "What is demonstrated": "Results and learning",
    "What was demonstrated": "Results and learning",
    "Skills demonstrated": "Skills and technologies",
    "Two-minute evaluation": "Try the application",
    "Currently verified evidence": "Current results",
    "Projects recommended for evaluation": "Main projects",
    "Evidence criteria": "How I keep information current",
    "Published quality": "Quality and validation",
    "Evidence index": "Project index",
    "Case evidence": "Project details",
    "CASE EVIDENCE": "PROJECT DETAILS",
    "Technical evidence": "Technical details",
    "technical evidence": "technical details",
    "public evidence": "public material",
    "evidence type": "validation method",
    "Demonstrated status": "Current status",
    "OPERATIONAL EVIDENCE": "WHERE I USE IT IN PRACTICE",
    "BREADTH EVIDENCE": "OTHER CONTEXTS",
    "EVIDENCE IN CONTEXT": "RESULTS IN USE",
    "PRIORITY SYSTEMS": "MAIN PROJECTS",
    "DEMONSTRATED SKILLS": "SKILLS AND PRACTICAL EXPERIENCE",
    "SKILL → EVIDENCE": "SKILLS IN PRACTICE",
    "Numbers tied to systems in use - not marketing.": "A few numbers from my current work.",
    "Numbers that point to systems in use — not marketing.": "A few numbers from my current work.",
    "Each indicator belongs to the system or environment that supports it. Operational values may evolve with usage.": "The numbers come from systems and routines I built or administer and may change as usage grows.",
    "Each indicator is contextualized in its corresponding case. Operational values may evolve with usage.": "Each number is linked to its project and may change as usage grows.",
    "Six deliveries that show my value in a few minutes.": "Projects that show different parts of my work.",
    "The selection balances operational evidence and technical breadth. Every case states its real status, outcome, limitations and evidence type.": "I selected projects across automation, internal systems, integrations, AI and architecture. Each case explains what I built, the result and its current state.",
    "Automation, AI, data and governance with evidence.": "Automation, AI, data and governance applied in real projects.",
    "For a quick evaluation, download the resume. To go deeper, open a case and use GitHub as technical evidence.": "The resume summarizes my experience, while the cases show how I built each solution in more detail.",
    "Bilingual portfolio designed for quick HR evaluation and deep technical exploration, without fictional missions or invented metrics.": "Bilingual portfolio bringing together my projects, results, technical decisions and current limits.",
}


def main() -> None:
    changed = 0
    for path in sorted(ROOT.rglob("*.html")):
        if "artifacts" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        for old, new in COMMON.items():
            text = text.replace(old, new)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1
            print(f"public voice updated: {path.relative_to(ROOT)}")
    print(f"public voice updated in {changed} files")


if __name__ == "__main__":
    main()
