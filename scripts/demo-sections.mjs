const demos = {
  "producao-operacional": {
    "type": "production",
    "title": "E se uma ordem chegar duas vezes?",
    "description": "Teste o que acontece quando a mesma solicitação é enviada novamente. Os dados, estados e resultados são inventados.",
    "controls": "<h3>Teste o recebimento</h3>\n<button class=\"demo-action primary\" id=\"demo-create\" type=\"button\"><span>01</span> Receber ordem OP-EXEMPLO <span aria-hidden=\"true\">↗</span></button>\n<button class=\"demo-action\" id=\"demo-approve\" type=\"button\"><span>02</span> Validar ordem <span aria-hidden=\"true\">→</span></button>\n<button class=\"demo-action\" id=\"demo-reset\" type=\"button\"><span>↺</span> Reiniciar teste</button>",
    "extra": "<div class=\"demo-metrics\"><div><strong id=\"demo-count\">00</strong><span>REGISTROS CRIADOS</span></div><div><strong id=\"demo-duplicates\">00</strong><span>DUPLICIDADES BLOQUEADAS</span></div></div>"
  },
  "manutencao-em-campo": {
    "type": "maintenance",
    "title": "O checklist está completo?",
    "description": "Selecione um equipamento fictício, marque as inspeções e tente registrar a atividade antes de concluir tudo.",
    "controls": "<h3>Revise uma inspeção</h3>\n<label class=\"demo-select\">EQUIPAMENTO FICTÍCIO<select id=\"demo-equipment\"><option value=\"EX-101\">Motor de exemplo · EX-101</option><option value=\"EX-102\">Exaustor de exemplo · EX-102</option><option value=\"EX-103\">Bomba de exemplo · EX-103</option></select></label>\n<label class=\"demo-check\"><input type=\"checkbox\"> Conferir identificação e etiqueta</label>\n<label class=\"demo-check\"><input type=\"checkbox\"> Registrar a inspeção visual</label>\n<label class=\"demo-check\"><input type=\"checkbox\"> Verificar a fixação</label>\n<button id=\"demo-register\" class=\"demo-action primary\" type=\"button\"><span>✓</span> Registrar inspeção fictícia <span aria-hidden=\"true\">↗</span></button>\n<button id=\"demo-reset\" class=\"demo-action\" type=\"button\"><span>↺</span> Limpar formulário</button>",
    "extra": "<div class=\"demo-metrics\"><div><strong id=\"demo-count\">0 / 3</strong><span>VERIFICAÇÕES MARCADAS</span></div><div><strong>LOCAL</strong><span>SEM DADOS EXTERNOS</span></div></div>"
  },
  "belarc-inventory": {
    "type": "belarc",
    "title": "O que acontece se um computador sair da rede?",
    "description": "Alterne entre comunicação disponível e indisponível para entender estados de inventário. Nenhuma máquina real é acessada.",
    "controls": "<h3>Inspecione a comunicação</h3>\n<label class=\"demo-select\">ESTAÇÃO FICTÍCIA<select id=\"demo-station\"><option value=\"LAB-EST-01\">Estação de teste · LAB-EST-01</option><option value=\"LAB-EST-02\">Estação de teste · LAB-EST-02</option></select></label>\n<button class=\"demo-action primary\" id=\"demo-sync\" type=\"button\"><span>01</span> Atualizar inventário <span aria-hidden=\"true\">↗</span></button>\n<button class=\"demo-action\" id=\"demo-network\" type=\"button\">Simular indisponibilidade</button>",
    "extra": "<div class=\"demo-metrics\"><div><strong id=\"demo-count\">00</strong><span>ATUALIZAÇÕES FICTÍCIAS</span></div><div><strong><i class=\"demo-status-dot\" id=\"demo-dot\"></i>ESTADO</strong><span>COMUNICAÇÃO SIMULADA</span></div></div>"
  }
};
export function renderDemo(slug) {
 const d=demos[slug]; if(!d)return '';
 return '<section id="demo" class="case-demo" data-demo="'+d.type+'" aria-labelledby="demo-title"><div class="container">' +
 '<div class="demo-head"><div><span class="demo-label">TESTE NO NAVEGADOR / DADOS INVENTADOS</span><h2 id="demo-title">'+d.title+'</h2></div><p>'+d.description+'</p></div>' +
 '<div class="demo-rack"><div class="demo-controls">'+d.controls+'</div><div class="demo-output">' +
 '<div class="demo-heading"><span>SIMULAÇÃO LOCAL / SEM SERVIDOR</span><em id="demo-meta">PRONTO</em></div>' +
 '<div class="demo-big" id="demo-result">Pronto para começar.</div><p class="demo-comment" id="demo-description">Use os controles para observar uma regra de negócio.</p>' +
 '<div class="demo-log"><strong>ÚLTIMO EVENTO</strong><span id="demo-log">LAB / READY / FICTÍCIO</span></div>' +
 '<div class="demo-note">Esta demonstração é ilustrativa. Não comprova instalação nem o comportamento integral do software original.</div>' +
 '<p id="demo-live" class="sr-only" role="status" aria-live="polite"></p>'+d.extra+'</div></div></div></section>';
}