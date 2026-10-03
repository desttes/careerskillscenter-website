# Blog Writing Guidelines

These guidelines are read by the blog pipeline's **Writer** agent.

---

## 1. Target Audience

The primary reader is a **working adult considering a career change** — someone in a retail, food service, or administrative job who's heard that a career like medical billing pays well and wants to know if it's real. They're not in school. They likely have a high school diploma or GED. Their English reading level is basic. Many are Black Americans, immigrants, or low-income workers looking for a realistic path out of minimum-wage entry-level work. They're cautious about spending money on training and skeptical of "too good to be true" promises.

Secondary audience: someone already in a healthcare admin, IT support, or trades-adjacent role who wants to specialize and earn more.

**Not our audience:** traditional college students, people already certified looking for job listings, or hiring managers.

## 2. Voice and Tone

Friendly expert neighbor — plain, direct, encouraging but honest. Write like you're explaining to a smart friend who's exploring career options, not like a school admissions page. No jargon without a plain-English definition right next to it. No exclamation marks in body copy. No "you'll love this career" or "exciting opportunity" — let the facts speak. Never talk down to the reader; respect that they're making a big life decision and need straight answers, not a sales pitch.

## 3. Reading Level and Language

Write at a **7th–8th grade reading level**. Short sentences (under 20 words when possible). One idea per paragraph. Define every technical term the first time it appears — not in a footnote, right in the sentence: "a CPC (Certified Professional Coder) credential." Avoid idioms and slang that don't translate well for ESL readers. Use "you" and "your" — speak directly to the reader. Prefer common words: "get" over "obtain," "pay" over "compensation," "test" over "examination." Break up walls of text with subheadings, bullet lists, and short paragraphs.

## 4. Honesty and Downsides

Always include the hard parts — don't just sell the upside. If the certification exam has a low pass rate, say so. If the training takes real study hours on top of a full-time job, say so. If entry-level pay in some areas is lower than the national median, say so. Our biggest advantage is that we have nothing to sell right now — we can be the one page that tells the whole truth. Structure it as: here's the opportunity, here's what it actually takes, here's what could go wrong, here's how to decide if it's right for you.

Use marketing judgment: know when to inspire and when to be blunt. The reader should finish the post feeling informed and empowered, not discouraged — but never misled.

## 5. Post Structure

Every post follows a predictable skeleton so readers always know where they are:

1. **Hook** — follow the Content Strategist's recommended angle, not a generic intro
2. **What the job actually is** — daily tasks in plain language ("you'd spend your day...")
3. **Pay** — BLS median with honest context (entry vs experienced, regional variation)
4. **How to get in** — training path, timeline, cost range (general industry, never CSC specifics)
5. **Certifications** — which ones matter, what the exam is like, what it costs
6. **The hard truth** — downsides, common surprises, who this is NOT a good fit for
7. **How to pay for training** — funding options, link to qualify.html
8. **Next step** — one clear action (see Guideline 6 for what to link to)
9. **FAQ** — 4–6 questions from the research brief, with FAQPage schema

The Writer can reorder or merge sections if the Content Strategist's angle calls for it, but every post must hit all nine topics somewhere.

## 6. Funnel Structure and CTAs

Every blog post is part of a funnel. The reader enters at curiosity and should leave closer to action.

### The funnel:
```
AWARENESS (broad posts)
  "Healthcare Jobs You Can Train For"
       ↓ links to...
CONSIDERATION (role-specific posts)
  "How to Become a Medical Biller"
       ↓ links to...
DECISION (action pages)
  qualify.html / career field guide / certifying body
       ↓ links to...
CONVERSION (future course page — COURSE-DEPENDENT)
  interest list / course page when live
```

### Every post must include:

1. **Deeper link (down the funnel):** Broad posts link to specific role posts. Role posts link to qualify.html and the career field guide. Always move the reader one step closer to a decision.

2. **Sideways link (related content):** 2–3 related posts via the `related()` helper — keeps readers exploring within our site.

3. **Action CTA (bottom of funnel):** "Check what funding you may qualify for" → qualify.html. Place it after the training/cost section where the reader is thinking "but how do I pay for this?"

4. **Course CTA (future conversion — COURSE-DEPENDENT):** A natural mention of Career Skills Center near the action CTA: *"Career Skills Center plans to offer training in [field]. Get updates when we launch."* Marked `<!-- COURSE-DEPENDENT: R-BLOG-xx -->`. When courses go live, this flips to link directly to the course page. **Place this where it feels earned** — after the post has delivered real value, never in the first half.

### CTA targets depend on the topic:

- **For certification/career path next steps:** Point to the **official certifying body** — AAPC, AHIMA, CompTIA, NHA, etc. These are nationwide certifications; don't funnel readers to a Massachusetts-specific resource for something national. Example: "Visit aapc.com to learn more about the CPC exam and find study resources."
- **For funding/paying for training:** Point to **qualify.html**. That's where the MA-specific funding conversation lives.
- **MassHire only appears** in the funding section or when the post is specifically about a Massachusetts-licensed career (electrician, plumber) where state licensing is part of the path. Never as the primary action CTA on a nationwide certification post.

