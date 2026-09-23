# Career Skills Center — Project Handoff & Deployment Guide

**Purpose of this document:** hand this project to a fresh chat/session whose job is to **put the website online**. It captures what the site is, how it's built, what's done, what's still open, and exactly how to deploy it.

---

## 1. Quick facts

| Item | Value |
|---|---|
| **Business name** | Career Skills Center (formerly "Career Skills Solutions" — fully renamed) |
| **Domain (owned)** | `careerskillscenter.com` |
| **Hosting** | Namecheap (shared hosting / cPanel) |
| **Email** | info@careerskillscenter.com |
| **Phone** | (617) 315-4323 |
| **Location** | Quincy, MA 02169 (marketing copy says "Massachusetts"; physical address stays "Quincy") |
| **Project folder** | `/Users/desttes/Documents/ETPL/Website` |
| **Type** | Static site — plain HTML/CSS/JS, no framework, no build tooling beyond one Python script |
| **Git** | Initialized. One commit so far ("Snapshot before pre-launch reorg"); **recent work is uncommitted** — commit before/after deploy. |

---

## 2. Tech stack & how to build / preview

Plain static site. The **inner pages are generated** from the shared header/footer/dialog in `index.html` by a Python script — do **not** hand-edit the generated inner pages; edit the source and rebuild.

