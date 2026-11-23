/* ABC Midwest — JS sin dependencias */
(function () {
  'use strict';
  var doc = document, root = doc.documentElement;
  root.classList.add('js');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- menú móvil y desplegable ---- */
  var burger = doc.querySelector('.burger'), nav = doc.getElementById('primary-nav');
  if (burger && nav) {
    burger.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  var ddBtn = doc.querySelector('.dd-toggle'), dd = doc.querySelector('.dd');
  if (ddBtn && dd) {
    ddBtn.addEventListener('click', function () {
      var open = dd.classList.toggle('open');
      ddBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }
  doc.addEventListener('keydown', function (e) {
    if (e.key !== 'Escape') return;
    if (dd && dd.classList.contains('open')) { dd.classList.remove('open'); ddBtn.setAttribute('aria-expanded', 'false'); ddBtn.focus(); }
    else if (nav && nav.classList.contains('open')) { nav.classList.remove('open'); burger.setAttribute('aria-expanded', 'false'); burger.focus(); }
  });

  /* ---- animaciones de aparición ---- */
  var items = doc.querySelectorAll('.reveal');
  if (items.length) {
    if (reduce || !('IntersectionObserver' in window)) {
      items.forEach(function (el) { el.classList.add('in'); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      items.forEach(function (el) { io.observe(el); });
    }
  }

  /* ---- slider del hero ---- */
  var hero = doc.querySelector('.hero');
  if (hero) {
    var slides = [].slice.call(hero.querySelectorAll('.slide')),
        dots = [].slice.call(hero.querySelectorAll('.dot')),
        toggle = hero.querySelector('.toggle'),
        idx = 0, timer = null, userPaused = reduce, hoverPaused = false;
    function show(n) {
      idx = (n + slides.length) % slides.length;
      slides.forEach(function (s, i) {
        var on = i === idx;
        s.classList.toggle('is-active', on);
        if (on) s.removeAttribute('aria-hidden'); else s.setAttribute('aria-hidden', 'true');
        s.querySelectorAll('a').forEach(function (a) { a.tabIndex = on ? 0 : -1; });
        var img = s.querySelector('img'); if (img && img.loading === 'lazy') img.loading = 'eager';
      });
      dots.forEach(function (d, i) { d.classList.toggle('is-active', i === idx); if (i === idx) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current'); });
    }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    function start() { stop(); if (!userPaused && !hoverPaused && !reduce) timer = setInterval(function () { show(idx + 1); }, 6500); }
    function setPaused(p) {
      userPaused = p;
      if (toggle) { toggle.classList.toggle('paused', p); toggle.setAttribute('aria-label', toggle.getAttribute(p ? 'data-play' : 'data-pause')); }
      start();
    }
    hero.querySelector('.prev').addEventListener('click', function () { show(idx - 1); start(); });
    hero.querySelector('.next').addEventListener('click', function () { show(idx + 1); start(); });
    dots.forEach(function (d, i) { d.addEventListener('click', function () { show(i); start(); }); });
    if (toggle) toggle.addEventListener('click', function () { setPaused(!userPaused); });
    hero.addEventListener('mouseenter', function () { hoverPaused = true; stop(); });
    hero.addEventListener('mouseleave', function () { hoverPaused = false; start(); });
    hero.addEventListener('focusin', function () { hoverPaused = true; stop(); });
    hero.addEventListener('focusout', function () { hoverPaused = false; start(); });
    doc.addEventListener('keydown', function (e) {
      var t = e.target, tag = t && t.tagName;
      if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;
      var r = hero.getBoundingClientRect();
      if (r.bottom < 0 || r.top > window.innerHeight) return; // solo si el hero está visible
      if (e.key === 'ArrowLeft') { show(idx - 1); start(); }
      else if (e.key === 'ArrowRight') { show(idx + 1); start(); }
    });
    doc.addEventListener('visibilitychange', function () { if (doc.hidden) stop(); else start(); });
    show(0); setPaused(reduce);
  }

  /* ---- formulario de cotización ---- */
  var form = doc.getElementById('quote-form');
  if (form) {
    var params = new URLSearchParams(window.location.search), pre = params.get('service');
    var sel = form.querySelector('#f-service');
    if (pre && sel && sel.querySelector('option[value="' + pre.replace(/[^a-z-]/g, '') + '"]')) sel.value = pre.replace(/[^a-z-]/g, '');
    var status = form.querySelector('.f-status'), btn = form.querySelector('button[type=submit]');
    function say(kind, msg) { status.hidden = false; status.className = 'f-status ' + kind; status.textContent = msg; }
    function clearErr() { form.querySelectorAll('.f-err').forEach(function (n) { n.remove(); }); form.querySelectorAll('.is-invalid').forEach(function (n) { n.classList.remove('is-invalid'); n.removeAttribute('aria-invalid'); }); }
    function validate() {
      clearErr(); var ok = true, first = null;
      form.querySelectorAll('[required]').forEach(function (f) {
        var bad = !f.value.trim() || (f.type === 'email' && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(f.value));
        if (bad) {
          ok = false; f.classList.add('is-invalid'); f.setAttribute('aria-invalid', 'true');
          var m = doc.createElement('div'); m.className = 'f-err'; m.textContent = form.dataset.required; f.parentNode.appendChild(m);
          if (!first) first = f;
        }
      });
      if (first) first.focus();
      return ok;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (form.website && form.website.value) { say('ok', form.dataset.success); form.reset(); return; } // honeypot: se ignora en silencio
      if (!validate()) { say('bad', form.dataset.invalid); return; }
      var data = {}; new FormData(form).forEach(function (v, k) { if (k !== 'website') data[k] = v; });
      btn.disabled = true; btn.textContent = form.dataset.sending; say('info', form.dataset.sending);
      var endpoint = form.dataset.endpoint || '';
      if (!endpoint || endpoint.indexOf('REPLACE_ME') > -1) { // sin endpoint configurado: abrir correo
        var body = Object.keys(data).map(function (k) { return k + ': ' + data[k]; }).join('\n');
        window.location.href = 'mailto:' + form.dataset.email + '?subject=' + encodeURIComponent('Quote request') + '&body=' + encodeURIComponent(body);
        say('info', form.dataset.mailto); btn.disabled = false; btn.textContent = form.dataset.send; return;
      }
      fetch(endpoint, { method: 'POST', headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' }, body: JSON.stringify(data) })
        .then(function (r) { if (!r.ok) throw new Error(r.status); say('ok', form.dataset.success); form.reset(); })
        .catch(function () { say('bad', form.dataset.error); })
        .then(function () { btn.disabled = false; btn.textContent = form.dataset.send; });
    });
  }
})();
