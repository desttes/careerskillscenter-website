## Compliance Review: How to Become a Pharmacy Technician in Massachusetts (2026)

Re-review after revision, 2026-10-04. Reviewed: `git diff tools/build-pages.py` (`_pt_faq`, `_pt_body`, page block, and the `BLOG_POSTS` card). I built the page in a scratch copy outside the repo (nothing committed) to check the rendered page and the JSON-LD. The previous review failed Check 3 only.

## Result: PASS

The two required Check 3 fixes are in, and the recommended fixes for Checks 3 and 5 were also made. All 12 checks pass. A few small notes are below. None of them blocks the post.

## Details:
- **Check 1 (No ghost CSC course details): PASS.** The post gives no CSC length, hours, cost, credential, format, start dates or VA status. There are only two CSC lines: "does not sell pharmacy technician training, so we can be honest" and the allowed line "plans to offer training in healthcare, IT and the skilled trades. Get updates when we launch." The blog card does not mention CSC. "the length of your program" in the cost section means any program the reader picks, not a CSC course.
- **Check 2 (No false ETPL/WIOA/state-approved/Express claims): PASS.** ETPL appears only as a question to ask about other programs ("Your MassHire Career Center can check"). WIOA is described as a MassHire funding source for "eligible people." The post never says "state-approved" about CSC and makes no Express claim.
- **Check 3 (Sourced facts): PASS.** This was the fail last time, and it is fixed.
  - FAQ 5 now reads "...$46,470 a year in May 2025, according to the U.S. Bureau of Labor Statistics (job code 29-2052)... The national median was $45,750 (same job code and date)." The scratch build shows this exact text in the FAQPage JSON-LD, so the SOC code travels with the answer.
  - The body now says "The median pay ... was $46,470 a year, according to BLS (May 2025 data, job code 29-2052). The median means half earn more and half earn less." The wrong "Most ... earn around" wording is gone. The national figure is in the same paragraph, and the source line names SOC 29-2052.
  - The figures match `docs/VERIFICATION_LOG.md`:
    - $46,470: line 187, SOC 29-2052
    - $45,750: line 368
    - 6% growth for 2025-35: line 373
    - $150 non-refundable license fee and the PT1/PT2 rules: line 377
    - PTCE $129, 90 questions (80 scored), 1 h 50 min: line 387
  - The out-of-date figures in research-brief.md ($43,460 from May 2024, and about 49,000 openings from 2024-34) are still left out.
  - Unsourced lines were softened as asked. "Pharmacy techs work in places like store pharmacies and hospitals" now reads as examples, not shares. The PTCE content claims were removed and the post points to PTCB's exam content outline. The DRAFT note (item 17) records each of these changes.
  - The 1,400 passing score comes from the brief only, and CORI comes from the strategy only. Both are listed in the DRAFT notes (items 10 and 8). That is acceptable for a draft.
  - The 13- and 25-week figures are simple arithmetic from 500 hours.
- **Check 4 (No funding promises): PASS.** The post says "No one can promise you will be approved for funding, but you may qualify for help." The CTA is "Check what you may qualify for." "Often no tuition" and "may not pay tuition" are hedged.
- **Check 5 (Readability, ~8th grade): PASS.** Sentences are short, and the post has a glossary, a quick-answer box and plain tables. The earlier jargon notes are fixed:
  - ASHP is spelled out.
  - NRCPhT is dropped from the routes table. The table now says "The Board's list names the exams it accepts."
  - The title/og title is shorter: "Pharmacy Technician in Massachusetts: 3 Ways to Get Licensed (2026)".
- **Check 6 (DRAFT marker at top): PASS.** `<!-- DRAFT -- facts to verify: ... -->` is the first thing in the article body (rendered line 199), the same place as in the phlebotomist post. The pre-deploy grep will catch it. It also contains `[VERIFY` markers, which correctly block deploy.
- **Check 7 (CTAs): PASS.**
  - The main CTA goes to `qualify.html`.
  - Other links go to MassHire locations (`MASSHIRE_URL`), JobQuest (`JOBQUEST_URL`), mass.gov, PTCB, NHA, CareerOneStop, `healthcare-careers.html` and the interest anchor `healthcare-careers.html#interest`.
  - Nothing says "our program" or "our courses."
- **Check 8 (COURSE-DEPENDENT markers): PASS.** Both CSC mentions are wrapped in `<!-- COURSE-DEPENDENT: R-BLOG-03 -->` ... `<!-- /COURSE-DEPENDENT: R-BLOG-03 -->`. The R-BLOG-03 register row and the course-mode copy file come later in the Publisher step. That is expected and not a fail.
- **Check 9 (JSON-LD): PASS.** The scratch build exited with code 0. Both `application/ld+json` blocks parse.
  - **BlogPosting:** the headline matches the new title, and datePublished is 2026-10-04 (a real date).
  - **FAQPage:** has 6 Question/Answer entries that match the visible FAQ.
  - The card renders in `blog.html`.
- **Check 10 (No fabricated testimonials or outcome stats): PASS.** The post has no quotes, reviews, success stories or outcome numbers.
- **Check 11 (Source quality): PASS.** Every source is primary or official: BLS (OOH, OEWS national and MA), mass.gov / 247 CMR 8.00 / the Board's programs-and-exams document, PTCB, NHA and CareerOneStop (U.S. DOL). There are no training providers, career blogs or salary aggregators.
- **Check 12 (Content strategy angle): PASS.** The post still follows `content-strategy.md`:
  - It opens with the "we don't sell this training" honesty hook.
  - It puts the three routes side by side and leads with the trainee route.
  - It covers what can stop you (record and CORI, age, diploma, trainee time limit, renewal), a cost checklist, a job-ad decoder with a JobQuest exercise, and honest downsides.
  - It has fit and not-fit lists, an ESL note, a comparison with phlebotomist and CNA jobs, the "before you pay" questions, and a funding path.
  - It uses the newest data and has no school rankings.

## Issues to Fix (if any):
- None required.
- (Optional, Check 3) The "hard truth" bullet "You learn drug names, medical abbreviations and dose math" is close to the PTCE content claim that was removed. It is a general statement and not a fail, but you could add it to DRAFT item 13 to confirm against BLS OOH "How to Become One."
- (Publisher, expected) Before publishing:
  - Add the R-BLOG-03 row to `docs/COURSE_CONTENT_REGISTER.md`.
  - Create `blog/course-mode-copy/pharmacy-technician-massachusetts.md`.
  - Add a VERIFICATION_LOG section for this post covering the 1,400 passing score, CORI, the trainee time limit, the ASHP expansion and the exam languages.
  - Add the post to `llms.txt`.
  - Get Emilio's decision on printing pay figures (same open question as the phlebotomist and healthcare-jobs posts).
  - Do not deploy while the DRAFT and `[VERIFY` markers are present.
