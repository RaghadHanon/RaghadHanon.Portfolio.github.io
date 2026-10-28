(() => {
  const controls = document.querySelector('.rx-controls');
  if (!controls) return;
  const cards = [...document.querySelectorAll('[data-rx-category]')];
  const buttons = [...controls.querySelectorAll('[data-rx-filter]')];
  const search = controls.querySelector('input[type="search"]');
  const count = controls.querySelector('.rx-count');
  const empty = document.querySelector('.rx-empty');
  let active = 'all';

  function update() {
    const terms = search.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    cards.forEach(card => {
      const inCategory = active === 'all' || card.dataset.rxCategory.split(' ').includes(active);
      const matches = terms.every(term => card.dataset.rxSearch.includes(term));
      card.hidden = !(inCategory && matches);
      if (!card.hidden) visible += 1;
    });
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.rxFilter === active)));
    count.textContent = `${visible} ${visible === 1 ? 'project' : 'projects'}`;
    empty.hidden = visible !== 0;
  }

  buttons.forEach(button => button.addEventListener('click', () => {
    active = button.dataset.rxFilter;
    update();
  }));
  search.addEventListener('input', update);
  controls.hidden = false;
  update();
})();
