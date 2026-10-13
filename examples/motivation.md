# Motivation lens: worked example

Two fresh agent sessions got the same draft and the same prompt: "Will this get at least 30 of 40 partners upgraded by March 1? Review it and tell me what to change." Both had my global instructions loaded. The only difference is that the second read [`lenses/motivation.md`](../lenses/motivation.md) first. Same model, 2026-10-13. The lens wording was tightened after this test; its rules are unchanged.

The draft is a fictional sample written for this test.

## The draft

> **Subject: Introducing SDK v3!**
>
> We're excited to announce SDK v3, our biggest release yet. v3 includes a redesigned rendering engine, 40% smaller bundle size, improved accessibility, new analytics events, dark mode support, a modernized API surface, better error handling, and TypeScript types out of the box.
>
> We recommend all partners upgrade at their earliest convenience. Full migration docs are available on our developer portal. v2 will reach end of support on March 1.
>
> Let us know if you have any questions!

## Without the lens (excerpts)

> No, this draft won't get you 30 of 40 on its own. It reads like a launch announcement.
>
> The deadline is buried. It never says what happens on March 1. It doesn't say how big the migration is. No owner, no next step.
>
> Tier the 40 partners before sending. Set milestones: target dates within two weeks, a mid-December checkpoint, a January nudge, a final notice.

A strong review with a practical follow-up plan.

## With the lens (excerpts)

> **The person and the moment:** the partner's integration engineer, opening this between other tickets. Their real goal is keeping the ad slot earning without surprises. Likely feeling (a guess): mild annoyance at more upgrade work, with no sense of urgency.
>
> v2 keeps running, so the default is to do nothing. A fix freeze isn't a forcing function until a bug hits.
>
> Eight features is a pitch for a switch they're being told to make anyway. Each extra reason adds resentment.
>
> **Second-order effect to decide on purpose:** if you hit 25 of 40, fifteen partners sit on an unsupported SDK. Decide now whether you'll enforce March 1 or quietly extend it. If you extend, partners learn the deadline is soft.
>
> **Cheapest test:** send the rewrite to five partners first and time the first migration step. If fewer than about 8 of 40 have started by mid-November, you're off pace.
>
> **Subject:** SDK v2 stops getting fixes on March 1: upgrade to v3 (about 2 hours for most integrations)
>
> The "two hours" figure is a placeholder. Use your real number, and if you can't say one confidently, find that out first.

## What changed

- **It started from the reader.** Naming the engineer and the moment they read it explains why the email fails: doing nothing is free for them.
- **It treated the feature list as a cost.** The baseline said to cut it for length. The lens said why: piling on reasons to do a required task breeds resentment.
- **It raised the decision behind the email.** Whether you'll enforce the deadline matters more than the wording, and the baseline never asked.

## What the lens missed

The baseline's follow-up schedule (target dates, checkpoints, a final notice) is more complete. The lens says to test and track pace, but it doesn't spell out the chase sequence that turns a 60% email into a 75% result.
