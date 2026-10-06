# Blog Queue

Add blog topics here for the blog agent to work on. The agent runs every 6 hours, picks up the next item, and moves it to "In Progress" or "Done."

## Next Up
- **Medical assistant (nationwide rewrite)** — NATIONAL credential (CMA/RMA/CCMA), so a NATIONWIDE post: Massachusetts only as a labeled section. Emilio (2026-10-05) left the title, angle and outline to the pipeline. Replaces the state-framed draft `blog/medical-assistant-massachusetts.html` (keep it until Emilio approves the new one; the three sibling drafts link to it). Target: "how to become a medical assistant". Also cover, where they fit: how many years, how hard is it, CMA vs RMA certification (AAMA, AMT, NHA, AMCA), salary, worth it, will AI replace MAs, part time. Full analysis in `docs/KEYWORD_ANALYSIS.md`, section "Medical assistant, round 2". Do NOT target physician/doctor's assistant terms.
- **How to Become an Electrician in Massachusetts** — role guide: apprenticeship path (8,000 hrs + 600-hr course), MA licensing (journeyman/master), MA pay (BLS SOC 47-2111), union vs non-union, job outlook. Target: "electrician massachusetts"
- **How to Become an HVAC Technician in Massachusetts** — role guide: what HVAC techs do, MA pay (BLS SOC 49-9021), state license + EPA 608 certification, refrigeration license, apprenticeship path, job outlook. Target: "HVAC technician massachusetts"

## In Progress
<!-- The agent moves items here while working on them. -->


## Done
<!-- Completed drafts. The agent logs the file path and date. -->
- **How to Become a Medical Assistant in Massachusetts (2026): Certification, Pay and Paid Training** — `blog/medical-assistant-massachusetts.html` — 2026-10-05 — status: draft, local/GitHub only, needs Emilio review (DRAFT marker blocks deploy; see VERIFICATION_LOG section R). Compliance review passed after round 2 fix.
- **Healthcare Jobs in Massachusetts You Can Train For (2026)** — `blog/healthcare-jobs-massachusetts.html` — 2026-10-03 — status: approved by Emilio 2026-10-05, held back from publishing (DRAFT marker blocks deploy; see VERIFICATION_LOG section N).
- **How to Become a Phlebotomist in Massachusetts (2026)** — `blog/phlebotomist-massachusetts.html` — 2026-10-03 — status: approved by Emilio 2026-10-05, held back from publishing (DRAFT marker blocks deploy; see VERIFICATION_LOG section O).
- **How to Become a Pharmacy Technician in Massachusetts (2026)** — `blog/pharmacy-technician-massachusetts.html` — 2026-10-04 — status: approved by Emilio 2026-10-05, held back from publishing (DRAFT marker blocks deploy; see VERIFICATION_LOG section P). Open decision: OK to print BLS pay figures in role-guide posts? (Rules allow pay only in the salary-by-state post; same question as sections N and O.)
- **How to Become a CNA in Massachusetts (2026): Training, Exam and Who Pays** — `blog/cna-massachusetts.html` — 2026-10-04 — status: approved by Emilio 2026-10-05, held back from publishing (DRAFT marker blocks deploy; see VERIFICATION_LOG section Q). Open decision: OK to print BLS pay figures in role-guide posts.

## Notes for the Agent
<!-- Any standing instructions: tone preferences, topics to avoid, priority order, etc. -->
- Follow all guide-mode rules in CLAUDE.md and GUIDE_MODE_SPEC.md
- Every post needs `<!-- DRAFT -->` until Emilio approves
- Use real publish dates only
- No CSC program facts (length, hours, cost, credentials)
- All pay figures must be BLS OEWS sourced and logged in VERIFICATION_LOG.md