**Rebuild all inner pages** (run after editing `index.html`'s shared chrome, or `tools/build-pages.py`):
```bash
cd /Users/desttes/Documents/ETPL/Website
python3 tools/build-pages.py
```

**Preview locally:**
```bash
python3 -m http.server 8123
# then open http://localhost:8123
```
(There is also a `.claude/launch.json` config named `site` for the preview server on port 8123.)

**Editing rules:**
- Shared header, footer, and contact dialog live in `index.html` → edit there, then rebuild to propagate to all inner pages.
- Page-specific content lives in `tools/build-pages.py` (each page is a `PAGES.append(dict(...))` block).
- `css/style.css` and `js/main.js` are shared by every page. Design tokens (colors, fonts) are at the top of `style.css` under `:root`.
- Browsers cache aggressively — hard-refresh (`Cmd+Shift+R`) after changes.

---

## 3. Project structure

**Deploy these (the live site):**
```
*.html            17 pages (see list below)
css/style.css     shared styles + design tokens
js/main.js        shared behavior (nav, hero crossfade, contact dialog, etc.)
images/           all site images (.webp) + aapc-logo.svg, comptia-logo.webp
```

**Do NOT deploy (dev-only):**
```
tools/build-pages.py   page generator
docs/                  internal notes (PAGES.md, SITE-STRUCTURE.md)
PROJECT-HANDOFF.md     this file
README.md              dev readme
.claude/  .git/        tooling / version control
../_archive/           archived, unpublished pages (wioa.html, financial-aid.html) — outside web root
```

**The 17 live pages:**
`index.html` (landing) · `our-programs.html` (programs overview / card grid) · `programs.html` (detailed programs — kept but **unlinked** from nav) · `it-support-specialist.html` · `medical-billing-coding.html` · `admissions.html` · `tuition.html` · `student-financing.html` · `about.html` · `team.html` · `career-services.html` · `faq.html` · `media.html` · `blog.html` · `contact.html` · `privacy-policy.html` · `terms-of-use.html`

---

## 4. What's been done (summary)

- **Rebrand:** entire site renamed "Career Skills Solutions" → **Career Skills Center**; logo mark → **CSC**; canonical/OG URLs + email → **careerskillscenter.com** / info@careerskillscenter.com. Verified 0 stale references in shipped files.
- **Images:** converted to `.webp`; all references point to `images/`.
- **Geography:** marketing copy uses "Massachusetts" (Boston/Greater Boston/Quincy market references removed); physical mailing address stays "Quincy, MA 02169".
- **WIOA withheld until certified:** WIOA page and the superseded financial-aid page moved to `../_archive/` (outside web root), removed from nav, and all WIOA advertising scrubbed site-wide (compliance: don't advertise WIOA until approved as an ETPL provider).
- **Programs restructured:** new `our-programs.html` card grid is the "Programs" nav destination; old `programs.html` kept as a file but unlinked. Detail pages built NTI-style for **IT Support Specialist** (CompTIA Tech+) and **Medical Billing & Coding** (AAPC CPC/CPB). Skilled Trades has no detail page yet.
- **Design polish (to match the NTI reference look):** navy `#003B69` + yellow `#FAB814` brand, blue `#1163A2` accent lines/numbers, charcoal `#343434` text, gray eyebrows; section titles resized to ~28–36px; two-column sections top-aligned site-wide; footer given `#1371b7` with a subtle side-vignette gradient.
- **Tuition:** comparison table's CSS "average tuition and fees" set to **$299 to $329** (IT $299 / Medical $329). Other comparison figures are still placeholders.
- **Certification disclosure:** Medical page Course Overview states students earn a Career Skills Center certificate (included) and can optionally add the paid AAPC certification.

---

## 5. DEPLOYMENT — putting it online (the main goal)

The site is a static bundle. Simplest path is **Namecheap cPanel File Manager**.

### Step-by-step (cPanel)
1. Log into **namecheap.com** → hosting → **cPanel**.
2. Open **File Manager** → go into **`public_html`**. Delete any default placeholder `index.html`/`default.html`.
3. Create a fresh deploy bundle from the project (excludes dev files):
   ```bash
   cd /Users/desttes/Documents/ETPL/Website
   find . -name .DS_Store -delete
   rm -f /tmp/careerskillscenter-site.zip
   zip -rq /tmp/careerskillscenter-site.zip *.html css js images -x "*.DS_Store"
   ```
4. In File Manager, **Upload** `careerskillscenter-site.zip` into `public_html`, then **right-click → Extract**.
5. Confirm the pages sit at `public_html/index.html` (not in a subfolder). Delete the zip.
6. Enable **AutoSSL / Let's Encrypt** in cPanel for HTTPS.
7. Visit **https://careerskillscenter.com** to verify.

### Domain pointing
If domain + hosting are both at Namecheap they're usually linked. If it doesn't resolve, confirm `careerskillscenter.com` is the primary domain pointing at `public_html`, and that the domain's nameservers point to the Namecheap hosting.

### Important: the assistant cannot log into Namecheap
There is **no Namecheap credential or connector available** to the assistant, and entering hosting passwords is not permitted. So the assistant **cannot upload the files directly** — it prepares the bundle and the human uploads it (steps above), unless a credential-free method (e.g., git-based deploy) is set up.

---

## 6. Outstanding before launch (TODO / known placeholders)

**Content to finalize (search for `class="tbd"`, `[Street Address]`, `Placeholder`):**
- **Street address** — footer + contact page show `[Street Address] [Suite] Quincy, MA 02169`. Add the real street/suite.
- **Skilled Trades tuition** — still `TBD` in the tuition catalog (only IT $299 and Medical $329 are confirmed).
- **Tuition comparison table** ("A Great Return on Your Investment") — CSS tuition is set ($299–$329), but the other CSS figures (education cost + lost income, median compensation, completion time, time to recover) are still NTI placeholder numbers. Confirm/replace and remove the "Placeholder comparison" note.
- **Program start dates**, some FAQ answers, VA benefits status — marked `TBD`.
- **Team page / Media page** — placeholder names/entries.
- **Blog** — placeholder article cards (link to `#`).
- **Program detail pages** — Skilled Trades and the individual trades have **no dedicated detail page** (only IT and Medical do). Nav "Skilled Trades" and its card link to the Our Programs overview.

**Functional:**
- **Contact form** — currently a demo; it shows a "thanks" message but does **not** send email. Needs a form backend (e.g., Formspree, a mailto fallback, or a cPanel PHP mailer) before real leads matter.
- **Logo** — header uses a text "CSC" mark. A real logo image was tested but rejected (files had spelling errors and were low-quality JPGs). When a correct **transparent PNG/SVG** of "Career Skills Center" is provided, wire it into the header + footer (replace the `.brand-mark`/`.brand-text` spans).
- **`images/logo.svg`** — referenced only inside an HTML comment (not a live broken image), so nothing is broken; ignore unless adding a real logo.

**Verify before promoting:** all program/tuition/credential facts are accurate for Career Skills Center (much of the copy was drafted from reference sites and marked TBD where unconfirmed).

---

## 7. First actions for the new (deployment) chat

1. Confirm working dir `/Users/desttes/Documents/ETPL/Website` and run `python3 tools/build-pages.py` to ensure pages are current.
2. Preview at `http://localhost:8123` and sanity-check.
3. (Recommended) `git add -A && git commit -m "Pre-deploy: rebrand + program pages"` to lock a restore point.
4. Build the deploy zip (section 5, step 3) and guide the user through the Namecheap cPanel upload.
5. After it's live, verify HTTPS and that all internal links work on the real domain.
