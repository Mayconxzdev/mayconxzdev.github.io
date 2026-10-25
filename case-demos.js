/* Simulações autônomas, 100% fictícias e sem chamadas de rede. */
(()=>{"use strict";
 const root=document.querySelector("[data-demo]");
 if(!root)return;
 const type=root.dataset.demo;
 const $=q=>root.querySelector(q);
 const output=$("#demo-result"),description=$("#demo-description"),log=$("#demo-log");
 const live=$("#demo-live");
 const set=(title,details,code,meta)=>{
  output.textContent=title;description.textContent=details;
  log.textContent=code;
  live.textContent=title+". "+details;
  if(meta)$("#demo-meta").textContent=meta;
 };
 if(type==="production"){
  let created=false,approved=false,attempts=0,duplicates=0;
  const summary=()=>{$("#demo-count").textContent=created?"01":"00";$("#demo-duplicates").textContent=String(duplicates).padStart(2,"0")};
  $("#demo-create").addEventListener("click",()=>{
   attempts++;
   if(created){duplicates++;set("A ordem já existe.","Uma segunda entrada com o mesmo identificador não cria outro registro.","EVENTO: DUPLICATE_SUPPRESSED · FICTÍCIO","SEM NOVO REGISTRO");}
   else{created=true;set("Ordem recebida.","A solicitação de demonstração OP-EXEMPLO entrou na fila de validação.","EVENTO: CREATED · FICTÍCIO","PENDENTE DE REVISÃO");}
   summary();
  });
  $("#demo-approve").addEventListener("click",()=>{
   if(!created){set("Ainda não há uma ordem.","Primeiro receba uma solicitação para poder validá-la.","EVENTO: NEEDS_RECORD","AGUARDANDO ENTRADA");return}
   if(approved){set("Revisão já concluída.","A ordem continua validada. Não é necessário repetir a operação.","EVENTO: ALREADY_APPROVED","APROVADA");return}
   approved=true;set("Revisão concluída.","Os dados sintéticos foram confirmados e a ordem foi marcada como validada.","EVENTO: REVIEW_APPROVED","VALIDADA");
  });
  $("#demo-reset").addEventListener("click",()=>{
   created=false;approved=false;attempts=0;duplicates=0;
   set("Nenhuma ordem na fila.","Clique em 'Receber ordem' para iniciar uma situação de teste.","LAB / READY / FICTÍCIO","PRONTO");summary();
  });
  summary();
 }
 if(type==="maintenance"){
  const choose=$("#demo-equipment"),checks=Array.from(root.querySelectorAll(".demo-check input"));
  let recorded=new Map;
  const clear=()=>{checks.forEach(c=>c.checked=false);recorded.clear();set("Inspeção ainda não registrada.","Selecione o equipamento demonstrativo e marque os itens que foram conferidos.","ATIVO: "+choose.value+" / DEMO","EM ABERTO")};
  choose.addEventListener("change",clear);
  checks.forEach(x=>x.addEventListener("change",()=>{
   const total=checks.filter(c=>c.checked).length;
   $("#demo-count").textContent=total+" / "+checks.length;
   set(total===checks.length?"Checklist completo.":"Checklist em andamento.",total===checks.length?"Agora a inspeção fictícia pode ser registrada.":"Ainda existem verificações pendentes.",total+"/"+checks.length+" ITENS CONFERIDOS","EM REVISÃO");
  }));
  $("#demo-register").addEventListener("click",()=>{
   const missing=checks.filter(c=>!c.checked).length;
   if(missing){set("Ainda faltam "+missing+" verificações.","O registro não é concluído enquanto o checklist estiver incompleto.","EVENTO: REVIEW_BLOCKED","PENDENTE");return}
   recorded.set(choose.value,true);
   set("Inspeção registrada.","Foi gerado apenas um comprovante fictício do equipamento selecionado. Não houve gravação externa.","REGISTRO: "+choose.value+" / DEMO","CONCLUÍDO");
  });
  $("#demo-reset").addEventListener("click",()=>{choose.selectedIndex=0;clear();$("#demo-count").textContent="0 / 3"});
  clear();
 }
 if(type==="belarc"){
  let online=true,updates=0;
  const station=$("#demo-station");
  const sync=()=>{
   if(!online){set("Estação sem conexão.","A simulação preserva o estado anterior até que a conexão seja restaurada.","SIMULATED_AGENT: OFFLINE","AGUARDANDO");return}
   updates++;
   set("Inventário recebido.","O agente fictício enviou um novo resumo de hardware e software ao serviço de demonstração.","EVENTO: INVENTORY_SYNCED · "+station.value,"ATUALIZADO");
   $("#demo-count").textContent=String(updates).padStart(2,"0");
  };
  $("#demo-network").addEventListener("click",()=>{
   online=!online;
   $("#demo-network").textContent=online?"Simular indisponibilidade":"Restabelecer comunicação";
   $("#demo-dot").classList.toggle("connected",online);
   set(online?"Conexão restabelecida.":"A estação saiu da rede.",online?"Você pode reenviar uma atualização de inventário fictícia.":"As informações anteriores não são apagadas por uma falha temporária.",online?"SIMULATED_AGENT: ONLINE":"SIMULATED_AGENT: OFFLINE",online?"CONECTADO":"SEM RESPOSTA");
  });
  $("#demo-sync").addEventListener("click",sync);
  station.addEventListener("change",()=>{
   updates=0;$("#demo-count").textContent="00";
   set("Estação selecionada.","Execute a atualização de demonstração ou teste uma falha de comunicação.","HOST: "+station.value+" / DEMO",online?"CONECTADO":"SEM RESPOSTA");
  });
  $("#demo-dot").classList.add("connected");
 }
})();