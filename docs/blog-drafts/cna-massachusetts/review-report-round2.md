# Review report, round 2: How to Become a CNA in Massachusetts (cna-massachusetts)

Reviewed 2026-10-04 after revision round 1. Source: uncommitted `PAGES.append` block in `tools/build-pages.py` (`_cna_faq`, `_cna_body`), the "Verified addendum" in `research-brief.md`, register row R-BLOG-04, and `blog/course-mode-copy/cna-massachusetts.md`. I built the site in a scratch copy (not the repo) to check the HTML, JSON-LD, blog card and sitemap.

## Result: PASS (16 of 16 checks)

Both round 1 failures are fixed:
- **Check 3:** every number that was out of the brief is now in the brief's verified addendum, with an [OPENED] source.
- **Check 7:** "apply" is gone from the post.

All 8 recommended fixes from round 1 were also made. What is left below is optional polish, plus the human checks that were already listed before publishing.

| # | Check | Result |
|---|---|---|
| 1 | No CSC program details | PASS |
| 2 | No ETPL / WIOA approval / "state-approved" / Express claims | PASS |
| 3 | Every number is in the research brief with a source | PASS |
| 4 | "May qualify"; no funding promises | PASS |
| 5 | Plain language, about 8th grade | PASS |
| 6 | DRAFT marker present | PASS (note) |
| 7 | CTAs / banned words | PASS |
| 8 | COURSE-DEPENDENT markers + course-mode copy file | PASS |
| 9 | BlogPosting + FAQPage JSON-LD valid | PASS |
| 10 | No testimonials or invented outcomes | PASS |
| 11 | No facts from aggregators, providers or blogs | PASS |
| 12 | Follows strategy angle; differentiators are real sections | PASS |
| 13 | Reader-first | PASS |
| 14 | Answers the Guideline 7 reader questions | PASS |
| 15 | Links to relevant existing posts | PASS |
| 16 | Community experiences match editorial decisions | PASS |

## Status of the round 1 fixes

| Round 1 fix | Status |
|---|---|
| 1. Out-of-brief numbers | Done. The addendum covers 4 months / 120 days (42 CFR 483.35(d)), 80% of non-critical steps, the $25 deposit with "returned only if the review goes your way", 3 business days, 20 minutes early / no-show, (888) 401-0462, the ID rules, languages including Haitian Creole, the dictionary rule and the May 2026 v7.0 handbook. |
| 2. "apply" (3 places) | Done. FAQ 6 now says "you can ask for reciprocity" and "You do this online". The body says "you can request reciprocity". |
| 3. FAQ pay-back caveat | Done ("Ask DPH how this works in Massachusetts."). It also appears in the FAQPage schema. |
| 4. Table "Often $0" | Done ("May be $0 if you qualify"). |
| 5. Unsourced "trips up many test takers" | Done ("Check this rule early, especially if your ID is from another country."). |
| 6. [VERIFY] on the DPH phone | Done. |
| 7. MassHire legal-help claim | Done. It now points straight to Mass Legal Help. |
| 8. Pre-hire health tests | Done ("background checks and other hiring steps"). |
| 9. National median | Done ($42,260, BLS May 2025, which is in the brief [OPENED]). |
| 10. Long-sentence splits | Partly done. The "You pay first" cell is now two sentences. The reciprocity waiver sentence is unchanged (optional). |

## Check-by-check

### 1. No CSC program details: PASS
CSC appears only in the two R-BLOG-04 places: "Career Skills Center does not sell CNA training, so we can be straight with you." and "plans to offer training in healthcare, IT and the skilled trades." There is no length, cost, format or credential.

### 2. No approval claims: PASS
WIOA appears only as a general funding route ("You may qualify through WIOA..."). "DPH-approved" always describes other programs. There is no Express, ETPL or "state-approved" wording about CSC.

