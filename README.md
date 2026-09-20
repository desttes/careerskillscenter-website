# Career Skills Solutions — website

Static site for https://careerskillssolutions.com (Quincy, MA). Trade, IT, and
medical career training.

- `index.html` — landing page
- 14 inner pages: programs, admissions, tuition, wioa, student-financing, about, team, career-services, faq, media, contact, privacy-policy, terms-of-use, plus the superseded financial-aid page
- `css/style.css`, `js/main.js` — shared styles and behaviour
- `images/` — site images
- `tools/build-pages.py` — regenerates the inner pages from the shared header, footer and dialog in `index.html`
- `docs/SITE-STRUCTURE.md` — design tokens, global components, landing-page map, open placeholders
- `docs/PAGES.md` — what every inner page contains, plus the content that must be verified before launch

The header, footer and contact dialog are duplicated across all 14 pages. Edit
them once in `index.html`, then run:

```bash
python3 tools/build-pages.py
```

Open `index.html` directly in a browser, or serve the folder with any static
server (for example `python3 -m http.server 8080`).
