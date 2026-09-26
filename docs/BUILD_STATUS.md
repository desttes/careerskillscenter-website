# Build Status — Code → Strategy log

Claude Code updates this file at the end of every session. The strategy side (Cowork + the "ETPL Massachusetts" Project) reads it.

## Current state (as of 2026-09-26)
- Now building: **`docs/GUIDE_MODE_SPEC.md` v1.4 (guide mode)**, which supersedes the Option A pre-launch spec. Brief `v1.3` still applies where the guide spec is silent.
- **Guide-mode steps 1–7 are DONE locally (not deployed).** See the 2026-09-26 session entry below. Steps 8 (For Employers) and 9 (blog CTA rework) are not started.

**LIVE on careerskillscenter.com:**
- The **contact-form backend** (`submit.php`, cPanel PHP mailer) — leads deliver to `vcanal@careerskillscenter.com`, confirmed working after fixing cPanel Email Routing to Remote (mailboxes are on Namecheap Private Email). GA4 `form_submit` fires.
- **Fake homepage testimonials removed.**

**Done LOCALLY, NOT deployed (awaiting Emilio's review + OK):**
- **Blog:** 8 launch posts, all expanded to target length, fact-checked against `VERIFICATION_LOG.md`, program-facts-compliant, real Sept 25 dates. Still marked `<!-- DRAFT -->`. Excluded from deploy until approved.
- **Option A pre-launch rework** (the whole site): program/tuition/careers/faq/admissions/Ways-to-Pay/about/homepage reworked to "program in development"; site-wide **interest-list form** (routes to the live mailer with `source=interest-list`); `programs.html` → redirect; `llms.txt` updated. Spec acceptance grep clean.

- **`qualify.html` (§3.2)** — the "See If You Qualify" 60-second wizard. Built and verified locally, posts to the live mailer with `source=qualify`. **Not yet linked in the nav** (nav restructure §1 is a separate task).

**Not started (later brief work):** nav/footer restructure (§1), `js/site-config.js`, the For Employers pages + reimbursement calculator (§4), the 4 MA landing pages (§3.4). `outcomes.html` withdrawn (no real graduates).

**Immediate next step:** decide whether to deploy the Option A rework + interest form (blog stays excluded). Everything is committed on `main`.

## Session log
<!-- Newest first. For each session: date · what was built (files/URLs) · status (local only / deployed) · TODOs -->

### 2026-09-26 — Guide mode (GUIDE_MODE_SPEC v1.4) steps 1–7 (LOCAL, not deployed)
Built the honest "guide to careers and funding in Massachusetts" that routes people **outward** to the state. All work is committed on `main` in seven step-by-step commits and verified in the in-app browser (no console errors, mobile nav works, wizard routing exercised). **Nothing deployed.**

**Step 1 — Groundwork.** New **`js/site-config.js`** — plain global `window.SITE_CONFIG` (alias `CSC`) with `SITE_MODE="guide"`, `COURSES_LIVE={healthcare,it,trades:false}`, the compliance flags (`FUNDING_ETPL_APPROVED`/`EXPRESS_PROVIDER_LISTED=false`), the Express figures (all still VERIFY), and the verified MassHire/JobQuest URLs. Loaded (cache-busted) before `main.js` on every page and on `index.html`.

**Step 2 — Nav + footer** (`index.html`, propagated by build). New menu: **Career Paths** (Healthcare · IT · Skilled Trades · All Career Paths) · **Resources** (Blog · Ways to Pay · Check Your Funding Options · FAQ) · **About** · **Contact**; header button **"Check Your Options" → qualify.html**. Footer mirrors it; broken "Catalog" link removed. (For Employers deliberately omitted until step 8 pages exist.)

**Step 3 — Three career-field guides** (new pages, replace the old program pages):
- `healthcare-careers-massachusetts.html`, `it-careers-massachusetts.html`, `skilled-trades-careers-massachusetts.html`.
- Each has an intro, **role cards** (per role: what it is · MA median pay with SOC cited · training path · sourced MA license/cert · honest "train online?"), a shared **how-to-pay** block, an **outward next-step** (MassHire + JobQuest), a **FAQ with FAQPage schema**, an interest-list secondary CTA, and related guides. **No `Course` schema.**
- **All pay = BLS OEWS May 2025, Massachusetts**, pulled via the in-app browser (bls.gov/oesm25st.zip still 403 curl). Logged in `VERIFICATION_LOG.md` **H1**. EKG tech and entry cyber/cloud carry explicit "broad category / entry pays less" caveats so the numbers aren't misleading.
- **MA licensing facts sourced** (`VERIFICATION_LOG.md` **H2**): CNA (DPH Nurse Aide Registry), pharmacy tech (Board of Pharmacy license, required even if nationally certified), electrician (8,000 hrs + 600-hr course), plumber (5,100 + 300 hrs), HVAC/refrigeration (state license + EPA 608), welder (no state license; AWS voluntary). Voluntary healthcare certs framed as general industry info.

**Step 4 — `career-paths.html` hub.** Cards for the 3 fields → their guides, plus a "Check Your Options" prompt and interest list. 301 target for our-programs/programs.

**Step 5 — `qualify.html` reworked to an outward funding-options tool.** Title/H1 → "Check Your Options" / "Find out what training help you may qualify for." Q1 → "Which field interests you?" (Healthcare/IT/Skilled Trades/Not sure). Email required, mobile optional, consent reworded. **Removed the "an advisor will text you" promise.** Result screen is **personalized outward next steps** (never a yes/no verdict): funded-fit shows the 5 MassHire/JobQuest/TIM/ITA-Section 30/state-approved-program steps + the 3 funding blog links; employer and other-ways-to-pay branches; always links the chosen field guide + an interest-list line. Logic rewritten in `js/main.js` (`routeResult`); both branches verified.

**Step 6 — Retired pages 301'd.** New **`.htaccess`** with server 301s + meta-refresh/canonical stubs (generated from a `REDIRECTS` map in `build-pages.py`) for: medical-billing-coding, it-support-specialist, skilled-trades, our-programs, programs, tuition, admissions, career-services, team, media. All dropped from the sitemap; a career-support paragraph was folded into `about.html`. Verified a stub redirects (tuition → student-financing).

**Step 7 — Remaining pages.** `index.html` reframed to "your guide to careers & funding in MA" (guide hero, how-funding section, latest guides, interest band; metadata updated). `student-financing.html` = full **Ways to Pay for Training in Massachusetts** guide (WIOA/ITA, Section 30, grants, employer-paid/Express, payment plans, private lenders, outward links, disclosure kept). `faq.html` rewritten around the guide. `contact.html` campus/parking placeholders removed. `llms.txt` rewritten as a MA career-and-funding guide.

**Course-dependent tracking.** `docs/COURSE_CONTENT_REGISTER.md` is current: every built row (R-NAV, R-HOME, R-HC, R-IT, R-TR, R-HUB, R-QUALIFY, R-PAY, R-FAQ, R-ABOUT, R-IFORM) has a matching `<!-- COURSE-DEPENDENT: R-xx -->` marker in source, with the "Location in source" column filled. R-LLMS lives in `llms.txt` (tracked there). R-BLOG/R-EMP/R-SCHEMA belong to steps 8–9 and are not marked yet.

**Verification.** Build clean (20 pages + 10 redirect stubs, sitemap 21 URLs). Root-HTML pre-deploy grep **clean** (no `[VERIFY]`/`DRAFT`). PRE_LAUNCH acceptance greps still clean (no $299/$329, 8/11 weeks, 89/117 hrs, FC0-U71, Marcus/David/alumni/graduate). Compliance grep clean (no "WIOA-funded"/"ETPL-approved"/"our course"/Express-listing claims; the only "ETPL-approved" hit is a blog draft describing the state ETPL system generically). No links to retired pages in any live page.

**Ready for Emilio's review (all local, not deployed):**
- New pages: `career-paths.html`, `healthcare-careers-massachusetts.html`, `it-careers-massachusetts.html`, `skilled-trades-careers-massachusetts.html`.
- Reworked: `index.html`, `qualify.html`, `student-financing.html`, `faq.html`, `about.html`, `contact.html`, nav/footer (all pages), `llms.txt`.
- New infra: `js/site-config.js`, `.htaccess`, 10 redirect stubs.
- Sources: `VERIFICATION_LOG.md` H1/H2.

**Open TODOs / notes for Emilio:**
- **Deploy is not done** (per instructions). When deploying: also upload `.htaccess` and `js/site-config.js`, and re-`chmod 644`. The auto-generated `sitemap.xml` lists the 8 blog drafts — keep excluding blog (and use the blog-free sitemap) until the drafts are approved, as before.
- **Express Program figures in `site-config.js` are still VERIFY** with express@commcorp.org (needed for step 8 employer pages/calculator, not used in steps 1–7).
- **Steps 8 (For Employers) and 9 (blog CTA rework) not started.** In step 9, the 8 blog posts' CTAs should be repointed to the field guides / `qualify.html` / MassHire (currently interim to contact/interest), and CSC mentions marked COURSE-DEPENDENT (R-BLOG).
- The old full page bodies for the retired program/enrollment pages remain in `build-pages.py` (unused, behind the `REDIRECTS` map) so they can be restored in course mode.

### 2026-09-25 (previous work below) —

### 2026-09-25 (later) — Built `qualify.html` — "See If You Qualify" wizard (§3.2) (LOCAL, not deployed)
Built the first lead magnet: a 6-step, one-question-per-screen wizard with a progress bar. **It captures a lead; it never renders a yes/no eligibility verdict** (only a MassHire career center decides).
- **`tools/build-pages.py`** — new `qualify.html` page block (title/H1 per brief §3.2) + a small `_q_opts()` helper for the radio option-cards. 6 steps: program · live in MA · work situation · public assistance · would employer pay · contact (first name/mobile/email required, preferred language, SMS consent). Hidden `source=qualify` + honeypot. Steps 1–5 auto-advance on selection.
- **`js/main.js`** — self-contained wizard module, feature-detected by `.qualify-form` (deliberately **not** `.contact-form`, so the shared handler ignores it). Handles step nav, progress bar, Back, per-step focus; on submit it validates the contact fields, POSTs to `submit.php`, fires GA4 **`form_submit` with `source=qualify`** (brief §2), then reveals a **soft-routing result screen**:
  - Funded fit (live in MA **and** [unemployed / laid off / part-time-or-low-wage **or** on public assistance]) → "You may be a good fit for state-funded training. An advisor will text you within 1 business day." Because **`FUNDING_ETPL_APPROVED` is false**, it appends "We'll also show you options to start now." (brief §3.2).
  - Employer = Yes/Maybe → adds the "your employer may be reimbursed by Massachusetts" line.
  - Otherwise → "Let's find the best way for you to pay. An advisor will text you within 1 business day."
- **`css/style.css`** — `.qualify-*` styles (progress bar, big tap-target option cards, step show/hide, light-section field styling, result screen).
- **Verified** (own local server, in-app browser): builds clean (26 pages, sitemap 24 URLs); both routing branches produce the correct copy; empty-contact submit is blocked by native validation; **no console errors**; **no horizontal overflow at 375px**; result screen renders (icon, headline, body, conditional employer line, CTAs, disclaimer). **Mandatory pre-deploy grep clean** on `qualify.html` (no `[VERIFY]`/`DRAFT`); compliance grep clean (no ETPL/WIOA-approval or Express-listing claims).
- **Decisions / TODOs:**
  - **`site-config.js` still doesn't exist**, so the `FUNDING_ETPL_APPROVED=false` result copy is written directly in `main.js`. When the config lands, make the two result strings flag-driven.
  - **`employers.html` (§4) doesn't exist yet** → the result's employer line links to `student-financing.html` (Ways to Pay) as interim. Swap to `employers.html` once §4 is built.
  - **Not linked in nav yet** — header CTA is still "Get in Touch"/dialog. Brief §1 wants the header CTA changed to "See If You Qualify" → `qualify.html` and an Admissions submenu entry; that's the separate nav-restructure task. `qualify.html` is in the sitemap and reachable by URL now.
  - Spanish/Portuguese versions are a later TODO (brief §3.2).


### 2026-09-25 (later) — Option A pre-launch rework across the site (LOCAL, not deployed)
Implemented the full "Program in development" rework from `docs/PRE_LAUNCH_SITE_SPEC.md`, now that the mailer works.
- **New shared pieces** (`build-pages.py`): `DEV_STATUS` line, `dev_hero()`, and `interest_form()` — the site-wide interest-list form (first name, email, mobile optional, program [preselected], preferred language, "how would you likely pay", SMS consent; hidden `source=interest-list` + honeypot; JS adds `page`). `main.js` fires a GA4 **`interest_list_signup`** event (program + pay_method) and shows the form's `data-success` message. `css`: light-background `.interest-form` overrides, `.consent-row`, `.pcard-badge`.
- **Program pages → "in development" template:** `it-support-specialist.html`, `medical-billing-coding.html`, `skilled-trades.html` rebuilt — status line, "about the career" with **BLS Massachusetts** median pay (IT $75,070; medical $60,350), "what we're planning" (general topics, "plan to align with an industry-recognized certification"), "what we'll tell you before enrollment," the interest form, and related blog posts. Removed all length/hours/price/credential/"Course Overview"/"How to Enroll".
- **`our-programs.html`:** "In development"/"Coming soon" badges, career-focused card text, cert-stacking claims removed, interest form.
- **`tuition.html`:** replaced the fake price table + invented ROI comparison with "Pricing coming soon" + ways-we-plan-to-help + interest form.
- **`career-services.html`:** reframed to future tense; removed the Alumni Network, TBD outcomes box, "Hire Our Graduates," graduate photos and "included in your tuition."
- **`faq.html`:** rewrote program/credential/cost/VA/campus answers to "in development / join the interest list" wording.
- **`admissions.html`:** "enrollment isn't open yet," future-tense steps + requirements, dropped the start-dates table; interest form.
- **`student-financing.html` → "Ways to Pay":** planned options only (no terms), funding-guide links, working-toward-approval disclosure, interest form.
- **`about.html` + homepage:** softened instructor/lab/campus/"graduates" claims to planned tense; homepage "What We Do" + Step-by-Step reframed to the interest list; testimonials already gone.
- **`programs.html`** (deprecated, unlinked): converted to a redirect to `our-programs.html` so it can't ship stale specifics.
- **`llms.txt`:** rewritten to "in development," removed Tech+/FC0-U71/CPC/CPB/8-11 weeks, "offering" → "developing".
- **Verified:** builds clean; **spec acceptance grep clean** (no $299/$329, hours, weeks, FC0-U71, graduate/alumni/Marcus/David in root HTML; llms.txt clean); no `[VERIFY]`/`DRAFT` in root HTML; 9 interest forms placed; interest form renders correctly on light sections; `programs.html` redirects; homepage/our-programs/IT page render with no console errors or overflow.
- **TODOs:** `contact.html` still says "campus"/parking TBD and `team.html`/`media.html` remain unlinked placeholders (out of this pass — convert or redirect later). Not deployed — awaiting review. When deploying, the `put *.html` list already covers these; consider adding an `.htaccess` 301 for `programs.html` too.

### 2026-09-25 (later) — Fixed live email delivery (mail routing)
The live form submitted OK but no email arrived. Diagnosis: `mail()` returned success (server accepted), but the domain's mailboxes are on **Namecheap Private Email** (MX = `mx1/mx2.privateemail.com`), while cPanel's **Email Routing** was delivering locally — so mail went to a non-existent local mailbox and was lost.
- **Fix (Emilio, in cPanel):** set Email Routing for `careerskillscenter.com` to **Remote Mail Exchanger** — confirmed working, the form now delivers to `vcanal@careerskillscenter.com`.
- **Code:** added the `-f` envelope sender to `mail()` (deliverability best practice). A temporary server-side diagnostic log was used to confirm `mail()` returned true, then removed; the mailer is back to its clean form.
- **Contact form is now fully working end to end, live.**

### 2026-09-25 (later) — DEPLOYED to live site (Emilio's OK)
Emilio authorized the live deploy and confirmed the `vcanal@careerskillscenter.com` mailbox exists. Pushed over SFTP:
- **Deployed:** all root `*.html` (form wiring in the shared dialog + testimonials removed from `index.html`), **`submit.php`** (the PHP mailer), `css/style.css`, `js/main.js`.
- **Excluded on purpose:** the 8 `blog/` drafts (still `<!-- DRAFT -->`, awaiting approval) and `sitemap.xml` (the local one now lists the not-yet-deployed blog URLs, which would 404 for crawlers — the live sitemap keeps the 15 public pages).
- **Verified live:** homepage HTTP 200; no `Marcus`/testimonial-quote content remains (only the removal comment); the contact form is wired to `submit.php`; `submit.php` GET → 405 and a honeypot POST → `{"ok":true}` (PHP executes, no stray email); `css`/`js` return 200.
- **Not yet tested live:** one real end-to-end lead email to `vcanal@` — recommend Emilio submit the live contact form once and confirm the email arrives.
- **Still live-but-unchanged (Option A backlog):** program/tuition pages keep their placeholder prices/hours/credentials; `llms.txt` still references old specifics; blog not published.

### 2026-09-25 (later) — Built the cPanel PHP mailer (form backend)
The form backend Emilio chose (cPanel PHP mailer) is built and wired. Local only — **not deployed**.
- **`submit.php`** (new, at docroot) — plain-PHP mailer, no database. Emails submissions to `vcanal@careerskillscenter.com` (`CSC_RECIPIENT`); visitors only ever see the public `info@careerskillscenter.com`. Features: POST-only, honeypot (`company_website`) that silently drops bots, required name + valid email, per-field length caps, mail-header-injection protection (strips CR/LF), a friendly body with human labels, and the hidden **`source`** field + JS-added **`page`** in every email. Returns JSON for the AJAX path and supports a `_redirect` no-JS fallback. Core logic is a pure, testable function (`csc_process`).
- **Wired both contact forms** (`contact-dialog` in `index.html`, `contact-page` in `build-pages.py`): `action="submit.php"`, hidden `source`, honeypot field. On blog subdir pages the action correctly relativizes to `../submit.php`.
- **`js/main.js`** — replaced the demo handler with a real `fetch` POST: client validation, "Sending…" state, success/error messages, a failure fallback ("email/call us"), and a GA4 **`form_submit`** event with the `source` parameter (brief §2).
- **`css/style.css`** — added `.hp-field` (visually-hidden honeypot).
- **Verified** (PHP 8.5 CLI + `php -S` + the in-app browser): GET→405, honeypot→drop, bad email→422, valid→200 with a correct logged email (subject `[source] …`, Reply-To = visitor, all fields + source + page), header-injection neutralized; browser dialog submit → 200, success message shown, GA event, no console errors.
- **Deploy notes** added to `PROJECT-HANDOFF.md` §5/§6 (upload `submit.php`, `chmod 644`, on-domain `From` for deliverability; `blog/` still excluded as drafts).
- **TODO for Emilio:** confirm the `vcanal@careerskillscenter.com` mailbox/alias exists; after deploy, send one real test submission and confirm the email arrives; optionally create a `no-reply@` alias and set `CSC_FROM`.

### 2026-09-25 (later) — Removed fake homepage testimonials (Option A, spec §7)
- **`index.html`** — deleted the entire Testimonials section (the fabricated "Marcus, Electrical Technician graduate" and "David, IT Support Specialist graduate" quotes, including the "helped me earn my CompTIA A+ and Network+" program specifics). Left an HTML comment noting why and that only real, consenting-student testimonials may replace it. The homepage now closes on the "Ready to Start?" steps band → footer (no gap).
- Not replaced with any quotes (per spec). Did **not** add the optional "Why we're building Career Skills Center" section — that can be added later if wanted.
- Career Services (`career-services.html`) has **no** fabricated quote testimonials; its alumni-network / TBD-outcomes / "Hire Our Graduates" claims are part of the broader §9 rework, left for that task. The `person1/person2` images stay as decorative photos (not presented as graduate quotes).
- Verified: no JS/CSS depends on `#testimonials`; rebuild clean; grep confirms no `Marcus`/`David`/graduate-quote text remains in any shipped HTML; homepage renders with no console errors, no overflow.
- **Still open in Option A:** program/tuition pages → "in development"; interest-list form (needs the cPanel PHP mailer); `career-services.html` §9 rework; `llms.txt` fixes; drop `outcomes.html`; `our-programs.html`, `faq.html`, `about.html`, `admissions.html`, `student-financing.html` reframes.

### 2026-09-25 (later) — Expanded posts #3, #4, #6, #7 to target length
All 8 blog drafts are now at their content-pack target lengths. Local only.
- **#3 `masshire-training-voucher`** — 805 → **1,312 words** (target 1,300–1,600). Rebuilt into the full 9-step JobQuest→TABE→ITA→approval flow, plus "what is an ITA," a Section 30 callout, "common mistakes," "after you're approved," and a 4-Q FAQ (schema).
- **#4 `is-wioa-training-free`** — 680 → **1,108 words** (target 1,100–1,300). Added the Section 30 income angle, a "free to you vs. free with conditions" box, the rough cap-vs-price math (no dollar amounts), "does everyone get funded," "beyond tuition," an "if WIOA doesn't cover you" list, and a 4-Q FAQ (schema).
- **#6 `can-medical-billing-coding-be-learned-online`** — 680 → **1,109 words** (target 1,100–1,400). Added coding-vs-billing, day-to-day, employer-respect, work-from-home honesty, pay pointer (#5), funding pointer (#1), and a 5-Q FAQ (schema).
- **#7 `can-you-learn-it-support-online`** — 700 → **1,104 words** (target 1,100–1,400). Added the CompTIA ladder (Tech+→A+→Network+/Security+), home-lab how-to, MA demand, pay pointer (#5), an AI-future honesty section, and a 5-Q FAQ (schema).
- Verified: builds clean; all JSON-LD valid; no visible `[VERIFY]`; no program-facts leakage; no page overflow. **All 8 posts now expanded and compliant.**

### 2026-09-25 (later) — Expanded posts #2 and #8 to target length
- **#2 `wioa-eligibility-massachusetts`** — 785 → **1,218 words** (target 1,200–1,500). Added: basic requirements + Selective Service (B7); priority-of-service explainer (B5); "training has to point to a real job"; income example framed as regional-only (B3); "you might qualify even if…"; a 5-question self-check (interim link to the ITA guide until `qualify.html` exists); a 4-question FAQ **with FAQPage schema**.
- **#8 `can-you-learn-a-trade-online`** — 685 → **1,101 words** (target 1,100–1,400). Added: OSHA 10/30 + EPA 608 online prep; the "HVAC is not one license" note; a Registered Apprenticeship section (Division of Apprentice Standards, earn-while-you-learn); an overpromising honesty callout; "do the trades pay off?" (links to #5); a "which trade fits you?" comparison; a 5-question FAQ **with FAQPage schema**. CTA switched to the interest list.
- Verified: builds clean; JSON-LD valid; no visible `[VERIFY]`; no program-facts leakage; no page overflow; both render with FAQ + tables. Compliance held (industry facts sourced, no CSC program specifics, dates real).
- **Remaining at draft length:** #3, #4, #6, #7 (pillar #1 and #5 already done; #2, #8 done this pass).

### 2026-09-25 — Applied VERIFICATION_LOG fixes to all 8 posts + fetched BLS wages
Picked up three more strategy commits (`643a20d` verification log + pre-deploy check, `a2bd448` program-facts-are-placeholders policy, `4ed64d4` pre-launch site spec). Applied every fact fix and the program-facts policy to the blog. **Local only.**

- **BLS wages (VERIFICATION_LOG §C):** bls.gov blocks curl (403) and the old per-state HTML tables are retired, so I pulled the data from the BLS OEWS Query System in the in-app browser (`data.bls.gov/oes/#/area/2500000/2025`). Got all 8 **Massachusetts** median annual wages (May 2025) and put them in **post #5** as a sourced table (no national fallback needed). Recorded in `docs/VERIFICATION_LOG.md` §G1. Post #5 title year corrected (2027) → **(2026)**.
- **Fact fixes (A/B):** center count "more than 25" (A1); Donnelly totals/dates → $7.4M **Oct 2025** + $5.9M Aug 2026 (A2); MassHire locator URL (A3); MA trade-license hours added (A8); softened B9/B10/B11/B14/B16; added AAPC exam cost $425/$499 as general info (B15).
- **Program-facts policy (§F1):** removed **every** CSC program specific from the blog (no more "11 weeks/117 hours," AAPC certificate, "our CompTIA program," "browse our programs"). Replaced with the sanctioned "Career Skills Center is planning… join our interest list" wording. Program-page CTAs re-pointed to the interest list (interim target: `contact.html`, until the mailer + form exist). VA line now points to the VA GI Bill Comparison Tool, no CSC VA claim.
- **Publish dates (§F2):** de-backdated — all 8 posts and the blog index cards now show **September 25, 2026**; the "Updated" line was removed from article meta (the `article()` helper no longer renders it) until a real update exists.
- **Verified:** builds clean (25 pages); all JSON-LD valid; **mandatory pre-deploy grep clean** — no visible `[VERIFY]` markers (only the checklist `[TODO]` placeholder kept per A9, and the intentional `<!-- DRAFT -->` notes); program-facts leakage scan clean (no prices/hours/credentials/fake grads); no page overflow; #5 wage table renders with all 8 MA medians.

**Still open / not done this session:**
- Checklist PDF (A9) — pillar keeps the placeholder; needs Emilio's content + the mailer.
- Posts #2–#8 are still at original draft **length** (this was a fact/compliance pass, not the length expansion the content pack also asks for).
- **Pre-launch site spec (Option A)** — not started: program/tuition pages → "in development," remove the fake homepage testimonials, interest-list form (needs the PHP mailer), `llms.txt` fixes, drop `outcomes.html`. Separate task.

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
- **Form backend: DONE →** cPanel PHP mailer (`submit.php`) is built and **live**, delivering to `vcanal@careerskillscenter.com`. Every form posts a hidden `source`. Confirmed working after switching cPanel Email Routing to Remote (mailboxes are on Namecheap Private Email).
- **Deploy decision needed:** the Option A rework + interest-list form are built and reviewed locally. OK to deploy? (Blog stays excluded until the drafts are approved.)
- **Blog approval:** the 8 drafts are ready for Emilio's review. Approve to publish (then add `put -r blog` to the deploy).
- **Checklist PDF** ("Paying for Training in Massachusetts"): still needed from Emilio to wire up the pillar post's email-capture download (placeholder in place).
- Confirm the `vcanal@` inbox is the right destination (unusual spelling — corrected from `vcanl@` this session).

## Decisions that differ from the brief
<!-- What you changed and why -->
- **Blog post URLs = real `/blog/<slug>.html` subdirectory** (per brief §2); required teaching `build-pages.py` to handle nested pages (relative-link rewriting). Older `docs/PAGES.md` flat-filename note is superseded — update it if approved.
- **Program-facts policy (v1.1 / spec) supersedes brief §3.3 program detail:** no CSC program length/hours/price/credential/certificate/VA/outcomes anywhere; pages say "in development" + join the interest list. `outcomes.html` withdrawn (no real graduates).
- **BLS wages** pulled from the OEWS Query System (`data.bls.gov`) rather than the zip (bls.gov blocks curl; per-state HTML retired). MA medians used and cited (May 2025).
- Pillar post CTA points to **Ways to Pay** instead of the checklist download until the PDF exists.
- Blog/interest-form CTAs point to `contact.html`/`#interest` (the interest list) as the interim for `qualify.html` until it's built.
