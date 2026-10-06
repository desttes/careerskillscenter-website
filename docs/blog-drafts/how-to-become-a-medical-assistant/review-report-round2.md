# Review report, round 2: How to Become a Medical Assistant (nationwide)

Reviewed 2026-10-05. Slug: `blog/how-to-become-a-medical-assistant.html`. Scope: NATIONWIDE (check 19 applies).
What I reviewed: the uncommitted `PAGES.append` block in `tools/build-pages.py` (`_htbma_faq`, `_htbma_body`, `_HTBMA_*`, lines about 7490-7863), the BLOG_POSTS card (line 3449), register row R-BLOG-06, `blog/course-mode-copy/how-to-become-a-medical-assistant.md`, `research-brief.md` (including the new "Verified addendum (director, 2026-10-05)"), `content-strategy.md`, `editorial-decisions.md`, `community-verification.md` and round 1 (`review-report.md`). I built the site in a scratch copy, not in the repo. I used the generated HTML to count words and paragraphs and to parse the JSON-LD.

## Result: FAIL (2 checks; both are small fixes)

All four round 1 failures are fixed (checks 3, 5, 14 and 18; details below). Cutting Allina left nothing orphaned. The two remaining failures are:
- **Check 3 (procedural):** The Community College of Philadelphia length, "about 8 weeks by day or 16 weeks in the evening", is not in `research-brief.md`. The addendum lists CCP's $2,799, 180 hours and optional externship, but not its length. The length appears only in `community-verification.md` (open item 4, opened page). This matters because "about 8 weeks" is now the post's shortest training time. It appears in the Quick answer, the route table, Route C, "How long" and the FAQ, and the figure comes from CCP. (Round 1 Fix 3 told the writer the brief had "about 8 weeks". That was my mistake: the figure was only in community-verification.)
- **Check 5:** The hero dek under the H1 (`<p class="page-hero-lede">`) has **3 sentences**. Round 1 counted the dek's words but did not check its paragraph shape, so this was missed then rather than caused by the edits.

Word count is **2,603 visible words** (round 1: 2,746). That passes.

## Check-by-check

| # | Check | Result |
|---|---|---|
| 1 | No CSC program details | PASS |
| 2 | No ETPL / WIOA approval / "state-approved" / Express claims | PASS |
| 3 | Every number is in the research brief with a source | **FAIL** (1 item, procedural) |
| 4 | "May qualify"; no funding promises | PASS |
| 5 | Plain language; paragraph shape | **FAIL** (hero dek has 3 sentences) |
| 6 | DRAFT marker present | PASS (note) |
| 7 | CTAs and banned words | PASS |
| 8 | COURSE-DEPENDENT markers + course-mode copy file | PASS |
| 9 | BlogPosting + FAQPage JSON-LD valid | PASS |
| 10 | No testimonials or invented outcomes | PASS |
| 11 | No facts from aggregators, sellers or career blogs | PASS |
| 12 | Follows strategy angle; differentiators are real sections | PASS |
| 13 | Reader-first | PASS |
| 14 | Answers the Guideline 7 reader questions concretely | PASS (round 1 fail fixed) |
| 15 | Links to relevant existing posts | PASS |
| 16 | Community experiences match editorial decisions | PASS (round 1 minor fixed) |
| 17 | Word budget (~2,500; fail above ~2,750) | PASS (2,603) |
| 18 | Named programs: allowed type, facts match, dated, "check current enrollment" | PASS (round 1 fail fixed) |
| 19 | National credential: nationwide framing | PASS |

### 1. No CSC program details: PASS
CSC appears only in the two R-BLOG-06 blocks: the intro honesty line ("does not sell medical assistant training") and the allowed "plans to offer training in healthcare, IT and the skilled trades" line. Neither gives a length, cost, format or credential.

### 2. No ETPL/WIOA/state-approved/Express claims: PASS
WIOA appears only as a link topic ("whether WIOA training is really free"). "Approved" appears only as "accredited (checked and approved) by CAAHEP or ABHES" and as Washington's "approved training". Neither refers to CSC. There is no Express mention.

### 3. Numbers in the research brief: FAIL (procedural, 1 item)
- **Now covered by the addendum:** Fred Hutch (2,000 hours, 410 hours, $4,850, 2 years, January 2027, 18+); Kaiser (2,000 hours, 12 to 24 months, 288 hours, 2 years, 18+); Anne Arundel ($4,112, 388 hours, 100-hour externship, 25 hours a week for 4 weeks); CCP ($2,799, 180 hours); Central Piedmont ($5,376 to $14,400, 2.5 semesters); NHA $169; CCMA and RMA work routes; Alternative Pathway 560/160/1,000/10/10; Washington $145/$115.
- **Already in the main brief (unchanged):** $45,690, $36,050, 13%, 109,700, "more than half" (56%), $42,260, the exam table, 405 on 200-800, 69% ("about 7 in 10"), 4 tries / 45 days, the renewals, the Massachusetts program facts, 6 credits, the associate degree's 2 years, "1 to 2 years" and "several months".
- **Derived figures I checked:** "$2,800 to $14,400" (rounded from $2,799 / $14,400), "$125 to $250" (covers all four exam fees), "8 months to a year" (Greenfield 8 months, Massasoit 9 months, MassBay two semesters). All OK.
- **Not in the brief:** "It runs about 8 weeks by day or 16 weeks in the evening" (Route C, CCP paragraph). The post's "about 8 weeks" low end rests on this figure. It appears in the Quick answer step 3, the route table row C ("As short as about 8 weeks"), the Route C first paragraph, the "How long" first paragraph and the FAQ physician-assistant answer. Its source is `community-verification.md` line 119: "Length: about 8 weeks (day) or about 16 weeks (evening)", from the opened ccp.edu page. The figure is verified and accurate. It fails only because it is not in the brief. See Fix 1.
- Non-number note (no fail): "a TB test" (What you need to start) and "Monday to Friday" are also only in community-verification (Anne Arundel). They could go into the same addendum line.

