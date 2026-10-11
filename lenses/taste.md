---
name: taste
description: Run last, as the verdict, before approving anything people outside the team will see (partner or customer copy, change notices, docs, decks, pricing, demos) and before giving a verdict on someone else's work. Not for code, refactors, READMEs, PR descriptions, tickets, or internal FYIs.
---

# Taste

Run this after every other check, as the final call on whether an artifact is good enough to put your name on. It returns a verdict someone can act on.

## Before judging

1. **Write what the artifact is for in one sentence, then judge it against that sentence only.** A partner change notice is for keeping trust while the terms move. A pricing page is for making the decision feel safe. If you can't write the sentence, the review isn't ready. Every comment traces back to it.
2. **Name the reader and the one thing they should do after reading.** If the artifact asks for nothing, it's an FYI and this lens doesn't apply.

## What good looks like

1. **The ask is on the first screen.** If the reader has to scroll to learn what you want, it isn't done.
2. **Cut test.** Delete the first paragraph. If nothing is lost, it was throat-clearing.
3. **Forward test.** Would the recipient forward it internally unchanged? If they'd have to explain it to their boss, rewrite it.
4. **Money is findable.** If it touches RPM, yield, fill rate, conversion or payout, the reader can find the number and the date it changes. If there's no real revenue angle, don't invent one.

## AI-smell check

Read it out loud as the recipient. Hedge-then-conclude phrasing, forced groups of three, the same bullet length everywhere, and a pleasant closer with no next step all tell the reader nobody cared. Cut them first; they hide the real problems. A stat nobody verified doesn't ship. See [`anti-ai`](anti-ai.md) for the full list.

## The verdict

1. **State confirmed problems as fact. Ask uncertain ones as a concrete question.** "The payout line is wrong for partners on net-30" beats "I wonder if the payout line might be confusing."
2. **The why ships with the verdict.** Tie it to the one-sentence job. If you can't state the why, you don't have a verdict yet.

## Output

- The artifact's job, in one sentence.
- Verdict: **ship**, **ship with fixes**, or **not yet**.
- Why, in one or two lines.
- Fixes as rewritten text. "Make it punchier" is not feedback.

Worked example: [`examples/taste.md`](../examples/taste.md).
