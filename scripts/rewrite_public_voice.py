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
    "tipo de prova": "o que está público",
    "Tipo de prova": "O que está público",
    "Estado comprovado": "Estado atual",
    "PROVA OPERACIONAL": "ONDE APLIQUEI NA ROTINA",
    "PROVA DE AMPLITUDE": "OUTROS CONTEXTOS",
    "PROVAS EM CONTEXTO": "RESULTADOS EM USO",
    "PROVAS VISUAIS": "TELAS E FLUXOS",
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
    "A material público não contém credenciais, dados pessoais ou informações internas sensíveis.": "A versão pública não contém credenciais, dados pessoais ou informações internas sensíveis.",
    "A evidência pública não contém credenciais, dados pessoais ou informações internas sensíveis.": "A versão pública não contém credenciais, dados pessoais ou informações internas sensíveis.",
    "Aplicação privada: material público é a arquitetura declarada, não uma captura de interface.": "Como a aplicação é privada, publico apenas a arquitetura e o fluxo — não capturas da interface interna.",
    "Aplicação privada: a evidência pública é a arquitetura declarada, não uma captura de interface.": "Como a aplicação é privada, publico apenas a arquitetura e o fluxo — não capturas da interface interna.",
    "Telas, fluxos e referências selecionados para mostrar o sistema em uso — sem substituir evidência por decoração.": "Telas e fluxos que mostram como o sistema funciona na prática.",
    "Veja o sistema em contexto": "Veja o sistema em uso",
    "O que esta galeria mostra": "Sobre as imagens",
    "A seleção prioriza telas reais, cópias sanitizadas ou fluxos técnicos declarados, sempre com o contexto indicado na legenda.": "As imagens abaixo mostram o produto real ou reconstruções sanitizadas. Quando algo não é uma captura direta, isso fica indicado na própria legenda.",
    "Imagem selecionada como evidência visual do case.": "Tela do produto em execução.",
    "Limite público": "Limites da versão pública",
    "O que este case não mostra": "Limites desta versão",
    "Se a operação crescesse": "Próximos passos",
    "Conteúdo baseado em sistemas reais, versões sanitizadas e limites declarados.": "Projetos reais, versões públicas sanitizadas e limites explicados com clareza.",
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
    "evidence type": "what is public",
    "Evidence type": "What is public",
    "Demonstrated status": "Current status",
    "OPERATIONAL EVIDENCE": "WHERE I USE IT IN PRACTICE",
    "BREADTH EVIDENCE": "OTHER CONTEXTS",
    "EVIDENCE IN CONTEXT": "RESULTS IN USE",
    "VISUAL EVIDENCE": "SCREENS AND FLOWS",
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
    "Public evidence contains no credentials, personal data or sensitive internal information.": "The public version contains no credentials, personal data or sensitive internal information.",
    "Private application: public material is the declared architecture, not an interface capture.": "This is a private application, so I only publish the architecture and flow — not screenshots of the internal interface.",
    "Screens, flows and references selected to show the system in use — without replacing evidence with decoration.": "Screens and flows that show how the system works in practice.",
    "See the system in context": "See the system in use",
    "What this gallery shows": "About the images",
    "The selection prioritizes real screens, sanitized copies or declared technical flows, always with context indicated in the caption.": "The images below show the real product or sanitized reconstructions. When something is not a direct capture, the caption says so.",
    "Image selected as visual evidence for this case.": "Screen from the running product.",
    "Public limit": "Public version limits",
    "What this case does not show": "Limits of this version",
    "If the operation grew": "Next steps",
    "Content based on real systems, sanitized releases and declared limitations.": "Real projects, sanitized public versions and clear limitations.",
    "Utilizo OpenAI, Gemini, Ollama, OpenRouter e Codex para criação assistida, análise, classificação, recuperação de contexto e geração de mídia em texto, imagem, áudio e vídeo. Estruturo prompts, JSON Schema, fallbacks, etapas de auditoria e revisão humana.": "Utilizo OpenAI, Gemini, Ollama, OpenRouter e Codex em criação assistida, análise, classificação e recuperação de contexto. Em projetos de mídia, trabalho com texto, imagem e áudio, sempre com revisão humana e fallbacks quando a integração permite.",
    "OpenAI · Gemini · Ollama · OpenRouter · Codex · APIs de LLM · engenharia de prompts · grounding · JSON Schema · IA multimodal · geração de mídia": "OpenAI · Gemini · Ollama · OpenRouter · Codex · APIs de LLM · prompts · grounding · JSON Schema · IA multimodal",
    "I use OpenAI, Gemini, Ollama, OpenRouter and Codex for assisted creation, analysis, classification, context retrieval and media generation across text, image, audio and video. I structure prompts, JSON Schema outputs, fallbacks, audit stages and human review.": "I use OpenAI, Gemini, Ollama, OpenRouter and Codex for assisted creation, analysis, classification and context retrieval. In media projects, I work with text, image and audio, with human review and fallbacks when the integration supports them.",
    "OpenAI · Gemini · Ollama · OpenRouter · Codex · LLM APIs · prompt engineering · grounding · JSON Schema · multimodal AI · media generation": "OpenAI · Gemini · Ollama · OpenRouter · Codex · LLM APIs · prompts · grounding · JSON Schema · multimodal AI",
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
