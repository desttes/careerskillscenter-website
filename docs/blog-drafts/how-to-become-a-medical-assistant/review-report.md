# Review report: How to Become a Medical Assistant (nationwide)

Reviewed 2026-10-05. Slug: `blog/how-to-become-a-medical-assistant.html`. Scope: NATIONWIDE (check 19 applies).
Sources reviewed: the uncommitted `PAGES.append` block in `tools/build-pages.py` (`_htbma_faq`, `_htbma_body`, `_HTBMA_*`), the new BLOG_POSTS card, register row R-BLOG-06 in `docs/COURSE_CONTENT_REGISTER.md` (uncommitted), `blog/course-mode-copy/how-to-become-a-medical-assistant.md`, `research-brief.md`, `content-strategy.md`, `editorial-decisions.md` and `community-verification.md`. I built the site in a scratch copy (not in the repo). I used the generated HTML to count words and paragraph lengths and to parse the JSON-LD.

## Result: FAIL (4 checks; all are quick fixes, and none needs new research)

This is a strong post. It follows the strategy's angle closely, scope is correctly nationwide, pay is national, all community items are approved paraphrases with no quotes, and readability is about grade 6 (Flesch-Kincaid estimate 6.2, 12 words per sentence). Nothing appears invented. The four failures are:
- **Check 3:** about 20 figures (Fred Hutch, Kaiser, Allina, the three non-Massachusetts college prices, Washington fees, the "18 or older" rule) are verified on official pages in `community-verification.md` but are **not in `research-brief.md`**. This is the same procedural fail as the CNA round 1, with the same fix: a verified addendum.
- **Check 5:** three sentence fragments in `<p>` tags.
- **Check 14:** the Quick answer gives training time as "a few months to 2 years", but the brief has a concrete low end (about 8 weeks).
- **Check 18:** Kaiser Permanente Washington, Allina Health and Central Piedmont are named without saying when the facts are from or telling readers to check current enrollment.

Word count (check 17) is **2,746 visible words**, just under the 2,750 fail line. It passes, but there is no room left, so the fix list includes optional cuts.

## Check-by-check

| # | Check | Result |
|---|---|---|
| 1 | No CSC program details | PASS |
| 2 | No ETPL / WIOA approval / "state-approved" / Express claims | PASS |
| 3 | Every number is in the research brief with a source | **FAIL** (procedural) |
| 4 | "May qualify"; no funding promises | PASS |
| 5 | Plain language; paragraph shape | **FAIL** (3 fragments; all lengths OK) |
| 6 | DRAFT marker present | PASS (note) |
| 7 | CTAs and banned words | PASS (note) |
| 8 | COURSE-DEPENDENT markers + course-mode copy file | PASS |
| 9 | BlogPosting + FAQPage JSON-LD valid | PASS |
| 10 | No testimonials or invented outcomes | PASS |
| 11 | No facts from aggregators, sellers or career blogs | PASS |
| 12 | Follows strategy angle; differentiators are real sections | PASS |
| 13 | Reader-first | PASS |
| 14 | Answers the Guideline 7 reader questions concretely | **FAIL** (1 vague phrase) |
| 15 | Links to relevant existing posts | PASS |
| 16 | Community experiences match editorial decisions | PASS (1 minor) |
| 17 | Word budget (~2,500; fail above ~2,750) | PASS (borderline: 2,746) |
| 18 | Named programs: allowed type, facts match, dated, "check current enrollment" | **FAIL** |
| 19 | National credential: nationwide framing | PASS |

### 1. No CSC program details: PASS
CSC appears twice: "Career Skills Center does not sell medical assistant training, so we can be straight with you." and the allowed "plans to offer training in healthcare, IT and the skilled trades" line. Both are wrapped in R-BLOG-06 markers. There is no length, cost, format or credential.

### 2. No ETPL/WIOA/state-approved/Express claims: PASS
WIOA appears only as a link topic ("whether WIOA training is really free", "who may qualify for WIOA training"). "The state's training list" describes other programs. There is no Express mention, and no approval is claimed for CSC.

