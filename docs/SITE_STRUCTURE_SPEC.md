# Site Structure Spec — v1.5 (Sept 27, 2026)

**From:** strategy side, approved by Emilio · **For:** Claude Code
**Supersedes:** the nav, page list and build order in `docs/GUIDE_MODE_SPEC.md` (v1.4). Everything else in v1.4 still applies: no ghost courses, funding language rules, `[VERIFY]` sourcing, `COURSE-DEPENDENT` markers, the register, and no deploys without Emilio's approval. Repo copy: `docs/SITE_STRUCTURE_SPEC.md`.

## Why this version
1. **Main goal right now: legitimacy.** Course providers will judge Career Skills Center (CSC) by this site and the corporate email. The site must look like a real, well-informed business, with nothing made up.
2. **Second goal: SEO.** Publish real reference content that ranks.
3. **Scope change:** CSC will also serve companies anywhere that train staff with their own budget. The funding pages stay Massachusetts-specific because WIOA (as run by MassHire) and Express are MA programs. Career Paths and Corporate Training use **no location framing**.

## New global rules (in addition to v1.4)
- **Career Paths:** remove "Massachusetts" from titles, H1s, copy and URLs. **No pay figures on any page for now.** Pay data will be researched separately, so leave a hidden slot and add register row R-PAY-DATA.
- **Corporate Training:** never say "out of state" and never imply state funding is needed.
- **Apprenticeship and graduates:** future tense only. Allowed wording: "As our programs launch, our graduates will become a hiring pipeline for partner employers." Never state or imply current students or graduates. Mark it `COURSE-DEPENDENT`.
- **No "For Training Providers" page.** Partner inquiries go through the Contact form (see page 7c).

## Navigation
```
Funding Guides
  WIOA Explained ................ wioa-explained.html            (NEW)
  Do I Qualify? ................. qualify.html                   (REWORK)
  Express Program Explained ..... express-program-explained.html (NEW)
For Employers
  Overview ...................... employers.html                 (NEW)
  Staff Training Grants ......... staff-training-grants.html     (NEW, calculator embedded)
  Apprenticeship Programs ....... apprenticeships.html           (NEW)
  Corporate Training ............ corporate-training.html        (NEW)
Career Paths
  Healthcare .................... healthcare-careers.html
  Information Technology ........ it-careers.html
  Skilled Trades ................ skilled-trades-careers.html
  All Career Paths .............. career-paths.html
Resources
  Blog .......................... blog.html
  FAQ ........................... faq.html
About ........................... about.html
Contact ......................... contact.html

Header button: "Do I Qualify?" → qualify.html
Footer: same groups + Privacy Policy · Terms · phone · email · Quincy, MA address · LinkedIn
```

## Pages, in build order

### 1. Home + About (credibility)
- **`index.html`**
  - H1: "Career training and funding, explained."
  - Sections: Funding Guides (WIOA, Express, Do I Qualify?) · For Employers teaser (apprenticeships, staff training grants, corporate training) · Career Paths · latest blog posts · interest list (secondary).
  - Allowed CSC line: "Career Skills Center plans to offer training in healthcare, IT and the skilled trades." `COURSE-DEPENDENT`
- **`about.html`**
  - Mission; what CSC is building (funded training, employer and apprenticeship training, corporate training).
  - Founder name and photo (Emilio to supply). Quincy-based. Real contact details.
  - Future tense throughout. No campus, instructors, accreditation or outcomes.