### 3. Numbers in the research brief: PASS
I matched every number in the body, the FAQ and the table:
- **Main brief:** $46,680; $42,260; May 2025; 3%; 2025-2035; 203,300; 36% / 32%; 75 / 16 hours; April 2026; 87 / 21 hours; early 2027; 37 / 29 / under 12 weeks; 60 questions / 60 minutes / 76%; 3-4 tasks / 40 minutes; $30 / $40 / $70; 4 / 3 tries; 24 months / 8 hours; 12 months; (617) 753-8144.
- **Verified addendum:** 4 months (120 days); 80%; $25; 3 business days; 20 minutes; (888) 401-0462; the May 2026 handbook.

Two notes, neither a failure:
- "one or two years" (contract length) and "two-person move" come from community experiences approved in `editorial-decisions.md` (C2, C5). They are framed as experiences, which check 16 covers.
- "compare six jobs in our guide" refers to our own healthcare-jobs post. I confirmed that post covers six jobs.

### 4. "May qualify": PASS
"May qualify" appears in the table, the CTA, the FAQ and the "What to do this week" list. The only "$0" without "may" is the column 1 "Training: $0". That is the federal no-charge rule for aides who are hired before training starts, so it is accurate. Minor and optional: "Often a work contract" in the same column states how often something happens, based only on community stories (see fix list).

### 5. Plain language: PASS
Estimated Flesch-Kincaid grade 5.8, 12.9 words per sentence (prose only, comments and scripts removed). There is a glossary, and terms are defined where they first appear. A few sentences run 29-32 words. None blocks reading (optional splits are in the fix list).

### 6. DRAFT marker: PASS (note)
`<!-- DRAFT -- facts to verify: ... -->` is at the top of `_cna_body` and renders in the HTML. It is long (items 0-11) rather than short, but it matches the other role posts and lists real open checks. Optional: trim it.

### 7. CTAs: PASS
- The funding CTA goes to `qualify.html`, placed right after the "Three ways to pay" section.
- CNA is a state certification, so pointing to DPH, the registry and D&S is correct. MassHire appears only for funding, which is allowed.
- No "our program", "our courses", "enroll" or "apply" in the post copy. A grep of the block found "apply" nowhere. The only "enrollment" hit is in a comment for a different block.

### 8. COURSE-DEPENDENT: PASS
`<!-- COURSE-DEPENDENT: R-BLOG-04 -->` with closing markers wraps both places. The R-BLOG-04 row is in `docs/COURSE_CONTENT_REGISTER.md`. `blog/course-mode-copy/cna-massachusetts.md` has guide and course versions for both places. The course-mode copy keeps "may qualify" and has no program details.

### 9. JSON-LD: PASS
In the scratch build, both blocks parse as valid JSON: BlogPosting (datePublished 2026-10-04) and FAQPage (6 questions that match the visible FAQ, including the new pay-back caveat). The blog card (Oct 4, 2026) and the sitemap entry are generated. The date is real, not backdated.

### 10. No testimonials or invented outcomes: PASS
The only voices are approved community items. There are no outcome stats. The unsourced "trips up many test takers" line from round 1 is gone.

