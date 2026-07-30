function initSite(){
  const themeToggle=document.querySelector('.theme-toggle');
  const themeMeta=document.querySelector('meta[name="theme-color"]');
  const language=document.documentElement.lang||'pt-BR';
  function applyTheme(value,{persist=false}={}){
    const theme=value==='dark'?'dark':'light';
    document.documentElement.dataset.theme=theme;
    if(themeToggle){
      const dark=theme==='dark';
      themeToggle.setAttribute('aria-pressed',String(dark));
      themeToggle.setAttribute('aria-label',language.startsWith('en')
        ?(dark?'Switch to light theme':'Switch to dark theme')
        :(dark?'Ativar tema claro':'Ativar tema escuro'));
    }
    themeMeta?.setAttribute('content',theme==='dark'?'#0a0a0a':'#ffffff');
    if(persist){
      try{localStorage.setItem('mf-theme',theme);}catch(_error){}
    }
  }
  if(themeToggle){
    let savedTheme='';
    try{savedTheme=localStorage.getItem('mf-theme')||'';}catch(_error){}
    applyTheme(savedTheme||document.documentElement.dataset.theme||'light');
    themeToggle.addEventListener('click',()=>{
      applyTheme(document.documentElement.dataset.theme==='dark'?'light':'dark',{persist:true});
    });
  }
  const menu=document.querySelector('.menu-button');
  const nav=document.querySelector('#main-nav');
  if(menu&&nav){
    menu.addEventListener('click',()=>{const open=nav.classList.toggle('open');menu.setAttribute('aria-expanded',String(open));});
    nav.addEventListener('click',e=>{if(e.target instanceof HTMLAnchorElement){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');}});
    document.addEventListener('keydown',e=>{if(e.key==='Escape'){nav.classList.remove('open');menu.setAttribute('aria-expanded','false');}});
  }
  const filters=[...document.querySelectorAll('.filter-button')];
  const rows=[...document.querySelectorAll('#project-grid .archive-row')];
  const search=document.querySelector('#project-search');
  const empty=document.querySelector('#empty-state');
  let active='all';
  function apply(){
    const term=(search?.value||'').trim().toLowerCase();
    let visible=0;
    rows.forEach(row=>{
      const matchFilter=active==='all'||row.classList.contains('persp-'+active);
      const matchText=!term||(row.dataset.search||'').includes(term);
      row.hidden=!(matchFilter&&matchText);
      if(!row.hidden)visible+=1;
    });
    if(empty)empty.hidden=visible!==0;
  }
  filters.forEach(button=>{
    button.setAttribute('aria-pressed',String(button.classList.contains('active')));
    button.addEventListener('click',()=>{
      filters.forEach(item=>{item.classList.remove('active');item.setAttribute('aria-pressed','false');});
      button.classList.add('active');
      button.setAttribute('aria-pressed','true');
      active=button.dataset.filter||'all';
      apply();
    });
  });
  search?.addEventListener('input',apply);

  const stage=document.querySelector('[data-tilt]');
  const reduced=window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  if(stage&&!reduced&&window.matchMedia?.('(pointer: fine)').matches){
    stage.addEventListener('pointermove',event=>{
      const rect=stage.getBoundingClientRect();
      const x=(event.clientX-rect.left)/rect.width-.5;
      const y=(event.clientY-rect.top)/rect.height-.5;
      stage.style.setProperty('--tilt-x',`${x*5}deg`);
      stage.style.setProperty('--tilt-y',`${-y*4}deg`);
    });
    stage.addEventListener('pointerleave',()=>{
      stage.style.setProperty('--tilt-x','0deg');
      stage.style.setProperty('--tilt-y','0deg');
    });
  }
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',initSite,{once:true});}else{initSite();}
