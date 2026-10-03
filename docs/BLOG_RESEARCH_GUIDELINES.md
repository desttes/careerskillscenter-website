# Blog Research Guidelines

These guidelines are read by the blog pipeline's **Data Researcher** and **Content Strategist** agents.

---

## Part A — Data Researcher

### 1. Source Hierarchy
Use sources in this priority order:
1. **Government:** BLS.gov (pay, outlook), mass.gov & state licensing boards (licensing), DOL.gov
2. **Official certifying bodies** for their own credentials: AAPC (CPC/CPB), AHIMA (CCA/CCS), CompTIA (A+/Network+/Security+), OSHA (safety certs), EPA (608), etc.
3. **Neutral career data:** O*NET, CareerOneStop
4. **Never use:** salary aggregators (Glassdoor, Indeed, ZipRecruiter, Salary.com, Payscale), training provider or education company websites, other career/training blogs, or any source with a financial interest in steering readers toward a product or program

### 2. Geographic Scope
Lead with **national data**. No Massachusetts-specific framing — these are nationwide certifications and careers. If a state-specific requirement exists (like a state license), note it as "some states require..." without centering the post on Massachusetts.

### 3. Required Data Points (every brief must include)
1. **BLS median pay** — annual + hourly, national, with SOC code cited
2. **Job outlook** — % growth and timeframe (e.g., "8% from 2025–2035, much faster than average")
3. **Licensing/certification requirements** — what's required, what's optional, which body manages it
4. **Typical training path and duration** (general industry info, NOT Career Skills Center specifics)
5. **Employer demand** — projected job openings, top industries hiring, growth drivers
6. **4–6 FAQ questions** sourced from Google People Also Ask, autocomplete, and related searches

**Optional (include when available):**
- Entry-level vs experienced pay range
- Related/adjacent occupations
- Remote work feasibility
- Top employers or sectors

### 4. Missing Data
If a data point can't be found from a trusted source, mark it as:
```
[DATA NOT FOUND — searched: source1, source2, source3]
```
Never substitute from an untrusted source. The Writer will work around the gap.

### 5. Certification Depth
For each relevant credential, gather:
- Managing body (AAPC, AHIMA, CompTIA, etc.)
- Credential name (CPC, CCA, A+, etc.)
- Eligibility requirements
- Exam format: number of questions, time limit, passing score
- Exam cost
- Renewal cycle
- Whether employers prefer or require it

Source everything from the certifying body's official site.

### 6. Exclusions
**Never source information from:**
- Training providers or education company websites (they steer info toward their own products)
- Other career/training blogs (not expert sources)
- Salary aggregators (Glassdoor, Indeed, ZipRecruiter, Salary.com, Payscale)
- Any source with a financial interest in steering the reader toward a product or program

### 7. FAQ Sourcing
Find FAQ questions from real search behavior:
- Google "People Also Ask" boxes
- Google autocomplete suggestions
- Related searches at the bottom of Google results

These reflect what actual readers are looking for, not what experts think they should ask.

### 8. Research Brief Format
Write findings to `research-brief.md` with this structure:
```
## Topic: [TOPIC]
## Target Keyword: [keyword]
## Pay Data (BLS OEWS, National)
## Job Outlook
## Licensing & Certification
## Training Paths (general industry)
## Employer Demand
## FAQ Questions (4-6)
## Sources (full URLs)
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
