# Product lens: worked example

Two fresh agent sessions got the same message and the same prompt: "Should we commit to this? Give me your recommendation and what to reply." Both had my global instructions loaded. The only difference is that the second read [`lenses/product.md`](../lenses/product.md) first. Same model, 2026-10-13.

The message is a fictional sample written for this test.

## The ask

> Our largest publisher partner (about 22% of our revenue) wants a custom ranking feature: their own house offers always show first in our placement, ahead of advertiser offers, on every page. They say a competitor offered this and they want it in 6 weeks or they'll start testing the competitor. Engineering says it's about 4 weeks of work. Can we commit? I'd like to say yes today.

## Without the lens (excerpts)

> Don't commit today, and don't say no. Commit to the problem and to a date for a scoped plan.
>
> "House offers always first, on every page" removes the highest-paying offer from slot one. If their house offers earn less per impression, the partner loses money too.
>
> A bespoke ranking override becomes the precedent every large partner asks for next.
>
> Offer a scoped pilot: a reserved first position with a frequency cap, run as a holdout test.

A good answer. It catches the yield problem, flags precedent, and proposes a pilot.

## With the lens (excerpts)

> **Recommendation: test first, with a narrowed scope.**
>
> "Always first, every page" is one answer to a goal nobody stated. The goal is probably one of three: promote their own offers, guarantee them a minimum placement, or avoid being outbid by advertisers. Each needs a different build. Ask which before scoping anything.
>
> **It will recur.** Any publisher with its own products will want this once they hear it exists. If we build it, build a generic partner-level setting with caps, not a custom feature for one partner.
>
> **Check for an existing setting first.** Engineering should confirm whether priority or targeting already covers house offers before anyone scopes four weeks of work.
>
> **Kill test:** if always-first drops the partner's total earnings on the test slice, they may not actually want it.
>
> **Outcome metrics:** partner revenue per session and our earnings on the account, against control.

## What changed

- **It asked what the partner is actually after.** The baseline judged the request as written. The lens split it into three possible goals that each lead to a different build.
- **It turned a one-off into a product decision.** "This will recur, so build the general setting" is the difference between serving one loud partner and building something every partner can use.
- **It checked for an existing setting before costing new work.** Four weeks of engineering may not be needed at all.
- **It came with a kill test and an outcome metric,** so the pilot has a result that ends the debate either way.

## What the lens missed

The baseline asked whether any advertiser contracts promise a position, which could make "always first" a breach. The lens didn't raise it. That check belongs in the commercial lens, which is why more than one lens runs on a call like this.
