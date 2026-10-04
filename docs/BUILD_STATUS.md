# Build Status — Code → Strategy log

Claude Code updates this file at the end of every session. The strategy side (Cowork + the "ETPL Massachusetts" Project) reads it.

## Current state (as of 2026-09-28)
- **🚀 THE FULL v1.5 SITE IS NOW LIVE at https://careerskillscenter.com (Emilio authorized the deploy, 2026-09-28).** All `[VERIFY]`/`DRAFT` were resolved in an Emilio review session, so the blog deployed too. See the "2026-09-28 — LIVE DEPLOY" entry below.
- Now building: **`docs/SITE_STRUCTURE_SPEC.md` v1.5**, which supersedes the nav, page list and build order in GUIDE_MODE_SPEC v1.4. Everything else in v1.4 still applies (no ghost courses, funding-language rules, `[VERIFY]` sourcing, `COURSE-DEPENDENT` markers, no deploys without Emilio's OK).
- **v1.5 is DONE and DEPLOYED.** See the 2026-09-27 (build) and 2026-09-28 (LIVE DEPLOY) session entries below.
- **⚠️ CHANGE FROM CLAUDE.md / the specs (Emilio, 2026-09-28):** Career Skills Center **provides the training only.** It does **not** help employers apply for grants, handle Express paperwork, or take payment for the grant process — Emilio says the Massachusetts Express rules mean a provider shouldn't help with or be paid for the application. All "we handle the paperwork / we help you apply" copy has been removed and reframed to: *we provide the training; eligible employers apply to the state directly and get reimbursed.* This **contradicts `CLAUDE.md`** ("CSC helps them get state-funded staff training … and handles the grant paperwork") and v1.5 §4 ("We help you apply for Express funding and handle the paperwork") — **strategy should update `CLAUDE.md` and the spec to match.** (Also saved to Code's memory.)
- **Still blocking deploy (`[VERIFY]` / missing):** Express per-person cap ($3,000/course), per-instructional-hour cap ($300), large-employer rate (50%) and the 21-day autostart in `js/site-config.js` — the CommCorp guidelines page appears to **confirm the $3,000 and $300 caps** (see VERIFICATION_LOG, and note the current guidelines show ≤100 employees at up to 100%, superseding the old 51–100 = 50% tier); the WIOA low-income example numbers; the Selective Service line; and the founder name/photo for `about.html`.
- **Cleared this session:** Express rate/annual-cap/size/timeline (Emilio-confirmed) and the Massachusetts apprenticeship tax-credit + GROW/ITA-RTI figures (sourced from mass.gov / DOL) are no longer `[VERIFY]`.

### Earlier (as of 2026-09-26)
- Guide-mode steps 1–7 (v1.4) were DONE locally. v1.5 below builds on and supersedes them.

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

### 2026-10-04 — Blog Manager: How to Become a CNA in Massachusetts (2026): Training, Exam and Who Pays (LOCAL, not deployed)
- **Built:** `blog/cna-massachusetts.html` (about 4,200 words including page chrome), added via `tools/build-pages.py`; `blog.html` index and `sitemap.xml` regenerated. Course-mode copy in `blog/course-mode-copy/cna-massachusetts.md`. Register row R-BLOG-04 added.
- **Angle:** lead with who pays. If a nursing home hires you or offers you a job first, federal rules (42 CFR 483.152) say it cannot charge for training. Three ways to pay, the state exam (D&S) and registry, what changes in 2026, honest downsides, with three approved community quotes.
- Compliance review: PASS (round 2). Pipeline files: docs/blog-drafts/cna-massachusetts/
- Status: LOCAL (not deployed). DRAFT marker and [VERIFY] comments in the post block deploy. Facts logged in VERIFICATION_LOG section Q.
- **Open TODOs / questions for Emilio:**
  1. Pay-figure policy: post prints MA $46,680 and national $42,260 (BLS). Handoff allows pay only in the salary-by-state post. Approve an exception for role-guide posts or swap for a BLS link (same question as healthcare-jobs, phlebotomist, pharmacy posts).
  2. Open the mass.gov pages (registry program, approved-program list, DPH advisory memo, reciprocity, registry phone 617-753-8144); they were SEARCH SUMMARY only. Confirm the 87-hour/21-practical-hour effective date.
  3. Spot check the $46,680 MA median at data.bls.gov/oes.
  4. Confirm the $70 skills test fee (from the 7.2024 handbook only) and first-exam fee rules on the D&S fee page.
  5. Add back-links to the CNA post from the phlebotomist, pharmacy technician and healthcare-jobs posts.
  6. `blog/healthcare-jobs-massachusetts.html` conflicts with this post: it says CNA training is "4 to 12 weeks" and "$500 to $2,000" (table and FAQ), with no neutral source. This post says tuition varies and the federal minimum is 75 hours. Fix the healthcare-jobs post.

