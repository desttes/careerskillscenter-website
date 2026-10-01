# Course Content Register

**Purpose:** one list of every place on the site whose content must change when Career Skills Center launches real courses. When a course goes live, work down this list and nothing gets missed.

**Owner:** Claude Code keeps it current. Every time you write course-dependent copy, add a row and put `<!-- COURSE-DEPENDENT: R-xx -->` next to it in the source (`tools/build-pages.py` or `index.html`).
**Switches:** `js/site-config.js` → `SITE_MODE` ("guide" / "courses") and `COURSES_LIVE.{healthcare,it,trades}`.
**Started:** Sept 26, 2026 (strategy seeded it from `docs/GUIDE_MODE_SPEC.md`; Code updates the "Location in source" column as pages are built).

## Rows

> **v1.5 update (Sept 27, 2026):** Career Paths pages were renamed to location-neutral slugs
> (`healthcare-careers.html`, `it-careers.html`, `skilled-trades-careers.html`) and their pay figures were
> removed pending sourced data (see **R-PAY-DATA**). New Funding Guides + For Employers pages were added.
> Most rows are tracked with `<!-- COURSE-DEPENDENT: R-xx -->`. Exceptions, tracked by other markers or as
> pending work: **R-PAY-DATA** (`<!-- PAY-DATA: pending -->`), **R-EMP** / **R-SCHEMA** (design flags, no
> inline marker yet), **R-LLMS** (whole file).
>
> **LIVE-DEPLOY update (Sept 28, 2026):** Emilio decided **no real wage/salary figures anywhere on the site** —
> so **R-PAY-DATA now applies to the blog too**: blog posts use qualitative wording + a BLS look-up link instead
> of dollar medians. Blog post **"Highest-Paying Certifications" was removed entirely** (file + all cross-links).
> R-BLOG still covers careers posts #6–#8. The full v1.5 site (incl. blog) is now LIVE.

