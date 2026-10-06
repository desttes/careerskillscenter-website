#!/usr/bin/env python3
"""Mechanical pre-review checks for a blog post (free; no LLM).

Usage:  python3 tools/blog-lint.py <slug>
Run `python3 tools/build-pages.py` first so blog/<slug>.html is current.
Exit code 0 = no FAIL lines, 1 = at least one FAIL (WARN lines never fail).

Checks (mirror the mechanical parts of the compliance reviewer):
  - every <p> has 1-2 sentences, at most 210 visible characters, no short fragments
  - visible word count (about 2,500 target; FAIL above 2,750)
  - numbers (dollar amounts, percentages, 3+ digit numbers) that appear in no pipeline file
  - banned phrases, DRAFT marker, COURSE-DEPENDENT markers, course-mode copy file
  - JSON-LD blocks parse; BlogPosting and FAQPage present
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_CHARS = 210
WORD_TARGET, WORD_FAIL = 2500, 2750
BANNED = [
    "according to", "percentile", "we did not find", "could not confirm", "source:", "sources",
    "our program", "our courses", "state-approved", "enroll with us", "apply to career skills",
    "soc code", "bureau of labor statistics says", "bls says",
]
# Words that may open a short sentence that is still complete ("No, they are different jobs.").
FRAGMENT_MIN_WORDS = 4

fails, warns = [], []


def fail(msg):
    fails.append(msg)


def warn(msg):
    warns.append(msg)


def visible(fragment):
    text = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def sentences(text):
    # Protect common abbreviations and decimals/prices before splitting.
    t = re.sub(r"\b(U\.S|e\.g|i\.e|vs|St|Mr|Mrs|Dr|No)\.", lambda m: m.group(0).replace(".", "\0"), text)
    t = re.sub(r"(\d)\.(\d)", r"\1\0\2", t)
    parts = re.split(r"(?<=[.!?])[\"')\]]*\s+", t)
    return [p.replace("\0", ".").strip() for p in parts if p.strip()]


def main(slug):
    page = ROOT / "blog" / f"{slug}.html"
    if not page.exists():
        sys.exit(f"missing {page}; run tools/build-pages.py first")
    raw = page.read_text()

    start = raw.find('class="container prose post-body"')
    if start < 0:
        sys.exit("could not find the post body (class 'prose post-body')")
    body = raw[start:]
    ends = [i for i in (body.find(m) for m in ("</article>", "</main>", "<footer")) if i > 0]
    if ends:
        body = body[:min(ends)]

    # --- paragraphs ---
    lede = re.findall(r'<p class="page-hero-lede">(.*?)</p>', raw, flags=re.S)
    paras = lede + re.findall(r"<p[^>]*>(.*?)</p>", body, flags=re.S)
    for i, p in enumerate(paras, 1):
        text = visible(p)
        if not text:
            continue
        sents = sentences(text)
        if len(sents) > 2 and not text.rstrip().endswith(":"):
            fail(f"paragraph {i}: {len(sents)} sentences: {text[:80]}...")
        if len(text) > MAX_CHARS:
            fail(f"paragraph {i}: {len(text)} characters (max {MAX_CHARS}): {text[:80]}...")
        for s in sents:
            if len(s.split()) < FRAGMENT_MIN_WORDS and not text.rstrip().endswith(":"):
                warn(f"paragraph {i}: possible fragment: \"{s}\"")

    # --- word count (H1 + body) ---
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', raw, flags=re.S)
    words = len(visible(" ".join(lede) + " " + body).split()) + (len(visible(h1.group(1)).split()) if h1 else 0)
    if words > WORD_FAIL:
        fail(f"word count {words} (target about {WORD_TARGET}, FAIL above {WORD_FAIL})")
    elif words > WORD_TARGET + 150:
        warn(f"word count {words} (target about {WORD_TARGET})")
    print(f"words: {words}   paragraphs: {len(paras)}")

    # --- banned phrases ---
    low = visible(body).lower()
    for phrase in BANNED:
        if phrase in low:
            fail(f'banned phrase in visible text: "{phrase}"')

    # --- numbers that appear in no pipeline file ---
    draft_dir = ROOT / "docs" / "blog-drafts" / slug
    corpus = ""
    for name in ("research-brief.md", "community-verification.md", "editorial-decisions.md",
                 "content-strategy.md"):
        f = draft_dir / name
        if f.exists():
            corpus += f.read_text() + "\n"
    if not corpus:
        warn(f"no pipeline files in {draft_dir}; skipped the numbers check")
    else:
        norm = corpus.replace(",", "")
        text = visible(body).replace(",", "")
        seen = set()
        for m in re.finditer(r"\$\d+(?:\.\d+)?|\d+(?:\.\d+)?%|\b\d{3,}\b", text):
            tok = m.group(0)
            if tok in seen or re.fullmatch(r"20\d\d", tok):  # skip years
                continue
            seen.add(tok)
            if tok.lstrip("$") not in norm:
                fail(f'number "{tok}" is not in the research brief, verification or decisions files')

    # --- markers and companion files ---
    if "<!-- DRAFT" not in raw:
        fail("no DRAFT marker")
    if "COURSE-DEPENDENT" not in raw:
        fail("no COURSE-DEPENDENT marker")
    if not (ROOT / "blog" / "course-mode-copy" / f"{slug}.md").exists():
        fail("missing blog/course-mode-copy file")

    # --- JSON-LD ---
    types = []
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', raw, flags=re.S):
        try:
            data = json.loads(block)
        except ValueError as e:
            fail(f"JSON-LD does not parse: {e}")
            continue
        for item in data if isinstance(data, list) else [data]:
            types.append(item.get("@type"))
    for needed in ("BlogPosting", "FAQPage"):
        if needed not in types:
            fail(f"JSON-LD {needed} missing")

    for w in warns:
        print("WARN", w)
    for f in fails:
        print("FAIL", f)
    print(f"{len(fails)} FAIL, {len(warns)} WARN")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
