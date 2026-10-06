# Blog Research Guidelines

These guidelines are read by the blog pipeline's **Data Researcher** and **Content Strategist** agents.

---

## Part A — Data Researcher

### 1. Source Hierarchy
Use sources in this priority order:
1. **Government:** BLS.gov (pay, outlook), mass.gov & state licensing boards (licensing), DOL.gov
2. **Official certifying bodies** for their own credentials: AAPC (CPC/CPB), AHIMA (CCA/CCS), CompTIA (A+/Network+/Security+), OSHA (safety certs), EPA (608), etc.
3. **Neutral career data:** O*NET, CareerOneStop
4. **Official program pages (Emilio, 2026-10-05):** public colleges, public workforce programs (MassHire, state-funded training), nonprofits and employers' own training pages. Allowed **only for that program's own facts**: hours, length, externship hours, cost, funding and dates. Record the date you checked.
5. **Never use:** salary aggregators (Glassdoor, Indeed, ZipRecruiter, Salary.com, Payscale), for-profit course sellers and lead-generation sites ("find programs near you", sponsored listings), or any source with a financial interest in steering readers toward a product or program. Career blogs may be read for leads only; a fact found only on one is marked `[SECONDARY: url]` and checked against an official page where possible.

### 1b. Read the top search results (Emilio, 2026-10-05; trimmed 2026-10-05 to save tokens)
Search the target keyword (and close variants) and open results until you have read **5 usable pages** (cap: 10 pages opened), using WebFetch or the browser tools (with a character limit) when a page blocks the fetch tool. **Skip any page that is trying to sell you a course** (enroll buttons, lead forms, "find programs near you", sponsored listings, for-profit schools); skipped pages do not count toward the 5. Log every URL as read or skipped, one line each. Use these pages to find the concrete facts readers need, then record each fact with the most official source you can find. The research brief itself stays about 1,500 words (hard cap 2,000).

### 2. Entry Requirements Filter
Only include careers/certifications that can be obtained with **no prior experience or education beyond a high school diploma or GED**. If a role requires a college degree, prior clinical experience, or any credential that itself requires higher education, exclude it from the research brief. The audience is working adults with a GED/high school diploma looking for accessible career paths.

### 3. Geographic Scope
Lead with **national data**. These are nationwide certifications and careers. For certifications managed by a national body (AAPC, AHIMA, NHA, etc.), present them as national credentials. For **state-level licenses** (like CNA registry, pharmacy tech license), note that requirements vary by state — guide readers to check their own state's licensing board, and include Massachusetts rules as a specific example. Don't center the entire post on Massachusetts, but don't ignore state-specific requirements either.

### 4. Required Data Points (every brief must include)
1. **BLS pay** — the median annual pay **and the 10th-percentile annual pay** (the entry-level figure), with SOC code cited. National for a nationwide credential; the state figure for a state-issued license (Emilio, 2026-10-05). No other percentiles. Include hourly only if annual is unavailable.
2. **Job outlook** — % growth and timeframe. Skip the BLS label ("faster than average") — just give the number and let the Writer contextualize it.
3. **Licensing/certification requirements** — what's required, what's optional, which body manages it
4. **Typical training path and duration** (NOT Career Skills Center specifics) — concrete figures: months, total hours, externship or clinical hours, whether evening/weekend options exist, whether any part is online. When BLS or DOL give none, use what public colleges, certifying bodies and official program pages publish.
5. **Typical training cost range** — concrete dollar ranges. Use neutral sources first (BLS, CareerOneStop, DOL); when they have none, use the published prices of public colleges and official program pages, and say which. If multiple program lengths exist (e.g., 4-week vs 4-month for medical billing), note the range for each. Use `[DATA NOT FOUND]` only when no official page publishes a figure. This is one of the reader's first questions — don't skip it.
5b. **Example programs** — 2 to 4 named public, nonprofit or employer programs (state-relevant for a state post), each with hours, externship hours, cost or funding, and dates, taken from the program's own official page, with the date you checked.
6. **Employer demand** — projected job openings, top industries hiring, growth drivers
7. **4–6 FAQ questions** sourced from Google People Also Ask, autocomplete, and related searches

**Optional (include when available):**
- Entry-level pay estimate (if available from BLS 25th percentile)
- Related/adjacent occupations
- Remote work feasibility
- Whether you can train while working a full-time job

### 5. Missing Data
If a data point can't be found from a trusted source, mark it as:
```
[DATA NOT FOUND — searched: source1, source2, source3]
```
Never substitute from an untrusted source. The Writer will work around the gap.

### 6. Certification Depth
For each relevant credential, gather:
- Managing body (AAPC, AHIMA, CompTIA, etc.)
- Credential name (CPC, CCA, A+, etc.)
- Eligibility requirements
- Exam format: number of questions, time limit, passing score
- Exam cost
- Renewal cycle
- Whether employers prefer or require it

Source everything from the certifying body's official site.

### 7. Exclusions
**Never source information from:**
- For-profit training providers, course sellers and lead-generation sites (they steer info toward their own products). Public colleges and public or employer programs are allowed for their own program facts (see 1.4).
- Other career/training blogs as the only source (read them for leads; mark `[SECONDARY]`)
- Salary aggregators (Glassdoor, Indeed, ZipRecruiter, Salary.com, Payscale)
- Any source with a financial interest in steering the reader toward a product or program

### 8. FAQ Sourcing
Find FAQ questions from real search behavior:
- Google "People Also Ask" boxes
- Google autocomplete suggestions
- Related searches at the bottom of Google results

These reflect what actual readers are looking for, not what experts think they should ask.

