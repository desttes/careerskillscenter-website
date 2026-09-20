# Career Skills Solutions — Inner Page Specifications

**Status: all pages below are built.** This file is now both the spec and the
record of what each page contains. Update it when a page changes.

Every page shares the global header, footer, Get in Touch dialog, fonts, and
`css/style.css` from `index.html`. Section patterns (eyebrow + H2, feature grid,
step cards, CTA band, arrow lists, FAQ accordion, data table, team cards) already
exist in the stylesheet; reuse those classes before adding new ones.

Every page starts with a `.page-hero` (navy, slanted bottom, Poppins H1 with a
yellow period, short intro, and two buttons) unless noted.

## Editing the shared header, footer or dialog

The header, footer and contact dialog are duplicated into all 14 HTML files, as
they must be for a static site with no build step. **Do not hand-edit them in 14
places.** Edit them once in `index.html`, then regenerate the inner pages:

```bash
python3 tools/build-pages.py
```

That script reads `index.html`, lifts the `<header>`, `<footer>` and `<dialog>`
out of it, and rewrites every inner page with the page body defined inside the
script. Page content lives in the script's `PAGES` list, so edit the copy there
rather than in the generated `.html` file, or your change will be overwritten on
the next run. `index.html` itself is never touched by the script.

Sitemap (all built):

```
/                         index.html            Home
/programs.html            Programs overview
  #trades                 Skilled Trades (anchor section; can become its own page later)
  #it                     Information Technology
  #medical                Medical
/admissions.html          Admissions overview
/tuition.html             Tuition
/wioa.html                WIOA (nav item is called "WIOA")
/student-financing.html   Student Financing
/financial-aid.html       ORPHAN — superseded by wioa.html, no inbound links
/about.html               About Career Skills Solutions
/team.html                Meet the Team
/career-services.html     Career Services
/faq.html                 FAQ
/media.html               Media / News
/blog.html                Blog (top-level nav item; replaced "Student Portal")
/contact.html             Contact
/privacy-policy.html      Privacy Policy
/terms-of-use.html        Terms of Use
(future)                  Blog articles — one page per post, see article template below
(file)                    Catalog PDF — TBD
```

The header top-level items are now: Programs ▾, Admissions ▾, About Us ▾,
**Blog**, Contact, Get in Touch. "Student Portal" was removed; add it back as its
own item if an LMS URL is ever needed.

## Content that must be verified before launch

These pages deliberately carry `TBD` markers and `.note` warnings rather than
invented values, because publishing them wrong creates regulatory exposure, not
just a bad page:

- **Tuition, fees and program lengths** (`tuition.html`, `programs.html`) — advertised pricing is a regulated disclosure.
- **WIOA / Eligible Training Provider approval** (`financial-aid.html`) — do not advertise workforce funding until the approval is in writing.
- **Payment plan terms and any finance charges** (`student-financing.html`) — consumer lending disclosures are regulated.
- **Placement and certification pass rates** (`career-services.html`) — publish verified figures only, with a documented methodology.
- **Accreditation and state approvals** (`about.html`) — never claim these before they are granted.
- **VA benefits acceptance** (`faq.html`, `financial-aid.html`) — requires approval first.
- **Program catalog and credentials** (`programs.html`) — confirm the final course list and licensing.

---

## programs.html — Programs

**Purpose:** overview of the three program areas with a section per area.
Linked from: header Programs, hero "Our Programs" button, "Leading Careers" feature, program cards, footer.

**Page hero:** H1 "Our Programs." Intro: "Career-focused training in the skilled trades, information technology, and the medical field, designed for the jobs employers in Greater Boston are hiring for now."

**Sections (in order):**
1. **Program area jump cards** — reuse `.program-grid` / `.program-card` with anchors to `#trades`, `#it`, `#medical`.
2. **`#trades` Skilled Trades** — eyebrow "Skilled Trades", H2 "Build a Hands-On Career". Two-column layout (photo left, copy right, same as home About section). Then a grid of program cards (`.feature` style) for individual programs. Candidate programs: Electrical, HVAC/R, Plumbing, Welding, Carpentry/Construction. Each card: title, 1-line description, length (weeks), credential earned, "Read more".
3. **`#it` Information Technology** — eyebrow "Information Technology", H2 "Launch Your Tech Career". Same layout. Candidate programs: IT Support (CompTIA A+), Networking (Network+), Cybersecurity (Security+), Cloud Fundamentals.
4. **`#medical` Medical** — eyebrow "Medical", H2 "Care for Your Community". Same layout. Candidate programs: Medical Assistant, Phlebotomy Technician, EKG Technician, Certified Nursing Assistant (CNA), Medical Billing & Coding.
5. **How programs work** — three columns (`.feature-grid`): Hands-on labs · Industry certifications · Job placement support.
6. **CTA band** — "Not sure which program is right for you?" + "Talk to an Advisor" (opens dialog).

