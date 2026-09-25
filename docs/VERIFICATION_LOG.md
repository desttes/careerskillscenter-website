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