| ID | Page / file | Section | Now (guide mode) | When a course launches (course mode) | Switch | Location in source |
|---|---|---|---|---|---|---|
| R-NAV | `index.html` header + footer | Menu | Funding Guides · For Employers · Career Paths · Resources; header button "Do I Qualify?" → qualify | Add a "Courses" or per-field "Train with us" item; decide header button | SITE_MODE | `index.html` (nav-list + footer-links, marked) |
| R-HOME | `index.html` | Hero + sections | "Career training and funding, explained"; Funding Guides + For Employers + Career Paths; interest list as secondary CTA | Feature live courses; primary CTA inward | SITE_MODE | `index.html` (hero + interest band, marked) |
| R-HC | `healthcare-careers.html` | "Get updates" interest block | Outward funding links + interest list "when we launch" | "Train with Career Skills Center" block: course name, details, enroll/apply CTA | COURSES_LIVE.healthcare | `build-pages.py` field_interest("healthcare") (marked) |
| R-IT | `it-careers.html` | same | same | same | COURSES_LIVE.it | `build-pages.py` field_interest("it") (marked) |
| R-TR | `skilled-trades-careers.html` | same | same | same | COURSES_LIVE.trades | `build-pages.py` field_interest("trades") (marked) |
| R-HUB | `career-paths.html` | Cards | Cards link to guides | Cards show "Now enrolling" badge + course link for live fields | COURSES_LIVE.* | `build-pages.py` career-paths.html (marked) |
| R-QUALIFY | `qualify.html` + `js/main.js` | Result screen + field note | Results-first: which WIOA group you may fit + outward next steps (MassHire, JobQuest, ITA, Section 30) | Result also routes inward: matching CSC course + "we'll help with funding" | SITE_MODE, COURSES_LIVE.* | `build-pages.py` qualify.html + `js/main.js` classifyQualify (marked) |
| R-PAY | `student-financing.html` | Options | Guide to MA funding options; no CSC terms; "working toward approval" disclosure | Add CSC tuition, payment plan terms, lenders; flip ETPL copy only if `FUNDING_ETPL_APPROVED` | SITE_MODE, FUNDING_ETPL_APPROVED | `build-pages.py` student-financing.html (marked) |
| R-FAQ | `faq.html` | Launch/program answers | "We plan to launch training; get updates" | Real length, cost, credential, schedule, VA answers | SITE_MODE | `build-pages.py` faq.html (marked) |
| R-ABOUT | `about.html` | "What we're building" + career support | Future tense | Present tense; instructors, delivery | SITE_MODE | `build-pages.py` about.html (marked) |
| R-WIOA | `wioa-explained.html` | Funding-note / CSC mention | "Working toward approval; plans to offer training" | CSC is an approved provider / has live courses | SITE_MODE, FUNDING_ETPL_APPROVED | `build-pages.py` wioa-explained.html (marked) |
| R-LLMS | `llms.txt` | Whole file | Site = career/funding guide; training planned | List live courses | SITE_MODE | `llms.txt` |
| R-IFORM | Interest-list form (site-wide) | Field select + success msg | "Get updates when we launch training in [field]" | Replace with enroll/apply form on live fields | COURSES_LIVE.* | `build-pages.py` interest_form() (marked) |
| R-BLOG | `blog/*.html` (careers posts #6–#8) | CTA boxes + "CSC plans to…" lines | CTAs → career guides / funding guides | CTAs → matching CSC course | COURSES_LIVE.* | `build-pages.py` post_cta() for #6/#7/#8 (marked) |
| R-BLOG-MBC | `blog/4-week-vs-4-month-medical-billing-coding-course.html` (CTA box) + `blog/medical-coding-billing-salary-by-state.html` (CTA box, same heading and form link) + `medical-billing-coding-info.html` | CTA box + interest form | Interest form: CTA box links to `/medical-billing-coding-info.html` (name, email, phone, state, start timing; posts `source=blog-mbc-4week`). No dates, prices or enrollment on the form page. Post also carries two Emilio-approved guide-mode exceptions: the $679 "4-week online course" price row and the CTA heading "Want to learn more about our courses?" | Re-route the CTA link to the course/enroll page; retire or redirect the info form page; revisit the $679 row and the CTA heading | COURSES_LIVE.healthcare | `build-pages.py` (marked `<!-- COURSE-DEPENDENT: R-BLOG-MBC -->` in both post bodies and the form page) |
| R-BLOG-MBC-ITU | `blog/4-week-vs-4-month-medical-billing-coding-course.html` | Paragraph "A 4-week course is much shorter…" | Names ITU Online's ICD-10/ICD-11 course and course list as examples of short online courses (hours of video, ~38 hours total) | **Remove the ITU Online reference** when CSC adds its own courses (Emilio, 2026-10-01) | COURSES_LIVE.healthcare | `build-pages.py` (marked `<!-- COURSE-DEPENDENT: R-BLOG-MBC-ITU -->`) |
| R-CORP | `corporate-training.html` | Whole page | "We're building training for employers; tell us what you need" | Live corporate offerings, formats, enrollment | SITE_MODE | `build-pages.py` corporate-training.html (marked) |
| R-APPR | `apprenticeships.html` | Graduate-pipeline line | "As our programs launch, our graduates will become a hiring pipeline…" (future tense) | Present tense; real graduate pipeline | SITE_MODE, COURSES_LIVE.* | `build-pages.py` apprenticeships.html (marked) |
| R-PAY-DATA | Career pages (`healthcare-careers.html`, `it-careers.html`, `skilled-trades-careers.html`) | Role-card pay slot | Pay figures omitted; hidden slot pending sourced entry-level data | Add sourced "Typical pay" to each role card | — (data task) | `build-pages.py` role_card() `<!-- PAY-DATA: pending -->` |
| R-EMP | `employers.html`, `staff-training-grants.html`, `express-program-explained.html` | Service description | **CSC provides the training only.** The employer applies for Express directly with the state; CSC does not handle paperwork, apply on the employer's behalf, or take payment for the grant process (per MA rules, Emilio 2026-09-28). No "our course" until `EXPRESS_PROVIDER_LISTED`. | If CSC lists its own Express courses: "our course," listing language only when `EXPRESS_PROVIDER_LISTED` | EXPRESS_PROVIDER_LISTED | `build-pages.py` staff-training-grants.html (no inline marker; flag-gated copy) |
| R-SCHEMA | JSON-LD on all pages | Structured data | EducationalOrganization only; no `Course` schema | Add `Course` schema with real data | COURSES_LIVE.* | TBD |

## Retired URLs (restore or re-point only in course mode)
| Old URL | Now 301s to | Course mode |
|---|---|---|
| `medical-billing-coding.html` | `healthcare-careers.html` | Could become a real course page |
| `it-support-specialist.html` | `it-careers.html` | Could become a real course page |
| `skilled-trades.html` | `skilled-trades-careers.html` | Could become a real course page |
| `healthcare-careers-massachusetts.html` | `healthcare-careers.html` | v1.4 → v1.5 slug rename |
| `it-careers-massachusetts.html` | `it-careers.html` | v1.4 → v1.5 slug rename |
| `skilled-trades-careers-massachusetts.html` | `skilled-trades-careers.html` | v1.4 → v1.5 slug rename |
| `our-programs.html`, `programs.html` | `career-paths.html` | Could list real courses |
| `tuition.html` | `student-financing.html` | Real tuition page |
| `admissions.html` | `career-paths.html` | Real admissions page |
| `career-services.html` | `about.html` | Real career services page |
| `team.html`, `media.html` | `about.html` | Real team page |
| `terms-of-use.html` | `terms.html` | Legal page rename (v1.5) |

## Course-launch checklist (run when a field goes live)
1. Confirm real facts with Emilio: course name, length, hours, price, credential, schedule, start date, delivery, VA status.
2. Flip `COURSES_LIVE.<field>` (and `SITE_MODE` to "courses" for the first course).
3. Work every row above for that field; `grep -rn 'COURSE-DEPENDENT' .` to find each spot.
4. Update the program facts policy in `CLAUDE.md` for that course.
5. Pre-deploy `[VERIFY`/`DRAFT` check, then deploy with Emilio's OK.
