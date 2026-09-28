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
