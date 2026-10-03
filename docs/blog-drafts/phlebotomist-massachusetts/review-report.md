## Compliance Review: How to Become a Phlebotomist in Massachusetts (2026): Certification, Pay and Help Paying for Training

Reviewed 2026-10-03: `git diff tools/build-pages.py` (new `_phl_*` block + `BLOG_POSTS` card), generated `blog/phlebotomist-massachusetts.html`, `blog/course-mode-copy/phlebotomist-massachusetts.md`, the R-BLOG-02 row in `docs/COURSE_CONTENT_REGISTER.md`, `research-brief.md`, `content-strategy.md`.

## Result: PASS (all 12 checks) — NOT ready to publish

None of the 12 checks fails. The post is still a draft. It cannot be deployed until the items under "Issues to Fix" are resolved: the pay-figure policy decision, live checks of the facts, and removing the DRAFT marker.

## Details:
- **Check 1 (No ghost courses): PASS.** No CSC length, hours, cost, credential, format, start date, VA status, instructor or campus details. The only CSC statements are "Career Skills Center does not sell phlebotomy training" (intro) and the allowed line "plans to offer training in healthcare, IT and the skilled trades. Get updates when we launch." The course-mode copy file is not rendered and also forbids program details.
- **Check 2 (No false claims): PASS.** There is no ETPL, WIOA, "state-approved" or Express claim about CSC. The "Watch out for 'state-approved' phlebotomy programs" box warns readers about this phrase, which is allowed. ETPL and WIOA are mentioned only as things a MassHire center can check or fund.
- **Check 3 (Sourced facts): PASS, with notes.** National pay ($45,230/yr, $21.75/hr, 10th percentile $35,780, 90th percentile $58,780) is cited to BLS OEWS/OOH SOC 31-9097 in the pay section source line, in the FAQ answer ("job code 31-9097") and in the Sources list. The outlook figures (7%, 143,900, about 18,000/yr) and the industry shares are attributed to BLS. Exam facts are attributed to NHA and ASCP. I found no invented numbers; every figure traces to `research-brief.md`. Notes:
  - (a) The "pay range is fairly narrow" bullet repeats $58,780 without an inline source. It relies on the pay section above.
  - (b) All figures came from search summaries, not live page fetches. The DRAFT block says so.
  - (c) The ASCP fee may now be $165 (the brief flags this). The BLS data vintage ("May 2025") is not confirmed.
- **Check 4 (No promises): PASS.** It says "may help pay," "may qualify," and "Funding is limited… no one can promise you will be approved." The CTA reads "Check what you may qualify for."
- **Check 5 (Readability): PASS.** Estimated Flesch-Kincaid grade is about 6.4 for the body. Sentences are short, there is a glossary with pronunciation, and there is an ESL note. Passages to simplify if possible:
  - The certification table cells ("approved or structured program in the last 5 years… Other routes exist"; "Credential Maintenance Program"; "The test adjusts to your answers as you go").
  - "Other outpatient health services" in the industry list.
  - The 26-word "Quick answer" opening sentence.
