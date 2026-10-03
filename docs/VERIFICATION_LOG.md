# Verification Log — blog drafts

**Checked by:** strategy side (Cowork), Sept 25, 2026
**For:** Claude Code (apply fixes) and Emilio (answer Bucket 1)
**Scope:** every inline `[VERIFY]` marker plus every claim in the `<!-- DRAFT – facts to verify -->` notes of the 8 posts in `/blog/`. I also found 4 issues on program pages while checking (section D).

**Verdicts:** ✅ Confirmed (keep; remove marker) · ✏️ Fix (replace with the given text) · 🔻 Soften (couldn't confirm from an official source; use the safer wording) · 👤 Emilio (business fact only he knows) · 🔧 Code (Code must fetch the data)

---

## A. Inline `[VERIFY]` markers

| # | Post | Marker / claim | Verdict | Use this | Source (checked 9/25/2026) |
|---|---|---|---|---|---|
| A1 | free-job-training-massachusetts | "about 29 [career centers] across the state [VERIFY count]" | ✏️ Fix | "more than 25 MassHire career centers across the state" | mass.gov/info-details/masshire-career-center-locations ("There are more than 25 locations across the state") |
| A2 | free-job-training-massachusetts | Donnelly "about $7.4 million (May 2026) and $5.9 million (August 2026) [VERIFY totals]" | ✏️ Fix, **date was wrong** (my content pack said May 2026) | "recent rounds awarded $7.4 million (October 2025) and $5.9 million (August 2026)" | mass.gov news, Oct 7, 2025 ($7.4M, 1,161 workers) · mass.gov news, Aug 5, 2026 ($5.9M, 951 workers) |
| A3 | free-job-training-massachusetts | "Search at mass.gov/masshire-career-centers [VERIFY URL]" | ✏️ Fix | Link to **https://www.mass.gov/info-details/masshire-career-center-locations** (list by region + map finder) | same page |
| A4 | free-job-training-massachusetts | "[VERIFY: CSC's VA benefit approval status before advertising.]" | 👤 Emilio | Until answered, use: "If you served, you may have education benefits. Ask the VA which schools are approved, and ask us about our current status." (matches faq.html) | faq.html says VA status is TBD |
| A5 | highest-paying-certifications-massachusetts | "[VERIFY: add current BLS OES MA median wages…]" (intro + 3 role markers) | 🔧 Code | See section C for exact instructions. National figures in C can be used if MA data can't be pulled, **labeled "U.S. median"** | BLS |
| A6 | can-you-learn-it-support-online | "[VERIFY: program length and exact credential level]" | ✅ from the site (Emilio to confirm the site is right) | "about 8 weeks (89 hours), preparing you for the CompTIA Tech+ (FC0-U71) exam" | it-support-specialist.html; tuition.html |
| A7 | can-medical-billing-coding-be-learned-online | "[VERIFY: program length and exam details]" | ✅ from the site (Emilio to confirm) | "about 11 weeks (117 hours), preparing you for the AAPC CPC and CPB exams" | medical-billing-coding.html; tuition.html |
| A8 | can-you-learn-a-trade-online | "[VERIFY: current Massachusetts licensing requirements for each trade]" | ✏️ Fix with confirmed examples | "For example, a Massachusetts journeyman electrician needs 600 hours of classroom instruction and 8,000 hours of supervised work over at least four years. A refrigeration technician needs either 6,000 hours as a licensed apprentice, or 450 hours of approved study, plus universal CFC (EPA 608) certification. Plumbing and gas fitting have their own rules set by the state board." | 237 CMR 13 (mass.gov); mass.gov "Apply for a Refrigeration Technician License" |
| A9 | free-job-training-massachusetts | "[…from Emilio]" checklist download placeholder | 👤 Emilio | Keep the placeholder until the checklist PDF exists | — |

## B. Claims in the DRAFT notes

| # | Post(s) | Claim | Verdict | Note / wording | Source |
|---|---|---|---|---|---|
| B1 | free-job-training | MDCS maintains the ETPL; only ETPL-listed programs can be paid with an ITA | ✅ | Keep | MassWorkforce issuance 100 DCS 14.106.2 (FY27 MA ETPL policy, 9/2/2026): an eligible provider must "be listed on the State ETPL" |
| B2 | free-job-training, is-wioa-training-free | Section 30/TOP: ≥20 classroom hrs/week, up to 26 extra weeks, apply by the 20th compensable week; doesn't pay tuition | ✅ | Keep | mass.gov/info-details/training-opportunities-program-section-30 |
| B3 | free-job-training, wioa-eligibility | MassHire Central 2026 thresholds $15,960–$60,124+ by family size; regional example only | ✅ | Keep the "example only" framing | masshirecentralcc.com training-assistance page |
| B4 | free-job-training | Donnelly funds go to partner organizations, not individuals | ✅ | Keep ("look for a program funded by one") | commcorp.org/program/senatordonnellygrants/ (grants to organizations, 2+ employer partners, cost-reimbursement) |
| B5 | wioa-eligibility | Priority of service: public assistance recipients, other low-income people, basic-skills-deficient; veterans get priority in all DOL programs | ✅ | Keep | dol.gov/agencies/eta/workforce-investment/adult |
| B6 | wioa-eligibility | Local career center makes the final eligibility decision | ✅ | Keep | DOL ("services… may vary from state to state"); MassHire center pages |
| B7 | wioa-eligibility, masshire-voucher | Basic requirements: 18+, live or worked in the service area, work authorization, Selective Service (men born after 1/1/1960) | ✅ | Keep; say "most centers" | masshirecentralcc.com |
| B8 | masshire-voucher | Steps: MyMassGov + JobQuest → Training Information Meeting (or required video) → TABE → counselor/career plan → documents → pick ETPL program → ITA/training proposal → approval; ~6–8 weeks | ✅ | Keep "steps vary by center" | masshirecentralcc.com; masshiremncareers.com; masshiredowntownboston.org |
| B9 | masshire-voucher | Training that starts before approval usually can't be paid | 🔻 Soften | "Don't start class until your career center approves your training in writing. Ask them first." | Not found in an official source |
| B10 | is-wioa-training-free | ITAs cover tuition and often books, fees and exams | 🔻 Soften | "An ITA pays for approved training. Some career centers also cover related costs like books or exam fees. Ask your counselor exactly what yours covers." | FY27 ETPL policy doesn't list covered items |
| B11 | is-wioa-training-free | Supportive services (transportation, childcare) may be available | 🔻 Soften | "Some career centers can help with other costs, like transportation or childcare, depending on local funding. Ask your counselor." | DOL says services vary locally |
| B12 | all funding posts | Don't state ITA dollar caps | ✅ | Keep; the FY27 policy sets no statewide cap figure | 100 DCS 14.106.2 |
| B13 | it-support, highest-paying | CompTIA Tech+ (FC0-U71) replaced ITF+ (retired mid-2025); it's entry level, below A+ | ✅ | Keep | CompTIA announcements via CBT Nuggets / training-provider summaries |
| B14 | it-support | Employers hire help desk on certs + skills more than degrees | 🔻 Soften | "Many employers hire for entry-level help desk roles based on skills and certifications, not only degrees." | General; no single official source |
| B15 | medical | AAPC CPC (coder) and CPB (biller) are real AAPC credentials; exams taken after training | ✅ | Keep. Exam cost: **$425 for 1 attempt / $499 for 2** (student $400 / $475) | aapc.com "How much does the CPC exam cost?" |
| B16 | medical | Exam can be taken online or at a test center | 🔻 Soften | "Check AAPC for current testing options (online or in person)." | Not confirmed (AAPC page didn't load) |
| B17 | trade | Online covers theory/code/safety; licensing needs supervised hours | ✅ | Keep; use A8 examples | 237 CMR 13; OPSI |
| B18 | trade | EPA 608 needed to handle refrigerant; OSHA 10/30 available online | ✅ | Keep (the MA refrigeration license also requires universal CFC certification) | mass.gov refrigeration technician page |
| B19 | all | mass.gov / commcorp.org / jobquest.mass.gov links resolve | ✅ | The mass.gov locator URL fix is in A3 | checked 9/25/2026 |

### Optional addition (Emilio decides)
**Workforce Pell (new):** Massachusetts started a Workforce Pell pilot on Sept 1, 2026 (Pell grants for 8–15-week, 150–599-hour programs). **Only accredited, federal-aid (Title IV) schools can offer it**, so CSC is not eligible. Mentioning it in the funding guide helps readers and builds trust, but it points some of them to community colleges. Source: 100 DCS 14.107 (9/1/2026).

## C. Salary data (post #5) — instructions for Code

I couldn't read BLS state tables with my tools. Code, running on Emilio's Mac, should:
1. Download **BLS OEWS May 2025 state data** (`https://www.bls.gov/oes/special-requests/oesm25st.zip`, or "State XLSX" at bls.gov/oes/tables.htm).
2. Filter to **AREA_TITLE = Massachusetts** and read **A_MEDIAN** for SOC codes 29-2072, 15-1232, 15-1231, 43-3021, 43-6013, 47-2111, 47-2152, 49-9021.
3. Write the numbers into post #5 as "Massachusetts median: $XX,XXX (BLS, May 2025)" and log them here.

**If the download fails, use these U.S. figures, labeled as national:**

| Job | U.S. median pay | Outlook | Source |
|---|---|---|---|
| Medical records specialists | **$51,140/yr** ($24.59/hr), 2025 | **+8%** 2025–2035, ~14,000 openings/yr | bls.gov/ooh (Medical Records Specialists) |
| Computer user support specialists | **$61,860/yr**, 2025 | **−3%** 2025–2035 (decline), ~48,700 openings/yr across computer support | bls.gov/ooh (Computer Support Specialists) |

⚠️ **IT outlook wording:** BLS projects computer support jobs to **decline 3%**, though there are still ~48,700 openings a year from turnover. Don't write "fast-growing" about IT help desk. Use "steady demand, with thousands of openings each year as people move up or retire."

## D. Issues on program pages (not blog), found while checking

| # | Page | Issue | Suggested fix | Who |
|---|---|---|---|---|
| D1 | medical-billing-coding.html | "Median pay is about $48,000 a year (roughly $23 an hour)" is outdated | "Median pay is about $51,000 a year (about $24.59 an hour) (BLS, 2025)" | Code |
| D2 | it-support-specialist.html | "$21 to $25 per hour" has no source; "in-demand field" conflicts with BLS −3% | Use BLS: "U.S. median about $61,860 a year (BLS, 2025)", or the MA figure from C; replace "in-demand" with "steady demand" | Code, Emilio approves |
| D3 | faq.html | Certification answer lists CompTIA A+/Network+/Security+ and CCMA/CPT/CET/CBCS, but the program pages say Tech+ and CPC/CPB | Rewrite to match: "IT: CompTIA Tech+. Medical Billing & Coding: AAPC CPC and CPB exam prep. Skilled Trades: coming soon." | Emilio confirms, Code edits |
| D4 | tuition.html | Table says **Exam fees: Free**, but the medical page says the AAPC exam is optional and paid, and AAPC charges $425+ | Emilio decides: is an exam voucher included in tuition? Then make the tuition, program and blog pages match | 👤 Emilio |

## E. For the Project (strategy note, not for the site)
The FY27 MA ETPL policy (100 DCS 14.106.2, 9/2/2026) says registered apprenticeships "follow the same protocols unless otherwise specified." That may weaken the "automatic ETPL eligibility via apprenticeship" shortcut in Project doc 11. Read Attachment A (initial eligibility) before relying on it.

---

## Bucket 1: what Emilio still needs to answer
1. **VA benefits:** is CSC approved to accept GI Bill benefits? (A4; post: free-job-training-massachusetts)
2. **Confirm program facts:** IT = 8 weeks / 89 hrs / CompTIA Tech+; Medical = 11 weeks / 117 hrs / AAPC CPC & CPB. (A6, A7)
3. **Exam fees:** included in tuition or not? (D4)
4. **Checklist PDF** content (A9)
5. Optional: mention Workforce Pell? (B, optional)

## Instructions for Code
- Apply every ✏️ and 🔻 row exactly. Remove each `[VERIFY]` marker once it's resolved.
- Keep 👤 items as-is until Emilio answers; they block publishing only those posts.
- Do section C. Record the numbers you insert in a new "Applied" section at the bottom of this file.
- Leave section D edits until Emilio approves (except D1, which is a sourced factual update).
- Commit, and update `docs/BUILD_STATUS.md`.

---

## F. UPDATE Sept 25, 2026: program facts are placeholders (supersedes A4, A6, A7, D3, D4 and Bucket 1 items 1–3)

Emilio confirmed that the program pages are **fillers**. Nothing about CSC's own programs (length, hours, price, credential, format, certificate, exam fees, VA status) is decided. **The blog must not state any CSC program detail.** The only allowed claim: *CSC plans to offer training in Information Technology and Medical Billing & Coding, and likely Skilled Trades. Details are coming.*

### F1. Sentences to change in the blog
| Post | Current text | Replace with |
|---|---|---|
| can-medical-billing-coding-be-learned-online | "At Career Skills Center, our Medical Billing & Coding program is delivered online, and students earn a Career Skills Center certificate. You can also choose to add the paid AAPC certification exam. [VERIFY…]" | "Career Skills Center is planning a Medical Billing & Coding program. Join our interest list to hear first when details are ready." |
| can-medical-billing-coding-be-learned-online | CTA "See what our online Medical Billing & Coding program covers, how long it takes, and how to pay for it." | "Interested in training for medical billing and coding? Join our interest list, and we'll let you know when our program opens." (CTA → contact dialog, program = Medical) |
| can-you-learn-it-support-online | "Our IT Support Specialist program is built around a recognized CompTIA credential and hands-on practice, delivered online. [VERIFY…]" | "Career Skills Center is planning an IT Support program. Join our interest list to hear first when details are ready." |
| can-you-learn-it-support-online | CTA "See how our online IT Support program works, what certification you train for, and how to pay for it." | "Interested in IT support training? Join our interest list, and we'll let you know when our program opens." (program = Information Technology) |
| can-you-learn-a-trade-online | "What we are building: Career Skills Center is developing skilled trades training." | OK as is. Make sure nothing after it gives trade names, lengths or dates. |
| free-job-training-massachusetts | "Veterans benefits… [VERIFY: CSC's VA benefit approval status before advertising.]" | "Veterans benefits. If you served, you may have education benefits (like the GI Bill). The VA's GI Bill Comparison Tool shows which schools are approved." Say nothing about CSC's VA status. |
| free-job-training-massachusetts, is-wioa-training-free | "Browse our programs to see what we offer." | "Career Skills Center is preparing programs in IT, Medical Billing & Coding and Skilled Trades. Join our interest list." |
| highest-paying-certifications-massachusetts | "Learn more: Medical Billing & Coding at Career Skills Center…" (and the IT and Trades equivalents); "Explore Our Programs" button | Link to the relevant **blog post** instead (e.g., "Can medical billing and coding be learned online?"). Button → "Join our interest list." |
| masshire-training-voucher | "Explore Our Programs" button | "Join our interest list" |
| all 8 posts, disclosure box | "…see your options to pay for training now…" | "…join our interest list, and we'll keep you posted as our programs and funding status develop." (Ways to Pay describes plans that aren't final either.) |

### F2. Publish dates
Several posts show backdated publish dates (Aug 14, Aug 21, Aug 28, Sept 18, Sept 22) although they were written Sept 24–25. Set **Published** to the real publish date when each post goes live, and remove "Updated" until there's a real update.

### F3. General-industry content is fine
Explaining CompTIA Tech+/A+, AAPC CPC/CPB, exam prices (AAPC $425/$499), BLS wages and MA license hours stays. That's industry information, not a CSC claim. Just don't write "our program prepares you for…"

### F4. Bucket 1 remaining (Emilio)
- ~~VA status~~ → not mentioned (F1)
- ~~IT/Medical program facts~~ → not mentioned (F1)
- ~~Exam fees included?~~ → not needed for the blog. Still matters for the program pages (see F5).
- Checklist PDF content (still open)
- Optional: mention Workforce Pell? (still open)

### F5. Program pages on the LIVE site (Emilio decides)
The live pages currently state specific prices ($299/$329), lengths (8/11 weeks), hours and credentials that are placeholders. Publishing concrete prices and credentials for programs that don't exist yet is a consumer-protection and credibility risk (and it contradicts itself, e.g., "Exam fees: Free" vs "paid AAPC exam"). Options:
- **(a) Recommended:** convert each program page to a "Program in development" page: what the career is, what the planned program will generally cover, "details coming soon," and a join-the-interest-list form. Hide the tuition table (or show "Pricing coming soon").
- **(b)** Keep the pages but add a visible banner: "Planned program. Length, price and credentials are not final and may change."
Code should not change these pages until Emilio picks (a) or (b).

---

## G. APPLIED by Code — Sept 25, 2026

### G1. BLS salary data (section C) — pulled successfully
Downloaded from the BLS OEWS Query System (data.bls.gov) rather than the zip (bls.gov blocks curl with 403; the old per-state HTML tables are retired and now redirect to the interactive tool). Read via the in-app browser at `data.bls.gov/oes/#/area/2500000/2025` (Massachusetts, May 2025), column "Annual median wage."

**Massachusetts median annual wages — BLS OEWS, May 2025:**

| SOC | Occupation | MA median |
|---|---|---|
| 29-2072 | Medical records specialists | **$60,350** |
| 43-3021 | Billing and posting clerks | **$56,110** |
| 43-6013 | Medical secretaries & administrative assistants | **$50,290** |
| 15-1232 | Computer user support specialists (IT help desk) | **$75,070** |
| 15-1231 | Computer network support specialists | **$88,650** |
| 47-2111 | Electricians | **$79,420** |
| 47-2152 | Plumbers, pipefitters & steamfitters | **$93,880** |
| 49-9021 | HVAC & refrigeration mechanics & installers | **$77,300** |

These MA figures are used in post #5 (cited "BLS OEWS, May 2025, Massachusetts"), so the national fallback in section C was not needed. Title changed from "(2027)" to "(2026)" to match the data year.

### G2. Fixes applied to the 8 blog posts
- **A1** ✏️ "about 29" → "more than 25 MassHire career centers."
- **A2** ✏️ Donnelly dates corrected → "$7.4 million (October 2025) and $5.9 million (August 2026)."
- **A3** ✏️ locator link → mass.gov/info-details/masshire-career-center-locations.
- **A8** ✏️ trade-licensing examples inserted (electrician 600 classroom + 8,000 work hrs; refrigeration 6,000 apprentice hrs or 450 study hrs + CFC/EPA 608).
- **B9, B10, B11, B14, B16** 🔻 softened to the given wording.
- **B15** exam cost ($425 / $499) added as general industry info.
- **F1** all CSC-program specifics removed from the blog and replaced with the "planning / join the interest list" wording; program-page CTAs re-pointed to the interest-list (interim: contact page, until the mailer + form exist).
- **F2** publish dates de-backdated (all set to the real drafting date) and the "Updated" line removed from article meta until a real update exists.
- **A4/VA** now: "you may have education benefits (like the GI Bill). The VA's GI Bill Comparison Tool shows which schools are approved." No CSC VA claim.
- Every inline `[VERIFY]` marker resolved and removed **except** the checklist-download `[TODO]` (A9, still pending Emilio's PDF). DRAFT notes kept (posts remain drafts).

### G3. Still blocked on Emilio (Bucket 1 / F4)
- Checklist PDF content (A9) — pillar keeps a placeholder.
- Optional: mention Workforce Pell? (left out for now.)
- Program-page rework (F5) and the pre-launch site spec (Option A) — not started; separate task.

---

## H. APPLIED by Code — Sept 26, 2026 (guide mode, GUIDE_MODE_SPEC v1.4 steps 3–5)

### H1. BLS OEWS May 2025 Massachusetts median annual wages (for the 3 career-field guides)
Pulled from the BLS OEWS Query System via the in-app browser (bls.gov still 403s curl; the `oesm25st.zip` download 403s too). Source for every figure: **BLS OEWS, May 2025, Massachusetts** — `data.bls.gov/oes/#/area/2500000/2025`, "Annual median wage" column. Checked 9/26/2026.

**Healthcare**
| SOC | Occupation (BLS) | MA median | Used on guide as |
|---|---|---|---|
| 29-2072 | Medical Records Specialists | $60,350 | Medical billing & coding |
| 31-9092 | Medical Assistants | $49,460 | Medical assistant |
| 31-9097 | Phlebotomists | $50,170 | Phlebotomy technician |
| 29-2052 | Pharmacy Technicians | $46,470 | Pharmacy technician |
| 29-2031 | Cardiovascular Technologists & Technicians | $105,580 | EKG technician — **broad category; EKG-only roles pay less. Guide states this caveat explicitly.** |
| 31-1131 | Nursing Assistants | $46,680 | Nurse aide (CNA) |
| 31-1120 | Home Health & Personal Care Aides | $40,910 | Home health aide |
| 43-6013 | Medical Secretaries & Administrative Assistants | $50,290 | Medical administrative assistant |
| 43-3021 | Billing & Posting Clerks | $56,110 | (context on billing roles) |

**IT**
| SOC | Occupation | MA median | Used as |
|---|---|---|---|
| 15-1232 | Computer User Support Specialists | $75,070 | Help desk / user support |
| 15-1231 | Computer Network Support Specialists | $88,650 | Network support technician |
| 15-1212 | Information Security Analysts | $136,550 | Cybersecurity — **full-occupation median incl. experienced analysts; entry roles pay less. Guide states this caveat.** |
| 15-1244 | Network & Computer Systems Administrators | $110,980 | Cloud support (closest category) — **advancement target; entry cloud/help-desk roles start lower. Caveat in guide.** |

**Skilled trades**
| SOC | Occupation | MA median | Used as |
|---|---|---|---|
| 47-2111 | Electricians | $79,420 | Electrician |
| 49-9021 | HVAC & Refrigeration Mechanics & Installers | $77,300 | HVAC/R technician |
| 47-2152 | Plumbers, Pipefitters & Steamfitters | $93,880 | Plumber |
| 51-4121 | Welders, Cutters, Solderers & Brazers | $62,570 | Welder |

### H2. Massachusetts licensing / registration facts (sourced) — used in guide "license" cells
- **CNA (nurse aide):** MA requires completing a DPH-approved Nurse Aide Training Program (NATP) and passing the state competency evaluation, after which you are listed on the Nurse Aide Registry. Source: mass.gov/nurse-aide-registry-program and mass.gov/info-details/learn-how-to-become-a-certified-nurse-aide-in-massachusetts (DPH, 105 CMR 156). Checked 9/26/2026.
- **Pharmacy technician:** MA requires a Pharmacy Technician license from the Board of Registration in Pharmacy — required even if nationally certified; must be 18+. Source: mass.gov/how-to/apply-for-a-pharmacy-technician-license and mass.gov/pharmacy-technician-licensing (247 CMR 8). Checked 9/26/2026.
- **Electrician:** Journeyman (Class B) needs 8,000 hrs practical experience over ≥4 years as an apprentice + the 600-hour Journeyman's Course, then the exam; Board of State Examiners of Electricians. Source: mass.gov/board-of-state-examiners-of-electricians-licensing (237 CMR 13). Checked 9/26/2026.
- **Plumber:** Apprentice needs ≥5,100 practical clock hours + 300 hrs theory over ~3 years, then the journeyman exam; Board of State Examiners of Plumbers and Gas Fitters. Source: mass.gov/plumber-licensing (248 CMR 11). Checked 9/26/2026.
- **HVAC/refrigeration:** MA refrigeration technician license (6,000 apprentice hrs, or 450 hrs approved study) **plus** federal EPA 608 (universal CFC) to handle refrigerant. Source: mass.gov "Apply for a Refrigeration Technician License"; EPA 608 (federal). (Matches VERIFICATION_LOG A8/B18.)
- **Welder:** No statewide Massachusetts welding license; employers use hands-on weld tests and voluntary AWS (American Welding Society) certification. Presented as general industry info (F3).
- **Voluntary-cert healthcare roles (no MA license):** medical billing & coding (AAPC CPC/CPB, AHIMA CCA), medical assistant (AAMA CMA, AMT RMA), phlebotomy (ASCP, NHA CPT), EKG tech (CCI CET, NHA CET), medical administrative assistant (NHA CMAA), home health aide (agency training). Certifications are voluntary/employer-preferred; presented as general industry info (F3), not as CSC claims and not as state requirements.

### H3. Outward destinations used (verified)
- MassHire Career Center locations: mass.gov/info-details/masshire-career-center-locations
- MassHire JobQuest: jobquest.mass.gov
(both in js/site-config.js as MASSHIRE_LOCATOR / JOBQUEST)

---

## I. APPLIED by Code — Sept 26, 2026 (deeper career-guide content)

Expanded the four Career Paths pages (career-paths hub, healthcare, IT, skilled trades) with training-pathway
content the guides were missing: an IT certification ladder, a healthcare "choose by work setting" section, a
skilled-trades "how you get in" (theory + apprenticeship) section with a per-trade licensing table, and a
"how training differs by field" comparison on the hub. All new material is **general industry information**
(VERIFICATION_LOG F3) and states no CSC course facts.

### I1. Certification / pathway facts (general industry info)
- **CompTIA ladder:** entry = Tech+ (FC0-U71) then A+ (help desk); Network+ (networking); Security+ (entry
  cybersecurity, expects prior support/networking experience). Consistent with B13. Cloud = vendor certs (AWS
  Certified Cloud Practitioner, Microsoft Azure AZ-900, Google Cloud Digital Leader). Programming presented as
  a separate, portfolio-driven path. Source: CompTIA certification roadmap (industry references), checked 9/26/2026.
- **Healthcare license vs. certification** and **trade licensing hours**: reuse the sourced facts already in
  H2 (CNA/pharmacy-tech MA licensing; electrician 600-hr course + 8,000 hrs; plumber 300 hrs theory + 5,100
  hrs; HVAC/R 450 hrs study or 6,000 apprentice hrs + EPA 608; welder no state license + AWS). No new licensing
  claims introduced.

### I2. Entry-level pay ranges (NEW — labeled "Massachusetts job-market data, 2026", kept separate from BLS medians)
Used to make the honest point that state-funded certificate courses start below the BLS occupation median.
| Role | Entry range used | Source (checked 9/26/2026) |
|---|---|---|
| IT support / help desk (MA) | ~$20–$31/hr to start | ziprecruiter.com (Entry-Level IT Support Specialist, MA; 25th–75th pct $41k–$64.4k) |
| CNA (MA) | ~$18–$25/hr to start | ziprecruiter.com (Entry-Level CNA, MA; 25th–75th pct $37.1k–$51.3k) |
| Phlebotomist (MA) | ~$17–$26/hr to start | ziprecruiter.com (Entry-Level Phlebotomist, MA) |
| Apprentice electrician (MA) | ~$25/hr average | indeed.com (Apprentice Electrician, MA) |
BLS OEWS May 2025 medians (H1) are cited alongside as the full-occupation figure. The IT "honest word on pay"
note frames the ~$36/hr (support) and ~$42/hr (network) BLS medians as experienced pay, and flags that
six-figure IT salaries sit on the security/cloud/programming rungs that need prior knowledge or a degree —
matching the owner's guidance that state-sponsored IT certificate roles top out well below degree-track roles.

### I3. New CSS
Added a self-contained `.ladder` component to `css/style.css` (guarded; braces balanced). All other new
content reuses existing tested components (`.program-items`, `.data-table`, `.check-list--num`, `.note`).

---

## I (REVISED) — Sept 26, 2026: pay claims re-sourced to BLS (supersedes the aggregator numbers above)

Emilio flagged that his "$25–$40/hr" was only an example and that crowdsourced salary sites are not authoritative.
Correct. All entry-level pay claims on the four Career Paths pages were rewritten to use **BLS Occupational
Outlook Handbook (OOH), May 2025** figures (national median, lowest-10%/highest-10%, and typical entry-level
education), fetched 9/26/2026. The ZipRecruiter/Indeed numbers and the "$20–$40/hr" and "$25/hr apprentice"
lines were removed.

**BLS OOH, May 2025 (national) — figures now used:**
| Occupation | Median | Lowest 10% | Entry education (BLS) | Source |
|---|---|---|---|---|
| Computer user support specialists | $61,860 | under $40,980 | Some college, or HS diploma + IT certifications | bls.gov/ooh/.../computer-support-specialists.htm |
| Computer network support specialists | $76,220 | under $47,120 | Associate's typical | same |
| Information security analysts | $129,180 | under $75,090 | Bachelor's + prior experience | bls.gov/ooh/.../information-security-analysts.htm |
| Software developers | $135,980 | under $82,460 | Bachelor's | bls.gov/ooh/.../software-developers.htm |
| Medical records specialists (billing/coding) | $51,140 | under $37,000 | Postsecondary nondegree award | bls.gov/ooh/healthcare/medical-records-and-health-information-technicians.htm |
| Nursing assistants (CNA) | $42,260 | under $33,940 | State-approved program + competency exam | bls.gov/ooh/healthcare/nursing-assistants.htm |
| Phlebotomists | $45,230 | under $35,780 | Postsecondary nondegree award | bls.gov/ooh/healthcare/phlebotomists.htm |
| Medical assistants | $45,690 | under $36,050 | Postsecondary certificate | bls.gov/ooh/healthcare/medical-assistants.htm |
| Electricians | $63,190 | under $42,640 | HS diploma; 4–5 yr apprenticeship; state license | bls.gov/ooh/.../electricians.htm |
| Plumbers, pipefitters, steamfitters | $63,800 | under $44,150 | HS diploma; 4–5 yr apprenticeship | bls.gov/ooh/.../plumbers-pipefitters-and-steamfitters.htm |
| HVAC/R mechanics & installers | $61,010 | under $40,050 | Postsecondary nondegree award; apprenticeship | bls.gov/ooh/.../heating-air-conditioning-and-refrigeration-mechanics-and-installers.htm |

MA-specific medians on the role cards remain as logged in H1 (BLS OEWS May 2025, Massachusetts). The IT "honest
word on pay" note now makes Emilio's point with sources: user support is entry-level (some college / HS + certs,
median $61,860, lowest 10% under $40,980), while the six-figure IT roles (info security analyst, software
developer) require a bachelor's and/or experience. Apprenticeship structure (4–5 yr, ~2,000 hrs paid OJT/yr)
is from the BLS OOH trade pages, replacing the aggregator apprentice-wage figure.

Note: BLS OOH slugs matter — nursing-assistants.htm (not ...-and-orderlies) and
medical-records-and-health-information-technicians.htm (not medical-records-specialists) are the working URLs.

## J. Express Program figures — confirmed by Emilio (2026-09-28)

Emilio confirmed these Workforce Training Fund Express figures directly (for the
staff-training-grants.html / express pages). Applied to `js/site-config.js` and the
`[VERIFY]` fallbacks on `staff-training-grants.html` cleared to real numbers for these:

- **Reimbursement rate (eligible small employers):** up to **100%** (`EXPRESS_RATE_SMALL = 1.00`).
- **Small-employer size:** **100 or fewer W-2 employees** (`EXPRESS_SMALL_EMPLOYER_MAX = 100`).
- **Annual cap per company:** up to **$15,000/year**, reusable across different trainings (`EXPRESS_ANNUAL_CAP_PER_COMPANY = 15000`).
- **Application → acceptance:** about **3 weeks** (`EXPRESS_APPLICATION_WEEKS = 3`).
- **Payout:** the state **sends the employer a check** (reimbursement after the employer pays).

Still `[VERIFY]` (Emilio has not confirmed against CommCorp yet): `EXPRESS_MAX_PER_PERSON_PER_COURSE`
($3,000), `EXPRESS_MAX_PER_INSTRUCTIONAL_HOUR` ($300), `EXPRESS_RATE_LARGE` (50%),
`EXPRESS_AGREEMENT_AUTOSTART_DAYS` (21). Those still gate the employer pages from deploy.

## K. Massachusetts Registered Apprenticeship — employer funding (sourced 2026-09-28)

For `apprenticeships.html`. Corroborated on the state/federal sites (not in project docs):

- **Model:** Registered Apprenticeship is "earn while you learn" — the apprentice is an **employee from day one**; training (on-the-job + related classroom instruction) happens **during** employment. It flips the "train first, then hire" model. (apprenticeship.gov; mass.gov Learn/Earn/Succeed.)
- **Registered Apprentice Tax Credit (claimed by the employer/sponsor):** 50% of the apprentice's wages, up to **$4,800/apprentice/yr**, up to **$100,000/employer/yr**, for up to **2 consecutive tax years**. Eligibility: registered with DAS as a sponsor with an approved agreement; apprentice works **≥180 days** in the tax year, primary workplace in MA; occupation on the eligible list (tech, healthcare, advanced manufacturing, life sciences, clean energy, other in-demand). Sources: mass.gov "Apply for a Registered Apprentice Tax Credit"; DAS Issuance 32-07012026 (TY2026 eligibility); DAS Issuance 28-12172025 (expansion).
- **GROW / RTI grants:** can fund the related (classroom) instruction; amounts set per grant round; program rules bar passing RTI cost to the apprentice. Sources: mass.gov Registered Apprenticeship funding opportunities; DAS Issuance 27-073025 (GROW FY26).
- **Corrected a misconception:** "ITA-train the person → then they become an apprentice → employer claims the credit" is NOT how it works. The credit requires a *registered apprentice* (trained on the job). ITA (classroom-first) and apprenticeship (earn-while-you-learn) are two separate funnels; a pre-apprenticeship can bridge them. Whether WIOA/ITA can fund apprenticeship RTI specifically is still unconfirmed — left off the site.
- Applied to `js/site-config.js` (APPRENTICE_TAX_CREDIT_* / APPRENTICE_MIN_DAYS) and rendered on apprenticeships.html via [data-cfg].

### K1. ITA can fund apprenticeship related instruction (confirmed 2026-09-28)

Follow-up to K. Corroborated on DOL: an Individual Training Account (ITA) can pay for the
related technical instruction (RTI / classroom part) of a Registered Apprenticeship.
- Registered Apprenticeships have **automatic ETPL eligibility** (20 CFR 680.470); the sponsor opts in.
- ITAs may cover apprenticeship classroom/distance-learning costs; **local WDBs/AJCs set the allowable-cost policy** (TEGL 13-16). So it varies by MassHire board, and the apprentice must personally be WIOA-eligible.
- Source: U.S. DOL TEGL 13-16 (dol.gov/node/162570); 20 CFR 680.470.
Added to apprenticeships.html (funding section + FAQ). Not asserting the wage-side OJT reimbursement detail on-site (kept scope to RTI).

## L. APPLIED by Code — Sept 28, 2026 (pre-launch verify sweep, all cleared for the LIVE deploy)

Emilio reviewed every remaining `[VERIFY]`/`DRAFT` one by one; the whole site (incl. blog) went live.

- **Express $3,000/person/course + $300/instructional hour — CONFIRMED.** Official CommCorp Express Program Guidelines: "Grant funds are limited to $15,000 per company per calendar year, $300 per instructional hour, and $3,000 per employee per course." Corroborated by Emilio's 851 Ventures training FAQ (training.851ventures.com). `[VERIFY]` cleared in `site-config.js`. Source: https://commcorp.org/subprogram/wtfp-express-program-guidelines/
- **"Larger employers 50%" tier — REMOVED (was wrong/obsolete).** Current CommCorp rule: ≤100 MA W-2 employees at up to 100% (the 51–100 tier was raised from 50% to 100%). Employers over 100 aren't the Express audience. Dropped `EXPRESS_RATE_LARGE` and the "larger employers" copy/table row; reimbursement calculator collapsed to the single ≤100-employee model.
- **21-day auto-start — REMOVED.** Not present in CommCorp guidelines or the 851 FAQ; dropped `EXPRESS_AGREEMENT_AUTOSTART_DAYS` and the sentence.
- **WIOA low-income example ($15,960–$60,124, MassHire Central 2026) — REMOVED.** Region-specific and potentially misleading; `qualify.html` and blog #2 now say limits vary by region/household and a MassHire center checks. Dropped `INCOME_EXAMPLE_*`.
- **Selective Service (men born on/after 1/1/1960 must register for WIOA funds) — CONFIRMED by Emilio.** Kept.
- **AAPC CPC exam $425 (one attempt) / $499 (two) — RE-VERIFIED** on aapc.com (2026). Kept in blog #6.
- **All real wage/salary figures — REMOVED site-wide** (Emilio: "no real figures"). Blog uses qualitative wording + a BLS look-up link. (The BLS OEWS May 2025 MA medians logged in §G1/§I-REVISED are no longer displayed; the old program pages that still contain them are 301 redirect stubs, so nothing renders live.)
- **ITA approval model — CORRECTED (Emilio).** The student selects from the already-approved ETPL; the counselor does not vet the school. Approval = eligible + program-on-ETPL + funding available. Fixed blog #3. (Also in Code memory.)

## M. Salary-by-state post — wage figures (2026-10-01/02; Emilio-approved exception to "no real figures")

`blog/medical-coding-billing-salary-by-state.html` is the one place the site shows real pay figures (it supersedes the "no real figures" sweep in §L for this post only; the rest of the site still has none). Sources, all checked against the files/pages themselves:
- **BLS OEWS May 2025**, state file `oesm25st.zip` and national file `oesm25nat.zip` (bls.gov/oes/tables.htm; plain curl gets a 403, a descriptive User-Agent works). Occupations: 29-2072 Medical Records Specialists, 43-3021 Billing and Posting Clerks, 00-0000 All Occupations.
- National table CONFIRMED against the national file except one fix: upper-25% hourly **$31.16 → $31.17** (H_PCT75 = 31.17). Mean $56,790, all-jobs median $50,980, 43-3021 median $48,500 / $23.32: match.
- Top-10 states table and the five FAQ states (DC, RI, HI, WA, CA; all above $61,000): match the state file. The 51-row state table is generated from the file by `tools/build-salary-table.py` (Vermont job count is "**" in BLS → "Not published").
- **BLS Occupational Outlook Handbook** (medical records specialists): 8 percent growth 2025–2035, "much faster than the average for all occupations"; the draft said "faster than average", corrected.
- **AAPC 2026 salary report** (aapc.com/resources/medical-coding-salary-survey): certified $67,260; non-certified $55,721 (20.7% more); CPC $67,147; 2 certifications $74,557; 3+ $81,227. All match.
- Next year: download the new `oesm<yy>st.zip`, run `python3 tools/build-salary-table.py <file>.xlsx` then `python3 tools/build-pages.py`, and re-check the hard-coded national, top-10 and FAQ numbers in the post's `PAGES.append` block by hand.

## N. Healthcare jobs post — national BLS pay, outlook, licensing and certification facts (2026-10-03, DRAFT, local)

`blog/healthcare-jobs-massachusetts.html` (publish date 2026-10-03). Compliance review: PASS (second review). Source file for everything below: `research-brief.md` (pipeline scratch, untracked).

**STATUS: NOT VERIFIED LIVE.** All figures were drawn from search summaries of official pages; bls.gov and mass.gov were unreachable (proxy-blocked) during research. The post carries a `<!-- DRAFT -->` marker that blocks deploy until every item below is checked live and Emilio approves.

**FLAGGED POLICY QUESTION (Emilio decides):** PROJECT-HANDOFF.md allows pay figures only in the salary-by-state post (section M). This post shows national BLS pay (median + 10th/90th percentile columns). Either (a) approve a second exception, or (b) remove the pay columns and link to the BLS pages instead. No Massachusetts OEWS medians were found, so the post uses national pay and links to https://www.bls.gov/oes/current/oessrcst.htm.

### N1. BLS OEWS May 2025, national (released 2026-05-15)

| Role | SOC | Median annual | Hourly shown | 10th pct / 90th pct annual |
|---|---|---|---|---|
| Nursing assistants (CNA) | 31-1131 | $42,260 | none (the brief's $20.13 belongs to the combined "nursing assistants and orderlies" row, $41,870; not used) | under $33,940 / over $51,980 [confirm which row the range belongs to] |
| Medical assistants | 31-9092 | $45,690 | $21.97 | under $36,050 / over $59,310 |
| Phlebotomists | 31-9097 | $45,230 | none | under $35,780 / over $58,780 |
| Pharmacy technicians | 29-2052 | $45,750 | none | under $36,020 / over $61,040 |
| Medical records specialists (coders) | 29-2072 | $51,140 | none | under $37,000 / over $81,150 |
| EKG technician | none (BLS groups under cardiovascular technologists 29-2031, median $74,310, associate's degree typical) | not shown | none | not shown |

### N2. BLS Employment Projections 2025-35, U.S.
CNA 3% (label used: about as fast as average); medical assistants 13% (much faster than average); phlebotomists 7% (label NOT used, brief flagged as inconsistent); pharmacy technicians 6% (faster than average); medical records specialists 8% (label NOT used, flagged); cardiovascular technologists 4% (not shown in post). Statement that many openings come from replacing workers (MA, phlebotomist, pharmacy tech, medical records only) is from the brief. Massachusetts projections (EOLWD) deliberately left out: vintage unknown.

### N3. Licensing facts
- CNA: MA DPH Nurse Aide Registry (https://www.mass.gov/nurse-aide-registry-program); state-approved training, state competency exam, registry listing required for nursing-home work; DPH-approved clinical sites. NOT stated in post: 87-hour minimum (effective date unconfirmed), exam vendor (Prometric vs. D&S conflict), exam fees, exam languages.
- Pharmacy technician: MA Board of Registration in Pharmacy (247 CMR 8.00; https://www.mass.gov/pharmacy-technician-licensing). License required for all techs. Trainee license: age 16+, HS or equivalent (or enrolled), good moral character. PT2: age 18+, HS or equivalent, good moral character, plus one of three routes (national exam PTCE/ExCPT/NRCPhT; board-approved program with final competency exam; 500 on-the-job hours as PT1 plus employer competency exam). Application fee $150, non-refundable. Renewal/CE terms not found; not stated.
- Medical assistant, phlebotomist, coder, EKG tech: no Massachusetts license found; post says "we did not find one; check with the state." Confirm with DPH, BHPL and the Clinical Laboratory Program (https://www.mass.gov/clinical-laboratory-program).
- DPH circular DCP 17-8-102 (2017): MAs who give immunizations in primary care need a CAAHEP- or ABHES-accredited program and direct supervision (https://www.mass.gov/files/documents/2017/09/28/cma-circular-17-8-102.pdf). 2017 document: confirm still current.

### N4. National certification facts (exam fees / questions / time)
- NHA CCMA: $169; 150 scored + 30 pretest items; 3 hours; HS/GED (or within 18 months) plus training within 5 years or work experience. https://www.nhanow.com/certification/nha-certifications/certified-clinical-medical-assistant-(ccma)
- AMT RMA: $150 (includes first annual fee); 210 questions; 2 hours. https://americanmedtech.org/medical-assistant
- NHA CPT: $134; 100 scored + 20 pretest; 2 hours; training program with 30 venipunctures and 10 capillary sticks on live people. https://www.nhanow.com/certification/nha-certifications/certified-phlebotomy-technician-(cpt)
- ASCP PBT: $155; 80 questions; 2 hours. https://www.ascp.org/boc/explore-credentials/view-all-credentials/PBT
- AMT RPT: $125; 200 questions; 2.5 hours. https://americanmedtech.org/phlebotomy-technician
- PTCB CPhT (PTCE): $129; 90 questions (80 scored); 1 h 50 min. https://ptcb.org/credentials/certification/certified-pharmacy-technician/
- AAPC CPC: $425 one attempt / $499 two (student $400 / $475); 100 questions; 4 hours; 70% to pass; passing earns CPC-A. https://www.aapc.com/resources/cpc-exam-faqs
- AHIMA CCA: $199 member / $299 non-member; HS diploma; 90-115 questions; 2 hours. https://www.ahima.org/certification-careers/certifications-overview/cca/
- NHA CET: $134; 2 hours; 10 live EKGs. https://www.nhanow.com/certification/nha-certifications/certified-ekg-technician-(cet)
- Passing scores for CCMA, RMA, CPT, PBT, RPT, PTCE, CCA, CET and the CET question count were not found; not stated.

### N5. BLS pages linked in the post
https://www.bls.gov/ooh/healthcare/nursing-assistants.htm · medical-assistants.htm · phlebotomists.htm · pharmacy-technicians.htm · medical-records-and-health-information-technicians.htm · cardiovascular-technologists-and-technicians.htm · https://www.bls.gov/oes/current/oessrcst.htm · https://www.mass.gov/info-details/masshire-career-center-locations · https://jobquest.mass.gov

### N6. Check live before deploy
1. Policy decision on pay columns (above).
2. Every figure in N1 and N2 against the live BLS OOH pages; CNA 10th/90th row; the 7% and 8% labels.
3. Pharmacy technician PT1/PT2 rules and $150 fee on mass.gov.
4. CNA registry wording; whether the 87-hour change is in force (if so, decide whether to mention it).
5. No-license statements for MA, phlebotomist, coder and EKG tech.
6. DPH circular 17-8-102 still current.
7. All exam fees, question counts and times in N4.
8. EKG tech grouping under 29-2031 (associate's degree typical).
9. "Coding is the only one of the six sometimes done from home" has no official source (hedged); unsourced work-environment lines to confirm against BLS.
10. FAQ questions are placeholders, not real People Also Ask data; capture real ones.
11. FAQ 4 wording "many employers prefer or require" vs. the brief's "may prefer or require".

## O. Phlebotomist post — national BLS pay, outlook, licensing and certification facts (2026-10-03, DRAFT, local)

`blog/phlebotomist-massachusetts.html` (publish date 2026-10-03). Compliance review: PASS (non-blocking issues 1-7, see `docs/blog-drafts/phlebotomist-massachusetts/review-report.md`). Source file: `docs/blog-drafts/phlebotomist-massachusetts/research-brief.md`.

**STATUS: from search extracts, not yet verified on live pages.** bls.gov, ascp.org, nhanow.com and mass.gov could not be opened during research. The post carries a `<!-- DRAFT -->` marker that blocks deploy until every item below is checked live and Emilio approves.

**FLAGGED POLICY QUESTION (Emilio decides):** PROJECT-HANDOFF.md allows pay figures only in the salary-by-state post (section M). This post shows national BLS pay for phlebotomists (same open question as section N). Either approve an exception or swap the pay section for a link to the BLS page.

**Note:** section H1 of this log holds a Massachusetts phlebotomist median of **$50,170** (SOC 31-9097, line ~186). It is **not used** in the post (the post shows national pay and links the BLS Massachusetts page). Confirm its source/vintage before any use.

### O1. BLS wage data, phlebotomists (SOC 31-9097), national, May 2025 (vintage to confirm on oes319097.htm; brief called it "2025 median pay")
- Median: $45,230/year; $21.75/hour
- 10th percentile: under $35,780/year; 90th percentile: over $58,780/year
- No Massachusetts pay shown (current MA figure not found).
- https://www.bls.gov/oes/current/oes319097.htm · https://www.bls.gov/ooh/healthcare/phlebotomists.htm · MA page linked: https://www.bls.gov/oes/current/oes_ma.htm

### O2. BLS outlook 2025-35
- 7% growth (label "much faster than average" deliberately not used); 143,900 jobs in 2025; about 18,000 openings a year.

### O3. BLS industry shares, 2025
- Hospitals 36%; medical and diagnostic labs 33%; other ambulatory health services 16%; physician offices 9%; outpatient care centers 2%.

### O4. BLS work environment / training (confirm wording live)
- Standing for long periods; mostly full time; nights/weekends/holidays in hospitals and labs; one of the highest rates of work injuries and illnesses.
- Programs usually take less than one year (community college, vocational, technical school); some people hired with HS diploma and trained on the job; lab technologist usually needs a bachelor's degree; medical assistant listed as related job.
- BLS also lists National Phlebotomy Association and NCCT as certifying groups.

### O5. Licensing facts
- States requiring phlebotomist certification/licensure per BLS and ASCP: California, Louisiana, Nevada, Washington. Massachusetts not on the list. https://www.ascp.org/boc/explore-credentials/state-licensure
- No mass.gov sentence stating "no phlebotomy license" was found. DPH Clinical Laboratory Program licenses labs and collection sites, not individuals (M.G.L. c.111D, 105 CMR 180.00). https://www.mass.gov/clinical-laboratory-program. Confirm with DPH. Also confirm "we did not find a Massachusetts state approval for phlebotomy programs."
- CNA Nurse Aide Registry mention (one sentence, comparison section): see section N3.

### O6. Certification facts
- NHA CPT: $134; 120 items (100 scored + 20 pretest); 2 hours; HS/GED (or within 18 months) plus training within 5 years OR 1 year supervised work within 3 years (or 2 within 5); 30 venipunctures + 10 capillary sticks on live people; renew every 2 years with 10 CE credits plus fee. https://www.nhanow.com/certification/nha-certifications/certified-phlebotomy-technician-(cpt) · https://www.nhanow.com/stay-certified
- ASCP PBT: $155 (a non-official site says $165 after Jan 2026: CHECK); 80 multiple-choice questions; 2 hours; adaptive; routes include NAACLS-approved program, structured program, 1 year full-time experience (all within 5 years); HS diploma or equivalent for training routes; 3-year Credential Maintenance Program. https://www.ascp.org/boc/explore-credentials/view-all-credentials/PBT · https://www.ascp.org/boc/maintain-your-credentials/view-credentials-to-maintain/PBT
- AMT RPT: no details in the post (table says "See AMT's site"). Section N4 holds $125 / 200 questions / 2.5 hours (unused here). https://americanmedtech.org/phlebotomy-technician

### O7. Claims drawn from the content strategy, not the research brief (confirm or remove)
- MassEducate / MassReconnect generally cover credit programs, not short non-credit certificates (needs mass.edu OSFA source or removal).
- "Some employers may train new workers and pay them while they learn" (hedged, no employer named).
- MassHire can point to free ESOL classes (unsourced).
- "Some people get hired with a high school diploma and learn on the job" (from BLS; confirm wording).
- Programs/employers may ask for immunizations, CPR, background check (written as "ask").
- FAQ questions are drafted from search patterns, not live People Also Ask data.

### O8. Check live before deploy
1. Pay-figure policy decision. 2. O1-O4 against live BLS pages. 3. O5 with DPH. 4. O6 on NHA/ASCP/AMT sites (ASCP $155 vs $165). 5. O7 items. 6. Optional: OSHA 29 CFR 1910.1030 cite for the blood-risk line.
