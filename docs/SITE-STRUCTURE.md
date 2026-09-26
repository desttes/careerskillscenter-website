# Career Skills Center — Site Structure & Design System

> **⚠️ Predates guide mode (Sept 26, 2026).** The page list, nav, file layout and
> company facts (phone, ZIP, service-area wording) below are OUTDATED. For the
> current site, read `docs/GUIDE_MODE_SPEC.md` and `docs/BUILD_STATUS.md`. Use
> this file only for the **design tokens and global components** (§3–§4), which
> are still accurate.

This document is the single source of truth for building every page of
careerskillscenter.com. Anyone (or any AI assistant) should be able to
build a new page from this file plus `PAGES.md` without seeing the reference
site again.

Reference design: https://nationaltradeinstitute.com/ (layout and visual
language only; all copy, branding, and images are ours).

---

## 1. Company facts

| Item | Value |
|---|---|
| Company name | Career Skills Center |
| Short form / logo mark | CSS (text mark until a logo file is supplied) |
| Location | Quincy, MA 02169 (street address and suite **still needed**) |
| Service area wording | "Quincy, the South Shore, and Greater Boston" |
| Phone | (617) 315-4323 — `tel:+16173154323` |
| Email | info@careerskillscenter.com |
| Domain | https://careerskillscenter.com |
| Office hours (placeholder) | Monday–Friday, 9:00am–5:00pm |
| Program areas | Skilled Trades · Information Technology · Medical |
| Tagline (footer) | "Our goal isn't just to help you achieve your potential. *It's to activate your potential.*" |
| Hero headline | kicker "Your Future" + H1 "Starts Here." (yellow period) |

---

## 2. File layout

```
/                       ← project root (currently /Users/desttes/Documents/Images)
├── index.html          ← landing page
├── programs.html       ← Programs (#trades, #it, #medical)
├── admissions.html     ← Admissions
├── tuition.html        ← Tuition
├── wioa.html           ← WIOA workforce grants (nav item "WIOA")
├── financial-aid.html  ← superseded by wioa.html; unlinked, safe to delete
├── student-financing.html
├── about.html          ← About Us
├── team.html           ← Meet the Team
├── career-services.html
├── faq.html
├── media.html
├── blog.html           ← Blog index (image-free; replaced Student Portal in nav)
├── contact.html
├── privacy-policy.html
├── terms-of-use.html
├── tools/build-pages.py ← regenerates every inner page from index.html's shared
│                          header/footer/dialog. Run after editing either.
├── css/style.css       ← global stylesheet, all tokens + components
├── js/main.js          ← header, mobile nav, hero crossfade, contact forms
├── images/             ← site images (copies of the originals in the root)
│   ├── Hero.png        ← hero slide 1 (mechanic / trades)
│   ├── hero2.png       ← hero slide 2 (laptop / IT)
│   ├── Todaybanner.png ← faint banner behind "Today's In-Demand Careers"
│   ├── Todaybanner2.png← reserved: hover-reveal photo for the Skilled Trades card
│   ├── hero3.jpeg      ← Step by Step section background (adult learners in class)
│   ├── aboutus.png     ← About Us / Mission section photo
│   ├── person1.png     ← testimonial 1 photo
│   └── person2.png     ← testimonial 2 photo
├── docs/
│   ├── SITE-STRUCTURE.md   ← this file
│   └── PAGES.md            ← spec for every inner page
└── (future pages)      ← programs.html, admissions.html, ... see PAGES.md
```

Inner pages live flat at the root (`programs.html`, `about.html`, etc.) so
relative links in the header/footer work unchanged. If the site is moved to
a CMS or a static-site generator, keep the same slugs.

---

## 3. Design tokens (from `css/style.css`)

### Colors

