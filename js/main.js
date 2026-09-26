/* ==========================================================================
   Career Skills Center — site behaviour
   Plain JS, no dependencies. Loaded with `defer` on every page.
   ========================================================================== */
(function () {
  'use strict';

  /* ---------- Header: solid background once the page scrolls ---------- */
  const header = document.getElementById('site-header');
  const onScroll = () => header.classList.toggle('is-scrolled', window.scrollY > 40);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ---------- Mobile navigation ---------- */
  const navToggle = document.getElementById('nav-toggle');
  if (navToggle) {
    navToggle.addEventListener('click', () => {
      const open = header.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', String(open));
    });
  }

  // Submenu accordions on small screens (desktop uses :hover / :focus-within)
  document.querySelectorAll('.dropdown-toggle').forEach((btn) => {
    btn.addEventListener('click', () => {
      const li = btn.closest('.has-dropdown');
      const open = li.classList.toggle('is-open');
      btn.setAttribute('aria-expanded', String(open));
    });
  });

  // Close the mobile menu after following an in-page link
  document.querySelectorAll('.primary-nav a[href^="#"]').forEach((a) => {
    a.addEventListener('click', () => {
      header.classList.remove('is-open');
      navToggle && navToggle.setAttribute('aria-expanded', 'false');
    });
  });

  /* ---------- Hero crossfade (Hero.webp -> hero2.webp) ---------- */
  const slides = document.querySelectorAll('.hero-slide');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (slides.length > 1 && !reduceMotion) {
    let i = 0;
    setInterval(() => {
      slides[i].classList.remove('is-active');
      i = (i + 1) % slides.length;
      slides[i].classList.add('is-active');
    }, 7000);
  }

  /* ---------- Contact dialog ---------- */
  const dialog = document.getElementById('contact-dialog');
  if (dialog) {
    document.querySelectorAll('.js-open-contact').forEach((btn) => {
      btn.addEventListener('click', () => {
        header.classList.remove('is-open');
        dialog.showModal();
      });
    });
    document.getElementById('contact-close').addEventListener('click', () => dialog.close());

    // Light-dismiss fallback for browsers without <dialog closedby> (Safari).
    if (!('closedBy' in HTMLDialogElement.prototype)) {
      dialog.addEventListener('click', (event) => {
        if (event.target !== dialog) return;
        const r = dialog.getBoundingClientRect();
        const inside = r.top <= event.clientY && event.clientY <= r.bottom &&
                       r.left <= event.clientX && event.clientX <= r.right;
        if (!inside) dialog.close();
      });
    }

  }

  /* ---------- Contact forms (dialog + contact page) ----------
     Real submit: POST to submit.php (the cPanel PHP mailer). Every form carries
     a hidden `source` field; we add `page` here. On failure we show a fallback
     with the phone/email so a lead is never silently lost. */
  document.querySelectorAll('.contact-form').forEach((form) => {
    const status = form.querySelector('.form-status');
    const submitBtn = form.querySelector('[type="submit"]');
    form.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (status) status.className = 'form-status';
      if (!form.checkValidity()) {
        form.reportValidity();
        if (status) {
          status.textContent = 'Please fill in your name, phone, email, and program of interest.';
          status.classList.add('is-error');
        }
        return;
      }

      const data = new FormData(form);
      data.set('page', window.location.pathname);
      if (submitBtn) submitBtn.disabled = true;
      if (status) status.textContent = 'Sending…';

      try {
        const res = await fetch(form.action, {
          method: 'POST',
          body: data,
          headers: { Accept: 'application/json' },
        });
        const json = await res.json().catch(() => ({}));
        if (!res.ok || !json.ok) throw new Error(json.error || 'Submission failed');

        const source = data.get('source') || 'contact';
        if (status) {
          status.textContent = form.dataset.success || 'Thanks! We’ll be in touch soon.';
          status.classList.add('is-success');
        }
        form.reset();
        if (typeof gtag === 'function') {
          if (source === 'interest-list') {
            gtag('event', 'interest_list_signup', {
              program: data.get('program') || '',
              pay_method: data.get('pay_method') || '',
            });
          } else {
            gtag('event', 'form_submit', { source: source });
          }
        }
      } catch (err) {
        if (status) {
          status.textContent = 'Sorry, that didn’t send. Please email info@careerskillscenter.com or call (617) 544-7155.';
          status.classList.add('is-error');
        }
      } finally {
        if (submitBtn) submitBtn.disabled = false;
      }
    });
  });

  /* ---------- "See if you qualify" wizard (qualify.html) ----------
     Multi-step lead form. One question per screen with a progress bar. It
     CAPTURES A LEAD and shows a soft-routing message — it never renders a
     yes/no eligibility verdict (only a MassHire career center can decide that).
     Self-contained: the form is `.qualify-form` (not `.contact-form`) so the
     generic handler above ignores it. Posts to submit.php with source=qualify. */
  const qForm = document.querySelector('.qualify-form');
  if (qForm) {
    const steps = Array.from(qForm.querySelectorAll('.qualify-step'));
    const result = qForm.querySelector('.qualify-result');
    const fill = qForm.querySelector('.qualify-progress-fill');
    const label = qForm.querySelector('.qualify-progress-label');
    const backBtn = qForm.querySelector('.qualify-back');
    const status = qForm.querySelector('.form-status');
    const submitBtn = qForm.querySelector('[type="submit"]');
    let idx = 0;

    const show = (n) => {
      idx = Math.max(0, Math.min(n, steps.length - 1));
      steps.forEach((s, i) => s.classList.toggle('is-active', i === idx));
      const pct = Math.round(((idx + 1) / steps.length) * 100);
      if (fill) fill.style.width = pct + '%';
      if (label) label.textContent = 'Step ' + (idx + 1) + ' of ' + steps.length;
      if (backBtn) backBtn.hidden = idx === 0;
      const focusable = steps[idx].querySelector('input, select, button');
      if (focusable) focusable.focus();
    };

    // Choice steps auto-advance when an option is picked.
    steps.forEach((step) => {
      if (!step.dataset.autoadvance) return;
      step.querySelectorAll('input[type="radio"]').forEach((radio) => {
        radio.addEventListener('change', () => { if (idx < steps.length - 1) show(idx + 1); });
      });
    });

    if (backBtn) backBtn.addEventListener('click', () => show(idx - 1));

    qForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (status) { status.className = 'form-status'; status.textContent = ''; }
      // Final step holds the required contact fields; let the browser validate them.
      if (!qForm.checkValidity()) {
        qForm.reportValidity();
        return;
      }

      const data = new FormData(qForm);
      data.set('page', window.location.pathname);
      if (submitBtn) submitBtn.disabled = true;
      if (status) status.textContent = 'Sending…';

      try {
        const res = await fetch(qForm.action, {
          method: 'POST', body: data, headers: { Accept: 'application/json' },
        });
        const json = await res.json().catch(() => ({}));
        if (!res.ok || !json.ok) throw new Error(json.error || 'Submission failed');
        if (typeof gtag === 'function') gtag('event', 'form_submit', { source: 'qualify' });
        routeResult(data);
      } catch (err) {
        if (status) {
          status.textContent = 'Sorry, that didn’t send. Please email info@careerskillscenter.com or call (617) 544-7155.';
          status.classList.add('is-error');
        }
        if (submitBtn) submitBtn.disabled = false;
      }
    });

    // Field → guide map (GUIDE_MODE_SPEC step 5). Result always routes OUTWARD.
    const FIELD = {
      healthcare: { label: 'healthcare', guide: 'healthcare-careers-massachusetts.html' },
      it:         { label: 'information technology', guide: 'it-careers-massachusetts.html' },
      trades:     { label: 'the skilled trades', guide: 'skilled-trades-careers-massachusetts.html' },
      unsure:     { label: 'a new field', guide: 'career-paths.html' },
    };
    // The five outward steps for a likely funded fit.
    const FUNDED_STEPS = [
      'Find your MassHire Career Center. See the list of locations at <a class="link-yellow" href="https://www.mass.gov/info-details/masshire-career-center-locations" target="_blank" rel="noopener">mass.gov</a> and contact the nearest one.',
      'Register on JobQuest at <a class="link-yellow" href="https://jobquest.mass.gov" target="_blank" rel="noopener">jobquest.mass.gov</a> — you need an account before you can get training funding.',
      'Attend a Training Information Meeting at your career center.',
      'Ask about an Individual Training Account (ITA). If you get unemployment benefits, ask about Section 30.',
      'Choose a state-approved training program in your field.',
    ];

    // Soft routing per GUIDE_MODE_SPEC step 5. Never a yes/no verdict; always outward.
    function routeResult(data) {
      const inMA = data.get('live_ma') === 'yes';
      const situation = data.get('situation');
      const fundedSituations = ['unemployed', 'laid-off', 'part-low'];
      const assistance = data.get('assistance') === 'yes';
      const employer = data.get('employer');
      const field = FIELD[data.get('field')] || FIELD.unsure;

      const fundedFit = inMA && (fundedSituations.indexOf(situation) !== -1 || assistance);
      const employerFit = employer === 'yes' || employer === 'maybe';

      const setText = (sel, text) => { const el = result.querySelector(sel); if (el) el.textContent = text; };
      const show = (sel, on) => { const el = result.querySelector(sel); if (el) el.hidden = !on; };

      const stepsList = result.querySelector('.result-steps');

      if (fundedFit) {
        setText('.result-head', 'You may qualify for state-funded training.');
        setText('.result-body', 'Here’s how to start in Massachusetts:');
        if (stepsList) stepsList.innerHTML = FUNDED_STEPS.map((s) => '<li>' + s + '</li>').join('');
        show('.result-steps', true);
        show('.result-readmore', true);
        show('.result-otherpay', false);
      } else {
        setText('.result-head', 'Let’s find the best way for you to pay.');
        setText('.result-body', 'You may still qualify for help. Based on your answers, start here:');
        show('.result-steps', false);
        show('.result-readmore', false);
        show('.result-otherpay', true);
      }

      // Employer line (shown when relevant, in addition to the above).
      show('.result-employer', employerFit);

      // Always: link to the picked field guide + interest-list line (COURSE-DEPENDENT).
      const guideBtn = result.querySelector('.result-guide');
      if (guideBtn) {
        guideBtn.setAttribute('href', field.guide);
        guideBtn.textContent = field.label === 'a new field'
          ? 'Explore career paths' : 'Explore ' + field.label;
      }
      setText('.result-field-note',
        'We’ll also let you know when Career Skills Center launches training in ' + field.label + '.');

      steps.forEach((s) => s.classList.remove('is-active'));
      if (fill) fill.style.width = '100%';
      if (label) label.textContent = '';
      if (backBtn) backBtn.hidden = true;
      result.classList.add('is-active');
      result.setAttribute('tabindex', '-1');
      result.focus();
      result.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    show(0);
  }

  /* ---------- Footer year ---------- */
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