### 3. Numbers in the research brief: FAIL (procedural)
**In `research-brief.md` with a source (OK):** $45,690; $36,050; 13% over 10 years; 109,700 openings; "more than half" (56%) in doctors' offices; $42,260 and 3% (CNA); 8 months (Greenfield); 9 months and 245-hour practicum (Massasoit); 12 weeks + 3-week internship and Spring 2027 January/February (Quincy); 2,000 hours + 8 weeks (QCC/UMass Memorial); 6 credits (MassEducate); 560 / 160 / 1,000 hours and 10 shots / 10 blood draws (Alternative Pathway); 200 questions / 160 minutes, $125 / $250; 405 on 200-800, 69% ("about 7 in 10"); about 210 questions / 2 hours, $150, 4 tries / 45 days, 3-year renewal (RMA); 150 + 30 / 3 hours, $169, 2-year renewal (CCMA); 175 questions / 2 h 30 min, $139 (CMAC); 5-year (60-month) CMA renewal; CCMA 1 yr in 3 or 2 in 5; RMA 3 yrs in 7; "1 to 2 years" and "several months" on the job (BLS); associate degree 2 years.

**Not in `research-brief.md`; found only in `community-verification.md` (official pages, [opened]) and listed as usable in `editorial-decisions.md`:**
- Fred Hutch: Seattle, 2,000 paid hours, $4,850 tuition, 410 unpaid coursework hours, 2-year commitment, January 2027 cohort (Route A paragraphs 2-4).
- Kaiser Permanente Washington: 2,000 hours, 12 to 24 months, 288 class hours, 2-year commitment (Route A paragraph 5; route table "About 1 to 2 years").
- Allina Health: 1-year work commitment (Route A paragraph 6).
- Central Piedmont CC: about 2.5 semesters, $5,376 to $14,400 (Route B paragraph; route table "One example: $5,376 to $14,400"; "How much does it cost?" "$2,800 to $14,400").
- Community College of Philadelphia: $2,799, 180 hours, 8 weeks by day / 16 weeks by evening (Route C; route table "As short as about 8 weeks" and "$2,799 to $4,112"; "How long" "about 8 weeks").
- Anne Arundel CC: $4,112, 388 hours, 100-hour unpaid externship; 25 hours a week for 4 weeks, Monday to Friday ("Can you train while working?").
- Washington DOH: certified credential $145, registered credential $115.
- "Some programs require you to be 18 or older" (Kaiser and Fred Hutch pages, in community-verification only).
- "and a TB test" (Anne Arundel page, community-verification only). This is a fact rather than a number.

All of these have an opened official source and match it. None look invented. Under the strict rule they still fail because they are not in the brief. Fix: see Fix 1.

### 4. "May qualify"; no funding promises: PASS
"Public training money may help if you qualify", "MassEducate may cover ... for eligible students", "A MassHire Career Center may help pay if you qualify", and the CTA says "may qualify" twice. "Tuition often covered" and "Paid training often costs you nothing" describe employer programs, not public funding, and all three named employer programs do cover tuition.

### 5. Plain language and paragraph shape: FAIL (fragments only)
- Readability: Flesch-Kincaid estimate is about 6.2 and the average sentence is 12 words. Terms are defined in line (accredited, externship, vital signs, immunizations, certification, registered apprenticeship). "Medical assistant" is written in full, never "MA."
- Paragraph shape: I counted all **85 `<p>` elements** (lead, Quick answer box, body, CTA box, CSC line and FAQ answers). Every one has 1 or 2 sentences. The **longest is 188 characters** (the Massachusetts "The provider must be in the building..." paragraph). **None is over 210.**
- **Fragments (fail):**
  1. "Can you train while working?" section, first paragraph: "**Yes, for most of the training.** Many programs are hybrid..."
  2. End of "How hard is it?": "**Not sure this job is for you?** Explore our career paths."
  3. CTA box text (`post_cta` second argument): "**Live in Massachusetts?** Answer a few short questions..."
  4. (Borderline, optional) FAQ physician-assistant answer: "**No.** A physician assistant needs..."
