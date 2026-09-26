# Guide Mode Spec — v1.4 (Sept 26, 2026)

**From:** strategy side (Cowork), approved by Emilio · **For:** Claude Code
**Supersedes:** `docs/PRE_LAUNCH_SITE_SPEC.md` (Option A) wherever they conflict. Where this spec is silent, BUILD_BRIEF v1.3 still applies.

## The idea in one line
**Now (guide mode):** careerskillscenter.com is an honest guide to how Massachusetts training and funding work, and it sends people **outward** to the state (MassHire, JobQuest, mass.gov). **Later (course mode):** when real CSC courses exist, the same pages start sending people **inward** to CSC.

## Why
CSC has no courses yet. The old site showed made-up ("ghost") courses. We don't pretend anything anymore. We publish real, useful reference content so the site looks legitimate and starts ranking in search now. Everything that will change when courses launch is tracked in `docs/COURSE_CONTENT_REGISTER.md`.

## Global rules
1. **No ghost courses.** No CSC course, program length, hours, price, credential, schedule, start date, instructor, campus, outcome or testimonial anywhere. (The program facts policy in `CLAUDE.md` still applies.)
2. **Allowed about CSC:** "Career Skills Center plans to offer training in healthcare, IT and the skilled trades. Get updates when we launch."
3. **Direct outward.** Calls to action point to official state resources (below) or to our own guides/blog. The interest list stays as a secondary CTA ("Get updates when we launch training").
4. **Track course-dependent copy.** Any sentence, CTA, link or block that must change when courses launch gets an HTML comment `<!-- COURSE-DEPENDENT: R-xx -->` and a row in `docs/COURSE_CONTENT_REGISTER.md`. Grep for `COURSE-DEPENDENT` must find every spot.
5. **Switches.** Create `js/site-config.js` (brief §6) and add:
   ```js
   export const SITE_MODE = "guide";   // "guide" now; "courses" once any course is live
   export const COURSES_LIVE = { healthcare: false, it: false, trades: false };
   ```
   Course-mode copy may be pre-written behind these switches, but must never render while they are false.
6. **Facts need sources.** Every pay figure (BLS OEWS May 2025, Massachusetts) and every licensing/certification requirement needs a source (bls.gov, mass.gov, the licensing board) logged in `docs/VERIFICATION_LOG.md`. Unsourced = `[VERIFY]` = not deployable.
7. Funding language rules are unchanged: never claim ETPL/WIOA approval or Express listing; "may qualify"; only a MassHire career center approves funding.

## Official outward destinations (verified)
- MassHire Career Center locations: https://www.mass.gov/info-details/masshire-career-center-locations
- MassHire JobQuest (registration required before training funding): https://jobquest.mass.gov
- Any other state URL: verify it loads and log it in VERIFICATION_LOG before using it.

## Build order (do in this order; deploy steps 1–7 together, then 8–9)

### Step 1 — Groundwork
`js/site-config.js` with the flags above plus the brief §6 values. Keep `docs/COURSE_CONTENT_REGISTER.md` current as you work.

### Step 2 — Menu and footer (edit `index.html`, rebuild)
- Menu: **Career Paths** (Healthcare · Information Technology · Skilled Trades · All Career Paths) · **For Employers** (add when step 8 pages exist) · **Resources** (Blog · Ways to Pay · Check Your Funding Options → `qualify.html`) · **About** · **Contact**.
- Header button: **"Check Your Options"** → `qualify.html`. Remove "Tuition," "Admissions," "Career Services," "Student Financing" labels.
- Footer: same structure; fix the broken "Catalog" link (remove it).

### Step 3 — Three career field guides (replace the program pages)
Each page is a **reference guide to a whole field in Massachusetts**, not a course page.
| New URL | Replaces (301) | H1 (suggested) |
|---|---|---|
| `healthcare-careers-massachusetts.html` | `medical-billing-coding.html` | Healthcare Careers in Massachusetts: Jobs, Pay and How to Train |
| `it-careers-massachusetts.html` | `it-support-specialist.html` | IT Careers in Massachusetts: Jobs, Pay and How to Train |
| `skilled-trades-careers-massachusetts.html` | `skilled-trades.html` | Skilled Trades Careers in Massachusetts: Jobs, Pay and Licensing |