### 9. Research Brief Format
Write findings to `research-brief.md` with this structure:
```
## Topic: [TOPIC]
## Target Keyword: [keyword]
## Pay Data (BLS OEWS, National)
## Job Outlook
## Licensing & Certification
## Training Paths (general industry — include duration and cost range)
## Employer Demand
## FAQ Questions (4-6)
## Sources (full URLs, SOC codes here — not in the body text the reader sees)
```

---

## Part B — Content Strategist

**This is the most important step in the entire blog pipeline.** The goal is to find an angle that makes our post genuinely different from everything already ranking — not a rewrite of existing content, but something that fills a real gap.

### What to Deliver
Write findings to `content-strategy.md` with the structure below.

### Process

#### 1. Deep SERP Audit
Analyze the **top 10 ranking pages** for the target keyword. For each, note:
- Title and URL
- Word count (approximate)
- Structure/format (listicle, step-by-step guide, table-heavy, Q&A, etc.)
- Key topics covered
- Tone (salesy, academic, casual, authoritative)
- Date last updated

#### 2. Content Gap Map
What questions appear in "People Also Ask" that **none of the top results answer well**? These are opportunities — real questions from real searchers that the current top pages miss or gloss over.

#### 3. Structural Gaps
Do all top results use the same format? If every result is a listicle, a well-structured comparison table stands out. If every result is a wall of text, a scannable guide with clear sections wins. Identify what format is missing.

#### 4. Freshness Gaps
Are the top results outdated? Look for:
- Old BLS data (anything older than May 2025)
- Expired certification requirements or exam formats
- Outdated job outlook numbers
- References to discontinued programs or policies

#### 5. Honesty Gaps
Where do competitors oversell, make vague promises, or hide downsides? Our angle is **honest, no-BS career guidance** — we don't have courses to sell yet, so we can afford to be straight with readers. Look for:
- Unrealistic salary promises ("earn six figures!")
- Glossed-over difficulty or time commitment
- Missing information about licensing hurdles
- "Easy career change" framing that hides real barriers

#### 6. Underserved Audience
Are the top results written for a different audience than ours? Look for gaps in serving:
- Career changers (not just new grads)
- ESL readers / plain-language seekers
- People exploring options (not ready to enroll somewhere)
- People who need funding help (WIOA, grants, employer-paid)

#### 7. Final Recommendation
Write a specific, actionable recommendation:
- **The angle:** one sentence describing what makes this post different
- **The hook:** how the post opens to grab attention
- **Key differentiators:** 2-3 specific things this post will cover that the top results don't
- **Why this wins:** why a reader (and Google) would prefer this post over what's already ranking

### Editorial round
After the community researcher runs, the strategist also reviews its candidates (KEEP / MAYBE / CUT, fit, balance, quote vs. paraphrase). See Part C.

### Content Strategy Output Format
```
## Content Strategy: [TOPIC]
## Target Keyword: [keyword]

## SERP Audit (top 10)
| # | Title | Format | Updated | Key Gap |
|---|-------|--------|---------|---------|

## Content Gaps Found
- [Gap 1: question/topic not answered well]
- [Gap 2: ...]

## Structural Opportunity
[What format is missing from the SERP]

## Freshness Opportunity
[What's outdated in the top results]

## Honesty Opportunity
[Where competitors oversell — our honest angle]

## Audience Opportunity
[Who the top results aren't serving]

## RECOMMENDED ANGLE
**Angle:** [one sentence]
**Hook:** [opening approach]
**Key differentiators:**
1. [specific thing we'll cover that others don't]
2. [...]
3. [...]
**Why this wins:** [why readers/Google prefer this]
```

---

## Part C — Community Researcher and the Editorial Round

**Why this exists:** other career blogs repeat the same official facts. What they don't have is what real people who did the job, or tried to get into it, went through. That first-hand experience is highly valuable to our reader, so we go and find it. (Emilio, 2026-10-04.)

### 1. Where to look
Reddit, Quora, public forums, and public Facebook posts or groups that show up in search. Never log in or get around a login. Prefer posts from the last 3 years.

### 2. What counts
First-hand experiences, honest opinions, tips, warnings, surprises and hidden costs that are **not already in the research brief or strategy**. Skip promotion, rants with no useful detail, posts about named people, and non-U.S. situations unless the point applies everywhere.

### 3. Forum posts are never a fact source on their own
Any number or rule inside a post (cost, hours, pay, pass rate, license rule) must be checked by the Data Researcher against an official source. CONTRADICTED claims kill the item. UNVERIFIABLE claims are dropped from the item. If the post gives a number, the blog uses the verified official figure.

### 4. Corroboration
An experience goes in only if at least 2 independent people in separate threads describe it, or an official source backs it up. Report the real mix of views. We never keep only the encouraging side.

### 5. Quotes
The team decides whether a quote is worth it. A quote must be clearer or more human than our own words, 25 words or fewer, exact, easy for a basic-English reader, and free of names, employers, places or other identifying details. Otherwise we paraphrase. This is Emilio's exception (2026-10-04) to the CLAUDE.md rule that quotes come only from consenting students. It applies only to items approved through this process.

### 6. Nothing that points to the person
No usernames, no thread links and no identifying details in the post. Source URLs stay in `community-insights.md` (internal) so reviewers can confirm every quote is real.

### 7. The editorial round (agents decide together)
1. **Community Researcher** proposes candidates in `community-insights.md`.
2. **Data Researcher** (verification mode) checks their facts in `community-verification.md`.
3. **Content Strategist** (editorial mode) judges value, fit and balance in `community-editorial.md`.
4. **The director** applies the rules above and writes `editorial-decisions.md` (approved items, where they go, quote or paraphrase, and the cut list with reasons). The stricter call wins; when unsure, cut.
5. **Writer** uses only approved items.
6. **Compliance Reviewer** checks that every experience and quote in the post was approved and used faithfully.
