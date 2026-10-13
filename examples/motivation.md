# Motivation lens: worked example

Two fresh agent sessions got the same draft and the same prompt: "Will this get at least 30 of 40 partners upgraded by March 1? Review it and tell me what to change." Both had my global instructions loaded. The only difference is that the second read [`lenses/motivation.md`](../lenses/motivation.md) first. Same model, 2026-10-13.

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

> No, not as written. The draft gives partners no reason to act and no step to take.
>
> Pick an internal target date a month before the real one. Say what staying on v2 costs them. Give an effort estimate, a named contact, and ask each partner to reply with a target date.
>
> Track all 40 individually. Set checkpoints at 30 and 60 days. If v2 keeps working after March 1 and nothing visible changes, many partners will wait.

A strong review with a practical follow-up plan.

## With the lens (excerpts)

> **The person and the moment:** the engineering lead at a mid-size publisher, reading this in mid-October. Their Q4 is holiday traffic, so they're probably in a code freeze or close to one. They want stable revenue through the holidays and no surprises at their next quarterly review.
>
> **The baseline wins.** Partners keep running v2 because it works. Nothing in the email moves them off it.
>
> **"At their earliest convenience" tells them it can wait.** Nobody's convenience arrives during a holiday freeze.
>
> **Knock-on cost:** an all-partner blast also reaches quiet integrations that had no reason to change. Some will start a risky upgrade mid-freeze. Accept that on purpose, or segment the send.
>
> **Give a timeline that fits their freeze:** upgrade after the holidays, done by mid-February.
>
> **Cheapest test:** send the new version to 5 partners and ask each for a committed date within a week. If fewer than 3 name one, 30 of 40 is out of reach without one-to-one outreach.

## What changed

- **It found the real obstacle by picturing the reader.** A holiday code freeze explains the likely failure better than any wording issue, and it reshapes the timeline.
- **It counted the cost of the send itself,** not only the gain: quiet partners nudged into risky upgrades.
- **It came with an early, cheap read** that says within two weeks whether 30 is reachable.

## What the lens missed

The baseline's follow-up machinery is more complete: an internal deadline a month early, per-partner tracking, and fixed checkpoints. The lens says to segment and test, but the chase plan that gets from a good email to 30 of 40 came from the baseline.
