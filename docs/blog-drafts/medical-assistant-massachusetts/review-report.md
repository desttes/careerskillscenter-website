# Review report: How to Become a Medical Assistant in Massachusetts

- Post: `blog/medical-assistant-massachusetts.html` (source: `_ma_faq` / `_ma_body` / `PAGES.append` block in `tools/build-pages.py`, right after the CNA block)
- DRAFT_DIR: `docs/blog-drafts/medical-assistant-massachusetts/`
- Reviewed: 2026-10-05, against CLAUDE.md, `docs/BLOG_WRITING_GUIDELINES.md`, `research-brief.md`, `content-strategy.md`, `community-verification.md`, `editorial-decisions.md`, and Emilio's 2026-10-05 decisions (one national BLS pay number, easy stats OK, no sources in the body, no named schools/programs/employers, 1-2 sentence paragraphs of at most 210 characters, no visible byline, never "MA" for medical assistant).
- Method: read the uncommitted diff of `tools/build-pages.py` and the three sibling HTML diffs. Parsed the generated HTML: character and sentence counts for every `<p>`, JSON-LD parsing, link-target checks, and greps for banned wording.

## Result: FAIL (small fixes only)

The post is close. It follows the angle well and has no CSC program details, no approval claims, no funding promises and no sources on the page. It fails on four fixable points:
1. One sibling-post edit breaks the paragraph rule.
2. The "what you need to start" answer is missing.
3. Some unconfirmed facts have no inline VERIFY comment.
4. A few community items are worded more firmly than the approved soft wording.

There are also two small accuracy fixes: "doctor or nurse" in the shot rule, and "practice questions" for the CCMA.

---

## Checks

### 1. No CSC program details: PASS
The only CSC lines are the intro honesty line ("does not sell medical assistant training") and "plans to offer training in healthcare, IT and the skilled trades. Get updates when we launch." Neither gives a length, cost, credential, format or date.

### 2. No ETPL / WIOA / "state-approved" / Express claims: PASS
ETPL and WIOA appear only as neutral reader guidance: the checklist question "Is the program on the state's list of eligible training programs (ETPL)?" and the MassHire/WIOA funding section. "state-approved" appears once, about CNA programs ("At least 75 hours in a state-approved program"), not about CSC. "Express" appears only in the shared footer nav.

### 3. Every number is in the research brief with a source: PASS (one wording fix)
Every number checks out against the brief: $45,690; 13%; 109,700; "more than half" (56%); 200 questions / 160 min; 210 / 2 h; 150 + 30 / 3 h; $125/$250, $150, $169; renewals of 5/3/2 years; "about 7 in 10" (69%); 720 / 160 hours; "3 years in the last 7"; "5 years"; "1 year in the last 3"; "about 8 months"; "about 12 weeks"; "6 credits"; "75 hours"; CNA 3%. The felony facts come from `community-verification.md` Q1, opened, and editorial-decisions approves them as official facts.
- The CCMA table cell calls the 30 extra items "practice questions." The brief says "pretest items." These are unscored questions mixed into the real exam, not practice questions. Fix 5.
- "Remote jobs that do exist are usually office work" and the AI paragraph are the Writer's own reasoning. The brief allows this only if it is labeled as reasoning or left out. "No one can say for sure" frames the AI part acceptably. The remote line is acceptable but stated flatly; this is optional softening only (Fix 11).
- "Often several thousand dollars at a public college" (table and FAQ) rests on one college's tuition math ($7,700-$8,900). "Often" generalizes from a single data point. Fix 10, minor.

### 4. "May qualify"; no funding promises: PASS
"may qualify" or "if you qualify" is used in MassHire, MassEducate ("eligible students may get"), the FAQ, the CTA block and "What to do this week." Nothing promises approval. No funding caps or rates are hard-coded.

### 5. Plain language; paragraph shape: PASS for the post (sibling FAIL, see Sibling edits)
- All 76 body `<p>` elements (lead, notes, CTA, CSC line) and all 12 FAQ answer paragraphs are 2 sentences or fewer and at most 210 visible characters. The longest is 184 characters (the article dek); the longest body paragraph is 181 characters (intro CSC line).
- Short label lines ("Patient care tasks can include:", "This job may fit you if:") are list lead-ins, which is accepted site pattern.
- "No state license required." is the wording Guideline 7 prescribes, so it is accepted.
- "Mostly no, because patient care is done in person." is a borderline fragment. Optional rewording in Fix 11.
- Reading level is about 8th grade. Terms are defined in "Words to know" (accredited, externship, vital signs, CORI, immunization), and medical assistant is set apart from physician assistant.
- No "MA" abbreviation for medical assistant anywhere in the body. The only "MA" hits are "Quincy, MA" in the shared footer.

