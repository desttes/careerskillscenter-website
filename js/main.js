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

  /* ---------- Config-driven numbers ([data-cfg]) ----------
     Funding numbers live ONLY in js/site-config.js (window.CSC). Pages render
     them into [data-cfg] elements so nothing is hard-coded in copy. Each element
     keeps a visible fallback (usually "[VERIFY]") so an un-run page still shows
     the marker and the pre-deploy grep can catch unverified figures. */
  function fmtMoney(n) {
    return '$' + Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  }
  function fillConfigValues() {
    const cfg = window.CSC || window.SITE_CONFIG;
    if (!cfg) return;
    document.querySelectorAll('[data-cfg]').forEach((el) => {
      const key = el.getAttribute('data-cfg');
      if (!(key in cfg)) return;
      const val = cfg[key];
      const fmt = el.getAttribute('data-cfg-format') || 'raw';
      if (fmt === 'money') el.textContent = fmtMoney(val);
      else if (fmt === 'percent') el.textContent = Math.round(val * 100) + '%';
      else if (fmt === 'number') el.textContent = Number(val).toLocaleString('en-US');
      else el.textContent = String(val);
    });
  }
  fillConfigValues();

  /* ---------- "Do I Qualify?" wizard (qualify.html) ----------
     One question per screen, then a RESULTS-FIRST screen (Site Structure Spec
     v1.5): it shows which WIOA group you may fit, any priority flags, and outward
     next steps — never a yes/no verdict (only a MassHire career center decides).
     Emailing the steps is optional and posts to submit.php with source=qualify.
     The classifier is a pure function (classifyQualify) with self-tests you can
     run by loading qualify.html#selftest. */
  function classifyQualify(a) {
    a = a || {};
    const inMA = a.live_ma === 'yes';
    const dislocated = a.situation === 'laid-off' || a.situation === 'self-closed' || a.situation === 'on-ui';

    const groups = [];
    if (a.age === 'under18' || a.age === '18-24') {
      groups.push('WIOA Youth (ages 14–24)');
    }
    if (a.age === '18-24' || a.age === '25plus') {
      groups.push('WIOA Adult');
    }
    if (dislocated) {
      groups.push('WIOA Dislocated Worker');
    }

    const priorities = [];
    if (a.assistance === 'yes') priorities.push('You receive public assistance');
    if (a.income_low === 'yes') priorities.push('Your household income may be low');
    if (a.veteran === 'yes') priorities.push('Veteran or military-spouse priority');

    const needFit = dislocated ||
      a.situation === 'unemployed' ||
      a.situation === 'part-low' ||
      priorities.length > 0;
    const likely = inMA && needFit;

    return {
      inMA: inMA,
      groups: groups,
      priorities: priorities,
      likely: likely,
      selectiveService: a.age === '18-24' || a.age === '25plus',
      workAuthConcern: a.work_auth === 'no',
      employerAngle: a.situation === 'full-time' || a.situation === 'part-low',
    };
  }

  // Self-tests (run only on qualify.html#selftest — silent unless something fails).
  function runQualifyTests() {
    const eq = (got, want, msg) => console.assert(got === want, msg + ' (got ' + got + ', want ' + want + ')');
    let r = classifyQualify({ live_ma: 'yes', age: '25plus', situation: 'laid-off', assistance: 'no', income_low: 'no', veteran: 'no', work_auth: 'yes', field: 'it' });
    eq(r.likely, true, 'laid-off MA adult is a likely fit');
    console.assert(r.groups.indexOf('WIOA Dislocated Worker') !== -1, 'laid-off -> Dislocated Worker');
    console.assert(r.groups.indexOf('WIOA Adult') !== -1, '25+ -> Adult');
    r = classifyQualify({ live_ma: 'yes', age: '18-24', situation: 'full-time', assistance: 'yes', income_low: 'no', veteran: 'no', work_auth: 'yes', field: 'healthcare' });
    console.assert(r.groups.indexOf('WIOA Youth (ages 14–24)') !== -1, '18-24 -> Youth');
    eq(r.likely, true, 'public assistance is a priority -> likely');
    eq(r.employerAngle, true, 'full-time -> employer angle');
    r = classifyQualify({ live_ma: 'no', age: '25plus', situation: 'unemployed', assistance: 'no', income_low: 'no', veteran: 'no', work_auth: 'yes', field: 'trades' });
    eq(r.inMA, false, 'not in MA flagged');
    eq(r.likely, false, 'not in MA -> not likely (this check is MA-only)');
    r = classifyQualify({ live_ma: 'yes', age: '25plus', situation: 'full-time', assistance: 'no', income_low: 'no', veteran: 'no', work_auth: 'yes', field: 'it' });
    eq(r.likely, false, 'full-time no-priority -> not a strong fit');
    eq(r.selectiveService, true, '25+ -> show Selective Service note');
    r = classifyQualify({ live_ma: 'yes', age: 'under18', situation: 'unemployed', assistance: 'no', income_low: 'yes', veteran: 'no', work_auth: 'unsure', field: 'unsure' });
    console.assert(r.groups.indexOf('WIOA Youth (ages 14–24)') !== -1 && r.groups.indexOf('WIOA Adult') === -1, 'under 18 -> Youth only');
    eq(r.selectiveService, false, 'under 18 -> no Selective Service note');
    console.log('[qualify] self-tests complete');
  }

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

    // Field -> guide map (Site Structure Spec v1.5 location-neutral slugs).
    const FIELD = {
      healthcare: { label: 'healthcare', guide: 'healthcare-careers.html' },
      it:         { label: 'information technology', guide: 'it-careers.html' },
      trades:     { label: 'the skilled trades', guide: 'skilled-trades-careers.html' },
      unsure:     { label: 'a new field', guide: 'career-paths.html' },
    };
    const FUNDED_STEPS = [
      'Find your MassHire Career Center. See the list of locations at <a class="link-yellow" href="https://www.mass.gov/info-details/masshire-career-center-locations" target="_blank" rel="noopener">mass.gov</a> and contact the nearest one.',
      'Register on JobQuest at <a class="link-yellow" href="https://jobquest.mass.gov" target="_blank" rel="noopener">jobquest.mass.gov</a> — you need an account before you can get training funding.',
      'Attend a Training Information Meeting at your career center.',
      'Ask about an Individual Training Account (ITA). If you collect unemployment, ask about Section 30 to keep your checks coming while you train.',
      'Choose a state-approved (ETPL) training program in your field.',
    ];

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

    const answers = () => {
      const d = new FormData(qForm);
      return {
        live_ma: d.get('live_ma'), age: d.get('age'), situation: d.get('situation'),
        assistance: d.get('assistance'), income_low: d.get('income_low'),
        veteran: d.get('veteran'), work_auth: d.get('work_auth'), field: d.get('field'),
      };
    };

    // Auto-advance; the LAST question shows results instead of a next step.
    steps.forEach((step, i) => {
      if (!step.dataset.autoadvance) return;
      step.querySelectorAll('input[type="radio"]').forEach((radio) => {
        radio.addEventListener('change', () => {
          if (i < steps.length - 1) show(i + 1);
          else showResults();
        });
      });
    });

    if (backBtn) backBtn.addEventListener('click', () => {
      if (result.classList.contains('is-active')) {
        result.classList.remove('is-active');
        show(steps.length - 1);
      } else {
        show(idx - 1);
      }
    });

    function el(sel) { return result.querySelector(sel); }
    function toggle(sel, on) { const n = el(sel); if (n) n.hidden = !on; }
    function setText(sel, t) { const n = el(sel); if (n) n.textContent = t; }
    function setList(sel, items) {
      const n = el(sel); if (!n) return;
      n.innerHTML = items.map((s) => '<li>' + s + '</li>').join('');
    }

    function showResults() {
      const a = answers();
      const r = classifyQualify(a);
      const field = FIELD[a.field] || FIELD.unsure;

      if (!r.inMA) {
        setText('.result-head', 'This check covers Massachusetts.');
        setText('.result-body', 'WIOA training funds exist in every state, but the steps below are for Massachusetts. Use the link to find your local American Job Center — and you can still explore the field you picked.');
        toggle('.result-groups', false);
        toggle('.result-priority', false);
        toggle('.result-steps-wrap', false);
        toggle('.result-notma', true);
        toggle('.result-selective', false);
        toggle('.result-workauth', r.workAuthConcern);
        toggle('.result-employer', false);
      } else {
        if (r.likely) {
          setText('.result-head', 'You may be a good candidate for WIOA-funded training.');
          setText('.result-body', 'Your answers line up with the groups WIOA prioritizes. Only a MassHire career center can decide, but here’s exactly how to check:');
        } else {
          setText('.result-head', 'You may still have options worth checking.');
          setText('.result-body', 'Your answers don’t point to the highest-priority groups, but WIOA’s adult program is broad and eligibility is decided locally. Here’s how to check, plus other ways to pay:');
        }
        setList('.result-group-list', r.groups.length ? r.groups : ['WIOA Adult']);
        toggle('.result-groups', true);
        toggle('.result-priority', r.priorities.length > 0);
        if (r.priorities.length) setList('.result-priority-list', r.priorities);
        setList('.result-steps', FUNDED_STEPS);
        toggle('.result-steps-wrap', true);
        toggle('.result-notma', false);
        toggle('.result-selective', r.selectiveService);
        toggle('.result-workauth', r.workAuthConcern);
        toggle('.result-employer', r.employerAngle);
      }

      const guideBtn = el('.result-guide');
      if (guideBtn) {
        guideBtn.setAttribute('href', field.guide);
        guideBtn.textContent = field.label === 'a new field' ? 'Explore career paths' : 'Explore ' + field.label;
      }
      setText('.result-field-note',
        'We’ll also let you know when Career Skills Center launches training in ' + field.label + '.');

      steps.forEach((s) => s.classList.remove('is-active'));
      if (fill) fill.style.width = '100%';
      if (label) label.textContent = 'Your results';
      if (backBtn) backBtn.hidden = false;
      result.classList.add('is-active');
      result.setAttribute('tabindex', '-1');
      result.focus();
      result.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    // Optional "email me these steps": posts answers + contact to submit.php.
    qForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      if (status) { status.className = 'form-status'; status.textContent = ''; }
      const email = qForm.querySelector('[name="email"]');
      if (!email || !email.value.trim()) {
        if (status) { status.textContent = 'Enter your email so we can send your steps.'; status.classList.add('is-error'); }
        if (email) email.focus();
        return;
      }
      if (!email.checkValidity()) { email.reportValidity(); return; }

      const data = new FormData(qForm);
      data.set('page', window.location.pathname);
      if (submitBtn) submitBtn.disabled = true;
      if (status) status.textContent = 'Sending…';
      try {
        const res = await fetch(qForm.action, { method: 'POST', body: data, headers: { Accept: 'application/json' } });
        const json = await res.json().catch(() => ({}));
        if (!res.ok || !json.ok) throw new Error(json.error || 'Submission failed');
        if (typeof gtag === 'function') gtag('event', 'form_submit', { source: 'qualify' });
        if (status) { status.textContent = 'Sent! Check your email for your next steps.'; status.classList.add('is-success'); }
      } catch (err) {
        if (status) { status.textContent = 'Sorry, that didn’t send. Please email info@careerskillscenter.com or call (617) 544-7155.'; status.classList.add('is-error'); }
        if (submitBtn) submitBtn.disabled = false;
      }
    });

    if (window.location.hash === '#selftest') runQualifyTests();
    show(0);
  }

  /* ---------- Express reimbursement calculator (staff-training-grants.html) ----
     Pure calcExpress() + a live UI. All figures come from js/site-config.js.
     Estimate only — CommCorp sets final amounts. Self-tests run on #selftest. */
  function calcExpress(inp, cfg) {
    const rate = inp.small ? cfg.EXPRESS_RATE_SMALL : cfg.EXPRESS_RATE_LARGE;
    const employees = Math.max(0, inp.employees || 0);
    const cost = Math.max(0, inp.costPerEmployee || 0);
    const perPersonUncapped = cost * rate;
    const perPerson = Math.min(perPersonUncapped, cfg.EXPRESS_MAX_PER_PERSON_PER_COURSE);
    const gross = perPerson * employees;
    const total = Math.min(gross, cfg.EXPRESS_ANNUAL_CAP_PER_COMPANY);
    return {
      rate: rate, perPerson: perPerson, gross: gross, total: total,
      cappedPerson: perPersonUncapped > cfg.EXPRESS_MAX_PER_PERSON_PER_COURSE,
      cappedCompany: gross > cfg.EXPRESS_ANNUAL_CAP_PER_COMPANY,
    };
  }

  function runExpressTests() {
    const cfg = window.CSC || window.SITE_CONFIG; if (!cfg) return;
    const eq = (g, w, m) => console.assert(g === w, m + ' (got ' + g + ', want ' + w + ')');
    let r = calcExpress({ employees: 5, costPerEmployee: 2000, small: true }, cfg);
    eq(r.perPerson, Math.min(2000 * cfg.EXPRESS_RATE_SMALL, cfg.EXPRESS_MAX_PER_PERSON_PER_COURSE), 'small perPerson');
    eq(r.total, Math.min(r.perPerson * 5, cfg.EXPRESS_ANNUAL_CAP_PER_COMPANY), 'small total capped by company');
    r = calcExpress({ employees: 1, costPerEmployee: 100000, small: true }, cfg);
    eq(r.cappedPerson, true, 'huge cost -> per-person cap hit');
    eq(r.perPerson, cfg.EXPRESS_MAX_PER_PERSON_PER_COURSE, 'per-person capped at config max');
    r = calcExpress({ employees: 100, costPerEmployee: 3000, small: false }, cfg);
    eq(r.cappedCompany, true, 'many employees -> company cap hit');
    eq(r.total, cfg.EXPRESS_ANNUAL_CAP_PER_COMPANY, 'total capped at company max');
    console.log('[express] self-tests complete');
  }

  const calc = document.querySelector('.express-calc');
  if (calc) {
    const cfg = window.CSC || window.SITE_CONFIG || {};
    const empEl = calc.querySelector('#calc-emp');
    const costEl = calc.querySelector('#calc-cost');
    const totalEl = calc.querySelector('.calc-total');
    const detailEl = calc.querySelector('.calc-detail');
    const money = (n) => '$' + Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    const recalc = () => {
      const small = (calc.querySelector('input[name="calc_size"]:checked') || {}).value !== 'large';
      const r = calcExpress({
        employees: parseInt(empEl.value, 10) || 0,
        costPerEmployee: parseFloat(costEl.value) || 0,
        small: small,
      }, cfg);
      if (totalEl) totalEl.textContent = money(r.total);
      if (detailEl) {
        const bits = ['At up to ' + Math.round(r.rate * 100) + '% of eligible cost, about ' +
          money(r.perPerson) + ' per person.'];
        if (r.cappedPerson) bits.push('Per-person amount is capped at ' + money(cfg.EXPRESS_MAX_PER_PERSON_PER_COURSE) + '.');
        if (r.cappedCompany) bits.push('Total is capped at the annual company max of ' + money(cfg.EXPRESS_ANNUAL_CAP_PER_COMPANY) + '.');
        detailEl.textContent = bits.join(' ');
      }
    };
    calc.addEventListener('input', recalc);
    calc.addEventListener('change', recalc);
    recalc();
    if (window.location.hash === '#selftest') runExpressTests();
  }

  /* ---------- Footer year ---------- */
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