### 4. "May qualify"; no funding promises: PASS
"Public training money may help if you qualify", "MassEducate may cover ... for eligible students", "A MassHire Career Center may help pay if you qualify", and the CTA says "may qualify" twice. "Tuition often covered" and "Paid training often costs you nothing" refer to employer programs (Fred Hutch covers tuition; Kaiser and QCC/UMass Memorial pay apprentices).

### 5. Plain language and paragraph shape: FAIL (1 item)
- Readability is unchanged from round 1 (about grade 6, short sentences, terms defined in line).
- **Count:** There are **81 content `<p>` elements**, covering the lead, the body, the CTA box, the CSC line and the FAQ answers (the Quick answer box uses a list). Every one has 1 or 2 sentences. The **longest is 188 characters** (Massachusetts: "The provider must be in the building..."), and **none is over 210**.
- **Round 1 fragments are all fixed:** "You can do most of the training while you work." / "If you are not sure this job is for you, explore our career paths." / CTA "If you live in Massachusetts, answer a few short questions..." / FAQ "No, they are different jobs." "No state license required." is the wording Guideline 7 requires. The two list lead-ins ending in a colon follow the accepted pattern.
- **Fail:** the hero dek (`article()` third argument, line about 7861) is one `<p>` with 3 sentences (158 characters): "Some employers pay you to train. Some cheap courses limit which certificate you can take. Here are the four routes, with real times, costs and the hard parts." See Fix 2.

### 6. DRAFT marker: PASS (note)
`<!-- DRAFT -- facts to verify: ... -->` is the first thing in `_htbma_body`. It is updated for round 2: Allina is marked as cut, and the CCP "8 or 16 weeks" note is there. It is still long (about 20 lines), which earlier reviews accepted. The `[VERIFY: ...]` comments (RMA question count, CCMA test plan, RMA renewal, mass.gov wording) remain and will trip the pre-deploy grep, as intended.

### 7. CTAs: PASS
Certification links go to AAMA, AMT, NHA and AMCA, plus AAMA's accredited-program list and state-by-state page. Funding goes to `qualify.html`. There is no "our program", "our courses" or "apply". "Applying" was changed to "start looking for jobs" (round 1 Fix 6 done). "Enrollment" appears only in the required phrase "Check current enrollment with the program."

### 8. COURSE-DEPENDENT markers and course-mode file: PASS
There are two R-BLOG-06 blocks with closing markers. The register row R-BLOG-06 describes both places, and the course-mode copy file exists. The file does not mention Allina or other cut content.

### 9. JSON-LD: PASS
Both blocks parse in the built page. BlogPosting: the headline matches the H1, datePublished and dateModified are 2026-10-05, and the author is the Organization "Career Skills Center". FAQPage: 5 Question/Answer pairs, with HTML stripped from the visible FAQ text.

### 10. No testimonials or invented outcomes: PASS
There are no quotes, reviews or outcome stats.

### 11. Source quality: PASS
Every fact comes from BLS, the certifying bodies, Washington DOH, malegislature.gov, mass.edu, or official public-college and employer pages. The figures from sellers, aggregators and nursejournal are not used.

### 12. Strategy angle and differentiators: PASS
The hook is "pick your route, not a school", with the keyword in the first sentence. Differentiator 1, the route table plus an H3 for each route, is intact. Differentiator 2, "How hard is it?" in four parts, is intact. Differentiator 3, exact figures and state rules, is intact, including the "Rules are different in some states" H2. The repeated "pick your route" paragraph was cut (round 1 Fix 8), and the H2 still reads well. The nationwide money pointer (American Job Center) is still absent. This was optional in round 1 and is still not sourced in the brief.

### 13. Reader-first: PASS
The visible text has none of: "percentile", "according to", "BLS", "Source", "Not shown", "we did not find", "could not confirm", SOC codes or growth labels. "13% over the next 10 years" is a plain figure, not a BLS label. There is no Sources section and no links to government data pages.

### 14. Reader questions: PASS (round 1 fail fixed)
- Quick answer step 3 now reads "about 8 weeks to 2 years".
- Route C now reads "as little as about 8 weeks". The FAQ now reads "after as little as about 8 weeks of training".
- Pay (median plus entry level, national), cost (concrete examples plus exam fees), working while training (the externship of 25 hours a week for 4 weeks), what you need to start, state license (most states no, Washington yes, Massachusetts no) and exam facts are all concrete.
- "Several months on the job" is the BLS wording, and there is no more precise figure.