### 6. DRAFT marker present: PASS
`<!-- DRAFT -- facts to verify: ... -->` is at the top of the post body. It is long (13 items), not "short," but it is an HTML comment and invisible to readers. The pre-deploy grep will catch it, as intended.

### 7. CTAs: PASS (one optional wording fix)
- Certifications point to AAMA, AMT and NHA eligibility pages, plus the AAMA page that links to the CAAHEP/ABHES lists.
- Funding points to `qualify.html` through `post_cta`.
- MassHire appears only in the funding section and in "What to do this week" (help paying). It is not the primary CTA.
- No "our program," "our courses," "enroll now" or "apply" in CTA copy.
- One literal "enroll" appears in ordinary reader advice, not a CSC CTA: "ask the college whether the credits count toward nursing before you enroll." To keep the banned-word grep clean, change it to "before you sign up" (Fix 9, optional).

### 8. COURSE-DEPENDENT markers and course-mode file: PASS
Both CSC blocks are wrapped in `<!-- COURSE-DEPENDENT: R-BLOG-05 -->` … `<!-- /COURSE-DEPENDENT: R-BLOG-05 -->`: the intro honesty line and the plans-to-offer line after "What to do this week." Register row R-BLOG-05 in `docs/COURSE_CONTENT_REGISTER.md` describes exactly these two places, the `healthcare-careers.html#interest` target (the anchor exists), and the switch `COURSES_LIVE.healthcare`. `blog/course-mode-copy/medical-assistant-massachusetts.md` exists and matches word for word in guide mode. Its course-mode copy keeps "may qualify" and forbids accreditation or certification claims about a future CSC course.

### 9. BlogPosting and FAQPage JSON-LD: PASS
Both blocks parse as valid JSON.
- BlogPosting: headline equals the H1; author is the Organization "Career Skills Center"; datePublished and dateModified are 2026-10-05 (today, not backdated).
- FAQPage: 6 Q&As that match the visible FAQ text.
- No visible byline (`author=None`), as Emilio wants.

### 10. No testimonials or invented outcomes: PASS
No quotes and no outcome stats. "These are personal experiences, not promises about any job" frames the community section.

### 11. No facts from salary aggregators, training providers or career blogs: PASS
All facts trace to BLS, the statute, the certifying bodies, mass.edu, and public-college and employer pages about their own programs (as the brief records). None of the competitor claims the strategy lists as off-limits ($17-$32/hr, 81%, "4 months," etc.) appears.

### 12. Follows the strategy's angle; differentiators are real sections: PASS
- The hook matches the strategy almost word for word ("Most guides … start with a list of schools. Start here instead." then paid training, then school choice decides certification).
- Differentiator 1: the "Three ways to become a medical assistant" H2 has a table with the employer route first.
- Differentiator 2: the "CMA, RMA or CCMA" H2 plus "The one state rule: giving shots" H3 and the "Before you pay" checklist H2.
- Differentiator 3: the "The hard truth: getting hired and staying" H2 covers hiring, why people leave and stay, AI, remote work, "worth it," and a 5-row medical assistant vs CNA table.
- The four positives from editorial-decisions correction 5 are kept: growth and openings, many like their work, hybrid works, concrete steps.
- Specialties are skipped, which the brief allows.

### 13. Reader-first, no sources or complexity: PASS
None of these appear: "we did not find," "could not confirm," percentiles, statistics explanations, SOC codes, BLS growth labels, "Not shown" cells, a Sources section, "Source:" notes, or "according to" / "BLS says." The growth line is plain ("expected to grow 13% over the next 10 years"). External links are action links only (certifying bodies, accredited-program lists, JobQuest, MassHire locations). There are no government data pages.

