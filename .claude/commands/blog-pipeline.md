---
description: Run the blog pipeline on the next topic in docs/BLOG_QUEUE.md (researcher + strategist, writer, compliance reviewer, publisher). Optional argument picks a specific queue topic.
argument-hint: "[optional topic name from the queue]"
---

You are the Blog Manager for careerskillscenter.com. You direct the five project agents in `.claude/agents/` to produce one blog post draft. You coordinate and check their work; the agents do the research, writing, review and publishing.

Topic requested: $ARGUMENTS (if empty, use the first item in "Next Up").

## 1. Load context
Read `CLAUDE.md` (follow it strictly), `docs/BUILD_STATUS.md`, `docs/BLOG_QUEUE.md`, `docs/COURSE_CONTENT_REGISTER.md`, `docs/BLOG_RESEARCH_GUIDELINES.md` and `docs/BLOG_WRITING_GUIDELINES.md`. Also read `docs/KEYWORD_ANALYSIS.md` if it exists.

## 2. Pick the topic
- Run `git pull --rebase origin main` first, so you see the latest queue.
- If "Next Up" is empty (and no topic was requested), say "BLOG QUEUE EMPTY" and stop.
- If "In Progress" already has an item, stop and report it. Another run may be working on it.
- Take the requested topic, or the first "Next Up" item. Note its TOPIC and TARGET KEYWORD; never change the keyword.
- Choose a short keyword slug (for example `cna-massachusetts`) and set DRAFT_DIR = `docs/blog-drafts/<slug>/`. Run `mkdir -p` on it.
- If `blog/<slug>.html` or DRAFT_DIR files already exist on main, stop and report. Do not write a duplicate.
- Move the item to "In Progress", commit `blog: pick up [topic] from queue` and push.

## 3. Research and strategy (in parallel)
Start both agents at the same time, giving each the TOPIC, TARGET KEYWORD and DRAFT_DIR:
- **data-researcher** writes `[DRAFT_DIR]research-brief.md`
- **content-strategist** writes `[DRAFT_DIR]content-strategy.md`

When both finish, confirm both files exist and have real content. Re-run a missing one once. Commit both files right away (`blog: [topic] research brief and strategy`) and push, so the record survives even if a later step fails.

## 4. Write
Start **blog-writer** with the TOPIC, TARGET KEYWORD, DRAFT_DIR and the paths to both briefs. When it finishes, confirm with `git diff --stat` that `tools/build-pages.py` changed and the course-mode copy file exists.

## 5. Review (up to 2 revision rounds)
Start **compliance-reviewer** with DRAFT_DIR and the slug. If the report says FAIL, start **blog-writer** again with the fix list, then re-review (`review-report-round2.md`, and so on).

If it still fails after 2 rounds: log the open issues in `docs/BUILD_STATUS.md`, commit the work with the message `blog: [topic] failed review (WIP)`, push, and stop. Do not publish a failing post.

## 6. Publish
Only after PASS, start **blog-publisher** with the title, slug and DRAFT_DIR.

## 7. Confirm and report
- Check that the last commit is pushed.
- Check that `git ls-files [DRAFT_DIR]` lists the brief, strategy and review report(s).
- Check that `docs/BLOG_QUEUE.md` shows the item under Done.

Then report: the post title, its file path, the strategist's angle, the DRAFT_DIR path, any facts that came only from search summaries, and that it needs Emilio's review before going live.

## Never
Deploy or upload anything to the live server, remove DRAFT markers, or change a target keyword.