### 2026-10-04 — Blog pipeline moved into the repo; scheduled runs paused (LOCAL + GitHub, not deployed)
- **Blog Manager routine paused** (`trig_01XgMjFh5eKjNm4qx8Gr9HdM`, `enabled: false`). Emilio asked for this until the agents write the way he expects. Re-enable it on claude.ai or by asking Code.
- **Agents now live in the repo:** `.claude/agents/` holds `data-researcher`, `content-strategist`, `blog-writer`, `compliance-reviewer` and `blog-publisher`. The director is the `/blog-pipeline` command in `.claude/commands/blog-pipeline.md`. Any Claude Code session on this repo can run them. Local runs can also open bls.gov and mass.gov, which the cloud routine's network blocks.
- **Pipeline files are kept:** every run saves `research-brief.md`, `content-strategy.md` and `review-report*.md` to `docs/blog-drafts/<slug>/`.
- **Healthcare jobs post rewritten** for the reader (`blog/healthcare-jobs-massachusetts.html`): training time and cost per role, "No state license required", one pay number per role, more internal links. **Its training cost and length ranges are NOT sourced.** They came from Code, not the research brief, which breaks Writing Guideline 10. Source them or remove them before approval.
- **Pharmacy technician post drafted** by the last scheduled run (`blog/pharmacy-technician-massachusetts.html`, VERIFICATION_LOG section P). It was written under the older prompt, so it still needs a reader-first review. A second run collided with it and stopped itself without pushing anything.
- **Questions for Emilio:** (a) pay figures in role-guide posts (still the open policy question from sections N, O and P); (b) send the keyword analysis from the Project so it can be saved as `docs/KEYWORD_ANALYSIS.md`.
- **6th agent added: `community-researcher`.** It finds first-hand experiences on Reddit, Quora and public forums or Facebook posts. A new editorial round decides what goes in: the data-researcher checks the facts, the strategist judges value and balance, and the director approves only items backed by 2+ independent people or an official source. Files: `community-insights.md`, `community-verification.md`, `community-editorial.md`, `editorial-decisions.md` in each draft folder. Rules: Research Guidelines Part C, Writing Guideline 13, reviewer check 16.
- **Blog article spacing (Emilio approved, 2026-10-04):** blog posts now wrap their body in `.post-body`, with 28px between paragraphs, 34px section headings with 72px above them, and 24px sub-headings (`css/style.css`, commit `89d13d5`). Legal pages are unchanged. Not deployed. Writer paragraph rule: 1-2 sentences, about 120-185 characters, max 210. Older posts break it (for example, the healthcare post's CNA license paragraph).
- **⚠️ DECISION DIFFERS FROM CLAUDE.md (Emilio, 2026-10-04):** CLAUDE.md allows quotes only from real, consenting students. Emilio now allows short, exact quotes from public posts when the team judges them worth it, with no usernames, no links and nothing identifying, and never implying they are CSC students. Strategy should update CLAUDE.md to match.
- **For strategy:** the guidelines live in `docs/BLOG_RESEARCH_GUIDELINES.md` and `docs/BLOG_WRITING_GUIDELINES.md`. If the Project adds this repo to its knowledge, it can read the pipeline's briefs directly.
<!-- Newest first. For each session: date · what was built (files/URLs) · status (local only / deployed) · TODOs -->

### 2026-10-04 — Blog Manager: How to Become a Pharmacy Technician in Massachusetts (LOCAL, not deployed)
- **Built:** `blog/pharmacy-technician-massachusetts.html` (generated by `tools/build-pages.py`; new card on `blog.html`; URL in `sitemap.xml`; listed in `llms.txt`, which is hand-maintained; course-mode row R-BLOG-03 in the register; course-mode copy in `blog/course-mode-copy/pharmacy-technician-massachusetts.md`). About 3,230 words of page text. Publish date October 4, 2026. Build exit 0, 32 pages.
- **Angle:** the only Massachusetts pharmacy technician guide not selling a course or exam prep. Three routes to the state license (500-hour trainee route plus employer test, Board-approved program, or national exam). The paid trainee route can mean no tuition. "What can stop you" section, including the criminal-record question. Honest downsides of the job. Plain-language glossary of job-ad terms for ESL readers.
- **Status:** LOCAL, not deployed. Needs Emilio's review; the DRAFT marker blocks deploy (pre-deploy grep matches the new post, as expected; the other `[VERIFY` text is inside the post's DRAFT comment). Facts logged in `docs/VERIFICATION_LOG.md` section P.
- **Open TODOs:**
  - Live-verify BLS pay and outlook, the 247 CMR 8.00 licensing facts, PTCB exam facts, and the P5 list (CORI/drug-felony rule, trainee time limit, ASHP full name, exam languages, ExCPT details, PTCB renewal, share of jobs by workplace, the "You learn drug names, medical abbreviations and dose math" line). mass.gov, bls.gov and ptcb.org were unreachable for the researchers.
  - The research brief was stale against the verification log (May 2024 pay and 2024-34 openings); the post uses the log's May 2025 / 2025-35 figures.
  - `llms.txt` still does not list the healthcare-jobs and phlebotomist posts (not added here).
  - Re-read the "does not sell pharmacy technician training" line when courses launch (R-BLOG-03).
- **Question for Emilio:** OK to print pay figures in role-guide posts? The rules say pay only in the salary-by-state post. The pharmacy technician post prints BLS medians (national $45,750, Massachusetts $46,470), like the healthcare-jobs and phlebotomist posts. Approve an exception, or we replace the pay section with a link to BLS.

### 2026-10-03 — Blog Manager: How to Become a Phlebotomist in Massachusetts (LOCAL, not deployed)
- **Built:** `blog/phlebotomist-massachusetts.html` (generated by `tools/build-pages.py`; new card on `blog.html`; URL in `sitemap.xml`; course-mode row R-BLOG-02 in the register; course-mode copy in `blog/course-mode-copy/phlebotomist-massachusetts.md`). About 2,900 words (2,877 counted from the page text), 11 min read. Publish date October 3, 2026.
- **Angle:** the only Massachusetts phlebotomy guide not written by a course seller. No state license, but live blood draws and employer rules decide hiring. Certification comparison table (NHA CPT / ASCP PBT / AMT RPT). Six questions to ask before paying. Honest outward funding section (MassHire, JobQuest).
- **Process:** blog pipeline of researcher, strategist, writer, compliance review (PASS). Pipeline files are in `docs/blog-drafts/phlebotomist-massachusetts/`.
- **Status:** LOCAL, not deployed. Needs Emilio's review; the DRAFT marker blocks deploy (pre-deploy grep matches the new post, as expected; no unexpected `[VERIFY]`). Facts logged in `docs/VERIFICATION_LOG.md` section O (from search extracts, not yet verified on live pages).
- **Open TODOs / questions for Emilio (review-report.md Issues 1-7):**
  - (1) Pay-figure policy: PROJECT-HANDOFF allows pay only in the salary-by-state post. Approve an exception or remove the pay section. The MA median $50,170 is on file in VERIFICATION_LOG H1 but unused in the post.
  - (2) Live verification of BLS, NHA, ASCP and AMT facts (bls.gov, ascp.org, nhanow.com, mass.gov were unreachable during research).
  - (3) MassEducate/MassReconnect caveat needs a mass.edu source or removal.
  - (4) Subtitle and card excerpt state a flat "no license"; hedge them ("not on the list of states that license").
  - (5) Unsourced ESOL claim.
  - (6) Unsourced "diploma plus on-the-job" claim.
  - (7) Optional: cite OSHA 29 CFR 1910.1030 for the blood-risk line.
  - Also: `llms.txt` does not list the new post yet; FAQ questions are not real PAA data; re-read the "does not sell phlebotomy training" line when courses launch (R-BLOG-02).

### 2026-10-03 — Blog Manager: Healthcare Jobs in Massachusetts You Can Train For (2026) (LOCAL, not deployed)
- **Built:** `blog/healthcare-jobs-massachusetts.html` (generated by `tools/build-pages.py`; new card on `blog.html`; URL in `sitemap.xml`; course-mode row R-BLOG-01 already in the register). About 3,250 words (estimated from the page text), 12 min read. Publish date October 3, 2026. The build also restamped asset `?v=` values and sitemap lastmod across generated pages.
- **Angle:** an honest "before you click Apply" guide. Job boards list openings most beginners can't take; one comparison table for six roles; Massachusetts license/registry hurdles; choose-by-situation; outward next-step checklist. EKG tech is included as a "partial fit" because BLS has no separate category and groups it under cardiovascular technologists, where an associate's degree is typical.
- **Process:** blog pipeline of researcher, strategist, writer, 1 revision round, 2 compliance reviews. The second review was PASS.
- **Status:** LOCAL, not deployed. Needs Emilio's review; the DRAFT marker blocks deploy (pre-deploy grep matches the new post, as expected). Facts logged in `docs/VERIFICATION_LOG.md` section N (NOT VERIFIED LIVE).
- **Open TODOs / questions for Emilio:**
  - (a) Policy exception: national BLS pay figures beyond the salary-by-state post (approve a second exception, or remove the pay columns).
  - (b) All figures come from search summaries and need a live check against bls.gov and mass.gov. No Massachusetts OEWS medians were found, so the post uses national pay and links to the BLS Massachusetts page.
  - (c) FAQ questions are placeholders, not real Google People Also Ask data.
  - (d) CNA 87-hour DPH change, exam vendor, exam languages and Massachusetts projections were deliberately left out as unverified.
  - (e) `llms.txt` does not list the new post yet.
  - (f) Optional: FAQ 4 wording "many employers prefer or require" vs. the brief's "may prefer or require", and unsourced work-environment lines to confirm against BLS.
  - (g) Re-read the "not to sell you training" line when courses launch.

