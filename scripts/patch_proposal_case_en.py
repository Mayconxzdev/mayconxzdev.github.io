from pathlib import Path
p=Path(__file__).resolve().parents[1]/'en/cases/vesper-propostas/index.html'
t=p.read_text(encoding='utf-8')
pairs=[
('<h1>Vesper Propostas</h1>','<h1>Proposta Comercial</h1>'),
('I built an application that brings together request data, customer and equipment identification, template selection, ODT/PDF generation, document review and email preparation.','I evolved the proposal workflow into a controlled internal application for request data, customer and template selection, ODT/PDF generation, review, approval, email preparation and history.'),
('Discovery, full development, deployment on four computers, training, user review and support.','I observed the existing process, gathered requirements with Commercial users, then developed, deployed, trained and supported the solution used by four professionals.'),
('Finding templates, copying information from email, reusing documents and preparing messages created manual steps and risked mixing customer data.','Finding templates, copying email data, reusing documents and preparing messages created manual steps and risked using the wrong customer, template, attachment or document version.'),
('Request reading, customer and equipment identification, template selection, ODT/PDF generation, history, preview, review and email preparation.','Request reading, customer/equipment identification, template selection, ODT/PDF generation, history, preview, human approval and email preparation.'),
('The application prepares and validates information, but review remains mandatory before sending.','Human review remains mandatory before the external effect; the workflow also preserves who prepared, approved and sent the proposal.'),
]
for old,new in pairs:
    if old in t:
        t=t.replace(old,new,1)
    elif new in t:
        continue
    else:
        raise RuntimeError(f'EN proposal case drift: {old[:90]}')
p.write_text(t,encoding='utf-8')
print('EN proposal case refreshed')
