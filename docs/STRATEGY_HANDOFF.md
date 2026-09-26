# Handoff — Website & Marketing Workstream (as of Sept 26, 2026)

**Read this first in any new chat about the website, blog or marketing.** Also saved in the "ETPL Massachusetts" Project as `claude/20-handoff-website-and-marketing.md`.

## What we're doing
Building the marketing engine for **Career Skills Center** (careerskillscenter.com, Quincy, MA): an honest pre-launch website + a Massachusetts-specific SEO blog, then B2B employer pages for the Workforce Training Fund Express Program. Strategy lives in the Project. The website is built by **Claude Code** in the local repo.

## Two-sided workflow
- **Website repo:** `/Users/desttes/Documents/ETPL/Website`. Git on `main`, local only (no remote). Live site deploys via SFTP (see `PROJECT-HANDOFF.md`).
- **To work on it from Cowork:** connect that folder with "Add folder." The strategy chat reads and writes files directly and commits to git.
  - After committing, remove `.git/*.lock`, `.git/objects/*.lock` and `tmp_obj_*`; this needs delete permission, so ask once.
- **Strategy → Code:** strategy writes these files in the repo:
  - `CLAUDE.md` (rules Code reads every session)
  - `docs/BUILD_BRIEF.md` (build spec, v1.3)
  - `docs/PRE_LAUNCH_SITE_SPEC.md` (Option A)
  - `docs/VERIFICATION_LOG.md` (fact-check verdicts + sources)
  - `docs/content/` (Massachusetts facts pack for the blog)
- **Code → Strategy:** Code logs every session in `docs/BUILD_STATUS.md`. **Read it at the start of each session.**
- Emilio tells Code: "Read CLAUDE.md and follow it," plus the specific task.

## Key decisions (don't reverse without Emilio)
1. **Program facts policy:** program details on the site were placeholders. Never state CSC program length, hours, price, credential, format, certificate, start dates or VA status. The only allowed claim: "CSC is developing training in IT and Medical Billing & Coding, and plans to add Skilled Trades."
2. **Option A pre-launch mode:** program pages = "Program in development" + an **interest-list form** (which asks "How would you likely pay?").
3. **No fake social proof:** fabricated testimonials removed (live). No testimonials or outcome stats unless real. `outcomes.html` withdrawn.
4. **No funding claims:** never claim ETPL/WIOA approval or Express listing. Use "working toward approval" and "may qualify."
5. **No deploys without Emilio's OK;** pre-deploy grep for `[VERIFY` / `DRAFT` must be clean.
6. **Real publish dates only.**
7. **Form backend** = cPanel PHP mailer (`submit.php`), live. Leads go to `vcanal@careerskillscenter.com`.

## Status
**Live:** mailer working; fake testimonials removed.
**Built locally, awaiting deploy OK:** full Option A rework + interest-list form + `programs.html` redirect.
**Blog:** 8 posts written, expanded, fact-checked, with MA BLS wages in post #5. Still DRAFT, awaiting Emilio's approval.

**Not built yet:**
- menu/footer restructure
- `js/site-config.js`
- For Employers pages: `employers.html`, `workplace-esol.html` (+ `-es`/`-pt`), `clinic-billing-training.html`, `reimbursement-calculator.html`
- `qualify.html`
- 4 Massachusetts landing pages

## Next steps
1. **Emilio:** approve deploying the Option A rework (the blog stays excluded until approved).
2. **Emilio:** review/approve the 8 blog drafts.
3. **Strategy: update the brief before Code builds more:**
   - (a) **Reword the employer pages** to match Project doc `13`. CSC is not yet an Express provider and has no own ESOL course. Phase 0 = sell other providers' approved courses and do the grant paperwork. Copy should say "we help you get state-funded training for your staff," not "our course."
   - (b) **Hold `qualify.html`**, or merge it into the interest form.
   - (c) **Hold the 4 MA landing pages** until programs are real.
4. **Emilio still owes:** checklist PDF content; Workforce Pell mention yes/no; VA FAQ wording.
5. **Leftovers:** `contact.html` "campus"/parking TBD; `team.html` and `media.html` placeholders to convert or remove.
6. **Verify with CommCorp (express@commcorp.org):** Express tiers (any-size at 50% vs. ≤100 employees).
7. **Strategy flag:** the FY27 MA ETPL policy (100 DCS 14.106.2) may weaken the "apprenticeship → automatic ETPL" shortcut. Read Attachment A.

## Read next
1. Project `claude/18-competitor-marketing-analysis.md`
2. Project `claude/19-website-build-brief.md`
3. Project `claude/13-express-esol-go-to-market-90-days.md`
4. Project `11-...` and `02-...` (funding facts)
5. Repo `docs/BUILD_STATUS.md`, then `CLAUDE.md`
