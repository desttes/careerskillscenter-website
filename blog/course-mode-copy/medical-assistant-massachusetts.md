# Course-mode copy: medical-assistant-massachusetts

Post: `blog/medical-assistant-massachusetts.html` (source: `tools/build-pages.py`, block "How to Become a Medical Assistant in Massachusetts (2026)")
Register row: **R-BLOG-05** in `docs/COURSE_CONTENT_REGISTER.md`
Switch: `COURSES_LIVE.healthcare` (and `SITE_MODE = "courses"`)

Course-mode copy must never render while those switches are off. It must not state any CSC program detail (length, hours, cost, credential, format, start dates) unless Emilio has approved real details by then.

---

## 1. Intro honesty line (marked `<!-- COURSE-DEPENDENT: R-BLOG-05 -->`, third paragraph)

**Guide mode (live now, renders in the HTML):**

> This guide shows the three ways in, what each costs you and the hard parts of the job. Career Skills Center does not sell medical assistant training, so we can be straight with you.

**Course mode (for later):**

- If CSC still does **not** offer medical assistant training: keep the line as is.
- If CSC **does** offer medical assistant training (or any healthcare training that could be read as competing): drop the last sentence and replace with:

> This guide shows the three ways in, what each costs you and the hard parts of the job. Career Skills Center offers training in healthcare, and we wrote this guide to help you compare any program, including ours, with clear questions.

## 2. CSC line (marked `<!-- COURSE-DEPENDENT: R-BLOG-05 -->`, after the "What to do this week" checklist)

**Guide mode (live now, renders in the HTML):**

> Career Skills Center plans to offer training in healthcare, IT and the skilled trades. [Get updates when we launch](../healthcare-careers.html#interest).

**Course mode (for later):**

> Career Skills Center now offers training in healthcare. [See our healthcare training and check if you may qualify for funded training](../<healthcare-course-page>.html).

Notes:
- Replace `<healthcare-course-page>` with the real course page URL when it exists.
- Keep "may qualify." Never promise funding approval.
- Only add "state-approved," ETPL or WIOA wording if `FUNDING_ETPL_APPROVED` is true.
- Do not say a CSC course is CAAHEP- or ABHES-accredited, or that it leads to the CMA (AAMA), RMA or CCMA, unless that is confirmed on the accreditor's or certifying body's own list.
- If CSC ever runs medical assistant training, re-check the "Three ways to become a medical assistant" table and the "Before you pay for a program" questions so they still read as neutral advice.