- Accepted: "No state license required." is the wording Guideline 7 requires. "So when you get a job offer, ask these questions:" and "...read the group's own page before you pay:" are list lead-ins, which is the accepted site pattern.

### 6. DRAFT marker: PASS (note)
`<!-- DRAFT -- facts to verify: (1)...(11) -->` is the first thing in `_htbma_body`. It is long (about 20 lines) rather than "short", the same as the other role posts, and earlier reviews accepted that. The `[VERIFY: ...]` comments on the RMA question count, the CCMA test plan, the RMA renewal cycle and the mass.gov wording will also trip the pre-deploy grep, as intended. Optional: trim it.

### 7. CTAs: PASS (note)
- Certification next steps link to the certifying bodies: AAMA eligibility, AMT, NHA CCMA and AMCA CMAC pages, plus AAMA's CAAHEP/ABHES list and state-by-state page.
- Funding links to `qualify.html` (post_cta), placed after the Massachusetts funding paragraphs. MassHire appears only in the Massachusetts section.
- There is no "our program", "our courses", "enroll now" or "apply" CTA. Notes: "start **applying** before you finish" (first-job part) refers to job applications, and "Check current **enrollment**" is the phrase Guideline 7 and check 18 require. Neither is a CSC CTA. Optional reword for the first is in Fix 6 to avoid a literal match (the CNA round 1 failed on a literal "apply").

### 8. COURSE-DEPENDENT markers and course-mode file: PASS
There are two `<!-- COURSE-DEPENDENT: R-BLOG-06 -->` ... `<!-- /COURSE-DEPENDENT -->` blocks (intro honesty line, CSC plans line). The register row R-BLOG-06 exists, uncommitted, and describes both places. `blog/course-mode-copy/how-to-become-a-medical-assistant.md` exists and has guide-mode and course-mode versions of both lines, with the right guardrails (no CSC details, "may qualify", no accreditation claims).

### 9. JSON-LD: PASS
Both blocks parse as valid JSON in the built page. BlogPosting has the headline (matches H1), datePublished and dateModified 2026-10-05 (today, not backdated), Organization author "Career Skills Center", mainEntityOfPage and description. FAQPage has 5 Question/Answer pairs. Their text matches the visible FAQ, with HTML stripped.

### 10. No testimonials or invented outcomes: PASS
There are no quotes, reviews or outcome stats. Employer program facts come from the programs' own pages. Nothing suggests results are typical.

### 11. Source quality: PASS
All facts trace to BLS, the certifying bodies, Washington DOH, malegislature.gov, mass.edu, and official public college and employer program pages. The seller and aggregator figures the brief flags ($44,200, "96% of employers", "23% growth", seller exam prices, lead-gen directory prices for Massasoit and others) are not used. The Greenfield "my arithmetic" cost estimate is correctly left out.

### 12. Strategy angle and differentiators: PASS
- Hook: it opens on "pick your route, not a school", with the keyword in the first sentence, the paid route and the online-course trade-off, and the "we don't sell" line. It matches the strategy's direction.
- Differentiator 1, the "pick your route" table with certificate eligibility: this is the H2 centerpiece, with 4 rows plus an H3 for each route. The Alternative Pathway is covered with "currently", never "permanent".
- Differentiator 2, "How hard is it?" in four parts: it has its own H2 with H3s for the classes, the exam, the first job and the work. It gives the 69% pass rate and the fix for the first job.
- Differentiator 3, precise numbers and state rules: exact times, costs, exam facts, May 2025 pay and 2025-35 outlook, and a "Rules are different in some states" H2 that points to AAMA's state page.
- Minor gap (optional): the strategy's nationwide money pointer (American Job Center / local workforce board) is not in the post. Nationwide readers only get the WIOA explainer link. See Fix 7.

