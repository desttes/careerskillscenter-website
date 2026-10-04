# Review report: How to Become a CNA in Massachusetts (cna-massachusetts)

Reviewed 2026-10-04. Source: uncommitted `PAGES.append` block in `tools/build-pages.py` (`_cna_faq`, `_cna_body`, lines ~6765-7170), `docs/COURSE_CONTENT_REGISTER.md` row R-BLOG-04, `blog/course-mode-copy/cna-massachusetts.md`. I built the site in a scratch copy (not in the repo) to check the HTML output, JSON-LD, blog card and sitemap.

## Result: FAIL (2 checks, both quick fixes; 14 checks pass)

The post is strong. It follows the angle, every community item matches `editorial-decisions.md`, and it reads at about a 5th-6th grade level (estimated Flesch-Kincaid 5.1, 11.6 words per sentence). The two failures are both strict-rule problems:
- **Check 3:** several exam and rule numbers are verified in `community-verification.md` but are not in `research-brief.md`.
- **Check 7:** the word "apply" is used for the reciprocity process.

## Check-by-check

| # | Check | Result |
|---|---|---|
| 1 | No CSC program details | PASS |
| 2 | No ETPL / WIOA approval / "state-approved" / Express claims | PASS |
| 3 | Every number is in the research brief with a source | **FAIL** |
| 4 | "May qualify"; no funding promises | PASS (2 minor wording fixes) |
| 5 | Plain language, about 8th grade | PASS |
| 6 | DRAFT marker present | PASS (note) |
| 7 | CTAs / banned words | **FAIL** (literal "apply") |
| 8 | COURSE-DEPENDENT markers + course-mode copy file | PASS |
| 9 | BlogPosting + FAQPage JSON-LD valid | PASS |
| 10 | No testimonials or invented outcomes | PASS (1 minor) |
| 11 | No facts from aggregators, providers or blogs | PASS |
| 12 | Follows strategy angle; differentiators are real sections | PASS |
| 13 | Reader-first (no research-process talk, percentiles, SOC in body, BLS labels, "Not shown") | PASS |
| 14 | Answers the Guideline 7 reader questions | PASS (note) |
| 15 | Links to relevant existing posts | PASS |
| 16 | Community experiences match editorial decisions | PASS (1 minor) |

### 1. No CSC program details: PASS
CSC appears in only two places: "Career Skills Center does not sell CNA training, so we can be straight with you." and the allowed "plans to offer training in healthcare, IT and the skilled trades" line. Both are marked R-BLOG-04. No length, cost, format or credential is given.

### 2. No ETPL/WIOA/state-approved/Express claims: PASS
WIOA appears only as a general funding route ("You may qualify through WIOA..."). "DPH-approved" and "approved by the state Department of Public Health" describe other people's programs, not CSC. No Express mention.

### 3. Numbers in the research brief: FAIL
These numbers are in `research-brief.md` with a source: $46,680, 3%, 2025-2035, 203,300, 36%/32%, 75/16 hours, 87/21 hours, April 2026, early 2027, 37/29/12 weeks, 60 questions/60 minutes/76%, 3-4 tasks/40 minutes, $30/$40/$70, 4/3 tries, 24 months/8 hours, 12 months, (617) 753-8144.

These are **not in the brief**:
- "up to 4 months (120 days)" (42 CFR 483.35(d)). Source: `community-verification.md` C2.5 [OPENED]. Not listed in `editorial-decisions.md` either.
- "at least 80% of the other steps" (handbook). Listed under C1 "Verified to use" in `editorial-decisions.md`.
- "$25 deposit" and "within 3 business days" (handbook). Same C1 list.
- "at least 20 minutes before your test" and the no-show/lose-fees rule. Source: `community-verification.md` "Check-in and no-shows" only.
- D&S phone "(888) 401-0462". Source: `community-verification.md` only.
- "D&S candidate handbook dated May 2026". The brief cites the 7.2024 handbook; May 2026 v7.0 comes from community-verification.

