function initRecruiterArchive(){
  const archive=document.querySelector('.archive');
  const button=document.querySelector('.archive-expand');
  const search=document.querySelector('#project-search');
  const filters=[...document.querySelectorAll('.filter-button')];
  if(!archive||!button)return;

  let expanded=false;
  const mobile=()=>window.matchMedia('(max-width: 720px)').matches;
  const hasActiveFilter=()=>{
    const active=filters.find(item=>item.classList.contains('active'));
    return Boolean((active?.dataset.filter||'all')!=='all'||(search?.value||'').trim());
  };

  function sync(){
    const filtering=hasActiveFilter();
    archive.classList.toggle('archive-filtering',filtering);
    archive.classList.toggle('archive-expanded',expanded&&!filtering);
    archive.classList.toggle('archive-collapsed',mobile()&&!expanded&&!filtering);
    button.setAttribute('aria-expanded',String(expanded&&!filtering));
    const label=expanded&&!filtering?button.dataset.expandedLabel:button.dataset.collapsedLabel;
    const text=button.querySelector('span:first-child');
    if(text&&label)text.textContent=label;
  }

  button.addEventListener('click',()=>{expanded=!expanded;sync();});
  filters.forEach(item=>item.addEventListener('click',()=>requestAnimationFrame(sync)));
  search?.addEventListener('input',()=>requestAnimationFrame(sync));
  window.addEventListener('resize',sync,{passive:true});
  sync();
}

if(document.readyState==='loading'){
  document.addEventListener('DOMContentLoaded',initRecruiterArchive,{once:true});
}else{
  initRecruiterArchive();
}
