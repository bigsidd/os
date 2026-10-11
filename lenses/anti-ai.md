---
name: anti-ai
description: Run before shipping any AI-assisted code, deck, document, or data analysis. Covers code-structure tells, deck and document layout tells, analysis tells, fabricated citations, and a principle for predicting new tells. Complements writing-level humanizers and UI de-slop tools.
---

# Anti-AI Tells

Read this before shipping any AI-assisted code, deck, document, or analysis where the output might carry visible AI tells. This file covers what's genuinely new or uncovered elsewhere — it does not restate `de-ai-ify` (CSS/UI slop patterns), `humanizer` (writing tells), or `typography` (UI text rules). Those three skills already own their domains; run them where they apply, and use this file for code structure, deck/document layout, analysis presentation, citation integrity, and the underlying mechanism that predicts new tells before anyone's catalogued them. Content here is built from a mix of published evidence and observed field pattern — each lens states explicitly which kind it is.

## Code-Structure Tells (run before shipping any AI-assisted code beyond styling — `de-ai-ify` covers CSS/UI, this covers code structure and logic)

1. **Flag "garbage code" as its own category, distinct from bad code.** Unnecessary code that doesn't serve the task — dead branches, comment-only stubs, logic that runs in the wrong direction for the stated goal — is a tell independent of whether the code even works. Read for what's present that the task never asked for, not just for what's broken.
2. **Over-engineered indirection is a tell on a one-off task.** A helper class, interface, or abstraction layer built for a single call site is disproportionate scaffolding — check whether the task's actual scope justifies the structure, or whether the structure was generated because it's the "expected" shape for that kind of problem.
3. **Defensive checks for states that structurally cannot occur are a tell, not caution.** A null-check, try/catch, or fallback branch guarding against an input that the calling code already guarantees can't happen is padding, not safety — trace whether the guarded state is actually reachable before treating the check as earned.
4. **Comments that restate WHAT over comments that explain WHY.** A comment that re-describes the line below it in English adds no information; a comment worth keeping explains a decision, a constraint, or a non-obvious reason — grep for comment density that tracks line count rather than decision density.
5. **Use reuse discipline and churn timing as the empirical fingerprint, not vibes.** Low code-reuse discipline — high duplication or copy-paste where extraction was the obvious move — and unusually high near-term churn — code revised again within days of being written — are both grep-able and reviewable. Check `git log` on recently-written files for revision frequency before trusting that a first pass was a real first pass.

## Manual Detection Beats Tools (run whenever deciding whether AI-generated output is trustworthy without running a detector)

1. **Don't reach for a stylometric detector — pattern-match holistically instead.** Classic AI-content detectors don't reliably transfer to catching real AI output; a human who works with LLM output daily and reads for the whole shape of the artifact outperforms an algorithmic score. Treat a detector's number as noise, not evidence.
2. **For code, require a named real input for every branch.** Every conditional, case, or handler should map to a scenario you can actually name — a real user action, a real data shape, a real failure mode. If you can't name a concrete situation that hits a given branch, that branch itself is the tell, independent of whether the code runs correctly.
3. **For any output, check for at least one genuinely surprising choice.** Ask whether a single decision in the artifact — a word choice, a structural call, a tradeoff — required something other than the median, most-expected answer. If every choice in the artifact resolves exactly as the flattened, default answer would, that absence of any surprising choice is itself the finding — don't shrug past it because nothing individually looks wrong.

## Deck/Document Tells (run before shipping any AI-assisted deck or document — distinct from `de-ai-ify`'s web-UI list)

