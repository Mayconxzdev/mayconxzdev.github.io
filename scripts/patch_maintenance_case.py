from pathlib import Path
import runpy
root=Path(__file__).resolve().parents[1]

def patch(rel,pairs):
    p=root/rel; t=p.read_text(encoding='utf-8')
    for old,new in pairs:
        if old not in t: raise RuntimeError(f'{rel}: missing source phrase')
        t=t.replace(old,new,1)
    p.write_text(t,encoding='utf-8')

patch('cases/vesper-manutencao/index.html',[
('Documentos, áudios, busca e IA assistiva','Ativos, checklists, evidências e rastreabilidade'),
('Desenvolvi um sistema privado para organizar materiais técnicos, registrar histórico e permitir consultas com respostas ligadas às fontes utilizadas.','Digitalizei um processo antes dependente de planilhas, pastas de rede, papel e memória das pessoas, criando uma fonte central para registrar e consultar a manutenção dos equipamentos.'),
('<div><span>Estado</span><b>Sistema privado em evolução</b></div><div><span>Tecnologias</span><b>FastAPI · React · SQLite FTS5 · Whisper · Ollama</b></div><div><span>Minha atuação</span><b>Produto · arquitetura · backend · frontend · IA · segurança</b></div>','<div><span>Uso atual</span><b>2 responsáveis registram · Qualidade consulta</b></div><div><span>Escopo</span><b>40+ ativos/equipamentos</b></div><div><span>Foco</span><b>Rastreabilidade · evidência · histórico</b></div>'),
('Conhecimento de manutenção ficava distribuído entre documentos, áudios, mensagens e experiência individual.','O processo dependia de planilhas, arquivos em rede, papel e memória. Localizar o ativo, comprovar uma execução ou recuperar histórico exigia trabalho manual.'),
('Ingestão de documentos e áudio, transcrição opcional, busca, histórico, equipamentos, eventos e consulta assistida por IA.','Fluxo por ativo com código/TAG/nome, checklist, data/hora, responsável, fotos, observações, evidências e histórico enviado ao servidor.'),
('FastAPI organiza a API; React entrega a interface; SQLite FTS5 mantém a busca; Whisper e Ollama são integrações opcionais.','Alterações preservam autor e valor anterior/novo; novas manutenções não apagam execuções anteriores. O histórico permanece consultável para acompanhamento e Qualidade.'),
('O projeto continua privado e em evolução. O case público mostra somente a arquitetura, os fluxos e os limites.','O sistema privado está em uso. Dois responsáveis registram as manutenções executadas e a Qualidade consulta o histórico; 40+ ativos são acompanhados.'),
])

patch('en/cases/vesper-manutencao/index.html',[
('AI-assisted technical knowledge','Assets, checklists, evidence and traceability'),
('Private system to centralize maintenance, documents, audio, history and technical-information search.','I digitized a process previously dependent on spreadsheets, network folders, paper and individual memory, creating a central source for equipment-maintenance records.'),
('<div><span>State</span><b>CONFIDENTIAL CASE</b></div><div><span>Technologies</span><b>FastAPI · React · SQLite FTS5 · Whisper · PWA</b></div><div><span>What is public</span><b>Confidential case with sanitized architecture</b></div>','<div><span>Current use</span><b>2 responsible users record · Quality reviews</b></div><div><span>Scope</span><b>40+ assets/equipment</b></div><div><span>Focus</span><b>Traceability · evidence · history</b></div>'),
('Maintenance documents and knowledge needed to be found and reviewed without depending on individual memory.','The process depended on spreadsheets, network folders, paper and individual memory. Finding the right asset, proving execution or recovering history required manual work.'),
('Product, FastAPI, interface, database, text search, transcription, audit trail and technician review.','Asset flow with code/tag/name, checklist, date/time, responsible person, photos, notes, evidence and server-side history.'),
('FastAPI, React, SQLite/FTS5, PWA, OpenAI transcription and local faster-whisper/whisper.cpp alternatives.','Changes preserve author and previous/new values; a new maintenance execution never overwrites the previous history.'),
])
runpy.run_path(str(root/'scripts'/'patch_proposal_case_en.py'),run_name='__main__')
print('Maintenance and EN proposal cases refreshed.')