### 14. Answers the Guideline 7 reader questions: FAIL
| Question | Covered? |
|---|---|
| Pay | Yes, one national number, $45,690. No Massachusetts figure and no CNA vs medical assistant dollar comparison (the CNA table has no pay row). Matches `healthcare-jobs-massachusetts.html` ($45,690). |
| Training length | Yes (route table, "How long does it take?", FAQ) |
| Training cost | Yes ("several thousand dollars at a public college", "prices vary"; exam fees in the table) |
| Working while training | Yes (hybrid, evening classes, daytime unpaid externship, paid employer route) |
| What you need to start | **Partly.** "High school diploma or GED" appears only inside the CNA comparison and the CCMA table row; CORI appears in the criminal-record section. The brief's entry requirements (physical exam and immunization records for college programs; employers may require CPR/Basic Life Support) are nowhere in the post. There is no single place that answers "what do I need to get started?" |
| State license yes/no | Yes, "No state license required." |
| Exam facts | Yes (questions, time, cost, first-try pass rate for the CMA) |

### 15. Links to relevant existing posts: PASS
In-body links: `healthcare-jobs-massachusetts`, `cna-massachusetts`, `phlebotomist-massachusetts`, `pharmacy-technician-massachusetts`, `free-job-training-massachusetts`, `masshire-training-voucher`, `wioa-eligibility-massachusetts`, `is-wioa-training-free`, `qualify.html`, `career-paths.html`, `student-financing.html`, `healthcare-careers.html` (and `#interest`). `related()` lists CNA, healthcare jobs and free job training. All targets resolve to existing generated files. The blog index card is added at the top of `BLOG_POSTS`. The sitemap is handled automatically, and the build keeps draft posts out of it.

### 16. Community experiences: FAIL (soft-wording fixes)
- **Only approved items, and nothing else: PASS.** C1 (first job is hardest, plus the other side; in Quick answer and opening the hard truth), C2 (externship site, classmate, contact; plus "Tell people you know"), C3 (no hands-on practice, with the official certification facts; plus checklist items 1 and 3), C4/C5 (leave and stay, both sides, no ratings or community pay numbers), C6 (CNA first if nursing is the goal; credits phrased as a question to ask the college), C7 (job varies by office plus the interview question). None of the CUT items appear: no "9 months," no CMA-over-CCMA preference, no bilingual or phlebotomy claim, no AG case, no new-hire pay stories.
- **No quotes: PASS.** The only quoted line is the suggested interview question "What would I do on a normal day?", which editorial-decisions supplies as wording, not a community quote.
- **No usernames, links or identifying details; no implication of CSC students; mixed views shown: PASS.**
- **Soft wording: FAIL.** The director asked for "some people say" / "many people who started say." These lines are stronger than that:
  - "What is a medical assistant?" paragraph 7: "**Medical assistants say** the job can change a lot from office to office." This presents a C7 experience as something all medical assistants say.
  - "Medical assistant or CNA?" after the table: "A medical assistant job is often daytime clinic work **and easier on the body**." The C6 "easier on the body" claim is stated as fact, outside the "some people say" frame of the sentence before.
  - Hard truth paragraph 3: "**people say** more doors open after that first job." Missing "some."
  - "Why people leave" paragraph 2: "People who want much more money often go back to school for nursing." This is C4 stated as fact. It is acceptable because the next paragraph and the disclaimer frame the section, but it is safer with soft wording.

---

## Extra checks requested by the director

### Sibling-post link additions (healthcare-jobs, phlebotomist, CNA): FAIL (one paragraph)
- **Nothing else changed: PASS.** Each diff (source and generated HTML) adds only a link sentence or paragraph. Generated HTML uses `../blog/...` paths, and the target exists.
- **CNA:** new paragraph "Thinking about a medical assistant job instead? Read how to become…" has 2 sentences and about 105 characters. OK.
- **Phlebotomist:** paragraph now has 2 sentences and about 140 characters. OK.
- **Healthcare jobs: FAIL.** The "2. Medical assistant" paragraph now has **3 sentences and 247 visible characters**: "A medical assistant works in a doctor's office or clinic. You check patients in, take vital signs (like blood pressure), help the doctor during exams and do some office work. Read more in our guide to becoming a medical assistant in Massachusetts." It was 2 sentences before; the added sentence broke the rule. Fix 1.
- Consistency note, not a fail: `healthcare-jobs-massachusetts.html` still says "Medical assistants often train for about 1 to 2 years." The new post says "a few months to 2 years." The strategy asked that this be flagged to the director rather than repeated. Fix 12.

