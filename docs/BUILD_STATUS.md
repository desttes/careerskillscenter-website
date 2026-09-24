# Build Status — Code → Strategy log

Claude Code updates this file at the end of every session. The strategy side (Cowork + the "ETPL Massachusetts" Project) reads it.

## Current state
- Brief version being built: `docs/BUILD_BRIEF.md` v1.0 (Sept 24, 2026)
- **Blog rebuilt (§2 + §5):** placeholder posts removed; 8 real launch drafts written and live locally. Everything else in the brief (nav/footer restructure, `js/site-config.js`, For Employers pages, qualify.html, Ways to Pay rewrite, Outcomes, MA landing pages, calculator) is **not started yet**.
- Status: **local only — NOT deployed.** Awaiting Emilio's review of the 8 drafts before anything goes live.

## Session log
<!-- Newest first. For each session: date · what was built (files/URLs) · status (local only / deployed) · TODOs -->

### 2026-09-24 (later) — Pillar post expanded from docs/content/ (brief v1.1)
Picked up the strategy-side handoff (commit `9aee0c0`: brief bumped to v1.1 + `docs/content/` pack). Expanded **post #1 only** this pass, per request.
- **`/blog/free-job-training-massachusetts.html`** rewritten from `docs/content/01-...md`: now **~2,004 words** (target 2,000–2,500). Added: the "5 main ways to pay" comparison table; "How the system is organized" (16 regions → boards → centers → ETPL); dedicated sections for **WIOA/ITA, Section 30/TOP** (get paid while training, 20-hr/wk, 26 extra weeks, 20th-week deadline), **Donnelly grants**, **Express (employer-paid)**, and payment plans; a "Which option fits you?" mapping; a 6–8 week timeline box; a "What to bring" checklist (with a placeholder for the future PDF download); JobQuest-first "honest first step"; a bottom-line close; and an **expanded 9-question FAQ** (visible + FAQPage schema kept in sync). Read time bumped to 12 min.
- Government sources linked inline: mass.gov (Section 30, MassHire locator), jobquest.mass.gov, commcorp.org (Donnelly).
- `[VERIFY]` markers left where the pack asked: career-center count, Donnelly totals, locator URL; plus the checklist-download `[TODO]`.
- Verified: builds clean; JSON-LD valid (BlogPosting + 9-Q FAQPage); no console errors; no page overflow; table scrolls within its wrapper on narrow screens.
- **Still at original draft length (not yet expanded):** posts #2–#8. Next pass. Post #5 salary numbers: per your call, I'll **fetch BLS OEWS May 2025 MA** medians (SOC codes in `docs/content/05`) when I expand it.

### 2026-09-24 — Blog cleanup + 8 launch drafts (§2, §5)
**Built (local only, all DRAFTS marked with `<!-- DRAFT – facts to verify: … -->`):**
- Rewrote `blog.html` index: removed the 6 placeholder cards + the "Placeholder content" notice + the disabled "More articles coming soon" button. Featured post is now the funding pillar. Category filter pills updated to the final 5 (Paying for Training · Medical · Information Technology · Skilled Trades · Career Advice) — still **visual-only** (not wired to filtering yet).
- 8 article pages, each at `/blog/<slug>.html` per the brief:
  1. `/blog/free-job-training-massachusetts.html` — pillar, ~2,000 words, FAQ + FAQPage schema
  2. `/blog/wioa-eligibility-massachusetts.html`
  3. `/blog/masshire-training-voucher.html`
  4. `/blog/is-wioa-training-free.html`
  5. `/blog/highest-paying-certifications-massachusetts.html` — salary figures deliberately omitted; marked `[VERIFY: BLS OES MA]`
  6. `/blog/can-medical-billing-coding-be-learned-online.html`
  7. `/blog/can-you-learn-it-support-online.html`
  8. `/blog/can-you-learn-a-trade-online.html`

**Build-system changes (in `tools/build-pages.py`):**
- Added **subdirectory support** so blog posts can live at `/blog/…` while sharing the same header/footer/dialog. The generator now rewrites every relative link one level up (`../`) for nested pages, and creates the `blog/` folder on build.
- Added an `@@EXTRAHEAD@@` head slot for per-page JSON-LD, and helpers: `article()`, `post_cta()`, `related()`, `faq_ld()` (FAQPage), `article_ld()` (BlogPosting).
- Added blog-article CSS (`.article-title`, `.article-meta`, `.post-cta`, related grid) to `css/style.css`; extended `.dot-sep` to article meta.
- `sitemap.xml` now auto-includes all 8 blog URLs (23 URLs total).

**Verified:** builds clean (25 pages); all JSON-LD parses; no console errors; no horizontal scroll at 375px; compliance grep clean (no ETPL/WIOA-approval or Express-listing claims; all 8 use "may qualify" / "working toward approval" language; funding disclosure box matches the `FUNDING_ETPL_APPROVED = false` wording).

**Compliance notes for review:**
- Posts explain the **state** funding landscape (WIOA / MassHire / ITA) generally — they do **not** claim CSC is ETPL-approved or that CSC training is free/WIOA-funded. Each funding post carries the standard disclosure box.
- **No funding dollar amounts** are stated (WIOA/ITA caps vary by career center and are not in `site-config.js`). No invented salaries, outcomes, or pass rates — all such spots are `[VERIFY …]` placeholders.
- `js/site-config.js` (brief §6) does **not exist yet** — this session didn't need it. It's the logical first step for the next session (nav/employer/calculator work all read from it).

**Open TODOs on the blog:**
- Emilio to review + approve the 8 drafts and resolve every `[VERIFY …]` / DRAFT note before publish.
- Post #1 references a **"Paying for Training in Massachusetts" checklist download** (brief §3.1/§5) — not built (needs the form backend + a PDF from Emilio). Currently the pillar's CTA points to Ways to Pay instead.
- CTAs point to `student-financing.html` (Ways to Pay) and the contact dialog because **`qualify.html` doesn't exist yet**. Swap in `qualify.html` links once it's built.
- Category filter pills are visual-only; wire to filtering/per-category pages later.
- Verify CSC program facts referenced in posts (program lengths, CompTIA level, AAPC exam details) against `it-support-specialist.html` / `medical-billing-coding.html`.

## Questions for strategy
<!-- Anything unclear or anything you disagree with in the brief. Emilio brings these to the Cowork session. -->
- **Form backend: DECIDED → cPanel PHP mailer** (Emilio, this session). Next build session will implement a small PHP mailer on the Namecheap host that emails submissions to info@careerskillscenter.com, with a hidden `source` field on every form, before building `qualify.html` and the employer forms.
- Checklist PDF ("Paying for Training in Massachusetts"): Emilio to provide the content so the pillar post's email-capture download can be wired up.
- Salary/wage figures for post #5 and the MA landing pages: confirm the plan is to pull from BLS OES Massachusetts and cite the source (no invented numbers).

## Decisions that differ from the brief
<!-- What you changed and why -->
- **Blog post URLs = real `/blog/<slug>.html` subdirectory** (per brief §2), which required teaching `build-pages.py` to handle nested pages (relative-link rewriting). The older `docs/PAGES.md` article template suggested flat `blog-<slug>.html` filenames; the brief supersedes it. `PAGES.md` should be updated to match if this approach is approved.
- Pillar post CTA points to **Ways to Pay** instead of the checklist download, because the download depends on the (not-yet-built) form backend + PDF. Will switch once those exist.
