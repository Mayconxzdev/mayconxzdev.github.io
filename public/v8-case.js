(()=>{const reduced=matchMedia("(prefers-reduced-motion:reduce)").matches;
if(reduced||!("IntersectionObserver" in window))return;
const sections=[...document.querySelectorAll(".case-essentials,.case-decisions,.case-proof,.case-next")];
if(!sections.length)return;
document.body.classList.add("v8-motion-ready");
const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add("v8-seen");observer.unobserve(e.target)}})},{rootMargin:"0px 0px 80px 0px",threshold:.05});
sections.forEach(x=>observer.observe(x));
})();
