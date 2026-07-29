function initSite(){
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
  filters.forEach(button=>button.addEventListener('click',()=>{
    filters.forEach(item=>item.classList.remove('active'));
    button.classList.add('active');
    active=button.dataset.filter||'all';
    apply();
  }));
  search?.addEventListener('input',apply);
}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',initSite,{once:true});}else{initSite();}
