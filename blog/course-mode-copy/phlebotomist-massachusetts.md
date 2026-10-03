# Course-mode copy: phlebotomist-massachusetts

Post: `blog/phlebotomist-massachusetts.html` (source: `tools/build-pages.py`, block "How to Become a Phlebotomist in Massachusetts (2026)")
Register row: **R-BLOG-02** in `docs/COURSE_CONTENT_REGISTER.md`
Switch: `COURSES_LIVE.healthcare` (and `SITE_MODE = "courses"`)

Course-mode copy must never render while those switches are off. It must not state any CSC program detail (length, hours, cost, credential, format, start dates) unless Emilio has approved real details by then.

---

## 1. Intro honesty line (marked `<!-- COURSE-DEPENDENT: R-BLOG-02 -->`, second paragraph)

**Guide mode (live now, renders in the HTML):**

> This guide shows you how that works, what it costs, who may help you pay, and the parts of the job other guides leave out. Most guides on this topic are written by schools or sites that earn money when you sign up for a course. Career Skills Center does not sell phlebotomy training, so we can be honest.

**Course mode (for later):**

- If CSC still does **not** offer phlebotomy training: keep the line as is.
- If CSC **does** offer phlebotomy (or any healthcare training that could be read as competing): drop the last sentence and replace with:

> This guide shows you how that works, what it costs, who may help you pay, and the parts of the job other guides leave out. Career Skills Center offers training in healthcare, and we wrote this guide to help you compare any program, including ours, with clear questions.

## 2. CSC line (marked `<!-- COURSE-DEPENDENT: R-BLOG-02 -->`, after the "What to do this week" checklist)

**Guide mode (live now, renders in the HTML):**

> Career Skills Center plans to offer training in healthcare, IT and the skilled trades. [Get updates when we launch](../healthcare-careers.html#interest).

**Course mode (for later):**

> Career Skills Center now offers training in healthcare. [See our healthcare training and check if you may qualify for funded training](../<healthcare-course-page>.html).

Notes:
- Replace `<healthcare-course-page>` with the real course page URL when it exists.
- Keep "may qualify." Never promise funding approval.
- Only add "state-approved," ETPL or WIOA wording if `FUNDING_ETPL_APPROVED` is true.

## 3. Funding CTA box (`post_cta`, links to `qualify.html`)

Not course-dependent. Same copy in both modes. In course mode, `qualify.html` handles routing to CSC courses (register row R-QUALIFY).

## 4. "How to pay for phlebotomy training in Massachusetts" section

**Guide mode (live now):** MassHire Career Center, JobQuest, ask about paid employer training, community college caveat.

**Course mode (for later, optional):** Keep all four steps. If CSC is then an approved provider (`FUNDING_ETPL_APPROVED` true), a line may be added: "Ask your career counselor about Career Skills Center's healthcare training." Do not add it before then.