### 13. Reader-first: PASS
The visible text has none of: "we did not find", "could not confirm", "percentile", statistics explanations, SOC codes, BLS growth labels, "Not shown", a Sources section, "Source:" notes, "according to" or "BLS says". There are no links to government data pages. The external links are all certifying-body action pages. The research notes stay in HTML comments.

### 14. Reader questions: FAIL (one vague phrase)
- Pay: median $45,690 and entry level $36,050, national. OK.
- Training length: concrete by route (8 weeks; 8 months to 2 years; 1 to 2 years; associate 2 years; externship 100 hours / 25 hours a week; Fred Hutch and Kaiser hours). OK.
- Cost: concrete ($2,799, $4,112, $5,376 to $14,400; exam $125 to $250; tuition covered in paid programs). OK.
- Working while training: hybrid and evening classes; the daytime externship warning with a concrete example. OK.
- What you need to start: diploma/GED, no experience, background check, physical, shot records, TB test, CPR/BLS, 18+, and the criminal-record advice. OK.
- State license: "Most states have no license", the Washington exception, and "No state license required" for Massachusetts. OK.
- Exam: questions, time, fee for all four; passing score and pass rate for the CMA; retakes. OK.
- **Fail:** Quick answer step 3, "Train for **a few months** to 2 years, depending on the route." The brief and verification file have a concrete low end (about 8 weeks, CCP; 12 weeks + 3 weeks, Quincy), and the body itself says "about 8 weeks". This is the featured-snippet answer, so it should be concrete. Also vague, but less important: Route C "teach the basics in **a few weeks or months**" and FAQ "can start after **months of training**". See Fix 3.

### 15. Internal links: PASS
Links: `healthcare-careers.html`, `career-paths.html`, `qualify.html`, `blog/is-wioa-training-free.html`, `blog/masshire-training-voucher.html`, `blog/wioa-eligibility-massachusetts.html`, `blog/free-job-training-massachusetts.html`, `blog/can-medical-billing-coding-be-learned-online.html`, `blog/cna-massachusetts.html` (DRAFT) and `blog/phlebotomist-massachusetts.html` (DRAFT). There is also a `related()` block with 3 posts. All targets exist in the build. It correctly does not link to the old `blog/medical-assistant-massachusetts.html`. Note: the two draft targets must be re-checked at publish (already in the DRAFT marker, item 10).

### 16. Community experiences: PASS (1 minor)
I checked each item against `editorial-decisions.md`:
- C1: the wording "Some people are hired at the site where they did their externship. Others wait months for an employer who will take a beginner." is word for word. The Quick answer line "It can be the hardest step, so plan for it early" matches. Both sides are shown.
- C2: "Some people who were hired with no training were later told to get certified." plus the three job-offer questions. The official CCMA, RMA and CMA routes are correct. The dropped "6 months" claim is absent.
- C3/C4: only official program facts are used, with the trade-offs (commitment, few spots, unpaid coursework on your own time). The back-door line is a plain fact, and no "priority to staff" rule is stated. Mercy is not named.
- C5+C9: actions only ("read local job ads..."; "Check the job ads in your area to see which certificates employers ask for"). The pay quote is not used, and nothing claims employers "treat them all the same."
- C6: the wording matches word for word and shows both sides.
- C7: the advice to ask the nursing school, and "General classes, like English or biology, are the most likely to count." No blanket claim about transfers.
- C8: "Some students say you can't learn shots and blood draws through a screen", with the AAMA requirement nearby.
- There are no quotes, usernames, links or identifying details, and nothing implies these are CSC students. No AI, exam or class experiences are invented.
- **Minor:** "The first job" opens with "**For many people,** this is the hardest step." C1 approves "can be the hardest step." "For many people" adds a quantity the community round did not establish. See Fix 5.