- **Check 6 (Draft marker): PASS.** `<!-- DRAFT -- facts to verify: (0)…(12) -->` sits at the top of the post body (line 199 of the generated HTML). This is the same place the existing healthcare-jobs draft uses. It will trip the mandatory pre-deploy grep, as intended.
- **Check 7 (CTA check): PASS.** The CTAs point to `qualify.html`, the MassHire Career Center locator (`MASSHIRE_URL`), JobQuest, `healthcare-careers.html` (field guide), `healthcare-careers.html#interest` (interest list; the anchor exists) and related funding posts. No "our program" or "our courses" wording. All internal link targets exist.
- **Check 8 (Course-dependent markers): PASS.** Both CSC mentions are wrapped in `<!-- COURSE-DEPENDENT: R-BLOG-02 -->` … `<!-- /COURSE-DEPENDENT -->`. The register row R-BLOG-02 was added and describes both spots. The course-mode copy file exists.
- **Check 9 (JSON-LD): PASS.** The generated page has two `application/ld+json` blocks. Both parse as valid JSON: `BlogPosting` (headline, description, datePublished/dateModified 2026-10-03, author, publisher) and `FAQPage` (6 Q&As, matching the visible FAQ). The publish date is the real date (today).
- **Check 10 (No testimonials): PASS.** No quotes, reviews, student stories or outcome stats. The MassHire/hospital paid-training example is generalized ("Some employers may…"), with no employer or result named.
- **Check 11 (Source quality): PASS, with a warning.** The cited sources are only BLS, mass.gov (DPH), ASCP, NHA and AMT. Competitor sites and aggregators (Dreambound, Research.com, ZipRecruiter and others) are explicitly not used, and their claims ("4 weeks," "$62,000+," "third-highest paying") are not repeated. Warning: the "free community college may not cover a short non-credit course" caveat (MassEducate/MassReconnect) is not in the research brief. It comes from `content-strategy.md`, whose evidence partly included a community college's own page (a training provider). The post hedges it ("may not count… ask the college"), but it needs an official source.
- **Check 12 (Angle check): PASS.** The post follows the recommended angle and covers all three differentiators:
  - Hook: the gap between job ads and reality, plus "we don't sell phlebotomy training."
  - Differentiator 1: the "real gatekeepers" chain, the NHA/ASCP/AMT comparison table, and "Before you pay… ask these 6 questions."
  - Differentiator 2: an honest MA funding section (MassHire first, the ETPL check, paid employer training, the MassEducate warning) with outward CTAs.
  - Differentiator 3: "The hard truth" downsides plus fit/not-fit lists, a glossary, the ESL note, the "Saw a phlebotomy job ad?" 10-ad JobQuest check, the CNA/MA comparison, and fresh 2025-35 projections.
  - Gaps: no OSHA bloodborne-pathogens citation (the strategy asked for one), and no Massachusetts pay figure even though one is on file (see Issues).

## Issues to Fix (if any):
These block publishing but are not checklist failures.

1. **Pay-figure policy (blocking).** `PROJECT-HANDOFF.md` allows pay figures only in the salary-by-state post. This post prints national BLS pay in the body, the FAQ and the "hard truth" list. Emilio must either approve an exception or the pay section must become a link to the BLS pages. This is DRAFT item (0) and matches the open question on the healthcare-jobs post.
2. **Massachusetts pay is on file but unused.** The code comment and DRAFT item (1) say "no current Massachusetts figures were found." However, `docs/VERIFICATION_LOG.md` §H1 already records BLS OEWS May 2025 MA median for SOC 31-9097 = **$50,170** (checked 9/26/2026), and `content-strategy.md` recommends using it. If pay is approved, add the MA median with its SOC/source. That is better than "Pay in Massachusetts is different." Correct the code comment either way.
3. **Live verification before deploy.** Check these live:
   - The BLS figures and data vintage (oes319097.htm and the OOH page).
   - The NHA CPT fee ($134) and the ASCP PBT fee ($155 vs. a possible $165).
   - The NHA live-draw requirement (30 + 10) and the renewal terms.
   - The MA no-individual-license status with DPH.
   - The "no Massachusetts state approval for phlebotomy programs" line.
   - The four-state list.
   - Capture the real People Also Ask questions for the FAQ.
4. **MassEducate/MassReconnect caveat.** Source it from the mass.edu OSFA 2025-26 guidelines, or remove it (DRAFT item 10). Do not rely on a college's own page.
5. **Overstated license line in the subtitle and card excerpt.** The article subtitle and `BLOG_POSTS` excerpt say "Massachusetts is not one of the states that license phlebotomists." That is stated flatly, while the brief found no mass.gov sentence confirming it. Use the body's hedged wording ("is not on the list of states that require…"), or confirm with DPH first.
6. **Unsourced minor claims.** These need a source or a softer wording:
   - "Your MassHire Career Center can point you to free English classes (ESOL)."
   - "Some people get hired with a high school diploma and learn on the job." Confirm this against the BLS OOH wording.
7. **Optional:** add the OSHA bloodborne pathogens standard (29 CFR 1910.1030) to the needlestick bullet and to Sources, as the strategy recommended. Optionally add an inline "(BLS)" to the $58,780 mention in "The hard truth."
8. **Before deploy:** remove the DRAFT comment only after items 1-6 are resolved and logged in `docs/VERIFICATION_LOG.md`. Then run the mandatory `[VERIFY` / `DRAFT` grep.