### Course-mode copy:

The Writer must write **both versions** of every course-dependent CTA and document them in a companion file (`blog/course-mode-copy/[post-slug].md`):
- **Guide mode (live now):** "Find state-funded training programs through your MassHire Career Center."
- **Course mode (for later):** "Career Skills Center offers training in medical billing and coding. Check if you qualify for funded training."

The guide-mode version renders in the HTML. The course-mode version sits behind the `SITE_MODE` switch in the code and is documented in the markdown file so the switchover is explicit and reviewable.

## 7. SEO

The Writer executes SEO based on the **target keyword assigned in the blog queue**. This keyword was chosen through prior analysis and is final. The Writer must NOT invent, substitute, or "improve" the target keyword. Every SEO decision flows from that assigned keyword:

- **Target keyword in the H1, the first paragraph, and one H2.** Don't force it elsewhere — natural language wins.
- **Long-tail variations** come only from the Content Strategist's SERP audit (People Also Ask, related searches) — use those as H2s/H3s, don't invent your own.
- **Title tag format:** "[Keyword-based title]: [Honest Hook] (2026) | Career Skills Center" — under 60 characters.
- **Meta description:** One plain sentence answering "why should I click this?" — under 155 characters, including the target keyword naturally.
- **Write for featured snippets:** Answer common questions (from the research FAQ) in a clean paragraph under 45 words or a short numbered list right under the H2.
- **Schema markup:** BlogPosting JSON-LD (via `article_ld()`) and FAQPage schema (via `faq_ld()`) on every post. Non-negotiable.
- **URL slug:** short, keyword-focused, lowercase, hyphens only.
- **Freshness signals:** Use the current year in the title only when the post has annually-updating data. Cite the data vintage ("BLS, May 2025 data").
- **Internal links:** at least 3 per post — the funnel links from Guideline 6 plus one to a related blog post. Use descriptive anchor text, not "click here."
- **No keyword stuffing.** If it feels forced, rewrite the sentence.

## 8. Hard Prohibitions

1. **Never state CSC program details** — no length, hours, cost, credentials, format, start dates, instructors, campus details, VA status
2. **Never claim ETPL/WIOA approval**, "state-approved," or Express Course Directory listing
3. **Never invent statistics, outcomes, testimonials, salary figures, or quotes** — only use what's in the research brief
4. **Never promise funding approval** — always "may qualify"
5. **Never source facts from training providers, career blogs, or salary aggregators** — if the research brief didn't include it, the Writer doesn't add it
6. **Never use a backdated publish date** — use today's actual date
7. **Never remove or skip the `<!-- DRAFT -->` marker** — every post ships as a draft until Emilio approves
8. **Never write "our program," "our courses," "enroll now," or "apply" in guide-mode copy** — CSC has nothing to enroll in yet. Write both guide-mode and course-mode versions of every course-dependent CTA and document the course-mode version in `blog/course-mode-copy/[post-slug].md`
9. **Never describe a specific CSC credential** — say "healthcare" or "the medical field," not "Medical Billing & Coding program"

## 9. Working With the Content Strategist's Angle

The Content Strategist's recommended angle is the **north star** — the Writer doesn't get to ignore it and write a generic post:

- **The hook** from the strategy must shape the opening paragraph. If the strategist says "open with the honest cost breakdown most sites hide," that's the opening — not "Medical billing is a growing field."
- **The key differentiators** must each appear as real sections or prominent points in the post, not buried in a sentence somewhere.
- **If the angle says "honesty gap"** — competitors oversell and hide downsides — the Writer leans into that. Dedicate a full section to the hard truth. Make it the thing readers remember.
- **If the Writer disagrees with the angle**, write a note at the top of the output explaining why, but still follow it. The angle was chosen from competitive research; the Writer hasn't seen the SERP.
- **After writing, self-check:** Would a reader notice what makes this post different from the top 10 Google results? If not, the angle isn't showing enough — rewrite the intro and strengthen the differentiators.

## 10. Technical Execution

The Writer adds code to `tools/build-pages.py`, not hand-written HTML files:

- **Study existing blog posts** in build-pages.py before writing. Match the exact pattern: `PAGES.append(...)` block, `article()` helper, `post_cta()`, `related()`, `faq_ld()`, `article_ld()`.
- **Blog index card:** Add a card to the blog.html section at the top of the card grid (newest first).
- **Sitemap:** Add the post URL to the sitemap entries.
- **JSON-LD:** Every post gets both `article_ld()` (BlogPosting) and `faq_ld()` (FAQPage). No exceptions.
- **DRAFT marker:** `<!-- DRAFT -- facts to verify: [list key facts] -->` at the very top of the post content.
- **COURSE-DEPENDENT markers:** Every CSC mention and every CTA that will change when courses launch gets `<!-- COURSE-DEPENDENT: R-BLOG-xx -->`.
- **Author:** "Career Skills Center" (organization, not a person) unless told otherwise.
- **Category:** Match existing ones — Medical, Information Technology, Skilled Trades, Paying for Training, or Career Advice.
- **Publish date:** Today's actual date. Never backdated.
