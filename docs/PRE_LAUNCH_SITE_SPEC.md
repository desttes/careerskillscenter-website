# Pre-Launch Site Spec — "Programs in development" (Option A)

> **SUPERSEDED in part (Sept 26, 2026)** by `docs/GUIDE_MODE_SPEC.md` (v1.4). The global honesty rules and the acceptance greps below still apply. The page-by-page plan (program pages "in development," tuition/admissions kept, program-specific interest form) is replaced by the guide-mode plan.

**From:** strategy side (Cowork), Sept 25, 2026 · **Decision by Emilio:** Option A
**For:** Claude Code. Implement through `tools/build-pages.py` / `index.html` as usual. Don't deploy until Emilio approves, and run the pre-deploy check in `CLAUDE.md`.

## Why
Career Skills Center has no programs, students or graduates yet. The live site currently shows made-up prices ($299/$329), lengths (8/11 weeks, 89/117 hours), specific credentials, and **testimonials from "graduates" who don't exist.** Until real programs exist, the site's job is to (1) explain the careers honestly, (2) collect an **interest list**, and (3) rank in search through the blog.

## Global rules for this change
- No CSC program length, hours, schedule, price, credential/exam, certificate, start date, VA status, outcome stat, graduate, alumni or testimonial claims **anywhere**.
- Allowed: "Career Skills Center is developing online training in Information Technology and Medical Billing & Coding, and plans to add Skilled Trades."
- Industry facts are OK with a source (BLS median pay/outlook, what the job involves, what certifications exist in the field).
- Planned intent is OK if clearly labeled: "We plan to align the program with an industry-recognized certification. Details will be confirmed before enrollment opens."
- Standard status line (use on every program-related page): **"Program in development. Details, pricing and start dates will be announced before enrollment opens."**

## The interest-list form (the main CTA site-wide)
Replaces "Get in Touch" / "Enroll" CTAs on program pages; the contact dialog can reuse it.
Fields: first name · email · mobile (optional) · program of interest (IT / Medical Billing & Coding / Skilled Trades / Not sure; preselected per page) · preferred language (English / Español / Português) · **"How would you likely pay?"** (Self-pay / My employer / State or grant funding / Not sure). This doubles as market research. · SMS consent checkbox.
- Hidden fields: `source=interest-list`, `page=<slug>`.
- Success message: "You're on the list. We'll email you when [program] details are ready."
- GA4 event: `interest_list_signup` with `program` and `pay_method` parameters.
- **Dependency:** needs the cPanel PHP mailer (already chosen). Build the mailer first. If it isn't ready, the form must not pretend to submit; show "Email us at info@careerskillscenter.com" instead.

## Page-by-page

### 1. `it-support-specialist.html` and 2. `medical-billing-coding.html` → "Program in development" template
- **Title:** "IT Support Training in Massachusetts (Coming Soon) | Career Skills Center" / "Medical Billing & Coding Training in Massachusetts (Coming Soon) | Career Skills Center"
- **H1:** "IT Support Training, Coming Soon" / "Medical Billing & Coding Training, Coming Soon"
- **Sections:**
  1. Hero: status line + "Join the interest list" button.
  2. **About the career** (sourced): what the job does; U.S. median pay and outlook from BLS. Medical records specialists: $51,140/yr (2025), +8% 2025–2035, ~14,000 openings/yr. Computer user support specialists: $61,860/yr (2025), −3% 2025–2035 but ~48,700 openings/yr from turnover (say "steady demand," not "fast-growing"). Cite "U.S. Bureau of Labor Statistics." Replace with Massachusetts figures once the BLS state data is pulled (VERIFICATION_LOG §C).
  3. **What we're planning** (no specifics): "an online program for Massachusetts adults," general topics (IT: hardware, operating systems, networking basics, security basics, customer support. Medical: medical terminology, coding systems like ICD-10-CM and CPT, claims and billing, privacy/HIPAA), plus the "plan to align with an industry-recognized certification" line.
  4. **What we'll tell you before enrollment opens:** length and schedule · cost and payment options · which certification it prepares for · whether state or employer funding can be used.
  5. Interest-list form.
  6. Related blog posts (the "can it be learned online?" post + the funding guide).
- **Remove:** program length/hours stats, credential badges (AAPC/CompTIA logos, as they imply partnership), "Course Overview" details, "How to Enroll," salary figures without a source, "$21 to $25 per hour," "Median pay about $48,000."