### 17. Word budget: PASS (borderline)
Visible post text in the built page: **2,746 words**. That is the H1 (16) + the dek (26) + the body from the lead to the end of the FAQ (2,704), including the 2 tables (229), the Quick answer box, the CTA box and the FAQ (259). The "Related articles" cards (about 25 words) are excluded. This is about 250 words over the 2,500 target and just under the 2,750 fail line, so it passes. Any wording added by the fixes below must be offset by cuts. Optional cuts that would bring it to about 2,550 are in Fix 8.

### 18. Named programs: FAIL
- Types: all allowed. Fred Hutch, Kaiser Permanente Washington and Allina Health are employer programs. Central Piedmont, Community College of Philadelphia, Anne Arundel, Greenfield, Massasoit, Quincy College and Quinsigamond are public colleges. UMass Memorial is an employer. No for-profit sellers are named, and nothing suggests a CSC partnership.
- Facts: all match the official pages recorded in the brief and in community-verification. Fred Hutch is not called the "AAMA" CMA. Kaiser uses 12-24 months, not 12-15. Massasoit and Quincy are not said to lead to the CMA (AAMA).
- Dated + "check current enrollment" is present for: Fred Hutch (as of October 2026), CCP and Anne Arundel ("These prices are as of October 2026. Check current enrollment with the program."), and the Massachusetts list ("as of October 2026. Check current enrollment with each program.").
- **Missing for:**
  1. **Kaiser Permanente Washington** (Route A paragraph 5): no date, no "check current enrollment."
  2. **Allina Health** (Route A paragraph 6): no date, no "check current enrollment." Its only source is a **February 2025** news page with no hours, pay or start dates (community-verification C3 calls it "not enough for a current paid program example on its own"). Present tense ("covers tuition") reads as current, so it should be dated "as of early 2025."
  3. **Central Piedmont CC** (Route B): no date, no "check current enrollment." The "as of October 2026" line sits in Route C and covers only CCP and Anne Arundel.

### 19. Scope (national credential): PASS
The title, H1, title tag, meta description, slug (`how-to-become-a-medical-assistant`), dek, blog card and first paragraph contain no state. Pay is the national median and entry-level figure only, with no Massachusetts pay. Massachusetts appears only in the labeled "If you live in Massachusetts" H2, its two H3s, and the CTA box placed right after it. Washington and the out-of-state colleges are labeled examples. Exam and next-step links go to the certifying bodies.

## Fix list (in order)

**Fix 1 (check 3; director or researcher, no writer change needed).** Add a "Verified addendum (2026-10-05)" section to `research-brief.md`. Copy these items from `community-verification.md`, with their opened URLs:
- Fred Hutch (C3 / open item 3)
- Kaiser Permanente Washington (C3 / open item 3)
- Allina (C3)
- Central Piedmont, Community College of Philadelphia and Anne Arundel, including the 25 hours a week x 4 weeks externship and the TB test (open item 4)
- Washington $145 / $115 (open item 5)
- The 18+ age rule (Kaiser, Fred Hutch)
- The NHA $169 store page (open item 2), which upgrades the brief's SEARCH SUMMARY tag

Alternatively, cut those figures from the post, but that would gut Route A and the cost answer, so the addendum is the better fix.

**Fix 2 (check 18; writer).** Add a date and an enrollment line to three program paragraphs, and keep each paragraph at 2 sentences and at most 210 characters:
- Kaiser (Route A, paragraph 5): turn it into two paragraphs, or shorten. For example: "Kaiser Permanente Washington runs a similar paid program: 2,000 hours on the job over 12 to 24 months, plus 288 hours of classes." / "It asks for 2 years of work after (as of October 2026). Check current enrollment with the program."
- Allina (Route A, paragraph 6): "As of early 2025, Allina Health covered tuition and asked for at least 1 year of work in its clinics. Check current enrollment with the program." Move "Spots are few, and before you sign, ask what happens if you leave early." to its own paragraph or into the Kaiser paragraph.
- Central Piedmont (Route B): add "(as of October 2026)" after the price and a short "Check current enrollment with the college." sentence. Or move the Route C line "These prices are as of October 2026..." so that it clearly covers all three colleges. Splitting into two paragraphs keeps both under 210 characters.