### 2026-09-29 — LIVE DEPLOY: qualify verdict rework + post-launch polish (Emilio-authorized)
Emilio said "send these changes live." Deployed the full stack of local commits since the 2026-09-28 launch. **All live at https://careerskillscenter.com.**

**What went live (commits `ece6ec3` → `c95c980`):**
- **qualify.html verdict system** — confident yes / maybe / no result (replaces the always-"you may" behavior), each with a colored badge, a "Why you're seeing this" reason line, priority-flag vs dislocated-worker distinction, and the honest out-of-state ("Outside Massachusetts → apply in your home state") + work-authorization ("Likely not a fit") branches. Green checkmark + rectangular badge on eligible; focus-outline flash removed.
- **Copy fix** — removed the now-inaccurate "never gives a yes/no verdict" line from the hero, meta desc, wioa-explained teaser and home CTA → "isn't an official decision."
- **Consent-checkbox layout bug** fixed site-wide (checkbox no longer stretches full-width; label flows normally) on the qualify email form + interest-list form.
- **www → non-www 301** added to `.htaccess`; **GA4 opt-out link** added to the privacy policy.
- **Image renames** `Hero.webp → hero.webp`, `Todaybanner.webp → today-banner.webp` — uploaded the new files and **removed the old-cased server files** (verified 404).

**Deploy (SFTP key `~/.ssh/namecheap_cfcb`, `premium164-1.web-hosting.com:21098`, docroot `~/careerskillscenter.com/`):** `chmod 644` first; moved the uncommitted `it-careers-massachusetts-draft.html` aside so `put *.html` wouldn't ship it, then restored it. Uploaded all root `*.html`, `blog/`, `.htaccess`, `submit.php`, `css/`, `js/`, `sitemap.xml`, `robots.txt`, `llms.txt`, the two renamed images; `rm`'d `images/Hero.webp` + `images/Todaybanner.webp`. Did **not** `put -r images` (would re-add the orphans); live `images/` stays the 7 referenced files. Mandatory `[VERIFY]`/`DRAFT` grep: clean.

**Verified live:** homepage + qualify 200; new images 200, old-cased images 404; `main.js` carries the verdict logic; `style.css` has the checkbox `:not([type=checkbox])` fix + verdict styles; www→non-www returns 301; a retired-page 301 (tuition→student-financing) still resolves; hero copy now reads "isn't an official decision"; and a live browser run of a priority case renders the green "You're very likely eligible" badge + reason line (screenshot).

