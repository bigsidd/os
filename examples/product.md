# Product lens: worked example

Two fresh agent sessions got the same message and the same prompt: "Should we commit to this? Give me your recommendation and what to reply." Both had my global instructions loaded. The only difference is that the second read [`lenses/product.md`](../lenses/product.md) first. Same model, 2026-10-13.

The message is a fictional sample written for this test.

## The ask

> Our largest publisher partner (about 22% of our revenue) wants a custom ranking feature: their own house offers always show first in our placement, ahead of advertiser offers, on every page. They say a competitor offered this and they want it in 6 weeks or they'll start testing the competitor. Engineering says it's about 4 weeks of work. Can we commit? I'd like to say yes today.

## Without the lens (excerpts)

> Don't say yes today. Say "yes to solving it" and commit to a scoped version after a quick check.
>
> If house offers always sit ahead of advertiser offers, the paid slot goes to an offer that earns nothing. That likely drops RPM on the publisher's own inventory.
>
> If any advertiser contract promises placement, "always first" could breach it.
>
> Once one partner has guaranteed first position, every other large publisher will ask for it. Offer a capped pilot with a holdout group.

A good answer. It catches the yield problem, the contract risk and the precedent, and proposes a pilot.

## With the lens (excerpts)

> **Recommendation: test first.**
>
> Their underlying goal is probably to control what their users see first, or to get paid for their own promotions. Get on a call and ask which.
>
> **Check the existing config before scoping any code.** A priority or pinned-slot setting may already do most of this. If it does, the answer is "configure what exists."
>
> **Precedent:** picture the next three partners. If they'd want a capped version, build that version once, not a custom one for this account.
>
> **Stop result:** the test shows a large RPM drop with no gain, and the partner still insists on the full spec. Then it's a pricing and retention decision for leadership, not a build decision.
>
> **Spend limit:** one week of account and product time plus a config-level test. No engineering build until the goal is clear.

## What changed

- **It asked what the partner is after** before judging the spec, and made that the first step.
- **It looked for a no-code answer first.** Four weeks of engineering may not be needed at all.
- **It turned one partner's ask into a product decision:** build the general version once, sized for the next three partners.
- **It set limits before starting:** what a week of testing may cost, and the result that ends the debate.

## What the lens missed

The baseline checked whether advertiser contracts promise a position, which could make "always first" a breach. The lens didn't. That check lives in the commercial lens, which is why a call like this runs more than one lens.