### 15. Internal links: PASS (no orphans)
Inline links: `healthcare-careers.html` (and `#interest`, which exists), `career-paths.html`, `qualify.html`, `blog/is-wioa-training-free.html`, `blog/masshire-training-voucher.html`, `blog/can-medical-billing-coding-be-learned-online.html`, `blog/cna-massachusetts.html` (DRAFT) and `blog/phlebotomist-massachusetts.html` (DRAFT). `wioa-eligibility-massachusetts.html` and `free-job-training-massachusetts.html` moved from the body into the `related()` block (5 cards). Every target exists in the build. The post still does not link to `blog/medical-assistant-massachusetts.html`.

Checks for references to cut content:
- "Allina" appears nowhere in the visible text or the course-mode file. It appears only in the DRAFT marker as "cut", which is correct.
- The "back door" paragraph (C4) remains. It is a general statement that does not depend on Allina.
- "The public college programs above" still refers to CCP, Anne Arundel and Central Piedmont, which are all still above it.
- "At one Maryland college" still matches Anne Arundel in Route C.
- No sentence refers to a 1-year commitment any more.

Both draft link targets still need a re-check at publish (DRAFT marker item 10).

### 16. Community experiences: PASS
"This can be the hardest step." now matches C1 (round 1 minor fixed). C1, C2, C4, C6, C7 and C8 are approved paraphrases, framed as experiences, with both sides shown where the experiences are mixed. C3 uses official program facts only and keeps the approved trade-offs: a 2-year work commitment, few spots, and unpaid coursework on your own time. C5 and C9 appear as actions only. There are no quotes, usernames or links, and nothing implies these people are CSC students.

### 17. Word budget: PASS
Visible text is **2,603 words**: H1, dek, and the body from the lead to the end of the FAQ, including the tables, boxes and CTA. The "Published / 11 min read" line and the Related cards are excluded. That is about 100 words over target and well under 2,750. Fix 2 should not add words.

### 18. Named programs: PASS (round 1 fail fixed)
- Kaiser: "As of October 2026, Kaiser asks for 2 years of work after the program. Check current enrollment with the program." The Kaiser page has no date, so "as of October 2026" (the date it was checked) is the right framing.
- Allina: cut from the post.
- Central Piedmont: "As of October 2026, it lists total costs of $5,376 to $14,400. Check current enrollment with the program."
- These were already dated and still are: Fred Hutch, CCP and Anne Arundel ("These prices are as of October 2026..."), and the Massachusetts list ("as of October 2026. Check current enrollment with each program.").
- Every named program is a public college or an employer program. The facts match the addendum and community-verification. No Massachusetts program is said to lead to the CMA (AAMA). The route table now says "if accredited" (optional round 1 note adopted).

### 19. Scope (national credential): PASS
The title tag, H1, meta description, slug, dek, first paragraph and blog card (line 3449) name no state. Pay is national only. Massachusetts appears only in the labeled H2 and its H3s, plus the CTA box after them. Washington and the out-of-state colleges are labeled examples.

## Fix list

**Fix 1 (check 3; director, no writer change needed).** In `research-brief.md`, "Verified addendum", add the CCP length to the Community College of Philadelphia line. For example:
"Community College of Philadelphia (PA), non-credit: $2,799, 180 hours, about 8 weeks (day) or about 16 weeks (evening), externship optional; 2026 start dates listed have passed." Source: https://www.ccp.edu/academic-offerings/professional-development/non-credit-courses/clinical-medical-assisting (opened 2026-10-05, community-verification open item 4).
Optional: add "TB test" and "Mon to Fri" to the Anne Arundel line. The other route would be to cut the CCP length from the post, but then the post's "about 8 weeks" low end would have no source, so the addendum is the right fix.

**Fix 2 (check 5; writer).** Rewrite the hero dek (`article()` third argument in the `PAGES.append` block) as 1 or 2 sentences. For example:
"Some employers pay you to train, and some cheap courses limit which certificate you can take. Here are the four routes, with real times, costs and the hard parts." (2 sentences, about 160 characters.) This matches the blog card excerpt at line 3451, which already joins the first two sentences.

**Optional (no fail):**
- Word budget: there are about 100 words to spare. If you want to get closer to 2,500, the FAQ "Will AI replace" second paragraph repeats the 13% figure from "Pay, and is it worth it?" (about -20 words).
- DRAFT marker: it could be trimmed, but that is not required.

**Before publishing (human; already in the DRAFT marker):**
- Confirm the RMA question count and 3-year renewal, the current NHA CCMA test plan and the mass.gov "not licensed" wording.
- Confirm that the Fred Hutch and Kaiser programs are still enrolling.
- Re-check the CNA and phlebotomist draft links.
- Decide whether `blog/medical-assistant-massachusetts.html` redirects to this post. Its blog card is still live at line 3454, so two medical assistant cards appear on the blog index.
