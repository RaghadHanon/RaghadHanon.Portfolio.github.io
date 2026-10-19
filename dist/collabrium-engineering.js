(() => {
  'use strict';
  const controls = document.querySelector('[data-ce-controls]');
  const search = document.querySelector('#ce-search');
  const modules = [...document.querySelectorAll('[data-ce-module]')];
  const filters = [...document.querySelectorAll('[data-ce-filter]')];
  const count = document.querySelector('#ce-module-count');
  const empty = document.querySelector('#ce-no-results');
  if (!controls || !search || !modules.length || !count || !empty) return;
  let group = 'All';
  const update = () => {
    const query = search.value.trim().toLowerCase();
    let visible = 0;
    modules.forEach(module => {
      const matchesGroup = group === 'All' || module.dataset.ceGroup === group;
      const matchesSearch = !query || module.dataset.ceSearch.includes(query);
      module.hidden = !matchesGroup || !matchesSearch;
      if (!module.hidden) visible++;
    });
    filters.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.ceFilter === group)));
    count.textContent = visible + ' of ' + modules.length + ' modules' + (query ? ' match your search' : '');
    empty.hidden = visible !== 0;
  };
  filters.forEach(button => button.addEventListener('click', () => {
    group = button.dataset.ceFilter;
    update();
  }));
  search.addEventListener('input', update);
  controls.hidden = false;
  update();
})();
