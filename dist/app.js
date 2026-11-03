(() => {
  'use strict';
  const header = document.querySelector('.site-header');
  const onScroll = () => header?.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, {passive: true});

  const menu = document.querySelector('.nav-links');
  const menuButton = document.querySelector('.menu-toggle');
  const closeMenu = () => { menu?.classList.remove('open'); menuButton?.setAttribute('aria-expanded', 'false'); menuButton?.setAttribute('aria-label', 'Open navigation'); };
  menuButton?.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') === 'true';
    menu.classList.toggle('open', !isOpen);
    menuButton.setAttribute('aria-expanded', String(!isOpen));
    menuButton.setAttribute('aria-label', isOpen ? 'Open navigation' : 'Close navigation');
  });
  menu?.querySelectorAll('a').forEach(a => a.addEventListener('click', closeMenu));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') { closeMenu(); } });
  document.addEventListener('click', e => { if (!header?.contains(e.target)) closeMenu(); });
  window.matchMedia('(min-width: 601px)').addEventListener('change', e => { if (e.matches) closeMenu(); });

  // Content is visible without JavaScript and if IntersectionObserver is unavailable.
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !reducedMotion) {
    document.documentElement.classList.add('js');
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible'); observer.unobserve(entry.target); } });
    }, {threshold: 0.08});
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
  }

  const sections = [...document.querySelectorAll('main > section[id]')];
  if ('IntersectionObserver' in window && sections.length) {
    const sectionObserver = new IntersectionObserver(entries => {
      entries.filter(e => e.isIntersecting).forEach(entry => {
        document.querySelectorAll('.nav-links a').forEach(a => {
          const active = a.getAttribute('href') === '#' + entry.target.id;
          if (active) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
        });
      });
    }, {rootMargin: '-15% 0px -55% 0px'});
    sections.forEach(section => sectionObserver.observe(section));
  }

  const tabs = [...document.querySelectorAll('.engineering-explorer [role="tab"]')];
  const visibleTabs = () => tabs.filter(tab => !tab.hidden);
  const activateTab = tab => {
    tabs.forEach(t => {
      const selected = t === tab;
      t.setAttribute('aria-selected', String(selected));
      t.tabIndex = selected ? 0 : -1;
      const panel = document.getElementById(t.getAttribute('aria-controls'));
      if (panel) panel.hidden = !selected;
    });
  };
  tabs.forEach(tab => {
    tab.addEventListener('click', () => activateTab(tab));
    tab.addEventListener('keydown', e => {
      const available = visibleTabs();
      const index = available.indexOf(tab);
      let next;
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') next = (index + 1) % available.length;
      if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') next = (index - 1 + available.length) % available.length;
      if (e.key === 'Home') next = 0;
      if (e.key === 'End') next = available.length - 1;
      if (next !== undefined && available[next]) {
        e.preventDefault(); activateTab(available[next]); available[next].focus();
        available[next].scrollIntoView({block: 'nearest', inline: 'nearest'});
      }
    });
  });
  const filters = [...document.querySelectorAll('[data-story-filter]')];
  filters.forEach(filter => {
    filter.addEventListener('click', () => {
      const category = filter.dataset.storyFilter;
      filters.forEach(button => button.setAttribute('aria-pressed', String(button === filter)));
      tabs.forEach(tab => { tab.hidden = category !== 'All' && tab.dataset.storyCategory !== category; });
      const available = visibleTabs();
      if (available.length) activateTab(available[0]);
      const count = document.querySelector('.story-count');
      if (count) count.textContent = available.length + (available.length === 1 ? ' decision' : ' decisions') + ' / ' + (category === 'All' ? 'actual project code' : category);
      const list = document.querySelector('.engineering-explorer .engine-tabs');
      if (list) { list.scrollTop = 0; list.scrollLeft = 0; }
    });
  });
  // Progressive enhancement: all source examples are available in the HTML without JS.
  if (tabs.length) {
    const controls = document.querySelector('.engine-controls');
    if (controls) controls.hidden = false;
    activateTab(tabs[0]);
  }

  document.querySelectorAll('[data-screen-explorer]').forEach(explorer => {
    const choices = [...explorer.querySelectorAll('[data-screen-choice]')];
    const panels = [...explorer.querySelectorAll('.screen-panel')];
    const selectScreen = choice => {
      choices.forEach(button => button.setAttribute('aria-pressed', String(button === choice)));
      panels.forEach(panel => { panel.hidden = panel.id !== choice.dataset.screenChoice; });
    };
    choices.forEach(choice => choice.addEventListener('click', () => selectScreen(choice)));
    if (choices.length) selectScreen(choices[0]);
  });

  const videos = [...document.querySelectorAll('video')];
  videos.forEach(video => {
    video.addEventListener('play', () => {
      videos.forEach(other => { if (other !== video) other.pause(); });
      video.closest('.video-frame')?.classList.add('is-playing');
    });
    const stop = () => video.closest('.video-frame')?.classList.remove('is-playing');
    video.addEventListener('pause', stop);
    video.addEventListener('ended', stop);
  });

  let toastTimer;
  const toast = document.querySelector('.toast');
  const announce = message => {
    if (!toast) return;
    toast.textContent = message; toast.classList.add('visible');
    clearTimeout(toastTimer); toastTimer = setTimeout(() => toast.classList.remove('visible'), 3500);
  };
  document.querySelectorAll('[data-copy-email]').forEach(button => {
    button.addEventListener('click', async () => {
      const email = button.dataset.copyEmail;
      try {
        if (navigator.clipboard && window.isSecureContext) await navigator.clipboard.writeText(email);
        else {
          const field = document.createElement('textarea');
          field.value = email; field.style.position = 'fixed'; field.style.opacity = '0';
          document.body.appendChild(field); field.select();
          const copied = document.execCommand('copy'); field.remove();
          if (!copied) throw new Error('Copy unavailable');
        }
        announce('Email copied. Let’s make something good.');
      } catch (_) { announce('Email: ' + email); }
    });
  });

  const lightbox = document.querySelector('.lightbox');
  const lightboxImage = lightbox?.querySelector('img');
  const caption = lightbox?.querySelector('p');
  document.querySelectorAll('[data-zoom]').forEach(button => {
    button.addEventListener('click', () => {
      if (!lightbox || typeof lightbox.showModal !== 'function') { window.open(button.dataset.zoom, '_blank', 'noopener'); return; }
      lightboxImage.src = button.dataset.zoom;
      lightboxImage.alt = button.querySelector('img')?.alt || 'Project screenshot';
      caption.textContent = button.dataset.caption || lightboxImage.alt;
      lightbox.showModal(); document.body.classList.add('lightbox-open');
    });
  });
  lightbox?.querySelector('.close-lightbox')?.addEventListener('click', () => lightbox.close());
  lightbox?.addEventListener('close', () => { document.body.classList.remove('lightbox-open'); });
  lightbox?.addEventListener('click', e => { if (e.target === lightbox) lightbox.close(); });
})();
