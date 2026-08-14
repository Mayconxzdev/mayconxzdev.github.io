from pathlib import Path
p=Path(__file__).resolve().parents[1]/'cases/vesper-propostas/index.html'
t=p.read_text(encoding='utf-8')
pairs=[
('<h1>Vesper Propostas</h1>','<h1>Proposta Comercial</h1>'),
('Desenvolvi uma aplicação para reunir os dados do pedido, identificar cliente e equipamento, selecionar modelos, gerar ODT/PDF, revisar o documento e preparar o envio por e-mail.','Evoluí o fluxo de propostas para reunir pedido, cliente, seleção de modelo, geração ODT/PDF, revisão, aprovação, preparação de e-mail e histórico em uma aplicação interna controlada.'),
('Levantamento, desenvolvimento, implantação em quatro computadores, treinamento, revisão com os usuários e sustentação.','Observei o processo existente, levantei requisitos com o Comercial e desenvolvi, implantei, treinei e sustento a solução usada por quatro profissionais.'),
('Buscar modelos, copiar informações de e-mails, reaproveitar documentos e preparar mensagens gerava etapas manuais e risco de misturar dados entre clientes.','Buscar modelos, copiar dados de e-mails, reaproveitar documentos e preparar mensagens gerava etapas manuais e risco de usar cliente, modelo, anexo ou versão incorretos.'),
('A aplicação prepara e valida informações, mas a revisão permanece obrigatória antes do envio.','A revisão humana permanece obrigatória antes do efeito externo; o fluxo preserva quem preparou, aprovou e enviou a proposta.'),
]
for old,new in pairs:
    if old in t:
        t=t.replace(old,new,1)
    elif new in t:
        continue
    else:
        raise RuntimeError(f'PT proposal case drift: {old[:70]}')
p.write_text(t,encoding='utf-8')
print('PT proposal case refreshed')
