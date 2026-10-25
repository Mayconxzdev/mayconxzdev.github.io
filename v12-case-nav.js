(()=>{const button=document.querySelector('.v12-case-menu-toggle');
const nav=document.getElementById('v12-case-primary');if(!button||!nav)return;
const close=()=>{nav.classList.remove('is-open');button.setAttribute('aria-expanded','false');button.setAttribute('aria-label','Abrir menu')};
button.addEventListener('click',()=>{const open=nav.classList.toggle('is-open');button.setAttribute('aria-expanded',String(open));button.setAttribute('aria-label',open?'Fechar menu':'Abrir menu')});
nav.addEventListener('click',e=>{if(e.target.closest('a'))close()});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('is-open')){close();button.focus()}});
document.addEventListener('click',e=>{if(!nav.contains(e.target)&&!button.contains(e.target))close()});
})();