| Token | Hex | Used for |
|---|---|---|
| `--navy` | `#003B69` | primary brand, program cards, CTA band, header when scrolled, testimonial quote panels |
| `--navy-dark` | `#002D5E` | footer link row, footer bottom bar, step numbers, dialog info column |
| `--navy-deep` | `#043A6D` | gradients |
| `--yellow` | `#FAB814` | CTA buttons, accents, icons, hero period |
| `--yellow-dark` | `#E0A50F` | button hover, "Learn more." links |
| `--ink` | `#343434` | headings, body text |
| `--ink-light` | `#4E4E4E` | paragraphs inside sections |
| `--muted` | `#8A8A8A` | small labels ("STEP") |
| `--surface-alt` | `#F7F7F7` | Programs section background |
| `--surface-gray` | `#F1F1F1` | Steps section background |

### Typography

| Role | Font | Size / weight |
|---|---|---|
| Hero H1, page-hero H1, step numbers, logo mark | Poppins 800 | H1 clamp(48px → 94px), uppercase |
| Hero kicker | Poppins 700 | clamp(20px → 30px), uppercase, letter-spacing .18em |
| Section H2 (`.section-title`) | Roboto 700 | clamp(34px → 60px) |
| Eyebrow (`.eyebrow`) | Roboto 700 | 14px, uppercase, letter-spacing .12em, short navy line to the left |
| Body | Roboto 400 | 16px / 1.75 |
| Buttons | Roboto 700 | 14px, uppercase, letter-spacing .06em |
| Nav links | Roboto 500 | 13px, uppercase, letter-spacing .08em |

Google Fonts import (in every page `<head>`):
`Poppins:wght@700;800` and `Roboto:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400`.

### Spacing & layout

- Container: `max-width 1180px`, side gutter `clamp(16px, 4vw, 40px)`.
- Section vertical padding: `clamp(64px, 9vw, 120px)` via `.section`.
- Header height: `88px` (fixed, transparent on top, navy after 40px scroll).
- Breakpoints used: `1024px` (mobile nav), `900px`, `800px`, `760px`, `720px`, `640px`, `560px`.

---

## 4. Global components

### Header (`.site-header`)
- Fixed, transparent over hero, `.is-scrolled` → navy background (toggled in `main.js`).
- Left: text logo (`.brand`) — **placeholder until a logo file exists**.
- Right: nav — Programs ▾, Admissions ▾, About Us ▾, Blog, Contact, **Get in Touch** (yellow pill, opens dialog).
- Dropdown contents:
  - Programs → Skilled Trades, Information Technology, Medical
  - Admissions → Tuition, WIOA, Student Financing
  - About Us → About Career Skills Center, Meet the Team, Career Services, FAQ, Media
- ≤1024px: hamburger, full-width navy panel, dropdowns become accordions.

### Buttons
- `.btn.btn-yellow` — primary CTA (yellow bg, navy text).
- `.btn.btn-navy` — secondary (navy bg, white text).
- `.btn-sm` — pill variant used in the header. `.btn-block` — full width.

### Section header pattern
```html
<p class="eyebrow"><span class="eyebrow-line" aria-hidden="true"></span>Eyebrow text</p>
<h2 class="section-title left">Section Title</h2>
```

### Page hero for inner pages (`.page-hero`)
Navy block with slanted bottom edge, Poppins H1 with yellow period, one-line
intro. Optional background photo with the same navy overlay as the home hero.

### Get in Touch dialog (`#contact-dialog`)
Native `<dialog closedby="any">`, opened by any element with class
`.js-open-contact`. Left: form (name, phone, email, program select, message,
Submit). Right: Address, Office hours, Call us, Email. The markup lives in
`index.html`; copy it verbatim into every page (or extract it into a partial
if a templating step is added). **Form backend is not wired yet** — see the
TODO in `main.js`.

### Footer (`.site-footer`)
1. Link row (navy-dark): Programs · Tuition · Career Services · About Us · Contact · Catalog.
2. Main (navy gradient), four columns: brand + tagline · Address · Contact us · Follow Us (+ accreditation badge placeholder).
3. Bottom bar: © year · Career Skills Center · Privacy Policy · Terms of Use.

