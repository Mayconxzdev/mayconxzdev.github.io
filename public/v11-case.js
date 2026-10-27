(()=>{const nav=document.querySelector('.v11-case-route');if(!nav)return;
 const links=[...nav.querySelectorAll('a[href^="#"]')];
 links.forEach(a=>a.addEventListener('click',e=>{const el=document.querySelector(a.getAttribute('href'));if(!el)return;
  // Let browser move immediately; deep-link remains shareable.
  el.setAttribute('tabindex','-1');requestAnimationFrame(()=>el.focus({preventScroll:true}));
 }));
})();