All of these have a sourced, opened official basis in `community-verification.md`. Nothing appears invented. Under the strict rule they still fail because they are not in the brief. The ID rules and Haitian Creole for the exam are facts rather than numbers, but they are also outside the brief, with the same source.

### 4. "May qualify"; no funding promises: PASS
"May qualify" is used in the table, the CTA, the checklist and the FAQ. Two minor wording risks:
- Table, column 2, "Cost to you": "Often $0 if you are approved". "Often" has no source and leans toward a promise.
- FAQ "Can I get CNA training for free": "the state must pay back part of your cost". The brief says how Massachusetts runs this reimbursement is not known. The body's "Ask DPH how the pay-back works" caveat is missing from the FAQ (and from FAQPage schema).

### 5. Plain language: PASS
The estimated grade level is about 5. There is a glossary at the top, and terms are defined (CORI, reciprocity, competency evaluation, clinical hours). About 10 sentences run over 25 words; the longest real one is the reciprocity waiver sentence (32 words). None blocks reading. Optional splits are in the fix list.

### 6. DRAFT marker: PASS (note)
`<!-- DRAFT -- facts to verify: ... -->` is at the top of `_cna_body` and renders in the HTML. It is long (12 items, about 16 lines) rather than "short", but it matches the phlebotomist and pharmacy posts. Optional: trim it.

### 7. CTAs: FAIL (wording only)
- Funding CTA goes to `qualify.html`, placed right after the "Three ways to pay" section. Correct.
- CNA is a state certification, not a national one, so pointing to DPH, the registry and D&S is correct. MassHire appears only in the funding context and in the "What to do this week" list (state-licensed career). Allowed.
- No "our program", "our courses" or "enroll".
- **"apply" appears 3 times**, all about the reader applying to the state for reciprocity:
  - FAQ 6: "you can apply for reciprocity" and "You apply online through D&S"
  - Body, "Already a CNA in another state?": "you can apply for reciprocity online through D&S"

  This is not a CSC CTA, but the rule bans the word in guide-mode copy, so swap it (see fixes).

### 8. COURSE-DEPENDENT: PASS
`<!-- COURSE-DEPENDENT: R-BLOG-04 -->` wraps both places (intro honesty line, CSC line after "What to do this week"). The register row R-BLOG-04 is added, and no other post uses that ID. `blog/course-mode-copy/cna-massachusetts.md` exists with guide and course versions for both places. The course-mode copy keeps "may qualify" and has no program details.

### 9. JSON-LD: PASS
In the built HTML, both blocks parse as valid JSON:
- BlogPosting: headline, datePublished 2026-10-04, author Organization "Career Skills Center".
- FAQPage: 6 questions that match the visible FAQ.

The blog index card (Oct 4, 2026) and the sitemap entry are generated. The publish date is today, not backdated.

### 10. No testimonials/invented outcomes: PASS (1 minor)
The only voices are the approved community items. No outcome stats. Minor: "This rule trips up many test takers, especially immigrants" (Bring the right ID) is an unsourced claim about how often this happens. The strategist wrote it as a gap note, and no source or community item backs it.

