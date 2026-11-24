(() => {
  const panel = document.querySelector('.mf-filters');
  const search = document.getElementById('mf-search');
  const category = document.getElementById('mf-category');
  const state = document.getElementById('mf-state');
  const reset = document.getElementById('mf-reset');
  const count = document.getElementById('mf-count');
  const empty = document.getElementById('mf-empty');
  const normalized = (text) => text.normalize('NFD').replace(/\p{Diacritic}/gu, '').toLocaleLowerCase('pt-BR');
  const projects = Array.from(document.querySelectorAll('#mf-archive [data-project]'), (item) => ({
    item, text: normalized(item.textContent),
    categories: item.dataset.categories.split(' '), state: item.dataset.state,
  }));

  function update() {
    const terms = normalized(search.value).trim().split(/\s+/);
    let visible = 0;
    for (const project of projects) {
      const match = (!category.value || project.categories.includes(category.value))
        && (!state.value || project.state === state.value)
        && terms.every((term) => project.text.includes(term));
      project.item.hidden = !match;
      if (match) visible += 1;
    }
    count.textContent = visible === 1 ? '1 case' : `${visible} cases`;
    empty.hidden = visible > 0;
  }

  search.addEventListener('input', update);
  category.addEventListener('change', update);
  state.addEventListener('change', update);
  reset.addEventListener('click', () => {
    search.value = category.value = state.value = '';
    update();
    search.focus();
  });
  panel.hidden = false;
  update();
})();
