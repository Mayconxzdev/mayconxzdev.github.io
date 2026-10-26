
/* Progressive chapter motion for smaller screens — no pinned scrolling.
   Images remain in natural document flow and readable if this file fails. */
(() => {
  "use strict";
  const reduced = matchMedia("(prefers-reduced-motion: reduce)");
  const compact = matchMedia("(max-width: 800px), (max-height: 600px)");
  const slides = [...document.querySelectorAll(".v8-world .world-slide")];
  if (!slides.length) return;
  const panels = slides.map(slide => slide.querySelector(".world-main-screen"));
  let frame = 0;
  function directMode() {
    try { return localStorage.getItem("lv-motion") === "direct"; }
    catch { return document.documentElement.classList.contains("v11-direct"); }
  }
  function reset() {
    for (const el of panels) {
      if (!el) continue;
      el.style.removeProperty("transform");
      el.style.removeProperty("opacity");
      el.style.removeProperty("clip-path");
      el.style.removeProperty("will-change");
    }
    document.documentElement.removeAttribute("data-mobile-cinema");
  }
  function run() {
    frame = 0;
    if (!compact.matches || reduced.matches || directMode()) { reset(); return; }
    const vh = innerHeight;
    let anyVisible = false;
    for (let index = 0; index < slides.length; index++) {
      const el = panels[index];
      if (!el) continue;
      const rect = slides[index].getBoundingClientRect();
      if (rect.bottom < -vh || rect.top > vh * 1.8) {
        el.style.removeProperty("will-change");
        continue;
      }
      anyVisible = true;
      const p = Math.max(0, Math.min(1, (vh * 0.91 - rect.top) / (vh * 0.69)));
      const q = 1 - p;
      const x = (index % 2 ? 10 : -10) * q;
      const y = 32 * q;
      const scale = 0.962 + 0.038 * p;
      el.style.transform = "translate3d(" + x.toFixed(1) + "px," +
        y.toFixed(1) + "px,0) scale(" + scale.toFixed(4) + ")";
      el.style.opacity = (0.82 + 0.18 * p).toFixed(3);
      el.style.clipPath = "inset(0 0 " + (10 * q).toFixed(2) + "% 0)";
      el.style.willChange = q > 0.001 ? "transform,opacity,clip-path" : "auto";
    }
    document.documentElement.dataset.mobileCinema = anyVisible ? "active" : "ready";
  }
  function queue() {
    if (!frame) frame = requestAnimationFrame(run);
  }
  addEventListener("scroll", queue, {passive:true});
  addEventListener("resize", queue, {passive:true});
  compact.addEventListener("change", queue);
  reduced.addEventListener("change", queue);
  addEventListener("pageshow", queue);
  // The motion preference belongs to the visitor. The site never overrides OS reduced motion.
  const toggle = document.getElementById("v11-motion-toggle");
  if (toggle && reduced.matches && !directMode()) {
    toggle.title = "Seu sistema solicitou movimento reduzido. Altere essa preferência no dispositivo para ver as animações.";
    toggle.setAttribute("aria-label", "Movimento reduzido pelo sistema. As animações seguem sua configuração de acessibilidade.");
  }
  queue();
})();
