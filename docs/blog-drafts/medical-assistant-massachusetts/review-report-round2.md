# Review report, round 2: How to Become a Medical Assistant in Massachusetts

- Post: `blog/medical-assistant-massachusetts.html` (source: `_ma_faq` / `_ma_body` / `PAGES.append` block in `tools/build-pages.py`)
- DRAFT_DIR: `docs/blog-drafts/medical-assistant-massachusetts/`
- Reviewed: 2026-10-05. Checked against CLAUDE.md, `docs/BLOG_WRITING_GUIDELINES.md`, `research-brief.md`, `content-strategy.md`, `community-verification.md` and `editorial-decisions.md`. Also checked against Emilio's 2026-10-05 rulings: national pay only ($45,690), no sources or attributions, no named schools, programs or employers, paragraphs of at most 2 sentences and 210 characters, no visible byline, and never "MA" for medical assistant.
- Method:
  - Read the uncommitted diff of `tools/build-pages.py` and the three sibling HTML diffs.
  - Rebuilt the site in a scratch copy of the repo. The generated post, the three sibling posts and `blog.html` are identical to the working tree (ignoring `?v=` stamps), so the HTML is current.
  - Parsed the generated HTML: visible character and sentence count for all 106 `<p>`, JSON-LD parsing, link targets, and banned-word greps.
  - Opened MGL c.112 s.265 live on malegislature.gov to check the shot-rule wording.

## Result: FAIL (one required wording fix, in two places)

All 12 items from round 1 are fixed or handled. The new "What do I need to start?" section and the new FAQ match the brief.

One accuracy problem remains, and it came from round 1's own suggestion. The post defines "primary care provider" as "a doctor or nurse practitioner." The statute does not limit it to those two. It defines the term by role ("a health care professional qualified to provide general medical care…"). Changing it to "such as a doctor or nurse practitioner" fixes it (Fix 1). Everything else passes.

---

## Round 1 fix confirmation

