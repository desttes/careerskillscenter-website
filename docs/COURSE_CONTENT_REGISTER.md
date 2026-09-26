# Course Content Register

**Purpose:** one list of every place on the site whose content must change when Career Skills Center launches real courses. When a course goes live, work down this list and nothing gets missed.

**Owner:** Claude Code keeps it current. Every time you write course-dependent copy, add a row and put `<!-- COURSE-DEPENDENT: R-xx -->` next to it in the source (`tools/build-pages.py` or `index.html`).
**Switches:** `js/site-config.js` → `SITE_MODE` ("guide" / "courses") and `COURSES_LIVE.{healthcare,it,trades}`.
**Started:** Sept 26, 2026 (strategy seeded it from `docs/GUIDE_MODE_SPEC.md`; Code updates the "Location in source" column as pages are built).

## Rows

| ID | Page / file | Section | Now (guide mode) | When a course launches (course mode) | Switch | Location in source |
|---|---|---|---|---|---|---|
| R-NAV | `index.html` header + footer | Menu | "Career Paths" → field guides; button "Check Your Options" → qualify | Add a "Courses" or per-field "Train with us" item; decide header button | SITE_MODE | `index.html` (nav-list + footer-links, marked) |
| R-HOME | `index.html` | Hero + sections | "Your guide to career training and funding in MA"; interest list as secondary CTA | Feature live courses; primary CTA inward | SITE_MODE | TBD |
| R-HC | `healthcare-careers-massachusetts.html` | "Get updates" block + Next step | Outward: MassHire + JobQuest; interest list "when we launch" | "Train with Career Skills Center" block: course name, details, enroll/apply CTA | COURSES_LIVE.healthcare | `build-pages.py` field_interest("healthcare") + outward_next_step (marked) |
| R-IT | `it-careers-massachusetts.html` | same | same | same | COURSES_LIVE.it | `build-pages.py` field_interest("it") + outward_next_step (marked) |
| R-TR | `skilled-trades-careers-massachusetts.html` | same | same | same | COURSES_LIVE.trades | `build-pages.py` field_interest("trades") + outward_next_step (marked) |
| R-HUB | `career-paths.html` | Cards | Cards link to guides | Cards show "Now enrolling" badge + course link for live fields | COURSES_LIVE.* | `build-pages.py` career-paths.html (marked) |
| R-QUALIFY | `qualify.html` + `js/main.js` | Q1 options + result screen | Collects lead, then outward next steps (MassHire, JobQuest, ITA, Section 30) | Result routes inward: matching CSC course + "we'll help with funding"; may restore an advisor follow-up promise if staffed | SITE_MODE, COURSES_LIVE.* | `build-pages.py` qualify.html + `js/main.js` routeResult (marked) |
| R-PAY | `student-financing.html` | Options | Guide to MA funding options; no CSC terms; "working toward approval" disclosure | Add CSC tuition, payment plan terms, lenders; flip ETPL copy only if `FUNDING_ETPL_APPROVED` | SITE_MODE, FUNDING_ETPL_APPROVED | TBD |
| R-FAQ | `faq.html` | Program answers | "We plan to launch training; get updates" | Real length, cost, credential, schedule, VA answers | SITE_MODE | TBD |
| R-ABOUT | `about.html` | Mission + career support paragraph | Future tense | Present tense; instructors, delivery | SITE_MODE | TBD |
| R-LLMS | `llms.txt` | Whole file | Site = MA career/funding guide; training planned | List live courses | SITE_MODE | `llms.txt` |
| R-IFORM | Interest-list form (site-wide) | Field select + success msg | "Get updates when we launch training in [field]" | Replace with enroll/apply form on live fields | COURSES_LIVE.* | TBD |
| R-BLOG | `blog/*.html` (8 posts) | CTA boxes + "CSC plans to…" lines | CTAs → field guides, qualify, MassHire | CTAs → matching CSC course | COURSES_LIVE.* | TBD (one row per post may be added) |
| R-EMP | `employers.html`, `workplace-esol*.html` | Service description | Concierge: we help you apply; training by approved providers | If CSC lists its own Express courses: "our course," listing language only when `EXPRESS_PROVIDER_LISTED` | EXPRESS_PROVIDER_LISTED | TBD |
| R-SCHEMA | JSON-LD on all pages | Structured data | EducationalOrganization only; no `Course` schema | Add `Course` schema with real data | COURSES_LIVE.* | TBD |

## Retired URLs (restore or re-point only in course mode)
| Old URL | Now 301s to | Course mode |
|---|---|---|
| `medical-billing-coding.html` | `healthcare-careers-massachusetts.html` | Could become a real course page |
| `it-support-specialist.html` | `it-careers-massachusetts.html` | Could become a real course page |
| `skilled-trades.html` | `skilled-trades-careers-massachusetts.html` | Could become a real course page |
| `our-programs.html`, `programs.html` | `career-paths.html` | Could list real courses |
| `tuition.html` | `student-financing.html` | Real tuition page |
| `admissions.html` | `career-paths.html` | Real admissions page |
| `career-services.html` | `about.html` | Real career services page |
| `team.html`, `media.html` | `about.html` | Real team page |

## Course-launch checklist (run when a field goes live)
1. Confirm real facts with Emilio: course name, length, hours, price, credential, schedule, start date, delivery, VA status.
2. Flip `COURSES_LIVE.<field>` (and `SITE_MODE` to "courses" for the first course).
3. Work every row above for that field; `grep -rn 'COURSE-DEPENDENT' .` to find each spot.
4. Update the program facts policy in `CLAUDE.md` for that course.
5. Pre-deploy `[VERIFY`/`DRAFT` check, then deploy with Emilio's OK.
