---
name: anti-ai
description: Run before shipping any AI-assisted code, deck, document or data analysis. Catches the signs that nobody with judgment looked at it, and fabricated citations.
---

# Anti-AI Tells

AI output fails in a predictable way: on every choice with many good answers, it picks the most average one. Readers notice, even when they can't say why. This lens names the common tells and gives a rule for spotting new ones.

## Code

1. **Code the task never asked for.** Dead branches, stub comments, a helper class with one caller. Read for what's there that shouldn't be, not only for what's broken.
2. **Guards for states that can't happen.** A null check or try/catch around input the caller already guarantees is padding. Trace whether the state is reachable before keeping it.
3. **Every branch needs a real case.** If you can't name the user action or data shape that hits a branch, the branch is the tell.
4. **Comments that repeat the code.** Keep comments that explain why. Cut the ones that restate what.

## Decks and documents

1. **Three boxes on every slide.** If every section lands in three parallel boxes whatever the content, the layout came from the generator, not from you.
2. **Same bullet count and length everywhere.** Real writing varies with what each slide needs to say.
3. **Same visual weight on every page.** If nothing is quiet, nothing stands out.
4. **Generic icons for abstract ideas.** A "growth" arrow that points at nothing specific is decoration.

## Analysis

1. **Precise numbers from small samples.** "Up 23.4%" on twelve data points claims more than the data supports. Check the denominator.
2. **Three takeaways by default.** If the data supports one finding or five, say one or five.
3. **"Key insight" boxes around the obvious.** Save the emphasis for what would surprise someone who read the raw numbers.
4. **Hedging that never lands.** An analysis exists to make a call. Make it.

## Citations

This is the one with real consequences. Fabricated cases have already led to court sanctions.

1. **Check every citation, quote and statistic against its source before it ships.** Confirm the source exists and says what you say it says. No exceptions.
2. **If you can't verify a number, cut it or label it as unverified.**

## Spotting new tells

For any choice in the work that had many valid answers (a word, a layout, a structure, a framing), ask what the most expected answer would be. If the work picked exactly that on every axis, the averageness is the finding, even when nothing looks wrong on its own.

## After a tell is flagged

1. **Fix the cause, not the sentence.** Regenerate with the specific thing to avoid named. If the tell comes back, the fix has to be structural.
2. **Compare against a real example.** Where a strong human-made version exists, put them side by side.
3. **Verify the fix.** "Should be fixed" and "checked and fixed" are different claims. Only the second one is done.