### VERIFY comments next to every unconfirmed fact: FAIL (gaps)
Present (9 inline): no state license; shot rule; employer pays hourly plus tuition (in "Three ways"); CMA exam format; CMA fees; RMA exam format; CCMA format; CCMA fee; renewal cycle; CMA pass rate; NHA felony rule.
Missing inline VERIFY, where the same unconfirmed fact appears again:
- Intro paragraph 2: "Some Massachusetts health centers **and hospitals** will pay you while they train you." Current enrollment is not confirmed (community-verification: NeighborHealth cohort status not shown; MGB is a 404). It is also the post's headline promise.
- "Employer-paid training" paragraph 1: "Some Massachusetts health employers pay you while you train and also cover tuition." Same fact, no VERIFY.
- Three-ways table, "Cost to you" for the employer route ("Often no tuition, and you are paid while you learn"). Same fact.
- "Often several thousand dollars at a public college" (table). It is only in DRAFT item 9.
- FAQ answers repeat the CMA pass rate, exam formats, the shot rule and the cost line with no inline VERIFY. The FAQ is built from a Python list, so a comment can't go inside the answer. The DRAFT header covers these, so this is acceptable. A Python comment above `_ma_faq` noting "FAQ repeats facts VERIFY-flagged in the body" would make it explicit (optional).

### Shot / immunization statement matches the verified brief: PASS with one accuracy fix
These match MGL c.112 s.265 as opened:
- "A primary care office may let a medical assistant give shots only if that person finished an accredited program."
- "The program must be accredited by CAAHEP or ABHES, or approved by the state health department."
- "must be in the building and ready to help" (statute: "present in the facility and immediately available").
- The post correctly avoids saying medical assistants can or cannot draw blood, and says other tasks depend on the employer.
- **Fix:** "A **doctor or nurse** must be in the building" (body) and "a doctor or nurse supervises you" (FAQ). The statute lets a licensed *primary care provider* delegate and supervise. The brief notes a separate DPH advisory for *nurse practitioners/APRNs*. A plain "nurse" (an RN) is not a primary care provider, so a reader could misread who can supervise. Use "a doctor or nurse practitioner" (or "your primary care provider"). Fix 4.

### Certification eligibility facts: PASS with one clarity fix
- **AAMA CMA needs an accredited program.** Table: "Students and graduates of a CAAHEP- or ABHES-accredited program, plus a few other routes." Body: "the CMA needs an accredited program. A short program that is not accredited will generally not get you there." Matches the brief, including the Alternative Pathway via "a few other routes."
- **RMA routes.** Accredited program with 720 hours including 160 externship hours; or 3 years of work in the last 7; or military. Matches AMT, opened. The hybrid and instructor routes are omitted, which is fine.
- **CCMA routes.** Matches NHA in substance. However, "High school diploma or GED plus a training program in the last 5 years; or 1 year of supervised work in the last 3" reads as if the work route needs no diploma/GED. NHA requires the diploma/GED for both routes. Fix 6.
- **"two of the three main certifications require hands-on training":** CMA (accredited program with hands-on skills) and RMA (160 externship hours). Correct per the brief and C3.
- **Felony wording is case-by-case.** "It is not an automatic ban, because each case is reviewed one by one." "For the CMA, a drug-related conviction can block a waiver." "For the CCMA, check with NHA." This matches the AAMA waiver form (Rev 4-25, opened) and the AMT checklist (opened). It does not say NHA has no rule. It does not frame the felony issue as CMA-only (the CMA and RMA are named together). PASS.

### "Is the school licensed?" checklist line: PASS
"Is the school licensed, and is the program accredited by CAAHEP or ABHES?" is a question for the reader to ask. It makes no claim about which agency licenses schools or that every school must be licensed. editorial-decisions (C9, CUT row) keeps exactly this advice: "check the school is licensed, get the full price in writing … already goes in the checklist." community-verification Q4 recommends it as a checklist line without a news hook. No VERIFY is needed. Optional: public community colleges are accredited rather than "licensed," so some readers may find the question odd there. Leaving it as is remains acceptable.

### No named schools, programs or employers: PASS
No college, employer or private school is named. NeighborHealth, QCC/UMass Memorial, MGB, Quincy College, GCC and MassBay are all absent. Named bodies are only accreditors (CAAHEP, ABHES), certifying bodies (AAMA, AMT, NHA), MassEducate, MassHire and JobQuest (state services).