| # | Round 1 fix | Status |
|---|---|---|
| 1 | Healthcare-jobs "2. Medical assistant" paragraph was 3 sentences / 247 chars | **Fixed.** The link is now its own `<p>` (72 chars, 1 sentence). The original paragraph is unchanged. |
| 2 | Add "What you need to start" | **Fixed.** New H3 "What do I need to start?" after the three-ways table, with 3 paragraphs. A matching FAQ item was also added. See the extra checks below. |
| 3 | Inline VERIFY on paid employer training and the cost cell | **Fixed.** VERIFY comments are now on: intro paragraph 2, the "For example, some Massachusetts health centers…" paragraph, the employer "Cost to you" cell, the accredited-program cost cell (one college's tuition math), and the "Employer-paid training" paragraph. A Python comment above `_ma_faq` notes that the FAQ repeats VERIFY-flagged facts. |
| 4 | "Doctor or nurse" too broad | **Changed, but now too narrow.** The body reads "A primary care provider (a doctor or nurse practitioner) must be in the building…". The FAQ reads "That is a doctor or nurse practitioner". "The supervising provider" replaces "doctor or nurse" in the other-tasks line. See Fix 1. |
| 5 | CCMA "practice questions" | **Fixed.** Now "150 scored questions plus 30 unscored questions, 3 hours". |
| 6 | CCMA eligibility: diploma/GED applies to both routes | **Fixed.** Now "High school diploma or GED, plus a training program in the last 5 years or 1 year of supervised work in the last 3". |
| 7 | "Medical assistants say…" | **Fixed.** Now "Some medical assistants say the job changes a lot from office to office." |
| 8 | Soft wording in the CNA and hard-truth sections | **Fixed.** Now "some people say a CNA is a more direct first step. They also say a medical assistant job is often daytime clinic work and easier on the body." Also "some people say more doors open after that first job." Also "Some who want much more money go back to school for nursing." |
| 9 | "before you enroll" (optional) | **Fixed.** Now "before you sign up". No "enroll" remains in the post. |
| 10 | "Often several thousand dollars" (optional) | **Fixed.** Now "Can cost several thousand dollars" in the table and "can cost several thousand dollars" in the FAQ. |
| 11 | Remote-work fragment (optional) | **Fixed.** Now "Most of this job is done in person, because it involves patient care. Remote jobs, when you find them, are usually office work like scheduling or records." |
| 12 | Healthcare-jobs "about 1 to 2 years" (director note) | **Open, as intended.** The older post was left alone. It is still a director decision. |

---

## Checks

### 1. No CSC program details: PASS
The only CSC lines are the intro honesty line and "plans to offer training in healthcare, IT and the skilled trades. Get updates when we launch." Neither gives a length, cost, credential, format or date.

### 2. No ETPL / WIOA / "state-approved" / Express claims: PASS
- ETPL and WIOA appear only as reader guidance: the checklist question and the MassHire/WIOA funding section.
- "state-approved" appears once, about CNA programs ("At least 75 hours in a state-approved program"). This matches the CNA post.
- "Express" appears only in the shared nav.

### 3. Every number is in the research brief with a source: PASS
These all trace to the brief: $45,690; 13%; 109,700; "more than half" (56%); "about 7 in 10" (69%); 200 questions / about 2 h 40 min; 210 / 2 h; 150 + 30 unscored / 3 h; $125/$250, $150, $169; renewals every 5/3/2 years; 720 / 160 hours; 3 years in the last 7; 5 years; 1 year in the last 3; about 8 months to 2 years; about 12 weeks; a few months to 2 years; 6 credits; 75 hours; CNA 3%.

The new section adds no numbers. The felony facts come from `community-verification.md`, and editorial-decisions approves them as official facts.

### 4. "May qualify"; no funding promises: PASS
"may qualify" or "if you qualify" appears in MassHire, MassEducate ("eligible students may get"), FAQ 6, the CTA block and "What to do this week." No caps or rates are hard-coded.

### 5. Plain language; paragraph shape: PASS
- All 106 `<p>` elements in the generated page have at most 2 sentences and at most 210 visible characters. That count includes the lead, notes, CTA, CSC line, all 7 FAQ answers (14 `<p>`) and the dek.
- Longest: 186 (FAQ "Can a medical assistant give shots"), 184 (dek), 181 (intro CSC line), 176 (intro paragraph 2).
- The script flagged one paragraph as 3 sentences, but that is a false positive: "U.S." in "…in the U.S. is expected to grow 13%… There are about 109,700 openings each year." It is 2 sentences and 140 characters.
- The new start-section paragraphs are 92, 104 and 112 characters, each 1 or 2 complete sentences.
- No "MA" for medical assistant. The only "MA" hits are "Quincy, MA 02171" in the shared footer.
- Reading level is about 8th grade. CORI, accredited, externship, vital signs and immunization are defined in "Words to know."

### 6. DRAFT marker present: PASS
The `<!-- DRAFT -- facts to verify: (1)…(14) -->` comment is at the top of the body. It is invisible to readers. Item 14 now covers the "What do I need to start" sources. It is long rather than "short," but that was accepted in round 1.

### 7. CTAs: PASS
- Certifications point to the AAMA, AMT and NHA eligibility pages and the AAMA page that links to CAAHEP/ABHES.
- Funding points to `qualify.html` through `post_cta`.
- MassHire appears only in the funding section and "What to do this week."
- No "our program," "our courses," "enroll" or "apply" in the post. A grep for "our program" matches only "Ask **your program** which exam…", which is reader advice.

### 8. COURSE-DEPENDENT markers and course-mode file: PASS
- Two marked blocks use `R-BLOG-05`: the intro honesty line and the plans-to-offer line.
- The register row R-BLOG-05 in `docs/COURSE_CONTENT_REGISTER.md` describes both places, the target `healthcare-careers.html#interest` (the anchor exists) and the switch `COURSES_LIVE.healthcare`.
- `blog/course-mode-copy/medical-assistant-massachusetts.md` matches the guide-mode text word for word in both places.
- Its course-mode copy keeps "may qualify" and forbids accreditation or certification claims about a future CSC course.

### 9. BlogPosting and FAQPage JSON-LD: PASS
Both blocks parse.
- BlogPosting: headline equals the H1, the author is the Organization "Career Skills Center", and datePublished and dateModified are 2026-10-05 (today).
- FAQPage: 7 Q&As, and each answer text equals the visible answer paragraphs joined together.
- No visible byline (`author=None`, and no byline in `<main>`).

Note: Guideline 6 says the FAQ has 4-6 questions. This post has 7. `content-strategy.md` (line 307) asks for "5-7 short Q&As," and the strategy's angle governs the post (Guideline 11), so this is accepted. Optional Fix 3 covers it if the director wants to stick to the guideline.

### 10. No testimonials or invented outcomes: PASS
There are no quotes and no outcome stats. The only quoted line is the suggested interview question from editorial-decisions C7.

### 11. No facts from salary aggregators, training providers or career blogs: PASS
All facts trace to BLS, the statute, the certifying bodies, mass.edu, and public-college or employer pages about their own programs, as the brief records.

### 12. Follows the strategy's angle; differentiators are real sections: PASS
- The hook matches the strategy.
- "Three ways to become a medical assistant" puts the employer route first.
- Certification is covered by the "CMA, RMA or CCMA" H2, the shot-rule H3 and the "Before you pay" checklist.
- "The hard truth" covers hiring, leaving and staying, AI, remote work, "worth it," and the CNA comparison.
- The four positives from correction 5 are still there.

### 13. Reader-first, no sources or complexity: PASS
None of the following appear: "we did not find," "could not confirm," percentiles, statistics explanations, SOC codes, BLS growth labels, "Not shown," a Sources section, "Source:" notes, "according to," or "BLS says."

External links are action links only: the certifying bodies, the accredited-program lists, JobQuest and MassHire locations.

### 14. Answers the Guideline 7 reader questions: PASS (was FAIL)
| Question | Covered? |
|---|---|
| Pay | Yes, one national number, $45,690, plus "New medical assistants often start lower." |
| Training length | Yes (route table, "How long does it take?", FAQ 2) |
| Training cost | Yes ("can cost several thousand dollars at a public college", "Prices vary", exam fees, FAQ 6) |
| Working while training | Yes (hybrid, evening classes, daytime unpaid externship, paid employer route) |
| What you need to start | **Yes, now.** The H3 "What do I need to start?" covers diploma/GED, no work experience, CORI, physical, shot records and CPR/BLS. FAQ 5 covers the same. |
| State license yes/no | Yes, "No state license required." |
| Exam facts | Yes (questions, time, cost, CMA first-try pass rate). The pass score is left out, which the brief allows. |

### 15. Links to relevant existing posts: PASS
- All 12 internal targets in `<main>` resolve: cna, free-job-training, healthcare-jobs, is-wioa-training-free, masshire-training-voucher, pharmacy-technician, phlebotomist, wioa-eligibility, career-paths, healthcare-careers (and `#interest`), qualify, student-financing.
- `related()` lists 3 posts.
- The blog index card is in `BLOG_POSTS`. While the post is a draft, the build keeps it out of `blog.html` and `sitemap.xml` (DRAFT_SLUGS), as designed.

### 16. Community experiences: PASS (was FAIL)
- Only approved items are used: C1, C2, C3, C4 (with C5), C6 and C7, plus the two official-fact items (criminal record, paid employer training). None of the CUT items appear.
- No quotes, usernames, links or identifying details. Nothing suggests these people are CSC students.
- Mixed views are shown: the leave and stay sides, and "There is another side."
- Soft wording is now used throughout. "Medical assistants who leave often talk about…" and "The jobs are there, but the first one is often the hardest to get" are framed as experience and match the approved C1/C4 wording ("Employers often ask for experience" is approved text).

---

## Extra checks requested by the director

### New "What do I need to start?" section and FAQ 5: PASS
Each claim is in the brief, and each one is worded softly:
- "To start, you usually need a high school diploma or GED." The brief's entry point (line 4) is "high school diploma or GED." NHA names it [OPENED]. The college pages don't state it, and the brief says to check each college. "Usually" is the right softness, and DRAFT item 14 records this. Not invented.
- "You do not need work experience." BLS lists "no work experience" [OPENED].
- "College programs **may** also ask for a background (CORI) check, a physical exam and your shot records." This comes from the Greenfield CC page (CORI, physical exam, immunization forms) [OPENED] and community-verification line 37. It is worded as "may" and gives no school name.
- "**Some** employers also want CPR (Basic Life Support) certification." BLS OOH [OPENED] says some employers require BLS/CPR. The wording is soft.
- "Ask each program and employer what they need before you start." This is a good closing action.
- FAQ 5 repeats the same four facts with the same softness. Its paragraphs are 81 and 150 characters, each 2 sentences.
- No inline VERIFY is needed, because these facts were opened. The DRAFT header (item 14) covers the generalization.

### New 7th FAQ ("Is a medical assistant the same as a CNA?") and the FAQ set: PASS
Against the brief:
- "works mostly in doctors' offices and clinics": physicians' offices 56% plus outpatient 10%.
- "needs no state license" and "A CNA gives daily care, mostly in nursing homes and hospitals": 36% plus 32%.
- "must pass a state exam and be on the Nurse Aide Registry": from the CNA brief.

All of these hold. There are no pay figures, as Emilio's national-pay-only ruling requires. It matches the body table and `blog/cna-massachusetts.html`. On the count of 7, see check 9.

### Shot-rule wording against the verified statute: FAIL (Fix 1)
I opened MGL c.112 s.265 live on 2026-10-05:
- Accreditation: "accredited by the committee on allied health education and accreditation of the American Medical Association or its successor [CAAHEP], the Accrediting Bureau of Health Education Schools or its successor or another certificate program that the commissioner of public health may approve." The post matches: "accredited by CAAHEP or ABHES, or approved by the state health department."
- Supervision: "present in the facility and immediately available … shall not be required to be present in the room." The post matches: "must be in the building and ready to help" and "they must be in the building."
- Employment: the person must be "employed in the medical practice of a licensed primary care provider." The post matches: "A primary care office may let…".
- **Who supervises:** the statute defines "Primary care provider" as "a health care professional qualified to provide general medical care for common health care problems who (i) supervises, coordinates, prescribes … (ii) initiates referrals … (iii) maintains continuity of care." It does not name doctors or nurse practitioners. The post's parenthetical "(a doctor or nurse practitioner)" and the FAQ's "That **is** a doctor or nurse practitioner" read as a complete list. Other primary care clinicians, such as physician assistants, are not excluded by the statute. Present doctors and nurse practitioners as examples instead.

  This wording came from round 1's own suggestion ("doctor or nurse practitioner"), so this is a correction to my earlier advice, not a writer error.
- Minor, no change needed: FAQ 1 ("To give shots in a primary care office, you must finish an accredited program.") leaves out the DPH-approved alternative. The body explains it, and adding the alternative to the FAQ would bring in "state-approved" wording, which we want to avoid. Acceptable.

### CCMA cell: PASS
- Eligibility: "High school diploma or GED, plus a training program in the last 5 years or 1 year of supervised work in the last 3." This matches NHA [OPENED]: diploma/GED and a program within 5 years, or diploma/GED and 1 year of supervised work in the last 3. The diploma/GED now clearly applies to both routes. The "2 years in last 5" variant is left out, which is fine.
- Exam: "150 scored questions plus 30 unscored questions, 3 hours". This matches the brief's "150 scored + 30 pretest items", and its VERIFY notes the 2022 test plan.
- Fee: "$169" with a VERIFY comment (SEARCH SUMMARY).

### VERIFY comments: PASS
There are 15 `[VERIFY` comments in the generated page. Every SEARCH SUMMARY or unconfirmed fact in the body has one nearby:
- no state license
- shot rule (DPH circular)
- paid employer training (×4)
- one-college cost math
- CMA format
- CMA fees
- RMA format
- CCMA format
- CCMA fee
- RMA renewal cycle
- CMA pass rate
- NHA felony rule

FAQ repeats are covered by the Python comment above `_ma_faq` and the DRAFT header. The pre-deploy grep will block this file, as intended.

### COURSE-DEPENDENT / register / course-mode copy match: PASS
See check 8. The guide-mode text in the course-mode file is identical to both rendered CSC blocks. The register row exists, and its target anchor resolves.

### Schema validity: PASS
See check 9. Both JSON-LD blocks parse. FAQ schema text matches the visible answers.

### Sibling-post edits only add the link: PASS (was FAIL)
- **CNA:** one new `<p>`, "Thinking about a medical assistant job instead? Read how to become a medical assistant in Massachusetts." That is 104 characters and 2 sentences. Nothing else changed.
- **Phlebotomist:** "Read how to become a medical assistant in Massachusetts." is appended to the existing 1-sentence paragraph. It is now 141 characters and 2 sentences. Nothing else changed.
- **Healthcare jobs:** one new `<p>`, "Read more in our guide to becoming a medical assistant in Massachusetts." That is 72 characters and 1 sentence. The original paragraph is unchanged.
- The generated HTML uses `../blog/medical-assistant-massachusetts.html`, and the target exists. Source and HTML diffs agree, and the rebuild produces the same files.

### Emilio's 2026-10-05 rulings: PASS
- Pay: one national number, $45,690. No Massachusetts figure, hourly rate, percentile or CNA dollar figure.
- No sources or attributions on the page.
- No named schools, programs or employers. Only accreditors, certifying bodies, MassEducate, MassHire and JobQuest are named.
- Paragraph limits are met.
- No visible byline.
- No "MA" for medical assistant.

---

## Fix list

1. **Required. Shot rule, "primary care provider" is narrowed too far.** Make doctors and nurse practitioners examples, not a full list. Both edits stay well under 210 characters and 2 sentences.
   - Body, `_ma_body`, "The one state rule: giving shots", third paragraph:
     - Change: "A primary care provider (a doctor or nurse practitioner) must be in the building and ready to help."
     - To: "A primary care provider, such as a doctor or nurse practitioner, must be in the building and ready to help."
   - FAQ, `_ma_faq`, "Can a medical assistant give shots in Massachusetts?", first paragraph:
     - Change: "That is a doctor or nurse practitioner, and they must be in the building."
     - To: "That can be a doctor or nurse practitioner, who must be in the building."

   Then rebuild. The FAQPage schema updates automatically.
2. **Director note (carried from round 1, no change in this post):** `healthcare-jobs-massachusetts.html` still says medical assistants "often train for about 1 to 2 years." This post says "a few months to 2 years." Decide whether to align the older post.
3. **Optional. FAQ count.** The post has 7 FAQs. Guideline 6 says 4-6, and the strategy says 5-7. If the director prefers the guideline, drop "Is a medical assistant the same as a CNA?", since the body's "Medical assistant or CNA?" section and table already answer it. Otherwise leave it as is.

After Fix 1, rebuild and re-run the paragraph check on the two edited paragraphs. No other re-review is needed.