**Fix 3 (check 14; writer).** Quick answer step 3: change "Train for a few months to 2 years, depending on the route." to "Train for about 8 weeks to 2 years, depending on the route." Optional changes:
- Route C first paragraph: "a few weeks or months" becomes "about 8 to 16 weeks in the examples below."
- FAQ physician-assistant answer: "after months of training" becomes "after as little as about 8 weeks of training."

**Fix 4 (check 5; writer).** Rewrite the fragments:
- "Can you train while working?": "Yes, for most of the training." becomes "**You can do most of the training while you work.** Many programs are hybrid, with classes online and labs in person, and some offer evening classes." (The second sentence is unchanged. Recount the characters: the paragraph must stay at or under 210.)
- End of "How hard is it?": "Not sure this job is for you? Explore our career paths." becomes "If you are not sure this job is for you, explore our career paths."
- `post_cta` text: "Live in Massachusetts? Answer a few short questions..." becomes "If you live in Massachusetts, answer a few short questions to see which funding options you may qualify for."
- Optional: FAQ "No. A physician assistant needs..." becomes "No, they are different jobs. A physician assistant needs a master's degree and a state license, and can diagnose and treat patients." Watch the 210-character limit.

**Fix 5 (check 16, minor; writer).** "The first job" H3: "For many people, this is the hardest step." becomes "This can be the hardest step."

**Fix 6 (check 7, optional; writer).** "start applying before you finish" becomes "start looking for jobs before you finish", to avoid a literal "apply" match.

**Fix 7 (check 12, optional; writer, only if words are cut elsewhere).** Add one nationwide money line in "How much does it cost?", for example: "Outside Massachusetts, a local American Job Center may help pay if you qualify." Only add it if the brief or addendum carries an official source (the strategy asked the researcher for dol.gov/CareerOneStop wording; it is not in the brief now). Otherwise skip.

**Fix 8 (check 17, optional cuts; writer).** Fixes 2 and 4 add about 30 words. To get back toward 2,500, cut repeats:
- Delete the second pay paragraph in "Pay, and is it worth it?" ("Most medical assistants earn around $45,690... $36,050"), since the Quick answer box already says it, or delete it from the box instead: about -17.
- Delete "How to become a medical assistant: pick your route first" paragraph 2 ("For example, a short online course can lead to the CCMA exam..."), since Route C paragraph 2 says the same: about -30.
- Delete or shorten the "How hard is it?" lead ("It takes real work... the work itself."): about -27.
- FAQ "Do you have to be certified...": cut the second paragraph (Washington is already covered in "Rules are different in some states"): about -18.
- FAQ "Medical assistant or CNA": drop the 13% vs 3% growth sentence, keeping the CNA link: about -16.
- Merge Route B paragraphs "You can look programs up on the CAAHEP and ABHES lists." and "The AAMA also currently accepts..." into one 2-sentence paragraph: about -5.
- "Help paying in Massachusetts", third paragraph: fold the two links into the MassHire paragraph or the related block: about -15.

**Optional accuracy notes (no fail):**
- Route table, College program row: "CMA (AAMA), RMA, CCMA or CMAC" applies to accredited or Alternative Pathway programs only. Consider "CMA (AAMA), RMA, CCMA or CMAC, if accredited". In the Massachusetts list, consider adding "ask whether it leads to the CMA (AAMA)" after Massasoit and Quincy, since their pages do not show CAAHEP (editorial-decisions, Massachusetts programs line).
- "Each one counts in any state.": true for national validity. Washington still requires its own state credential on top of the exam, and the next H2 covers that, so this is fine.

**Before publishing (human; already in the DRAFT marker):** confirm the RMA question count and 3-year renewal, the current NHA CCMA test plan, the mass.gov "not licensed" wording, and that the Fred Hutch, Kaiser and Allina programs are still enrolling. Re-check the CNA and phlebotomist draft links. Decide whether the old `blog/medical-assistant-massachusetts.html` redirects to this post.