### 11. Source quality: PASS
Facts come from BLS, eCFR/Cornell, 105 CMR, the D&S handbook (the state's testing vendor), mass.gov, CMS and CareerOneStop. There is no provider tuition and no aggregator pay.

Three handbook facts are in `community-verification.md` [OPENED] but not in the brief's addendum. They are facts, not numbers, and their source is the official handbook, so this passes:
- "Some programs pay the fees for you" (path step 4 and exam box)
- "You pay the test fees before you can pick a test date"
- "You can tell the nurse you want to make a correction, as long as time is left"

They should still be added to the addendum (fix list).

### 12. Angle and differentiators: PASS
- **Hook:** follows the strategy (the federal no-charge rule first).
- **Differentiator 1:** "Three ways to pay" is an H2 with a table, the fine print and an H3 on contracts.
- **Differentiator 2:** the current rules are covered by the 87-hour announcement, the dated exam H2 with the "Exam day at a glance" box, the 2027 note, renewal and the reciprocity H2.
- **Differentiator 3:** barriers are covered by the ID H3, languages and dictionaries, and CORI with a legal-help pointer.
- **Structure:** the checklist, the 7-question box, the yes/no fit lists and the comparison box are all present.

### 13. Reader-first: PASS
There is no "we did not find" or "could not confirm", no percentiles, no statistics explanation, no BLS growth label and no "Not shown" cells. The SOC code appears only in the Sources section and in source comments. "The facts below come from the D&S candidate handbook dated May 2026" is the dating note the editorial decisions require.

### 14. Guideline 7 questions: PASS
- **Pay:** MA $46,680, national $42,260, "New CNAs often start lower."
- **Length:** 75 hours (87 announced), 29 of 37 programs under 12 weeks.
- **Cost:** tuition varies, ask for the full price; exam fees given. There is no neutral tuition range, which matches the brief.
- **Working while training:** evening and weekend classes, plus the 4-month earn-while-you-learn rule.
- **What you need to start:** ask about health tests, shots and background checks. The post correctly states no age or education rule.
- **State license:** "Yes."
- **Exam:** questions, time, passing score and cost.

### 15. Internal links: PASS
All 11 strategy targets are linked and exist: healthcare-jobs, phlebotomist, pharmacy-technician, free-job-training, masshire-training-voucher, wioa-eligibility, is-wioa-training-free, qualify, career-paths, student-financing, healthcare-careers. `related()` has 3 posts.

### 16. Community experiences: PASS
- **Quotes:** 3 quotes (the maximum): C1, C4 and C7. Each is word for word as in `community-insights.md` (only the apostrophes are typographic), and the meaning is kept.
- **Approved items only:** C1 drops "say every step out loud" and uses the handbook rule. C2 shows both sides and makes no enforceability or 12-month-stay claim. C3 has no stars claim and no ratio. C4 is paired with "Slow is normal. Unsafe is not." and the harder units / okay-to-leave line. C5 uses the BLS sentence verbatim plus the two-person-move paraphrase. C6 has no figures. C7 is paired with an equally weighted hard-side paraphrase and "personal experiences, not promises." C9 appears as questions only. C10 uses the verified dictionary and language rules.
- **Cut items:** C8 is absent. C11 is absent, and there is no "3 days".
- There are no usernames, links or identifying details, and nothing implies these people are CSC students.
- The attribution "As one CNA put it" / "One CNA summed it up" fits single-person quotes and Guideline 13. It was accepted in round 1.

## Fix list

**Required:** none.

**Recommended (minor, can ship as is):**
1. **`research-brief.md` Verified addendum:** add three handbook facts the post uses, copying them from `community-verification.md` (the exam-fees paragraph and C1.2):
   - "testing fees must be paid before you can schedule"
   - "Some training programs pre-pay testing fees"
   - you may tell the RN Test Observer you want to make a correction within the 40 minutes

   This is brief housekeeping only. The post does not change.
2. **"Three ways to pay" table, "Strings attached", column 1:** "Often a work contract." states a frequency that only community stories support. Consider "May come with a work contract. Read it before you sign."

**Optional:**
3. **Split long sentences:**
   - "Already a CNA in another state?": the waiver sentence (about 32 words). For example: "Did you finish an approved nurse aide course in another state, or a clinical course in an approved nursing school? You may be able to take the Massachusetts exam without repeating training."
   - "Free training and work contracts": "If you are told you owe money, call ... before you sign." Split into two sentences.
4. **Trim the DRAFT comment** to the open human checks.

**Before publishing (human, unchanged from round 1; already in the DRAFT marker):**
- Open the DPH 87-hour memo and the mass.gov nurse aide pages.
- Spot-check $46,680 at data.bls.gov/oes.
- Confirm the $70 skills fee on the D&S fee page.
- Settle the open pay-figure policy question (DRAFT item 0).

**For the director (outside this post):**
- `blog/healthcare-jobs-massachusetts.html` still says CNA training is "4 to 12 weeks" and "$500 to $2,000". No neutral source backs these.
- The strategy asks for reverse links to this post from the phlebotomist, pharmacy-technician and healthcare-jobs posts.
