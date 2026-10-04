# Course-mode copy: pharmacy-technician-massachusetts

Post: `blog/pharmacy-technician-massachusetts.html` (source: `tools/build-pages.py`, block "How to Become a Pharmacy Technician in Massachusetts (2026)")
Register row: **R-BLOG-03** in `docs/COURSE_CONTENT_REGISTER.md`
Switch: `COURSES_LIVE.healthcare` (and `SITE_MODE = "courses"`)

Course-mode copy must never render while those switches are off. It must not state any CSC program detail (length, hours, cost, credential, format, start dates) unless Emilio has approved real details by then.

---

## 1. Intro honesty line (marked `<!-- COURSE-DEPENDENT: R-BLOG-03 -->`, second paragraph)

**Guide mode (live now, renders in the HTML):**

> This guide explains all three ways in, what each one costs, the rules that can stop you, and the parts of the job other guides leave out. Career Skills Center does not sell pharmacy technician training, so we can be honest.

**Course mode (for later):**

- If CSC still does **not** offer pharmacy technician training: keep the line as is.
- If CSC **does** offer pharmacy technician training (or any healthcare training that could be read as competing): drop the last sentence and replace with:

> This guide explains all three ways in, what each one costs, the rules that can stop you, and the parts of the job other guides leave out. Career Skills Center offers training in healthcare, and we wrote this guide to help you compare any program, including ours, with clear questions.

## 2. CSC line (marked `<!-- COURSE-DEPENDENT: R-BLOG-03 -->`, after the "What to do this week" checklist)

**Guide mode (live now, renders in the HTML):**

> Career Skills Center plans to offer training in healthcare, IT and the skilled trades. [Get updates when we launch](../healthcare-careers.html#interest).

**Course mode (for later):**

> Career Skills Center now offers training in healthcare. [See our healthcare training and check if you may qualify for funded training](../<healthcare-course-page>.html).

Notes:
- Replace `<healthcare-course-page>` with the real course page URL when it exists.
- Keep "may qualify." Never promise funding approval.
- Only add "state-approved," ETPL or WIOA wording if `FUNDING_ETPL_APPROVED` is true.
- Do not describe a CSC course as a Board-approved pharmacy technician program unless the Board has approved it.