### 11. Source quality: PASS
Facts come from BLS, eCFR/Cornell, 105 CMR, the D&S handbook (the state's testing vendor), mass.gov, CMS and CareerOneStop. The provider tuition figure the brief rejected is not used, and no aggregator pay is used. Mass Legal Help is a referral link, not a fact source.

### 12. Strategy angle and differentiators: PASS
- **Hook:** the hook follows the strategy almost word for word (the money question first, the federal no-charge rule).
- **Differentiator 1:** "Three ways to pay" is an H2 with a comparison table, the fine print and a contracts H3.
- **Differentiator 2:** current rules are covered by the 87-hour announcement in the path and length sections, the exam H2 with the "Exam day at a glance" box, the 2027 note, renewal and the reciprocity H2. The "exam no longer free" item is left out, which is correct because the editorial decisions mark it unconfirmed.
- **Differentiator 3:** barriers are covered by the ID H3, languages and dictionaries in the exam box and study tips, and CORI. CORI is only a bullet in the hard-truth list, but the brief has almost nothing verified on CORI, so a bullet is right.
- **Structure:** the real-path checklist, the 7-question box, the "is this job for you" yes/no lists and the CNA vs. other jobs comparison box are all present.

### 13. Reader-first: PASS
There is no "we did not find" or "could not confirm", no percentiles, no statistics explanation and no BLS growth label ("expected to grow 3%... steady demand"). There are no "Not shown" cells. The table has complete data in every cell. The SOC code appears only in the Sources section at the bottom, which is allowed. "The facts below come from the D&S candidate handbook dated May 2026" is a dating note the editorial decisions require, not research-process talk.

### 14. Reader questions (Guideline 7): PASS (note)
- **Pay:** $46,680 (MA median) plus "New CNAs often start lower."
- **Training length:** 75 hours minimum, 87 announced, 29 of 37 programs under 12 weeks, plus the timeline note.
- **Training cost:** tuition varies by school; ask for the full price. The brief has no neutral tuition range, so this is the right handling. Exam fees are given.
- **Working while training:** "Can you do it while working?" covers evening and weekend classes and the 4-month earn-while-you-learn rule.
- **What you need to start:** "ask what health tests, shots and background checks they need". This is correct because the brief forbids stating an age or education rule.
- **State license:** "**Yes.**", with the certification vs. license explained.
- **Exam:** questions, time, passing score and cost are all there.

Note: Guideline 6/7 asks for the *national* median. The post gives only the MA median. Optional: add the national $42,260 (in the brief), as the phlebotomist post does, or keep MA-only on purpose and note it in the DRAFT comment.

### 15. Internal links: PASS
All 11 strategy links are present and exist in `build-pages.py`: healthcare-jobs, phlebotomist, pharmacy-technician, free-job-training, masshire-training-voucher, wioa-eligibility, is-wioa-training-free, qualify, career-paths, student-financing, healthcare-careers. `related()` has 3 posts.

### 16. Community experiences: PASS (1 minor)
- **Quotes:** 3 quotes, which is the maximum. C1, C4 and C7 are each word for word as in `community-insights.md`, and the meaning is kept.
- **C1:** the "say every step out loud" tip is dropped and replaced with the handbook rule. Hand washing is not called the first step. The tips are dated to the May 2026 handbook. "View Failed Steps", the $25 deposit and 3 business days are used as verified.
- **C2:** both sides are shown (owed nothing vs. 1-2 year contracts with payback threats). The post does not say payback clauses are unenforceable, and does not present 12 months as a minimum stay. It says to ask in writing and to call DPH or legal aid before signing.
- **C3:** no quote, no 3-star claim and no ratio number. Care Compare is described as showing separate ratings for inspections, staffing and quality.
- **C4:** the quote is paired with "Slow is normal. Unsafe is not." and the harder units / okay-to-leave line.
- **C5:** the BLS sentence is used verbatim, plus the two-person-move paraphrase. The "hide back pain" tip is not used.
- **C6:** shift length, weekends, night pay and saying no. No figures.
- **C7:** the quote is paired with a paraphrase of the hard side and the purpose / workplace-matters side, with no pay or bonus figures. The "These are personal experiences, not promises" line is good.
- **C9:** used as questions only, plus the DPH-list check. No MA requirement claim and no dollar amounts. The scam story and SNAP are left out.
- **C10:** the verified dictionary and language rules, including "can't switch back to English". No English-level claim.
- **Cut items:** C8 is absent. C11 is reflected only through the official reciprocity facts, with no "3 days".
- No usernames, links or identifying details. Nothing suggests these people are CSC students.
- Minor: `editorial-decisions.md` says "Attribute as 'CNAs say…'". The quotes use "As one CNA put it" / "One CNA summed it up". That is accurate for single-person quotes and matches Guideline 13's example, so it is acceptable. Flagged so the director can confirm.

## Fix list

**Required (to pass):**
1. **Check 3: bring the out-of-brief numbers into the brief, or cut them.** The best fix is for the director or researcher to add a short "Verified addendum" to `research-brief.md` that copies these items with their [OPENED] sources from `community-verification.md`. Nothing needs to be re-researched.
   - 42 CFR 483.35(d) 4 months / 120 days
   - Handbook May 2026 v7.0: 80% non-critical steps; $25 Test Review deposit within 3 business days; arrive 20 minutes early or no-show and lose fees; D&S (888) 401-0462; ID rules; exam languages including Haitian Creole; dictionary rule; "Some training programs pre-pay testing fees"

   Otherwise, remove these numbers from `_cna_body`:
   - "How long does CNA training take", "Can you do it while working?" paragraph (4 months / 120 days)
   - "Why people fail the skills test" (80%, $25, 3 business days)
   - "Exam day at a glance" (20 minutes)
   - "Bring the right ID" (phone)
2. **Check 7: replace "apply" (3 places).**
   - FAQ 6 (`_cna_faq`, last entry): "you can apply for reciprocity" becomes "you can ask for reciprocity". "You apply online through D&S Diversified Technologies" becomes "You do this online through D&S Diversified Technologies".
   - Body, "Already a CNA in another state?": "you can apply for reciprocity online through D&S" becomes "you can request reciprocity online through D&S".

**Recommended (minor):**
3. **FAQ "Can I get CNA training for free":** after "the state must pay back part of your cost", add "Ask DPH how this works in Massachusetts." This keeps the FAQ and schema in line with the body and the brief's "how MA pays: not found".
4. **Table "Cost to you", column 2:** change "Often $0 if you are approved" to "May be $0 if you qualify".
5. **"Bring the right ID" opening:** replace "This rule trips up many test takers, especially immigrants." with something like "Check this rule early, especially if your ID is from another country." This removes an unsourced claim.
6. **DPH phone in body:** the "Free" training and work contracts paragraph has "(617) 753-8144" without an inline `<!-- [VERIFY: ...] -->`. The number is a mass.gov search-summary fact, and the editorial decisions say mass.gov facts keep [VERIFY] markers. Add one next to it. It is listed in the DRAFT comment, item 5.
7. **Hard truth, "Background checks" bullet:** "A MassHire Career Center can point you to free legal help about your record" is not in any source. Replace it with a direct pointer to Mass Legal Help (already linked in the post), or cut it.
8. **"How long does CNA training take", paragraph 2:** "Employers also need time for background checks and health tests when they hire you." Pre-hire health tests are UNVERIFIABLE (community-verification C9.1). Soften to "Employers may also need time for background checks and other hiring steps."
9. **Optional:** add one sentence with the national median ($42,260, BLS May 2025) per Guideline 6.3/7, or note in the DRAFT comment that MA-only is deliberate.
10. **Optional:** split the two longest sentences:
    - The table "You pay first" cell (31 words)
    - The reciprocity waiver sentence (32 words)

**For the director (outside this post, do not edit here):**
- `blog/healthcare-jobs-massachusetts.html` still says CNA training is "4 to 12 weeks" and "$500 to $2,000". There is no neutral source for these (content-strategy consistency watch). This post does not repeat them, but the older post conflicts with the brief.
- The strategy asks for reverse links to this post from the CNA boxes in the phlebotomist, pharmacy-technician and healthcare-jobs posts.
- Human checks before publishing (already in DRAFT marker): open the DPH 87-hour memo and the mass.gov nurse aide pages, spot-check $46,680 at data.bls.gov/oes, confirm the $70 skills fee on the D&S fee page, and settle the open pay-figure policy question.
