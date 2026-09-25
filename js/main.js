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

        if (status) {
          status.textContent = 'Thanks! We’ll be in touch soon.';
          status.classList.add('is-success');
        }
        form.reset();
        if (typeof gtag === 'function') {
          gtag('event', 'form_submit', { source: data.get('source') || 'contact' });
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

  /* ---------- Footer year ---------- */
  const year = document.getElementById('year');
  if (year) year.textContent = String(new Date().getFullYear());
})();