### 2. WIOA Explained + Do I Qualify?
- **`wioa-explained.html`** — Title: "WIOA Training Funds Explained: Who Qualifies and How to Apply in Massachusetts"
  - Sections: what WIOA is · the three groups (Adult, Dislocated Worker, Youth) · priority of service (public assistance, low income, basic skills deficient, veterans) · the ITA voucher (what it covers and what it doesn't) · ETPL, and why the program must be on it · step-by-step (MassHire career center → JobQuest → Training Information Meeting → ITA; Section 30 for people on unemployment benefits) · FAQ with FAQPage schema.
  - All caps, amounts and timelines are `[VERIFY]` with a mass.gov or dol.gov source.
- **`qualify.html`** (rework of the v1.4 wizard)
  - Title: "Do I Qualify for WIOA Training? Free Eligibility Check"
  - One question per screen:
    1. Do you live in Massachusetts?
    2. Your age: under 18 · 18–24 · 25+
    3. Work situation: unemployed · laid off or received a layoff notice · on unemployment benefits · part-time or low-wage · employed full-time · self-employed and business closed
    4. Does your household receive SNAP, TAFDC, SSI or other public assistance?
    5. Is your household income low? Show the income table from config, marked `[VERIFY]`.
    6. Are you a veteran or the spouse of a veteran?
    7. Are you legally allowed to work in the US?
    8. Which field interests you?
  - Result screen is never a yes/no verdict. It says which group you *may* fit (Adult / Dislocated Worker / Youth), lists any priority flags, and gives outward next steps (MassHire, JobQuest, ITA, Section 30). Include this line for men born on or after Jan 1, 1960: "WIOA requires Selective Service registration." `[VERIFY]`
  - Not in MA: "WIOA exists in every state, but this check covers Massachusetts. Find your local American Job Center." Link `[VERIFY]`.
  - **Change from v1.4:** show results first, then offer "Email me these steps" (optional: first name, email, mobile, language, consent). Posts to `submit.php` with `source=qualify`.
  - Logic lives in one JS function with test cases, like the calculator.

### 3. Express Program Explained
- **`express-program-explained.html`** — neutral reference page for SEO.
  - Sections: what the Workforce Training Fund is · who can apply · what's covered (live instruction only) · reimbursement rates and caps (from config, `[VERIFY]` with CommCorp) · how to apply · timeline · FAQ with FAQPage schema.
  - CTA → `staff-training-grants.html`.

### 4. For Employers
- **`employers.html`** — Overview: three cards (Staff Training Grants · Apprenticeships · Corporate Training) plus the employer inquiry form (`source=employer`).
- **`staff-training-grants.html`** — the service page.
  - Service line: "We help you apply for Express funding and handle the paperwork." Never "our course"; follow the `EXPRESS_PROVIDER_LISTED` flag.
  - Embeds the reimbursement calculator (brief §4.4 logic, config values). Form preset to `source=employer-express`.
- **`apprenticeships.html`**
  - Sections: what a Registered Apprenticeship is · how it works (sponsor, on-the-job learning, related instruction, wage progression) · employer benefits (retention, trained pipeline, grants and tax credits available in MA, each sourced from apprenticeship.gov or mass.gov, otherwise `[VERIFY]`) · the future graduate-pipeline line (`COURSE-DEPENDENT`) · form (`source=employer-apprenticeship`).
- **`corporate-training.html`**
  - Audience: any company that wants to train its staff, with or without state funding.
  - Copy: "We're building training for employers. Tell us what your team needs." `COURSE-DEPENDENT`
  - Form fields: company, team size, training topic, timeline. Posts with `source=corporate`.
  - No location wording. No prices, formats or course names.

### 5. Career Paths (location-neutral, no pay)
- Rename the v1.4 guides and drop "Massachusetts" everywhere:

| Old URL | New URL |
|---|---|
| `healthcare-careers-massachusetts.html` | `healthcare-careers.html` |
| `it-careers-massachusetts.html` | `it-careers.html` |
| `skilled-trades-careers-massachusetts.html` | `skilled-trades-careers.html` |

  301 any old URL that was deployed, and re-point the v1.4 program-page 301s to the new URLs.
- Keep the role lists and content. For each role show: what the job is · typical training path · certifications (national bodies) · "Can you train online?"
- Licensing varies by state: give a general note, and add MA specifics only as a clearly labeled example.
- Pay: hidden slot `<!-- PAY-DATA: pending -->`, register row R-PAY-DATA.

### 6. Blog: three clusters
| Cluster | Supports | Posts |
|---|---|---|
| Funding | WIOA + Express pages | #1–4 (keep). Backlog: "Express Program: How MA Employers Get Training Reimbursed" |
| Employers | Employer pages | Backlog: "What Is a Registered Apprenticeship?", "Apprenticeship Benefits for Employers", "How to Build an Employee Upskilling Program" |
| Careers | Career Paths | #6–8 (remove MA framing). Backlog: role-by-role "How to Become a …" posts |

- Post #5 ("Highest-Paying Certifications…") is **on hold** until the pay-data work is done.
- CTAs point to the page each cluster supports, never to "our program."

### 7. Supporting pages
- a. **`faq.html`:** funding, employers, and "when will CSC launch training?"
- b. **`privacy-policy.html` + `terms.html`** (NEW): cover form data, SMS consent and GA4. Draft them, marked for Emilio's review; he may want a legal check.
- c. **`contact.html`:** add a "Reason for contacting" dropdown (General question · Employer training · Partnership · Media). The dropdown value posts as a field. Remove any campus text.

## On hold (build nothing, keep files)
`workplace-esol*.html`, `clinic-billing-training.html`, `outcomes.html`.

## Register updates (`docs/COURSE_CONTENT_REGISTER.md`)
- Add these rows:
  - R-CORP (corporate-training copy)
  - R-APPR (graduate-pipeline line)
  - R-PAY-DATA (career pay slots)
  - R-WIOA (any CSC mention on wioa-explained)
- Update the URLs in R-HC / R-IT / R-TR and R-NAV.

## Acceptance
- Nav and footer match this spec on every page (desktop + mobile).
- `grep -rni 'massachusetts'` on the career-path pages returns only labeled MA examples.
- No pay figures on career pages.
- No "out of state" anywhere.
- Every form posts a distinct `source`.
- `qualify.html` and calculator tests pass.
- v1.4 acceptance checks still pass.
- Update `docs/BUILD_STATUS.md`.