### Pay rules (Emilio 2026-10-05): PASS
One national number ($45,690) in the Quick answer and the pay H2, plus "New medical assistants often start lower." No Massachusetts pay, no hourly figure, no percentiles, and no CNA dollar figure in this post.

---

## Fix list (numbered; what to change and where)

1. **`tools/build-pages.py`, `_hcj_body`, "2. Medical assistant" paragraph (247 chars, 3 sentences).** Move the link into its own paragraph. Keep "A medical assistant works in … office work." as is and add a new `<p>`: "Read more in our <a href="blog/medical-assistant-massachusetts.html">guide to becoming a medical assistant in Massachusetts</a>." Rebuild.
2. **Add a "What you need to start" answer (check 14).** Suggested spot: right after the "Three ways" table or as the first paragraphs of "How long does it take?". Two short paragraphs, all from the brief:
   - "To start, you usually need a high school diploma or GED. College programs may also ask for a background (CORI) check, a physical and your shot records."
   - "Some employers also want CPR (Basic Life Support) certification. Ask each program and employer what they need."
   Each must stay at most 210 characters and 2 sentences. Consider adding the same as a short FAQ item, or folding it into an existing FAQ answer.
3. **Add inline VERIFY comments** next to the paid-employer-training statements:
   - intro paragraph 2 ("Some Massachusetts health centers and hospitals will pay you…")
   - the "Employer-paid training" first paragraph
   - the employer column "Cost to you" cell
   - the "Often several thousand dollars at a public college" cell
   Use e.g. `<!-- [VERIFY: paid MA trainee programs, employer page opened 2026-10-05, current enrollment not confirmed] -->` and `<!-- [VERIFY: one college's 2026-27 tuition math only] -->`.
4. **Shot rule: "doctor or nurse" is too broad.** In the body ("A doctor or nurse must be in the building and ready to help.") and the FAQ answer ("a doctor or nurse supervises you"), change "doctor or nurse" to "doctor or nurse practitioner" (or "your primary care provider"). Also check "Other tasks depend on the employer and the supervising doctor or nurse." It is less critical because it does not state the statute, but keep it consistent.
5. **CCMA table cell:** change "150 scored questions plus 30 practice questions, 3 hours" to "150 scored questions plus 30 unscored questions, 3 hours".
6. **CCMA eligibility cell:** make clear the diploma/GED applies to both routes, e.g. "High school diploma or GED, plus a training program in the last 5 years or 1 year of supervised work in the last 3".
7. **Soft wording, "What is a medical assistant?":** change "Medical assistants say the job can change a lot from office to office." to "Some medical assistants say the job changes a lot from office to office."
8. **Soft wording, "Medical assistant or CNA?" (after the table):** keep the C6 claim inside the experience frame, e.g. "If nursing is your goal, some people say a CNA is a more direct first step. They also say a medical assistant job is easier on the body." (That is 141 characters; it drops "often daytime clinic work". If you keep it, check the 210 limit.) In "The hard truth" paragraph 3, change "people say more doors open" to "some people say more doors open." Optional: change "People who want much more money often go back to school for nursing." to "Some who want much more money go back to school for nursing."
9. **Optional:** change "before you enroll" (CNA section, credits-toward-nursing line) to "before you sign up" so the banned-word grep for "enroll" stays clean.
10. **Optional (accuracy of "often"):** in the three-ways table and FAQ answer 5, change "Often several thousand dollars at a public college" / "often costs several thousand dollars" to "can cost several thousand dollars," since it rests on one college's figures.
11. **Optional:** "Can you work from home?" Change "Mostly no, because patient care is done in person." to a full sentence, e.g. "Most of this job is done in person, because it involves patient care." Optionally soften the second sentence to "Remote jobs, when you find them, are usually office work like scheduling or records."
12. **Note for the director (do not change in this post):** the training length in `healthcare-jobs-massachusetts.html` ("about 1 to 2 years") is less complete than this post's "a few months to 2 years." The strategy's consistency watch asked for a flag. Decide whether to align the older post.

After fixes 1-8, rebuild and re-run the paragraph check: every `<p>` at most 2 sentences and 210 visible characters, including the edited healthcare-jobs paragraph.