These also **replace the 4 MA landing pages in brief §3.4** (don't build those separately).

Per page:
1. Intro: what the field looks like in Massachusetts; who it suits.
2. **Role cards / table**, one per role: what the job is · MA median pay (BLS OEWS May 2025 MA, cite SOC code) · typical training path (short certificate, apprenticeship, degree) · MA license/registration/certification requirements (sourced) · "Can you train online?" (honest).
   - Healthcare: medical billing & coding, medical assistant, phlebotomy technician, pharmacy technician, EKG technician, nurse aide (CNA), home health aide, medical administrative assistant.
   - IT: help desk / computer user support, network support technician, entry-level cybersecurity, cloud support.
   - Skilled trades: electrician, HVAC/R technician, plumber, welder (add others only if sourced).
3. **How to pay for training in MA** → short summary linking to the blog funding posts and `qualify.html`.
4. **Next step (outward):** find your MassHire Career Center + register on JobQuest.
5. Secondary CTA: interest list, "Get updates when Career Skills Center launches training in this field." `<!-- COURSE-DEPENDENT -->`
6. Related blog posts. FAQ (4–6 Qs) with FAQPage schema.
- Title pattern: "Healthcare Careers in Massachusetts: Jobs, Pay & Training (2026) | Career Skills Center". Real year only.
- No `Course` schema.

### Step 4 — `career-paths.html` (hub; 301 from `our-programs.html` and `programs.html`)
Cards for the 3 fields, each linking to its guide. Short intro: "Explore careers you can train for in Massachusetts." Interest list secondary.

### Step 5 — `qualify.html` → outward funding-options tool (KEEP it)
Keep the 6-step wizard; it **collects the lead** (posts to `submit.php`, `source=qualify`) and then **sends the person to the state**.
- Rename the concept: title "Check Your Options for State-Funded Training in Massachusetts"; H1 "Find out what training help you may qualify for." Button/nav label "Check Your Options."
- Q1 becomes "Which field interests you?" (Healthcare / IT / Skilled Trades / Not sure).
- Keep Q2–Q5. Q6 contact: first name, email (required), mobile (optional), preferred language, consent checkbox "Send me updates from Career Skills Center (email/SMS)."
- **Remove the promise** "An advisor will text you within 1 business day." CSC has no advisors yet.
- **Result screen = personalized outward next steps** (never a yes/no verdict):
  - Likely funded fit (lives in MA and unemployed / laid off / part-time-low-wage, or on public assistance): "You may qualify for state-funded training. Here's how to start:" 1) Find your MassHire Career Center (link) 2) Register on JobQuest (link) 3) Attend a Training Information Meeting 4) Ask about an Individual Training Account (ITA); if you get unemployment benefits, ask about Section 30 5) Choose a state-approved training program in your field. Links to blog posts #1, #2, #3.
  - Employer = Yes/Maybe: "Your employer may be able to get training costs reimbursed by Massachusetts" → `employers.html` once built (interim: blog post #1 Express section).
  - Otherwise: "Here are other ways to pay" → Ways to Pay + the field guide.
  - Always: link to the field guide they picked + "We'll let you know when we launch training in [field]." `<!-- COURSE-DEPENDENT -->`
- **Course mode later:** results route inward (CSC program + our funding help). Pre-write behind `SITE_MODE`; register row R-QUALIFY.

### Step 6 — Retire pages that imply enrollment (301s via `.htaccess`, Code decides mechanics)
- `tuition.html` → 301 to `student-financing.html`.
- `admissions.html` → 301 to `career-paths.html`.
- `career-services.html` → fold one short future-tense paragraph into `about.html`; 301 to `about.html`.
- `team.html`, `media.html` → remove; 301 to `about.html`.
- Remove all retired pages from nav, footer, sitemap and `llms.txt`.

### Step 7 — Remaining pages
- `index.html`: reframe as "Your guide to career training and funding in Massachusetts." Sections: the 3 career paths · how state funding works (→ qualify, blog) · For Employers teaser (when built) · latest guides · interest list. No course claims.
- `student-financing.html` ("Ways to Pay for Training in Massachusetts"): a guide to MA options (WIOA/ITA, Section 30, Donnelly, employer-paid/Express, payment plans in general, private lenders in general), outward links, disclosure kept. No CSC terms.
- `about.html`: mission, Quincy-based, what we're building; no campus/instructors/accreditation claims.
- `faq.html`: rewrite around the guide (how funding works, how to find your career center, when CSC will launch training).
- `contact.html`: remove "campus"/parking text.
- `llms.txt`: describe the site as a Massachusetts career-and-funding guide; CSC plans training in healthcare, IT and skilled trades.

### Step 8 — For Employers (real service now; see BUILD_BRIEF §4 with this framing)
CSC helps employers get state-funded training for their staff and handles the grant paperwork. CSC is **not** a listed Express provider and has no course of its own: never "our course." Pages: `employers.html` (with embedded eligibility form, `source=employer`), `workplace-esol.html` + `-es` + `-pt`, `reimbursement-calculator.html`. `clinic-billing-training.html` is on hold.

### Step 9 — Blog
- Update the 8 drafts: CTAs point to the field guides, `qualify.html` and MassHire, not to "our program." Mark any CSC mention `COURSE-DEPENDENT`.
- Post #6 keeps its specific topic (it targets an exact search). Add a new broad post to the backlog: "Healthcare Jobs You Can Train For in Massachusetts (2026)."
- Backlog (one per role, after approval of the 8): "How to Become a [Phlebotomist / Pharmacy Technician / CNA / Medical Assistant / Electrician / HVAC Technician] in Massachusetts."

## Acceptance
- `grep -rn 'COURSE-DEPENDENT' --include='*.html' .` matches every row in the register.
- Spec acceptance greps from PRE_LAUNCH_SITE_SPEC still return nothing.
- No link to a retired page anywhere; every retired URL 301s.
- Pre-deploy `[VERIFY`/`DRAFT` check clean on everything being deployed.
