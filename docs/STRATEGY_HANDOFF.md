# Handoff — Website & Marketing Workstream (as of Sept 26, 2026)

**Read this first in any new chat about the website, blog or marketing.** Also saved in the "ETPL Massachusetts" Project as `claude/20-handoff-website-and-marketing.md`.

## What we're doing
Building the marketing engine for **Career Skills Center** (careerskillscenter.com, Quincy, MA). **Since Sept 26 the site is in "guide mode":** CSC has no courses yet, so the site is an honest guide to Massachusetts careers and training funding that sends people **outward** to the state (MassHire, JobQuest, mass.gov). When real courses launch, it switches to **course mode** and sends people **inward**. Goal now: look legitimate and build SEO with real content. The one real service today: helping MA employers get state-funded staff training (Express Program) and doing the grant paperwork.

## Two-sided workflow
- **Website repo:** `/Users/desttes/Documents/ETPL/Website`. Git on `main`, local only. Live site deploys via SFTP (see `PROJECT-HANDOFF.md`).
- **From Cowork:** connect that folder with "Add folder." The strategy chat reads/writes files and commits. After committing, remove `.git/*.lock`, `.git/objects/*.lock`, `tmp_obj_*` (needs delete permission; ask once).
- **Strategy → Code** (files in the repo): `CLAUDE.md` · `docs/GUIDE_MODE_SPEC.md` (v1.4, current plan) · `docs/BUILD_BRIEF.md` (v1.3 detail, v1.4 note on top) · `docs/COURSE_CONTENT_REGISTER.md` · `docs/VERIFICATION_LOG.md` · `docs/content/` · `docs/PRE_LAUNCH_SITE_SPEC.md` (superseded in part).
- **Code → Strategy:** `docs/BUILD_STATUS.md`. Read it at the start of each session.
- Emilio tells Code: "Read CLAUDE.md and follow it," plus the task.

## Key decisions (don't reverse without Emilio)
1. **Guide mode (Sept 26):** no ghost courses. Program pages become career field guides: **Healthcare** (not "Medical Billing & Coding"; broad reference on many medical roles), **IT**, **Skilled Trades**. Allowed CSC claim: "plans to offer training in healthcare, IT and the skilled trades."
2. **Outward now, inward later.** CTAs point to MassHire/JobQuest/our guides; interest list is secondary ("get updates when we launch").
3. **`qualify.html` stays:** collects the lead, then gives outward next steps to enroll with the state. No "advisor will text you" promise. Routes inward only in course mode.
4. **Track course-dependent copy** in `docs/COURSE_CONTENT_REGISTER.md` + `<!-- COURSE-DEPENDENT -->` markers; switches `SITE_MODE` / `COURSES_LIVE` in `js/site-config.js`.
5. **No fake social proof,** no funding claims (never ETPL/WIOA approval or Express listing; "may qualify").
6. **Employer pages:** "we help you get state-funded training and handle the paperwork," never "our course." Clinic billing page on hold.
7. **No deploys without Emilio's OK;** pre-deploy `[VERIFY`/`DRAFT` grep clean. Real publish dates only.
8. **Form backend** = cPanel PHP mailer (`submit.php`), live; leads → `vcanal@careerskillscenter.com`.

## Status
**Live:** mailer; fake testimonials removed. The live program/tuition pages still show old made-up course details until the guide-mode build ships.
**Built locally (not deployed):** Option A rework, interest form, `qualify.html`, 8 blog drafts. These get reworked into guide mode, not deployed as-is.
**Next:** Code builds GUIDE_MODE_SPEC steps 1–7, then Emilio approves one deploy; then step 8 (employer pages) and step 9 (blog CTA updates + approval).

## Open items
- Emilio: approve the 8 blog drafts (after step 9 CTA updates); checklist PDF content; Workforce Pell mention (yes/no); VA FAQ wording.
- Verify Express tiers with express@commcorp.org (DCS Info 26-102 vs doc `11`).
- FY27 ETPL policy (100 DCS 14.106.2): check Attachment A before relying on the apprenticeship → ETPL shortcut.