### 3. `skilled-trades.html`
Already "Coming Soon." Align it to the same template. Careers: electrician, HVAC/R, plumbing, as general info only. Add the MA licensing reality (600 classroom + 8,000 work hours for journeyman electrician; refrigeration tech 6,000 apprentice hours or 450 hours of study + CFC; source 237 CMR 13 / OPSI). Interest-list form (program = Skilled Trades).

### 4. `our-programs.html`
- Each card gets an **"In development"** badge; the card text describes the career, not the program.
- Remove "Stack industry certifications from help-desk fundamentals through networking, security and cloud," "certification exam preparation built into every program," and "CompTIA certification training."
- Intro: "We're building online career training for Massachusetts adults. Join the interest list for the program you want."

### 5. `tuition.html`
- Replace the tuition table and the "Great Return on Your Investment" comparison (NTI placeholder numbers) with a **"Pricing coming soon"** section: "We'll publish full costs, including books and exam fees, before enrollment opens. No hidden fees." Add the interest-list CTA.
- Keep it in nav, or temporarily point the Tuition nav link to the same content inside Admissions. Code chooses the simpler option.

### 6. `programs.html` (unlinked, still on the server)
It contains old fake details (A+/Network+/Security+, CCMA, OSHA prep). **Stop deploying it** and delete it from the server at the next deploy (or 301-redirect to our-programs.html via `.htaccess`). Also check `team.html` and `media.html` for fake content and handle them the same way.

### 7. `index.html` (homepage)
- **Remove the Testimonials section entirely** ("Marcus, Electrical Technician graduate"; "David, IT Support Specialist graduate"). Don't replace it with any quotes. Optional replacement: a short **"Why we're building Career Skills Center"** section (mission, Massachusetts focus, honest online training) + the interest-list CTA.
- Remove "helped me earn my CompTIA A+ and Network+" and any other program specifics.
- Soften feature bullets to planned tense where they promise things that don't exist yet ("Knowledgeable instructors to support you" → "Instructors with real industry experience").
- Keep the For Employers entry point when those pages are built.

### 8. `faq.html`
Rewrite the program answers:
- "What certifications will I earn?" → "We plan to align each program with an industry-recognized certification. We'll confirm which one before enrollment opens."
- "How long are programs?" / "What does it cost?" → "Details will be announced before enrollment opens. Join the interest list to hear first."
- "Do you accept VA benefits?" → "Not at this time. We'll update this page if that changes." (Emilio: confirm this wording.)
- "Do you help with job placement?" → describe **planned** career support; remove "graduates come back years later," "included in your tuition."
- Keep general answers (online learning, who it's for, funding explainer links to the blog).

### 9. `career-services.html`
Remove the "Alumni Network," "Graduates use us again years later," "Our graduates arrive with current credentials," "Hire Our Graduates," and the TBD outcomes box. Reframe as **"Career support we're building into every program"** (resume help, interview practice, employer connections), all in future tense.

### 10. `admissions.html`, `student-financing.html`
- Admissions: "Enrollment isn't open yet. Here's how it will work, and how to get on the list." Keep general steps and drop dates.
- Student Financing ("Ways to Pay"): describe the options *we plan to offer* (payment plans, employer-paid, state funding once approved) with no terms, plus a link to the funding guide blog post. Keep the working-toward-approval disclosure.

### 11. `about.html`
Keep the mission. Make sure it doesn't claim a campus, instructors on staff, accreditation, or years in operation.

### 12. `llms.txt` and JSON-LD
- `llms.txt`: rewrite program lines to "in development," remove "CompTIA Tech+ (FC0-U71)," "CPC/CPB," "8 weeks," "11 weeks," and change "offering" to "developing."
- JSON-LD `EducationalOrganization`: fine. Don't add `Course` schema with prices or durations.

### 13. Brief correction
BUILD_BRIEF §3.3 said to reuse the Marcus and David testimonials on the Outcomes page. **Withdrawn.** Don't build `outcomes.html` until there are real graduates. Remove it from the nav plan.

## Acceptance check
Run these on the built site before asking Emilio to deploy:
```
grep -rn -E '\$299|\$329|89 hours|117 hours|8 weeks|11 weeks|FC0-U71|Tech\+ Training|CPC & CPB Training|graduate\b|Graduates|alumni|Alumni|Marcus|David,' --include='*.html' . | grep -v '/blog/' 
grep -n -E 'Tech\+|CPC|CPB|weeks' llms.txt
```
Both must return nothing, except industry mentions that are clearly general (e.g., in a "certifications in this field" sentence). Then list in BUILD_STATUS every page changed, for Emilio's review.