**Data needed:** final program list, lengths, tuition, credential names, schedule (day/evening), start dates.

---

## admissions.html — Admissions

**Purpose:** explain the enrollment process end to end.
Linked from: header Admissions, "Easy Enrollment" feature.

**Page hero:** H1 "Admissions." Intro: "Getting started is simple. Call, get qualified, enroll."

**Sections:**
1. **Step by Step** — reuse home `.steps` section (three cards) verbatim; keep the placeholder background until `steps-bg.png` exists.
2. **Admission requirements** — `.arrow-list`: 18+ (or 17 with consent), high school diploma or GED, valid ID, entrance interview, program-specific prerequisites (e.g., immunizations for Medical).
3. **What to bring / documents** — short checklist.
4. **Funding overview** — three feature cards linking to tuition.html, financial-aid.html, student-financing.html.
5. **Start dates** — simple table (placeholder until known).
6. **CTA band** — "Ready to apply?" + "Get in Touch".

---

## tuition.html — Tuition

**Purpose:** transparent pricing per program.

**Page hero:** H1 "Tuition." Intro: "Clear, upfront pricing with no surprises."

**Sections:**
1. **Tuition table** — one row per program: Program · Length · Tuition · Books/Supplies · Exam fees · Total. Group rows under Skilled Trades / IT / Medical subheadings. (Data TBD; render with placeholder values marked "TBD".)
2. **What's included** — arrow list (instruction, lab materials, certification exam voucher, career services).
3. **Ways to pay** — three feature cards → Financial Aid, Student Financing, Employer sponsorship.
4. **CTA band**.

---

## wioa.html — WIOA

**Purpose:** the workforce-grant page. This is the nav item under Admissions,
labelled "WIOA". Its section order and layout follow the reference site's WIOA
page; the copy is written for Career Skills Solutions and Massachusetts, since
the reference is a Texas school working through the Texas Workforce Commission
while we work through MassHire.

**Page hero:** label "WIOA Program", H1 "Free Career Training." No background
image yet — the hero is solid navy until a photo is chosen.

**Sections, in order:**
1. **WIOA Program Grants / Career Training at No Cost to You** — what the act is, who created it, and that MassHire administers it locally. Carries the ETPL verification note.
2. **WIOA Funding / The Basics** — image placeholder left, four-item accordion right: who funds it, how to check eligibility, how much is available, how long until training starts.
3. **Career Skills Solutions WIOA Programs / Get Started on Your Journey** — image placeholder, copy about short credential programs, "Explore Programs" button.
4. **WIOA Eligibility / You May Be Eligible If…** — seven-item `.check-list` (age, work authorization, diploma or GED, benefits eligibility, dislocated worker, terminated or laid off, self-employed but not working), plus a note that the career center makes the final call.
5. **Find Your Fit / Talk With an Enrollment Advisor** — image placeholder, phone number, "Talk to an Advisor" button.
6. **WIOA Approved Programs / Career Opportunities for a Better Future** — stackable-credentials argument plus the three program-area cards.
7. **Approved to Accept WIOA Funding** — ETPL listing status, currently TBD.
8. **CTA band** — "Ready to find out if you qualify?"

**Images:** three `.img-placeholder` blocks and the hero are intentionally empty,
to be filled later.

**Must be verified before publishing:** the ETPL listing. The headline says
"Free Career Training," which cannot be advertised until the school is an
approved Eligible Training Provider.

---

## financial-aid.html — superseded

Replaced by `wioa.html`. The file is still generated so it stays consistent with
the shared header, but **nothing links to it**. Delete it, or repurpose it for
non-WIOA funding such as veterans benefits and scholarships, which it already
covers in its "Additional Funding Sources" section.

**Original purpose:** grants and workforce funding options.

**Page hero:** H1 "Financial Aid." Intro: "You may qualify for funding that covers some or all of your training."