1. **Three-box content chunking is the default AI layout — treat it as a tell, not a format.** When every slide or section resolves into exactly three parallel boxes regardless of what the content actually needs, that's the generator's default shape asserting itself, not a considered layout choice.
2. **Uniform bullet length and count across every slide is a tell.** Real writers vary — sometimes two bullets, sometimes one standalone line — driven by what that specific slide needs to say. Identical bullet cadence slide after slide is the flattened, no-judgment version.
3. **Generic flat single-color line icons standing in for abstract concepts are a tell.** An icon meant to represent "growth" or "strategy" with no real referent to the actual content is decoration borrowed from a stock set, not a considered visual choice — check whether each icon actually maps to something specific in the material.
4. **Identical visual weight and density on every slide is a tell.** If nothing is de-emphasized, nothing is actually emphasized either — real decks vary density and weight based on which slide is carrying the argument that moment.
5. **Do not cite unverified detection-rate statistics as fact.** A claim along the lines of "most viewers can identify an AI-made deck within a few slides" could not be verified to a primary source during research for this file. Do not present a number like that as settled research — omit it, or if referenced at all, label it explicitly as unconfirmed folklore, never as a cited finding.

## Analysis/Data Presentation Tells (run before shipping any AI-assisted analysis, chart, or data narrative)

**Evidence-base note:** unlike the other lenses in this file, this one is the author's own observed field pattern, not yet backed by published research. Treat it as a real but unverified pattern, not settled doctrine.

1. **Spurious precision on a tiny sample is a tell.** A specific percentage change reported with unwarranted confidence from a small-n result reads as more certain than the data supports — check the denominator before trusting the precision of the number stated.
2. **A default three-takeaways structure regardless of fit is a tell.** If the analysis actually supports one dominant finding or five real ones, forcing it into three is the generator's default shape, not the honest shape of the data.
3. **A "key insight" callout regardless of actual novelty is a tell.** If the boxed insight is something anyone reviewing the raw numbers would already expect, the callout is theater — reserve the visual emphasis for findings that are actually surprising.
4. **Hedge-then-conclude phrasing that never commits is a tell.** In analysis specifically, it shows up as raising a claim and immediately qualifying it into non-committal mush without ever landing on a stated position — avoiding the actual judgment call the analysis was supposed to make.

## Verify-Don't-Fabricate (run before any citation, quote, or specific factual reference goes into outbound work)

1. **Treat a fabricated citation as the single highest-consequence tell category here.** Across documented cases where AI-generated work caused someone real legal or reputational damage, the mechanical, recurring failure is identical: a citation, quote, or reference that simply doesn't exist, presented with full confidence. This is not hypothetical — real, sanctioned court cases exist from exactly this failure mode.
2. **Verify every citation, quote, and specific reference against the actual source before it ships — no exceptions.** Unlike the aesthetic/quality tells elsewhere in this file, this one carries documented real-world consequences, which is why it gets a harder rule than "notice and consider fixing." Confirm the source exists and says what it's being cited as saying, every time, before it goes outbound.

## The Generalizing Principle (run whenever encountering an AI-tell category not covered by any lens above, or by `de-ai-ify`/`humanizer`/`typography` — read this one to predict a new tell before anyone's written a checklist for it)

1. **Alignment training collapses output toward the single most "expected" choice along any axis with many valid options.** This applies across vocabulary, color and layout, code structure, slide layout, analysis framing, and citation confidence — anywhere the model had real choices, it tends toward the flattened median one.
2. **Operationalize it this way:** pick any creative or judgment axis present in the work — not just the ones already catalogued above — and ask what the single most expected, flattened, median answer would look like on that axis. That flattened answer is the tell, independent of whether it matches a pattern that's already been written down. When output is suspiciously average along an axis where real variation was possible, treat the averageness itself as the finding.

## Verification Workflow (run immediately after any lens above flags something — the missing "now what" step)

1. **Don't patch the surface symptom — re-generate with a more specific, constrained prompt that names the exact thing to avoid, then check whether the same tell recurs.** If it does, the fix needed is structural, not a better prompt — a prompt-level fix that doesn't hold on a second attempt is signal, not noise.
2. **Force a named, concrete alternative before accepting the first output as fixed.** Generate a second real option and compare the two side by side, rather than accepting whatever came back from the first correction attempt as automatically resolved.
3. **Where a real human-made example of the same artifact type exists, diff against it directly.** Comparing the AI output to an actual reference beats relying on memory of what "good" is supposed to look like.
4. **Treat a flagged tell like a data bug: verify the fix against real output, don't trust that the patch should have worked.** A tell that "should be fixed now" and a tell that's actually confirmed fixed are different claims; only the second one is done.