### Decorations
- `.deco-dots` — dotted triangle patterns in section corners (navy dots; yellow variant on the About photo).
- Slanted section edges use `clip-path: polygon(...)`.

---

## 5. Landing page (index.html) — section by section

| # | Section id | Layout | Images | Notes |
|---|---|---|---|---|
| 1 | `#hero` | Full-viewport, left-aligned text, navy overlay, slanted bottom | `Hero.png` → `hero2.png` crossfade every 7s | Buttons: Get in Touch (navy, opens dialog), Our Programs (yellow, anchors to `#programs`) |
| 2 | `#what-we-do` | Centered H2 + paragraph, then 3 feature columns | none | Columns: Easy Enrollment → admissions.html · Leading Careers → programs.html · Career Services → career-services.html |
| 3 | `#programs` | Eyebrow "Programs", H2 "Today's In-Demand Careers", 3 navy cards | `Todaybanner.png` faint banner behind cards | Cards: Skilled Trades · Information Technology · Medical, each with inline SVG icon. **Hover reveal effect intentionally not built yet** (see TODO comments in HTML and CSS; `data-hover-image` attributes pre-wired) |
| 4 | `#about` | Photo left (4:5), copy right, 5 arrow bullets in 2 columns | `aboutus.png` | H2 "Our Mission" |
| 5 | CTA band | Navy band, centered question + yellow button | none | Opens dialog |
| 6 | `#steps` | Eyebrow "Step by Step", H2 "Ready to Start?", 3 white step cards, full-width navy button | `hero3.jpeg` (adult learners in class) behind a light gradient wash | Swap the url() in `.steps::before` to change the photo |
| 7 | `#testimonials` | Two alternating photo + navy quote blocks | `person1.png`, `person2.png` | Names/quotes are **sample copy** |
| 8 | Footer | see §4 | none | Street address is a placeholder |

---

## 6. Open placeholders (to fill in before launch)

- [ ] Logo file (SVG preferred) → replace `.brand` text mark in header and footer.
- [ ] Street address + suite for Quincy, MA (footer and dialog).
- [x] Step by Step background — `images/hero3.jpeg` (adult learners in class).
- [ ] Hover-reveal photos for the IT and Medical program cards (Skilled Trades uses `Todaybanner2.png`).
- [ ] Real testimonials (names, programs, quotes).
- [ ] Medical program photo (`images/medical.png`) for the Programs page.
- [ ] Team headshots, names, titles and bios for the Meet the Team page.
- [ ] Campus photos and a map embed for the About and Contact pages.
- [ ] Tuition, fees and program lengths (every figure is currently TBD).
- [ ] WIOA / Eligible Training Provider approval status before advertising funding.
- [ ] Payment plan terms for Student Financing, and lending partner agreements.
- [ ] Verified placement and certification pass rates for Career Services.
- [ ] Legal review of the Privacy Policy and Terms of Use templates.
- [ ] Social profile URLs (Facebook, X, Instagram, LinkedIn).
- [ ] Accreditation / BBB badge image.
- [ ] Real blog articles (the six index cards + featured post are placeholder drafts).
- [ ] Course catalog PDF.
- [ ] Contact form backend (Formspree / Netlify / custom endpoint).
- [ ] Favicon (`favicon.ico` + `apple-touch-icon.png`).

---

## 7. Deferred work

- **Program card hover effect**: recreate the reference behaviour where hovering a card fades the navy panel and icon out, reveals a full-bleed photo (from `data-hover-image`), and slides the label to a bottom strip. Keep `:focus-visible` parity.
- Optional scroll-in animations (the reference fades sections in on scroll). Not needed for v1.
- Image optimisation: the PNGs are 1.5–2.3 MB each; export WebP/AVIF at 1600px and 800px widths and switch to `<picture>` / `srcset` before launch.