**Sections:**
1. **WIOA / MassHire** — explain Workforce Innovation and Opportunity Act funding through MassHire career centers (Quincy Career Center is the nearest). Eligibility bullets. **Confirm approved-provider status before publishing.**
2. **Other programs** — Veterans benefits, employer tuition reimbursement, scholarships (placeholders).
3. **How to apply** — 3 numbered steps (`.step-list`).
4. **FAQ excerpt** — 3–4 questions with links to faq.html.
5. **CTA band** — "Find out if you qualify".

---

## student-financing.html — Student Financing

**Purpose:** in-house payment plans and third-party lenders.

**Page hero:** H1 "Student Financing."

**Sections:**
1. **Payment plans** — monthly installment option description, no-interest terms if any (TBD).
2. **Third-party lenders** — logos/links placeholder.
3. **Estimate your payment** — simple calculator widget (optional later phase).
4. **CTA band**.

---

## about.html — About Career Skills Solutions

**Purpose:** story, mission, values, facility.
Linked from: header About Us, "Learn more." in What We Do, footer.

**Page hero:** H1 "About Us." Intro: "A career school built for Quincy and the South Shore."

**Sections:**
1. **Our Mission** — reuse home `.about` section verbatim (aboutus.png + arrow list).
2. **Our Story** — two paragraphs (founding, why trades/IT/medical, community focus). Copy TBD.
3. **Our Values** — 4 feature cards: Hands-on learning · Student support · Industry relevance · Community.
4. **Our Campus** — photo gallery placeholder (3–6 images) with address and directions to Quincy, MA; embed map placeholder.
5. **Accreditation & approvals** — badge placeholders + text.
6. **CTA band**.

---

## team.html — Meet the Team

**Page hero:** H1 "Meet the Team."

**Sections:**
1. **Leadership** — grid of cards: photo (placeholder), name, title, 2-line bio.
2. **Instructors** — same grid, grouped by Trades / IT / Medical.
3. **Join our team** — short paragraph + "Email us" link to info@careerskillssolutions.com.

**Data needed:** names, titles, bios, headshots.

---

## career-services.html — Career Services

**Purpose:** what happens after graduation.
Linked from: "Career Services" feature, header About Us dropdown, footer.

**Page hero:** H1 "Career Services." Intro: "Get certified. Begin your career."

**Sections:**
1. **What we offer** — feature grid: Resume & interview prep · Employer connections · Certification exam prep · Job search support · Alumni network.
2. **Employer partners** — logo strip placeholder.
3. **Outcomes** — stats tiles placeholder (placement rate, certification pass rate) — only publish verified numbers.
4. **Testimonials** — reuse home `.testimonial` blocks.
5. **For employers** — short paragraph + "Hire our graduates" (opens dialog).
6. **CTA band**.

---

## faq.html — FAQ

**Page hero:** H1 "FAQ."

**Sections:**
1. **Accordion** grouped by topic: Programs · Admissions · Tuition & Funding · Schedules · Career Services. Use native `<details>/<summary>` styled to match (add `.faq-item` styles to `style.css`).
2. **Still have questions?** — CTA band with phone and dialog button.

Seed questions: How long are programs? Are classes in person? Do you offer evening classes? Do I need experience? Is financial aid available? What certifications will I earn? Do you help with job placement? Where are you located?

---

## media.html — Media

**Page hero:** H1 "Media."

**Sections:**
1. **News & updates** — card grid (image, date, title, excerpt). Static for v1; can become a blog later.
2. **Photo gallery** — grid placeholder.
3. **Press kit** — logo downloads and boilerplate paragraph.

---

## blog.html — Blog (index)

**Purpose:** the blog landing page. Top-level nav item (replaced Student Portal).
**Image-free by design** — the whole blog uses type, borders, and colour accents
instead of photos, so it stays fast and easy to maintain.

**Page hero:** label "Blog", H1 "Career Insights." No background photo (solid
navy, like the legal pages). Buttons: Get in Touch + Our Programs.

**Sections:**
1. **Intro + filters** — eyebrow "Latest", H2 "From the Blog", one-line intro,
   then a `.blog-filters` row of `.filter-pill` category chips (All, Skilled
   Trades, Information Technology, Medical, Admissions & Funding, Career Advice).
   The pills are **visual only** right now; wire them to per-category pages or
   client-side filtering once the archive grows.
2. **Featured post** — one `.post-featured` navy panel (category tag, date,
   reading time, title, excerpt, "Read article"). Use it for the newest or most
   important piece.
