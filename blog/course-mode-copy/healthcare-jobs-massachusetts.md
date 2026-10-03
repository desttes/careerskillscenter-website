# Course-mode copy: healthcare-jobs-massachusetts

Post: `blog/healthcare-jobs-massachusetts.html` (source: `tools/build-pages.py`, block "Healthcare Jobs You Can Train For in Massachusetts (2026)")
Register row: **R-BLOG-01** in `docs/COURSE_CONTENT_REGISTER.md`
Switch: `COURSES_LIVE.healthcare` (and `SITE_MODE = "courses"`)

Course-mode copy must never render while those switches are off. It must not state any CSC program detail (length, hours, cost, credential, format, start dates) unless Emilio has approved real details by then.

---

## 1. CSC line (marked `<!-- COURSE-DEPENDENT: R-BLOG-01 -->`, after the "What to do this week" checklist)

**Guide mode (live now, renders in the HTML):**

> Career Skills Center plans to offer training in healthcare. [Get updates when we launch](../healthcare-careers.html#interest).

**Course mode (for later):**

> Career Skills Center now offers training in healthcare. [See our healthcare training and check if you may qualify for funded training](../<healthcare-course-page>.html).

Notes:
- Replace `<healthcare-course-page>` with the real course page URL when it exists.
- Keep "may qualify." Never promise funding approval.
- Only add "state-approved," ETPL or WIOA wording if `FUNDING_ETPL_APPROVED` is true.

## 2. Funding CTA box (`post_cta`, links to `qualify.html`)

Not course-dependent. Same copy in both modes:

> **Check what funding you may qualify for.** Answer a few short questions to see which Massachusetts funding options you may qualify for, and where to go next. [Check what you may qualify for](../qualify.html)

In course mode, `qualify.html` itself handles routing to CSC courses (register row R-QUALIFY), so this box does not change.

## 3. "How people in Massachusetts pay for training" section

**Guide mode (live now):** Find your MassHire Career Center, register on JobQuest, read the free-training guide.

**Course mode (for later, optional):** Keep the MassHire and JobQuest steps (they are the real path to state funding). If CSC is then an approved provider (`FUNDING_ETPL_APPROVED` true), a fourth line may be added: "Ask your career counselor about Career Skills Center's healthcare training." Do not add it before then.