**⚠️ DEVIATION still open for strategy:** the yes/no verdict overrides Spec v1.5 §2 and the CLAUDE.md "use 'may qualify'" rule (Emilio's call). Strategy should reconcile the spec + CLAUDE.md. Also still pending Emilio content: founder name/photo on `about.html`; real street address/suite.

### 2026-09-28 (later) — qualify.html: confident yes/maybe/no verdict (⚠️ DEVIATION from spec §2) (LOCAL, not deployed)
Emilio: the tiered result still wasn't decisive enough — he asked for a "yes / no / you may fit" verdict. **This deviates from Site Structure Spec v1.5 §2 ("the result is never a yes/no verdict") and the CLAUDE.md hard rule "never promise approval; use 'may qualify.'"** I flagged both; Emilio chose the **"confident but honest"** option (2026-09-28), which keeps the yes/no/maybe structure without promising funding or giving a false hard "no." **Strategy should update spec §2 + CLAUDE.md to match.** Not deployed.

- **`classifyQualify` now returns `verdict` ∈ {yes, maybe, no}** on top of `tier`:
  - **`yes`** — priority tier (WIOA priority-of-service flag or dislocated worker). Badge "You're very likely eligible" (green). Never says "approved"; body adds "A MassHire career center makes it official."
  - **`maybe`** — candidate/explore tiers (Adult program is broad, decided locally). Badge "You may qualify" (amber).
  - **`no`** — a genuine WIOA disqualifier: **not authorized to work in the US** (a real requirement). Badge "Likely not a fit for WIOA" (red). Still routes to other ways to pay (`student-financing.html`) — never a dead end. This is the only hard "no"; a false "no" for eligible people is deliberately avoided.
  - Not-in-MA keeps its own scope message (amber badge).
- **UI:** new colored verdict **badge** (`.result-verdict` pill, green/amber/red) above the headline, and a new `.result-otherpay` line (Ways to Pay) shown on the `no` branch and the softest `explore` case. Both added to `tools/build-pages.py` (qualify block) + `css/style.css`; JS in `js/main.js` (`setVerdict` helper + rewritten `showResults` with `no` → not-MA → yes/maybe precedence). The bottom disclaimer ("This tool doesn't decide your funding — only a MassHire center can approve") is unchanged and still shows on every result.
- **Verified:** reworked `#selftest` (verdict + disqualifier-override cases) — all pass in-browser, no console errors. Drove all five outcomes (yes / maybe-candidate / maybe-explore / no / not-MA) through the real form UI; badge text, color, headline and section visibility all correct. Screenshot of the "yes" result confirmed. Rebuilt; asset `?v=` bumped and index.html re-stamped in sync.

### 2026-09-28 (later) — qualify.html result tiers (fix "everything says you may fit") (LOCAL, not deployed)
Emilio reported that almost every answer set on `qualify.html` concluded "you may fit." Diagnosed and fixed. **Not deployed.**

- **Root cause:** the verdict was a single `likely` boolean (`js/main.js` `classifyQualify`) built from an OR of nearly every condition. A sweep of all answer combinations showed **98% of in-Massachusetts respondents (423/432)** hit the strong "You may be a good candidate" message — 5 of the 6 work situations flipped it true on their own, and any one priority flag flipped it true regardless. Both headlines also began "You may…", so even the weak branch read as a soft yes.
- **Fix (Emilio: "differentiate results into tiers"):** replaced `likely` with a three-tier `tier` — **priority** (matches a WIOA priority-of-service flag: public assistance / low income / veteran, or a dislocated worker), **candidate** (an active job-seeker need — unemployed or part-time/low-wage — with no flag), **explore** (employed full-time, no flags → softest "here's how to check"). Not-in-MA still handled separately. Distinct headline + body per tier; the priority-flag list only shows when actually flagged. `likely` is retained (derived) for back-compat.
- **Result:** for a typical user with no priority flags, the outcome now varies by work situation (laid-off/on-UI/self-closed → priority; unemployed/part-low → candidate; full-time → explore) instead of one universal message. Copy still never gives a yes/no verdict (spec §2).
- **Verified:** rewrote the `#selftest` cases for tiers — all pass in-browser (no console errors). Drove all four branches through the real form UI and confirmed the correct headline, groups and priority list render for each. Rebuilt; bumped the cache-bust `?v=` on `main.js` across generated pages and `index.html`.

### 2026-09-28 (later) — Post-launch polish: www 301, cookie note, image renames (LOCAL, not deployed)
Tackled two of the four post-launch open items (Emilio: "no preference," so I did the two that need no input from him). The other two (founder name/photo on `about.html`; real street address/suite) still need content from Emilio. All committed on `main`; **nothing deployed** (awaiting Emilio's OK).

- **www → non-www 301 (`.htaccess`).** Added a `mod_rewrite` block at the top that 301-redirects `www.careerskillscenter.com` → `careerskillscenter.com` (keeps GA4/SEO on one host). Sits above the existing `mod_alias` redirects.
- **Cookie/analytics note (privacy policy).** The policy already had a "Cookies and analytics" section describing GA4 + cookies; strengthened it with a concrete opt-out (Google Analytics Opt-out Browser Add-on link) alongside the existing browser-settings / Google privacy-policy links. Edited in `tools/build-pages.py` and rebuilt `privacy-policy.html`.
- **Image renames (uppercase → lowercase-hyphen).** `git mv images/Hero.webp → images/hero.webp` and `images/Todaybanner.webp → images/today-banner.webp`. Updated every **source** reference — `index.html` (og:image, preload, hero `<img>`, comments), `tools/build-pages.py` (shared `og:image`, `hero()` default, the Financial-Aid and Contact hero calls), and a comment in `js/main.js` — then rebuilt. `grep` confirms **no `Hero.webp`/`Todaybanner.webp` refs remain** in any source or generated page (excluding the untracked `it-careers-massachusetts-draft.html` and `Claude outputs/`).
  - Left `images/Todaybanner2.webp` untouched — it's the reserved `data-hover-image` on the trades card, never loaded, and outside the two filenames Emilio named.
- **Verified:** build clean (26 pages). Against the running dev server: `images/hero.webp` and `images/today-banner.webp` both 200; homepage references the new names. Mandatory `[VERIFY]`/`DRAFT` grep clean on all touched pages. (Local macOS FS is case-insensitive, so the old paths still resolve here — the rename only *matters* on the live Linux server.)

**⚠️ Deploy notes for these changes:**
- Upload the renamed images **and remove the old server files** `images/Hero.webp` + `images/Todaybanner.webp` — the live Linux server is case-sensitive, so the old-cased files would otherwise linger as orphans (and any external link/cache pointing at the old paths would 404). Live `images/` should end up as {hero, hero2, today-banner, aboutus, comptia, electrician, medicalbilling}.webp.
- Upload the new `.htaccess` (www 301) and the rebuilt `privacy-policy.html`.
- Re-run the pre-deploy `[VERIFY]`/`DRAFT` grep and exclude `it-careers-massachusetts-draft.html`.

**Still open (need Emilio's content):** founder name/photo for `about.html`; real street address/suite for footer + `contact.html`. Also noted in passing: `privacy-policy.html` still carries a bracketed `[Confirm and list any additional advertising or tracking tools before publishing.]` placeholder (class `tbd`) — it shipped live in the 2026-09-28 deploy and isn't caught by the `[VERIFY]`/`DRAFT` grep; decide whether to resolve/remove it.

### 2026-09-28 — LIVE DEPLOY of the full v1.5 site + blog (Emilio-authorized)
Emilio directed the full deploy and reviewed every `[VERIFY]`/`DRAFT` one by one in this session. **The whole site is now LIVE at https://careerskillscenter.com**, including the blog. Committed locally as restore point `6083475` before deploy.

**Funding verifies resolved** (sources: CommCorp Express Program Guidelines + Emilio's 851 Ventures training FAQ):
- Express **$3,000/person/course** and **$300/instructional hour** confirmed → `[VERIFY]` cleared in `site-config.js`.
- **Dropped the obsolete "larger employers 50%" tier** (current rule: ≤100 employees at up to 100%). Removed `EXPRESS_RATE_LARGE`; collapsed the reimbursement calculator (`calcExpress` + `staff-training-grants.html`) to the single ≤100-employee model.
- **Removed the unverified 21-day auto-start** claim + `EXPRESS_AGREEMENT_AUTOSTART_DAYS`.
- **Removed the regional WIOA income-example dollars** ($15,960–$60,124) from `qualify.html` and blog #2 → now "varies by region/household; a MassHire center checks." Removed `INCOME_EXAMPLE_*`.
- Selective Service line (confirmed by Emilio) and AAPC CPC exam cost **$425/$499** (re-verified on aapc.com) kept.

**Blog — reviewed post by post, 7 approved + 1 removed:**
- **Removed "Highest-Paying Certifications" entirely** (Emilio) — deleted the file, its 3 career-page cross-link cards, and 3 inline links in posts #6/#7/#8; out of the index/sitemap.
- **Removed all real wage/pay figures site-wide** (Emilio: "no real figures"). Blog now uses qualitative wording + a BLS look-up link. The old program pages that still contained BLS medians (`it-support-specialist.html`, `medical-billing-coding.html`) are 301 redirect stubs, so those figures never render live.
- **Corrected the ITA approval model** (Emilio): the student picks from the already-approved **ETPL**; the counselor does **not** vet the school. Approval = eligible + program-on-ETPL + funding. Fixed post #3 (was "be ready to explain how training leads to a job"). Saved to Code memory.
- Removed the cap / "pay the difference" framing from posts #3 and #4.
- Reframed post #2's "training has to point to a real job" (was student-burden wording).
- Cleared all 8 `DRAFT` markers (7 to "Approved by Emilio"; #5 deleted).

**Chrome cleanup:** removed the visible "Accreditation badge" footer placeholder (compliance); contact **dialog** "Program of interest" → "Reason for contacting" (matches `contact.html`; no implied programs).

**Deploy details (SFTP, `premium164-1.web-hosting.com:21098`, user `ihrwgcpm`, docroot `~/careerskillscenter.com/`):**
- Uploaded 33 root `*.html` (real pages + 301 redirect stubs), **`.htaccess`** (was missing on the server — 301s are now active), `submit.php`, `css/`, `js/`, **`blog/` (7 posts, new dir)**, `sitemap.xml` (27 urls, includes blog), `robots.txt`, `llms.txt`.
- **Images managed:** uploaded only the **7 referenced images**; **removed 15 orphan images** from the server (incl. the `billing&coding.webp` `&` file, old hero variants, person photos, unused logos) so live `images/` = exactly {Hero, Todaybanner, aboutus, comptia, electrician, hero2, medicalbilling}.webp. Excluded the uncommitted `it-careers-massachusetts-draft.html` from the upload.
- **Verified live:** homepage + all new pages/blog/assets 200; every 301 redirect resolves (tuition→student-financing, our-programs→career-paths, it-support-specialist→it-careers, medical-billing-coding→healthcare-careers, terms-of-use→terms, MA-named guides→neutral); removed images 404; **0 `[VERIFY]`** on live funding pages; `submit.php` GET→405 (mailer active); removed post #5 → 404; dialog shows "Reason for contacting"; no "Accreditation badge" text.

**Open TODOs / notes for Emilio:**
- Two uppercase image filenames remain (`Hero.webp`, `Todaybanner.webp`) — work fine (refs match), but rename to lowercase-hyphen sometime for safety.
- `about.html` still uses the founder **placeholder** (name/photo) — supply when ready.
- Real **street address/suite** still TBD (footer/contact say "Quincy, MA 02171").
- Consider a `www → non-www` 301 and a cookie/analytics note in the privacy policy (GA4 is live).
- If a "Paying for Training in Massachusetts" checklist PDF is produced later, the pillar post's download note was removed and can be re-added.

### 2026-09-28 — Employer compliance rework + Express/apprenticeship funding (LOCAL, not deployed)
Follow-up to v1.5, driven by Emilio. All committed on `main`, verified in the in-app browser. **Nothing deployed.**

**Compliance: "we provide the training only."** Removed every "we handle the paperwork / we help you apply for grants" claim across the site (`employers.html`, `staff-training-grants.html`, `express-program-explained.html`, `index.html` teaser, `about.html`, `faq.html`, `privacy-policy.html`). Reframed to: *CSC provides the training; eligible employers apply to the state directly and get reimbursed.* Apprenticeship copy that implied we "set up/administer" programs was reframed to CSC = the related-classroom-instruction provider (employer is the sponsor, claims the credit). This overrides `CLAUDE.md`/spec v1.5 §4 (flagged above; saved to memory).

**staff-training-grants.html copy (Emilio).** Eyebrow → "For Massachusetts businesses · 100 or fewer W-2 employees"; hero lede → hands-on training + "Massachusetts reimburses up to 100% … for eligible companies with 100 or fewer employees." New **"How the reimbursement works"** section: up to 100% reimbursed, up to $15,000/yr (reusable across trainings), ~3 weeks application→acceptance, state sends a check. Numbers render from `site-config.js` via `[data-cfg]`.

**Express figures.** Emilio confirmed the rate (up to 100%), annual cap ($15,000), small-employer size (100 W-2), and ~3-week timeline → cleared their `[VERIFY]`, logged in VERIFICATION_LOG **J**, added `EXPRESS_APPLICATION_WEEKS=3`. Also researched the official CommCorp/mass.gov rules (reported to Emilio): ≤100 employees, up to 100%, $3,000/employee/course, $300/instructional hour, $15,000/company/yr — the per-person and per-hour caps still carry `[VERIFY]` in config pending a formal clear.

**Bug fix.** Employer inquiry form fields were invisible on the light sections (dark-dialog input styling); added a `.employer-form` class with light-background input styles. Affects all four employer pages.

**apprenticeships.html rewritten with sourced funding (VERIFICATION_LOG K, K1).** Corrected the model (earn-while-you-learn: apprentice is an employee from day one, trained on the job — not "train first, then hire"). New Funding section: **Registered Apprentice Tax Credit** (50% of wages, up to $4,800/apprentice/yr, $100k/employer/yr, 2 consecutive years; DAS-sponsor + ≥180 days + eligible occupations), **GROW/RTI grants** for the classroom side, and **ITA can fund apprenticeship related instruction** (Registered Apprenticeships are auto-ETPL-eligible — 20 CFR 680.470; TEGL 13-16; local MassHire policy varies). Figures render from `site-config.js` (`APPRENTICE_TAX_CREDIT_*`). Removed the old `[VERIFY]` placeholder. Corrected a misconception Emilio raised: "ITA-train → then apprentice → employer claims credit" is not how it works (the credit needs a *registered* apprentice trained on the job).

**Config/docs.** `js/site-config.js` — Express figures updated + apprenticeship tax-credit block added. `VERIFICATION_LOG.md` — sections J, K, K1. `docs/COURSE_CONTENT_REGISTER.md` R-EMP updated (training-only).

### 2026-09-27 — Site Structure Spec v1.5 (all build-order groups) (LOCAL, not deployed)
Built the v1.5 restructure. The spec was uploaded and saved to `docs/SITE_STRUCTURE_SPEC.md`. All work committed on `main` in step-by-step commits and verified in the in-app browser (self-tests pass, no console errors, pages 200, redirects serve). **Nothing deployed.**

**Nav + footer (every page).** New groups: **Funding Guides** (WIOA Explained · Do I Qualify? · Express Program Explained) · **For Employers** (Overview · Staff Training Grants · Apprenticeship Programs · Corporate Training) · **Career Paths** (Healthcare · IT · Skilled Trades · All Career Paths) · **Resources** (Blog · FAQ) · About · Contact. Header button **"Do I Qualify?" → qualify.html**. Footer mirrors; Terms → `terms.html`.

**Step 1 — Home + About.** `index.html` reframed to "Career Training & Funding, Explained" with Funding Guides + For Employers teaser + Career Paths + latest guides + interest band (removed the standalone funding band and the on-home mission section). `about.html`: "what we're building" (funding help, employer/apprenticeship, corporate training), **founder placeholder (Emilio to supply name/photo)**, future tense, no instructor/accreditation/outcome claims.

**Step 2 — WIOA + Qualify.** New **`wioa-explained.html`** (what WIOA is, the three groups, priority of service, the ITA, ETPL, step-by-step, Section 30, FAQ+schema; facts sourced from VERIFICATION_LOG). **`qualify.html` reworked to 8 questions, results-first** (MA residency, age, work situation, public assistance, low income, veteran, work authorization, field). Shows which WIOA group you may fit + priority flags + outward next steps — never a yes/no verdict. Removed the "advisor will text you" promise; emailing the steps is now optional. Logic is a pure `classifyQualify()` in `js/main.js` with self-tests (`qualify.html#selftest`). New config-driven `[data-cfg]` filler so funding numbers render only from `site-config.js`.

**Step 3 — Express.** New **`express-program-explained.html`** (what the Workforce Training Fund is, who can apply, what's covered — live instruction, rates/caps table, how to apply, timeline, FAQ+schema). All figures render from `site-config.js` via `[data-cfg]` with visible `[VERIFY]` fallback.

**Step 4 — For Employers.** New **`employers.html`** (overview + inquiry form, `source=employer`), **`staff-training-grants.html`** ("we handle the paperwork," never "our course," follows `EXPRESS_PROVIDER_LISTED=false`; embeds the **reimbursement calculator** — pure `calcExpress()` in main.js with self-tests, `source=employer-express`), **`apprenticeships.html`** (`source=employer-apprenticeship`; COURSE-DEPENDENT graduate-pipeline line, R-APPR), **`corporate-training.html`** (future tense, no location/price/course names; `source=corporate`, R-CORP). New `employer_form()` helper.

**Step 5 — Career Paths.** Renamed to location-neutral slugs: `healthcare-careers.html`, `it-careers.html`, `skilled-trades-careers.html` (301s from the v1.4 MA-named URLs and re-pointed the program-page 301s). Dropped all "Massachusetts" framing (only a clearly labeled MA licensing **example** on the trades page) and **removed all pay figures** (hidden `<!-- PAY-DATA: pending -->` slot, R-PAY-DATA). `role_card()` reworked (training · certifications · license · online). New location-neutral `career_pay_block()`.

**Step 6 — Blog.** CTAs repointed to the cluster page each post supports (funding → WIOA/qualify; careers → career guides; never "our program"). Careers-post CSC mentions marked `COURSE-DEPENDENT` (R-BLOG). **Post #5 (Highest-Paying Certifications) put on hold** — off the index, noindex, off the sitemap (new HOLD set) until pay-data is ready.

**Step 7 — Supporting.** `faq.html` gained a "For employers" group and updated launch/employer answers. `contact.html` "Program of interest" → **"Reason for contacting"** dropdown (general/employer/partnership/media), posted as a field. `privacy-policy.html` now describes form data, the eligibility-check answers, SMS consent and GA4 (still a template marked for legal review). `terms-of-use.html` → `terms.html`. `llms.txt` rewritten for the new structure/URLs.

**Register + redirects.** `docs/COURSE_CONTENT_REGISTER.md` updated: new/renamed URLs, new rows R-WIOA/R-CORP/R-APPR/R-PAY-DATA (+ R-EMP/R-SCHEMA notes), Retired-URLs table extended. `.htaccess` + `REDIRECTS` re-pointed to new slugs and added the MA-career and terms redirects.

**Verification.** Build clean (27 pages + redirect stubs). Every rendered `COURSE-DEPENDENT` marker has a register row (no orphans). Acceptance greps clean: no pay figures and no non-example "Massachusetts" on career pages; no "out of state" anywhere; every form posts a distinct `source`; nav/footer match on every page; qualify + calculator self-tests pass. Pre-deploy `[VERIFY]`/`DRAFT` scan: **held out of deploy** — `express-program-explained.html`, `staff-training-grants.html`, `apprenticeships.html`, `qualify.html` (all carry `[VERIFY]` funding figures) and the 8 blog `DRAFT`s.

**Open TODOs / notes for Emilio:** verify the Express figures, WIOA income example, apprenticeship grants/tax credits and the Selective Service line (all `[VERIFY]`); supply the founder name/photo for About; then the new pages can deploy. The pre-existing uncommitted `it-careers-massachusetts-draft.html` course-mode experiment and `Claude outputs/` previews were left untouched (not part of v1.5).

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

**Post-step-7 tweaks (same session).**
- Added hero background images to the three field guides (same images as the career-paths cards): healthcare → `images/medicalbilling.webp`, IT → `images/comptia.webp`, trades → `images/electrician.webp`.
- CSS fix: a button/paragraph directly after a `.check-list` was flush against the last list item (button paragraph had `margin:0`). Added `.check-list + p { margin-top: 28px; }` — fixes the "Check your funding options" spacing on the field guides and the Ways to Pay page.

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
- **⚠️ `qualify.html` now gives a yes/maybe/no verdict (Emilio, 2026-09-28)** — directly overrides Site Structure Spec v1.5 §2 ("never a yes/no verdict") and the CLAUDE.md hard rule "never promise approval; use 'may qualify.'" Implemented as **"confident but honest"**: a green "very likely eligible" for priority matches (no approval guarantee), amber "you may qualify" for the broad middle, and a red "likely not a fit for WIOA" **only** for a real disqualifier (no US work authorization), which still routes to other ways to pay. The "only a MassHire center decides" disclaimer stays on every result. **Strategy should reconcile spec §2 + CLAUDE.md.**
- **Blog post URLs = real `/blog/<slug>.html` subdirectory** (per brief §2); required teaching `build-pages.py` to handle nested pages (relative-link rewriting). Older `docs/PAGES.md` flat-filename note is superseded — update it if approved.
- **Program-facts policy (v1.1 / spec) supersedes brief §3.3 program detail:** no CSC program length/hours/price/credential/certificate/VA/outcomes anywhere; pages say "in development" + join the interest list. `outcomes.html` withdrawn (no real graduates).
- **BLS wages** pulled from the OEWS Query System (`data.bls.gov`) rather than the zip (bls.gov blocks curl; per-state HTML retired). MA medians used and cited (May 2025).
- Pillar post CTA points to **Ways to Pay** instead of the checklist download until the PDF exists.
- Blog/interest-form CTAs point to `contact.html`/`#interest` (the interest list) as the interim for `qualify.html` until it's built.

---

## Update — 2026-09-30: new post "4-Week vs. 4-Month Medical Billing and Coding Courses" + info form page

**Built (in `tools/build-pages.py`; pages regenerated, not hand-edited):**
- `/blog/4-week-vs-4-month-medical-billing-coding-course.html` — Category Medical, byline Vicent Canal, published 2026-09-30 (visible date + `datePublished`/`dateModified`). Text, links, BlogPosting + FAQPage JSON-LD and `COURSE-DEPENDENT: R-BLOG-MBC` markers copied from the source doc. Added to `blog.html` (top of grid) and `sitemap.xml`.
- `/medical-billing-coding-info.html` — name, email, phone (optional), state, "When would you like to start?" (ASAP / 1-3 months / Just exploring); posts to `submit.php` with `source=blog-mbc-4week`; success text "Thanks! We'll email you more information soon." No dates, prices or enrollment mentioned. Marked `R-BLOG-MBC`. **noindex and left out of the sitemap** (lead-capture page).
- `docs/COURSE_CONTENT_REGISTER.md`: added row **R-BLOG-MBC**.

**Guide-mode exceptions (approved by Emilio for this post only):**
1. The **$679** price in the "What you'll pay in total" table (generic "4-week online course" row; also stated in the lead sentence of that section).
2. The CTA heading **"Want to learn more about our courses?"**

**Small differences from the source file / decisions to confirm:**
- Source had a CODE note "no author byline"; the task says byline Vicent Canal, so the visible byline is Vicent Canal. The JSON-LD author was kept as written (Organization: Career Skills Center).
- Related line: links to `/healthcare-careers.html` (the live guide) instead of `/healthcare-careers-massachusetts.html` (now a 301), and adds post #6 "Can Medical Billing and Coding Be Learned Online?" as the source CODE note asked.
- FAQ markup converted to the site's `details.faq-item` accordion (same text as the JSON-LD); tables use `.data-table`; CTA uses `.post-cta`.
- Page hero "dek" = the meta description.
- In-article links are plain grey with no underline site-wide (`.prose a`), which hides this post's many source links. Added a small **scoped** style in this post's `<head>` only (navy + underline). **Recommend a site-wide `.prose a` rule later** (would need a CSS deploy).
- `og:type` stays `website` (shared template), not `article`.
- The form's generic JS validation message still reads "…name, phone, email, and program of interest" (shared `js/main.js`); not changed because only the named files are deployed.
- The post's price table uses third-party prices checked Sept 30, 2026 (per the source). Nothing in it is a CSC program fact except the approved $679 row.

**Checks:** pre-deploy `grep -rn -e '[VERIFY' -e 'DRAFT'` on the new/changed files: no matches. Local form test: payload has `source=blog-mbc-4week`, success message shows; `submit.php` email body verified via `csc_process`. Mobile (375px): no horizontal scroll, tables scroll inside their wrapper, no console errors.

**DEPLOYED 2026-09-30 (Emilio approved; SFTP, only these 4 files, chmod 644):** `blog/4-week-vs-4-month-medical-billing-coding-course.html`, `medical-billing-coding-info.html`, `blog.html`, `sitemap.xml`. Live check: all four URLs return HTTP 200; `blog.html` and `sitemap.xml` list the new post; the post shows the Vicent Canal byline. Live form test: POST to `submit.php` with `source=blog-mbc-4week` returned `{"ok":true}` (subject `[blog-mbc-4week] Website inquiry from TEST - please ignore…`). **Open: confirm the test lead actually arrived in the `vcanal@` inbox** (I can't read that mailbox; delete the test lead afterward).

- **2026-10-01:** ITU Online reference in the 4-week vs 4-month post stays as written for now (Emilio). Marked `R-BLOG-MBC-ITU` in source + register: remove it when CSC launches its own courses. Comment-only source change; not deployed (no visible change).

## Update — 2026-10-01/02: salary post "Medical Coding and Billing Salary by State" (DEPLOYED 2026-10-02)

**DEPLOYED 2026-10-02 (Emilio approved the deploy and the $31.17 correction; SFTP, only these 4 files, chmod 644):** `blog/medical-coding-billing-salary-by-state.html`, `blog/4-week-vs-4-month-medical-billing-coding-course.html`, `blog.html`, `sitemap.xml`. Live check: all four return 200; the post has all 68 table rows, `$31.17`, the left-hand H2 list and the 4-week post's Related link; `blog.html` and `sitemap.xml` list the post; `it-careers-massachusetts-draft.html` is still 404 (not uploaded). Pre-deploy grep for `[VERIFY` / `DRAFT` / `CODE:` on the 4 files: no matches.

**Page layout (added after the first build, at Emilio's request):** an "On this page" list in the left column, side by side with the article column and spanning the width of the header title (from 1100px up; stacked below that). Plain bold links, no underline or background: the H2s from the second one on, then each of the 5 FAQ questions as its own link (clicking one opens that FAQ item), then Sources. The "Do medical coders get paid well?" H2 and FAQ question share a title, so it appears twice in the list. The date stays in the normal meta line (a large date block was tried and reverted).

**Open TODO:** `llms.txt` now lists the salary post locally but was not part of the approved 4-file deploy; upload it with the next deploy (needs Emilio's OK). Also logged: `docs/VERIFICATION_LOG.md` §M (wage sources) and a `PROJECT-HANDOFF.md` note that this post is the one exception to "no pay figures".

**Sitemap fix:** the live sitemap already listed `it-careers-massachusetts-draft.html` (a 404) since the 2026-09-30 deploy. `build-pages.py` now keeps that draft out of the sitemap (`HOLD`); the new sitemap has 28 URLs.

**Built (in `tools/build-pages.py`; pages regenerated, not hand-edited):**
- `/blog/4-week-vs-4-month-medical-billing-coding-course.html` — Category Medical, byline Vicent Canal, published 2026-09-30 (visible date + `datePublished`/`dateModified`). Text, links, BlogPosting + FAQPage JSON-LD and `COURSE-DEPENDENT: R-BLOG-MBC` markers copied from the source doc. Added to `blog.html` (top of grid) and `sitemap.xml`.
- `/medical-billing-coding-info.html` — name, email, phone (optional), state, "When would you like to start?" (ASAP / 1-3 months / Just exploring); posts to `submit.php` with `source=blog-mbc-4week`; success text "Thanks! We'll email you more information soon." No dates, prices or enrollment mentioned. Marked `R-BLOG-MBC`. **noindex and left out of the sitemap** (lead-capture page).
- `docs/COURSE_CONTENT_REGISTER.md`: added row **R-BLOG-MBC**.

**Guide-mode exceptions (approved by Emilio for this post only):**
1. The **$679** price in the "What you'll pay in total" table (generic "4-week online course" row; also stated in the lead sentence of that section).
2. The CTA heading **"Want to learn more about our courses?"**

**Small differences from the source file / decisions to confirm:**
- Source had a CODE note "no author byline"; the task says byline Vicent Canal, so the visible byline is Vicent Canal. The JSON-LD author was kept as written (Organization: Career Skills Center).
- Related line: links to `/healthcare-careers.html` (the live guide) instead of `/healthcare-careers-massachusetts.html` (now a 301), and adds post #6 "Can Medical Billing and Coding Be Learned Online?" as the source CODE note asked.
- FAQ markup converted to the site's `details.faq-item` accordion (same text as the JSON-LD); tables use `.data-table`; CTA uses `.post-cta`.
- Page hero "dek" = the meta description.
- In-article links are plain grey with no underline site-wide (`.prose a`), which hides this post's many source links. Added a small **scoped** style in this post's `<head>` only (navy + underline). **Recommend a site-wide `.prose a` rule later** (would need a CSS deploy).
- `og:type` stays `website` (shared template), not `article`.
- The form's generic JS validation message still reads "…name, phone, email, and program of interest" (shared `js/main.js`); not changed because only the named files are deployed.
- The post's price table uses third-party prices checked Sept 30, 2026 (per the source). Nothing in it is a CSC program fact except the approved $679 row.

**Checks:** pre-deploy `grep -rn -e '[VERIFY' -e 'DRAFT'` on the new/changed files: no matches. Local form test: payload has `source=blog-mbc-4week`, success message shows; `submit.php` email body verified via `csc_process`. Mobile (375px): no horizontal scroll, tables scroll inside their wrapper, no console errors.

**DEPLOYED 2026-09-30 (Emilio approved; SFTP, only these 4 files, chmod 644):** `blog/4-week-vs-4-month-medical-billing-coding-course.html`, `medical-billing-coding-info.html`, `blog.html`, `sitemap.xml`. Live check: all four URLs return HTTP 200; `blog.html` and `sitemap.xml` list the new post; the post shows the Vicent Canal byline. Live form test: POST to `submit.php` with `source=blog-mbc-4week` returned `{"ok":true}` (subject `[blog-mbc-4week] Website inquiry from TEST - please ignore…`). **Open: confirm the test lead actually arrived in the `vcanal@` inbox** (I can't read that mailbox; delete the test lead afterward).

- **2026-10-01:** ITU Online reference in the 4-week vs 4-month post stays as written for now (Emilio). Marked `R-BLOG-MBC-ITU` in source + register: remove it when CSC launches its own courses. Comment-only source change; not deployed (no visible change).

## Update — 2026-10-01/02: salary post "Medical Coding and Billing Salary by State" (DEPLOYED 2026-10-02)

**⛔ Deploy held, per the task rule "if any national figure doesn't match the BLS file, stop and report":** one national figure in the draft did not match BLS (see "Changes" #1). It is a one-cent correction, already fixed in the page, but Emilio should confirm before the deploy goes out.

**Built (in `tools/build-pages.py`; pages regenerated, not hand-edited):**
- `/blog/medical-coding-billing-salary-by-state.html` — Medical, published October 1, 2026, **7 min read** (1,496 words in the article body incl. tables, FAQ and sources, ÷ 230 = 6.5, rounded up), no byline (`article()` now accepts `author=None`). BlogPosting + FAQPage JSON-LD kept as written (both parse). Template: `.table-wrap` + `.data-table`, `.post-cta`, `details.faq-item`, as in the 4-week post. Added a small post-scoped style (navy underlined links like the 4-week post, caption style, `.data-table--narrow` so the 2–3 column tables don't get the 660px minimum).
- `blog.html` card (top of the grid) and `sitemap.xml` (regenerated by `build-pages.py`).
- `blog/4-week-vs-4-month-…html`: salary post added to its "Related:" line.
- `tools/build-salary-table.py`: reads `state_M2025_dl.xlsx` and rewrites everything between `<!-- STATE-TABLE:START/END -->` in `tools/build-pages.py` (51 rows, DC included, PR/Guam/VI left out; "*"/"**" → "Not published"; "#" → "or more"). Yearly update: `python3 tools/build-salary-table.py <file.xlsx>` then `python3 tools/build-pages.py`. Needs `openpyxl`.
- `docs/COURSE_CONTENT_REGISTER.md`: R-BLOG-MBC now also covers the salary post's CTA box.
- All "CODE:" comments followed and removed.

**BLS data:** `oesm25st.zip` (state) downloaded from bls.gov (plain curl gets a 403; a descriptive User-Agent with a contact address works). The state file has **no national row**, so the national checks used the matching `oesm25nat.zip` from the same May 2025 release.

**Changes to the draft (checked against BLS):**
1. **National table, "Upper 25%" hourly: $31.16 → $31.17** (BLS H_PCT75 = 31.17). This is the national mismatch that holds the deploy. Every other national figure matched: A_PCT10/25/50/75/90 = 37,000 / 43,490 / 51,140 / 64,820 / 81,150; H_PCT10/25/50/90 = 17.79 / 20.91 / 24.59 / 39.01; mean $56,790; all-jobs median $50,980.
2. 43-3021 median $48,500 / $23.32: matches.
3. Top-10 states table: all 10 states and figures match, same order.
4. Last FAQ (visible and JSON-LD): the five states (DC, RI, HI, WA, CA) are correct; the lowest, CA at $61,810, is above $61,000.
5. Job outlook wording: BLS Occupational Outlook Handbook says 8 percent, 2025 to 2035, "**much faster** than the average for all occupations". Draft said "faster than average"; changed to match BLS.
6. Related line: draft linked `/healthcare-careers-massachusetts.html` (now a 301); changed to `healthcare-careers.html`, as in the 4-week post.
- AAPC figures ($67,260, $55,721, $67,147 for CPC, $74,557, $81,227) checked against the live AAPC page: match. The "about 21 percent" is AAPC's 20.7%.

**Checks:** grep for `[VERIFY`, `DRAFT`, `CODE:` on the post, the 4-week post, `blog.html`, `sitemap.xml`: no matches. Mobile (375px): the page does not scroll sideways; only the 51-row state table scrolls, inside its box. Vermont's job count is "Not published" in BLS (`**`).

## Update — Sept 26, 2026: deeper Career Paths content

Expanded the four Career Paths pages with the training/pathway depth they were missing (all general
industry info, guide-mode compliant — no CSS course claims):
- **it-careers-massachusetts.html** — "Where you start and where it leads" certification ladder
  (help desk → networking → cybersecurity → cloud → programming) + honest entry-pay note.
- **healthcare-careers-massachusetts.html** — "Pick your path by where you want to work" (home/community,
  hospital/facility, clinic/office, remote) + license-vs-certification and entry-pay notes.
- **skilled-trades-careers-massachusetts.html** — "How you actually get into a trade" (theory + apprenticeship),
  a per-trade licensing table, online can/can't note, apprentice-vs-journeyman pay note.
- **career-paths.html** — "How training differs by field" comparison table.
- Added `.ladder` CSS component (style.css). Entry-level pay sources logged in VERIFICATION_LOG §I.
- Verified: all 4 pages parse clean, sections balanced, no ghost-course phrases, COURSE-DEPENDENT markers intact,
  local server returns HTTP 200. Not deployed (awaiting Emilio's OK per handoff rule 2c).

## 2026-10-04 follow-up: CNA numbers removed from healthcare-jobs post
- Emilio confirmed the CNA length ("4 to 12 weeks") and cost ("$500 to $2,000") in `healthcare-jobs-massachusetts` were made up. Removed from the table, the intro box and both FAQ answers; replaced with "varies by school (federal minimum 75 hours)" and "may be free if an employer hires you first".
- Back-links to `blog/cna-massachusetts.html` added in the healthcare-jobs, phlebotomist and pharmacy-technician posts.
- OPEN: the same post still has other unsourced length/cost figures (phlebotomist 4-8 weeks, EKG 4-12 weeks and $500-$2,000, medical assistant, billing/coding, pharmacy tech) from the same unknown source. Emilio to confirm whether to strip those too.
- Pay figures in role guides and mass.gov / D&S fee checks: Emilio said leave as is.