3. **Post grid** — `.post-grid` of `.post-card` links. Each card: `.post-tag`
   (category), `.post-meta` (date · reading time), `<h3>` title, excerpt,
   `.read-link`. The whole card is one `<a>`.
4. **Load more** — `.blog-more` with a disabled button; becomes pagination or a
   real "load more" when there are enough posts.
5. **CTA band** — "Have a topic you want us to cover?"

**Current content is placeholder.** Six draft cards plus a featured WIOA piece,
there to show the layout. Replace them with real articles one at a time. Article
links point to `#` until the article pages exist.

**Data source:** the `BLOG_POSTS` list and the featured block live in
`tools/build-pages.py` under the `blog.html` entry. Edit there, then rebuild.

---

## Blog article page (template — build per post)

Each article is its own page, e.g. `blog-wioa-free-training.html`. Keep the same
head/header/footer/dialog as every other page. **No inline images** unless we
decide otherwise later.

**Page hero:** the category as the eyebrow label, the article title as the H1
(no yellow dot needed on long titles, or keep it — designer's call), and a meta
line under it: date · reading time · author. Solid navy, no photo.

**Body:** one `.container.narrow` with a `.prose` block — the same long-form
style used by the legal pages. Supports `<h2>`/`<h3>`, paragraphs, `<ul>`,
`.quote-block` pull quotes, and `.note` callouts. Aim for a lead paragraph, 3–6
sections with subheads, and a short closing with a call to action.

**After the body (optional, all image-free):**
- A short author line or box (initials in a coloured circle instead of a photo).
- "Related articles" — 2–3 `.post-card`s reusing the blog grid.
- CTA band ("Ready to get started?").

**When building one:** add a `PAGES.append(...)` entry in `tools/build-pages.py`
with `nav="blog.html"` (so Blog stays highlighted), point the matching card/
featured link on `blog.html` at the new slug, and rebuild.

---

## contact.html — Contact

**Purpose:** full-page version of the Get in Touch dialog.
Linked from: header Contact, footer.

**Page hero:** H1 "Contact Us." Intro: "You're moments away from a new career and a brighter future."

**Sections:**
1. **Two-column** — left: contact form (same fields as dialog: name, phone, email, program, message). Right: Address (placeholder street, Quincy, MA 02169), Office hours, Phone (617) 315-4323, Email info@careerskillssolutions.com, social icons.
2. **Map** — embed placeholder (Google Maps iframe once address is final).
3. **Directions / parking / public transit** — Quincy Center MBTA Red Line mention (verify once address is known).

---

## privacy-policy.html and terms-of-use.html

Plain text pages: `.page-hero` with H1, then a single `.container.narrow` with
headings and paragraphs. Content to be supplied by the company / legal. Add
"Last updated" date at the top.

---

## Build checklist for any new page

1. Add an entry to the `PAGES` list in `tools/build-pages.py` with `slug`, `nav`
   (the header href to mark current, or `None`), `title`, `ogtitle`, `desc` and
   `main`.
2. Build `main` from the `hero(...)` helper plus the sections you need. The
   helpers `cta()`, `prog_item()`, `faq()`, `team_card()` and `media_card()`
   keep markup consistent.
3. Add the page to the header nav and/or footer in `index.html` so it is
   reachable, then run `python3 tools/build-pages.py`.
4. Keep every image in `images/`; if a needed image is missing, leave a labeled
   placeholder block and list it in `SITE-STRUCTURE.md` §6.
5. Check the page at 375px, 768px and 1280px widths, and confirm no console
   errors and no horizontal scroll.

## Reusable CSS components added for these pages

`.page-hero` / `.page-hero-bg` · `.btn-outline` · `.section--alt` ·
`.section--tight` · `.section-intro` · `.split-grid` (`.reverse`) ·
`.program-items` / `.program-item` / `.program-meta` · `.check-list` ·
`.faq` / `.faq-item` / `.faq-group-title` · `.table-wrap` / `.data-table` ·
`.team-grid` / `.team-card` · `.media-grid` / `.media-card` ·
`.stat-grid` / `.stat-tile` · `.logo-strip` / `.logo-slot` ·
`.gallery-grid` / `.gallery-slot` · `.img-placeholder` · `.map-placeholder` ·
`.contact-grid` / `.contact-panel` / `.contact-details` · `.quote-block` ·
`.prose` · `.note`
