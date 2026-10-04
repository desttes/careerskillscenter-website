## Topic: How to Become a CNA in Massachusetts
## Target Keyword: "CNA massachusetts"

Research date: 2026-10-04. Entry filter: PASSES. CNA training needs no prior experience or college. Nothing in the sources I saw requires a diploma or GED to enter training (see Licensing section: age/education rule NOT confirmed).

Access note: mass.gov, careeronestop.org and ecfr.gov returned HTTP 403 (or a redirect) to my fetch tool. Every mass.gov fact below is therefore `[SEARCH SUMMARY]` (seen in search result summaries, not on the open page). The Writer or a human should open the mass.gov pages once before publishing. Confirmed-by-open-page items are marked `[OPENED]`.

---

## Pay Data (BLS OEWS, National)

- National median annual pay, Nursing Assistants (SOC 31-1131), May 2025: **$42,260**. [OPENED] https://www.bls.gov/ooh/healthcare/nursing-assistants.htm (page last modified Aug 27, 2026). Also confirmed through the BLS public API (series OEUN000000000000031113113 = 42260, year 2025).
- Orderlies (SOC 31-1132) are a separate job with median $38,290. BLS combines both on one page (combined median $41,870). Use the 31-1131 figure for CNAs.
- Entry-level pay: BLS OOH page gave "lowest 10% earned less than $33,940" (that is the 10th percentile, not the 25th). The 25th percentile was not shown. [OPENED] same OOH page. Optional.
- **Massachusetts example (May 2025, BLS OEWS via BLS public API, https://api.bls.gov/publicAPI/v2/timeseries/data/):**
  - MA median annual wage: **$46,680** (series OEUS250000000000031113113). Hourly median $22.44 (series ...08). $22.44 x 2,080 hours is about $46,675, which agrees.
  - MA annual mean wage: $47,700. MA employment: 38,130 jobs. National employment (May 2025): 1,448,910.
  - MA annual 25th percentile $44,340 (series ...12). Note: this sits close to the median; the Writer should skip it unless re-checked at https://data.bls.gov/oes/ (area = Massachusetts, SOC 31-1131). I decoded the series IDs by the OEWS data-type code table, not from a page that labeled them, so a quick human spot check on the BLS OEWS tool is worthwhile before publishing the MA numbers.
  - The BLS state table web pages (bls.gov/oes/current/oes311131.htm) returned 403 to me; the API was the only route.
- Caution: the website bls.gov/oes/current page copy I could reach via a mirror (blsmon1.bls.gov) showed May 2022 data ($35,760). It is stale. Do not use it.

## Job Outlook

- National projected growth 2025-2035: **3%** (about 41,100 new jobs). Annual job openings: about **203,300** per year on average (includes replacement of workers who leave). Employment 2025: 1,558,700 for nursing assistants and orderlies combined. [OPENED] https://www.bls.gov/ooh/healthcare/nursing-assistants.htm
- O*NET (older projection cycle, 2024-2034): 1-2% growth, 204,100 projected openings; "Bright Outlook" tag. [OPENED] https://www.onetonline.org/link/summary/31-1131.00 . Use the BLS 2025-2035 figure as primary.
- Massachusetts-specific projection: `[DATA NOT FOUND — searched: lmi.dua.eol.mass.gov Long-Term Occupation Projections (search summary only, figures looked inconsistent so I did not trust them), mass.gov projections page, careeronestop (403)]`. Do not cite a MA growth number.

## Licensing & Certification

National frame: federal law (42 CFR 483.152) sets the floor for nurse aide training, and each state runs its own nurse aide registry. BLS says nursing assistants must pass a state competency exam and get state certification (often called CNA). [OPENED] BLS OOH page above. Writer should tell readers to check their own state's registry; Massachusetts is the example below.

Federal floor: at least 75 clock hours of training, including at least 16 hours of supervised practical training. [OPENED] https://www.law.cornell.edu/cfr/text/42/483.152 (mirror of the eCFR; official copy https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-483/subpart-D/section-483.152 was blocked).

Federal money rule (useful, affects "is it free?"): an aide who is employed by, or has an offer from, a nursing facility on the day training starts may not be charged for any part of the program, including textbooks. If someone not yet employed gets hired by a facility within 12 months of finishing, the State must reimburse the training cost pro rata over the period they work as a nurse aide. [OPENED] Cornell page above (same text as eCFR 483.152). Whether and how Massachusetts pays that reimbursement: `[DATA NOT FOUND — searched: mass.gov search results, eCFR]`.

### Massachusetts (example state) [SEARCH SUMMARY unless noted]
- Managing body: Massachusetts Department of Public Health (DPH) Nurse Aide Registry Program. Phone (617) 753-8144, nars@mass.gov (seen in search summary). https://www.mass.gov/nurse-aide-registry-program
- Path: finish a DPH-approved nurse aide training program, then pass the competency evaluation (knowledge test plus skills test). You must pass both parts to be listed on the Massachusetts Nurse Aide Registry. https://www.mass.gov/info-details/learn-how-to-become-a-certified-nurse-aide-in-massachusetts
- Finding approved programs: DPH "Check a License" site, License Board = Nurse Aide Registry, License Type = Nurse Aide Training Provider Approval; also an interactive map of CNA training sites on mass.gov. DPH approves classroom-based programs; partly online courses considered if classroom and clinical parts meet minimums. https://www.mass.gov/info-details/information-for-nurse-aide-training-programs
- Current state rule on hours: 105 CMR 156.300 says each course is a minimum of **75 hours**. The regulation text as shown on Cornell does not split classroom vs. clinical hours. https://www.law.cornell.edu/regulations/massachusetts/105-CMR-156-300 [OPENED]
- **FRESHNESS FLAG (important):** A DPH advisory memo dated April 2026 (one source snippet said April 3, another April 4) says DPH is raising the minimum from the federal 75 hours to **87 hours, including 21 hours of supervised practical training**, under a new State-Approved CNA Curriculum Framework. Programs must update curricula; revised exams are expected to roll out in **early 2027**. A free online learning platform (40+ hours, English/Spanish/Haitian Creole) is being built for approved programs that opt in. https://www.mass.gov/info-details/dph-advisory-memo-new-certified-nurse-aide-cna-curriculum-framework and https://www.mass.gov/news/new-certified-nurse-aide-cna-curriculum-framework [SEARCH SUMMARY; I could not open the memo]. I could not confirm the exact date new hours take effect, or whether the 75-hour rule in 105 CMR 156.300 has been formally amended. The Writer should say "75 hours is the long-standing minimum; DPH has announced 87 hours" and tell readers to ask any program which standard it follows. This needs a human to open the memo.
- Competency exam: administered by D&S Diversified Technologies (DPH's testing vendor). Source is the vendor's candidate handbook, not a mass.gov page, flagged as the state's contracted tester. https://hdmaster.com/testing/cnatesting/Massachusetts/forms/MA%20NA%20Candidate%20Handbook%20V5%207.2024%20TRANSLATABLE.htm [OPENED, handbook dated 7.2024; a newer 1.2025 handbook exists at https://www.hdmaster.com/testing/cnatesting/Massachusetts/forms/MA%20NA%20Candidate%20Handbook%201.2025.pdf, not opened. Fees and format may have changed, and the early-2027 exam revision may change them again.]
  - Knowledge test: 60 multiple-choice questions, maximum 60 minutes, pass at 76% or better.
  - Skills test: three to four randomly assigned tasks, maximum 40 minutes.
  - Fees per attempt: knowledge $30 (audio version $40), skills $70. So $100 for a first try at both parts.
  - Attempts: 4 for knowledge, 3 for skills. If you use them all you must finish another approved program. Training does not expire.
  - Languages: exam offered in English, Spanish, Traditional and Simplified Chinese; audio knowledge option on request.
- Training waiver: people who finished an approved nurse aide course in another state, or a clinical course in an approved nursing school, may qualify to test without repeating training (105 CMR 156.100(A)(2)). Application is on the D&S site. [SEARCH SUMMARY]
- Reciprocity: a CNA certified in another state, current and in good standing, never certified in MA, can apply for reciprocity through D&S (since Dec 4, 2023); typical processing 15 days. [SEARCH SUMMARY] https://www.mass.gov/info-details/learn-how-to-become-a-certified-nurse-aide-in-massachusetts
- On-site observation / work credit page exists (https://www.mass.gov/info-details/nurse-aide-on-site-observation-and-work-credit); I could not read it. `[DATA NOT FOUND — searched: mass.gov (403)]`
- Renewal: every 24 months; requires at least 8 consecutive hours of paid work as a nurse aide in the prior 24 months (handbook [OPENED]; mass.gov renewal page agrees per search summary). Renewal fee: `[DATA NOT FOUND — searched: mass.gov renewal page (403), search results; the $180 fee seen is for Certified Medication Aide, a different credential — do NOT use]`
- Minimum age, diploma/GED requirement, and criminal background (CORI) rules for CNA training/registry: `[DATA NOT FOUND — searched: mass.gov nurse aide pages (403), 105 CMR 156 summaries, D&S handbook (opened; silent)]`. Note: CORI checks are done by employers at hire (search summary). The Writer must not state an age or education rule.
- Employer preference: CNA registry listing is the standard for nursing facility work (BLS says state certification is expected). Hospital/home health employer preferences: `[DATA NOT FOUND]`.

### Not a CNA, but nearby (avoid mixing up)
- Certified Medication Aide (CMA) is a separate, later credential in MA. Personal Care Attendant (PCA) and Home Health Aide need no CNA exam. Do not describe these in detail unless the Writer wants an "other options" line.

## Training Paths (general industry — include duration and cost range)

- Length: BLS says state-approved programs are offered at high schools, community colleges, vocational schools, hospitals and nursing homes, and entry requires a state exam. [OPENED] BLS OOH. CareerOneStop's Massachusetts Local Training Finder lists 37 nursing assistant programs: 29 under 12 weeks, 7 from 12 weeks to under 1 year, 1 two-year associate degree; 33 in person, 4 with online options. [SEARCH SUMMARY] https://www.careeronestop.org/Toolkit/Training/find-local-training-results.aspx?keyword=Nursing+Assistant%2FAide+and+Patient+Care+Assistant%2FAide&location=Massachusetts&schoolprogram=p . The minimum is 75 hours (87 announced), which is a couple of weeks full time or a few months of evenings/weekends depending on schedule. Do not say "X weeks" as a rule.
- Clinical hours are hands-on and in person (a care facility). Evening/weekend sections exist: `[DATA NOT FOUND from a neutral source — searched: BLS, CareerOneStop summaries. Not stated.]`
- Cost: `[DATA NOT FOUND from a neutral source — searched: BLS OOH, CareerOneStop (403), O*NET, mass.gov search summaries]`. What I can source: the state exam fees ($30 + $70 = $100 for first attempts, vendor handbook). Training tuition is only published by schools. In search summaries I saw one Massachusetts community college listing about $2,689, but a college price page is a provider site, so I did NOT use it. Writer should say tuition varies by school and tell readers to ask each school for the full price including exam fees, books, uniform, background check.
- Free paths (sourced): (1) Federal rule above: an aide employed or offered a job by a nursing facility when training starts cannot be charged. (2) A Massachusetts workforce notice listed a free four-week CNA program at a Lexington nursing facility where the employer paid training and testing (a single employer example, undated in my summary; not a general promise). https://www.mass.gov/doc/dcs-info-14-258-certified-nursing-assistant-free-training-program-available/download [SEARCH SUMMARY]. Writer may say "some nursing homes pay for training," not name them. MassHire / WIOA funding eligibility belongs to the site's funding pages, and CareerOneStop marks programs "WIOA" when they are eligible. Do not promise funding.
- Working while training: `[DATA NOT FOUND — searched: BLS, mass.gov summaries]`.

## Employer Demand

- 36% of nursing assistants work in nursing care facilities and 32% in hospitals. [OPENED] BLS OOH. Other settings (home health, assisted living, rehab) exist but percentages not captured.
- About 203,300 openings a year nationally; most come from workers leaving the job or moving up, since growth is only 3%. [OPENED] BLS OOH.
- Work conditions (honesty material): physical, on your feet, high injury rates, may include nights, weekends and holidays. [OPENED] BLS OOH.
- Growth drivers (BLS wording not captured beyond the numbers above): `[DATA NOT FOUND — summary for aging population not captured; the OOH "Job Outlook" paragraph can be opened and quoted]`.
- Massachusetts: MA employment 38,130 CNAs (May 2025, BLS API). Massachusetts job openings count: `[DATA NOT FOUND]`.
- Career step: CNA experience is a common route toward LPN or RN, but those require more schooling and are outside this post's entry filter; one sentence at most. O*NET related jobs: Home Health Aides, LPNs, Medical Assistants, EMTs, RNs. [OPENED] O*NET.

## FAQ Questions (4-6)

I could not view live Google People Also Ask boxes or autocomplete with my tools. ALL questions below are PLACEHOLDERS inferred from the keyword and topic; the Content Strategist should replace them with real PAA/autocomplete if the SERP audit finds them.

1. [PLACEHOLDER] How long does it take to become a CNA in Massachusetts? (Answer from facts above: 75-hour minimum, 87 announced; length depends on schedule.)
2. [PLACEHOLDER] How much does CNA training cost in Massachusetts? (Answer: varies by school; exam $100 first try; may be free if a nursing facility employs you. Neutral tuition range NOT FOUND.)
3. [PLACEHOLDER] Can you get CNA training for free in Massachusetts? (Federal rule on facility-employed aides; employer-paid examples; do not promise.)
4. [PLACEHOLDER] How do I take the Massachusetts CNA exam, and what is on it? (60 questions, 76% to pass, skills test; $30 + $70.)
5. [PLACEHOLDER] How much do CNAs make in Massachusetts? (MA median $46,680, May 2025.)
6. [PLACEHOLDER] I'm a CNA in another state. Can I work in Massachusetts? (Reciprocity through D&S; waiver option.)

## Sources (full URLs, SOC codes here — not in the body text the reader sees)

SOC code: 31-1131 Nursing Assistants (31-1132 Orderlies is separate).

Opened and read:
- BLS Occupational Outlook Handbook, Nursing Assistants and Orderlies: https://www.bls.gov/ooh/healthcare/nursing-assistants.htm
- BLS public data API (OEWS May 2025, series OEUN000000000000031113113, OEUS250000000000031113113, ...04, ...01, ...08, ...12): https://api.bls.gov/publicAPI/v2/timeseries/data/
- O*NET 31-1131.00: https://www.onetonline.org/link/summary/31-1131.00
- 42 CFR 483.152 (Cornell mirror of federal text): https://www.law.cornell.edu/cfr/text/42/483.152
- 105 CMR 156.300 (Cornell mirror of state regulation): https://www.law.cornell.edu/regulations/massachusetts/105-CMR-156-300
- D&S Diversified Technologies (DPH's testing vendor), MA Nurse Aide Candidate Handbook (7.2024): https://hdmaster.com/testing/cnatesting/Massachusetts/forms/MA%20NA%20Candidate%20Handbook%20V5%207.2024%20TRANSLATABLE.htm

Search summary only (page returned 403 to me; needs a human to open before publishing):
- https://www.mass.gov/info-details/learn-how-to-become-a-certified-nurse-aide-in-massachusetts
- https://www.mass.gov/info-details/information-for-nurse-aide-training-programs
- https://www.mass.gov/nurse-aide-registry-program
- https://www.mass.gov/info-details/renewal-information-for-massachusetts-certified-nurse-aides
- https://www.mass.gov/info-details/dph-advisory-memo-new-certified-nurse-aide-cna-curriculum-framework
- https://www.mass.gov/news/new-certified-nurse-aide-cna-curriculum-framework
- https://www.mass.gov/info-details/massachusetts-certified-nurse-aide-cna-curriculum-frameworks
- https://www.mass.gov/info-details/nurse-aide-on-site-observation-and-work-credit
- https://www.mass.gov/doc/dcs-info-14-258-certified-nursing-assistant-free-training-program-available/download
- https://www.mass.gov/lists/nurse-aide-registry-laws-and-regulations (regulation list)
- https://www.careeronestop.org/Toolkit/Training/find-local-training-results.aspx?keyword=Nursing+Assistant%2FAide+and+Patient+Care+Assistant%2FAide&location=Massachusetts&schoolprogram=p
- https://www.hdmaster.com/testing/cnatesting/Massachusetts/forms/MA%20NA%20Candidate%20Handbook%201.2025.pdf (newer handbook, not opened)
- CMS memo QSO-26-08 (April 8, 2026) "Clarification regarding Nurse Aide Training Competency..." https://www.cms.gov/files/document/qso-26-08-nh-original-release-date-2026-04-08.pdf — PDF unreadable to me; may matter for nurse-aide-in-training rules. Unread.

Rejected / do not use: blsmon1.bls.gov mirror (stale 2022 data), community college tuition page seen in a search summary (provider site), $180 CMA renewal fee (wrong credential), MA LMI projection numbers in a search summary (inconsistent).

## Items for the human or director to resolve before publishing
1. Open the DPH CNA curriculum framework memo: confirm 87 hours / 21 practical hours, effective date, and whether current students are affected.
2. Open the mass.gov "Learn how to become a certified nurse aide" page: confirm age/education/background requirements, fees, and the on-site observation/work credit rule.
3. Spot check MA median $46,680 at https://data.bls.gov/oes/ .
4. Replace placeholder FAQs with real PAA/autocomplete.
5. Neutral tuition range remains missing.
