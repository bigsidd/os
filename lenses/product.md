---
name: product
description: Run before committing people or money to a new direction, before saying yes to a partner or customer ask that implies new build, and before making a prioritization call between options. Not for routine implementation, copy review, or pricing a deal that's already been scoped.
---

# Product Judgment

Most bad product calls come from starting with what we can build instead of who needs it. This lens moves the conversation back to the person and the outcome. It returns a decision with its reasoning attached.

## Before anything else

1. **Name the person and what they're trying to get done right now.** A real role at a real company, in a real moment. If you can't say it concretely, you aren't ready to judge the idea.
2. **Treat the request as one possible answer to a goal nobody stated.** Ask what they're really trying to do. The goal tends to carry over to other customers. The specific request rarely does.
3. **Translate vague value claims into behavior.** "Easy to use" or "adds value" can make anything sound good. Say what the person will do differently and why. If the claim doesn't survive that, drop it.

## When a partner asks for something new

1. **Ask whether it will recur.** The test is whether other partners will want the same shape of thing. One partner's urgency, however loud, isn't enough to justify building for everyone.
2. **Check for an existing setting first.** A targeting rule or config option often covers the need with no new code. If it does, say so and push back on the ask as written.
3. **Pick the response on purpose:** decline, narrow the scope, send them to someone who already solves it, or do it once as an exception. Then ask the tiebreaker out loud. Does this partner's volume justify custom work, and does yes here commit us to the next partner who asks?
4. **Keep integrations consistent.** If one partner's request would break naming or behavior that every other integration relies on, the answer is no, even when it looks reasonable on its own.
5. **Lead the reply with what they can do today,** then ask about the goal before offering a counter-proposal.

## Before funding a new bet

1. **Write four things down.** Who will act and why (the demand hypothesis). What changed that makes this possible now. The most you'll spend before you get a real read. The result that would kill it.
2. **"The pieces exist" explains timing, nothing more.** It doesn't show anyone wants the thing.
3. **Find the cheapest honest test.** An afternoon that removes real doubt beats a finished feature nobody asked to see. Start from the assumption it won't work and look for evidence against it.
4. **Make people rank the problem.** Asked in isolation, everyone says their current problem matters. Ask where it sits against their other priorities.
5. **When model output is the product, write the eval first.** A set of real cases with pass/fail criteria does the job a spec used to do.
6. **Label pure capability experiments as such.** No demand hypothesis yet, sized only by what you can afford to lose, with a stated second job: a demo, a proof, or groundwork for something bigger.

## Choosing between options

1. **Agree on the principles before debating the options.** List what this decision has to satisfy, rank them, then pick the option that serves the top ones. A better third option often shows up during the ranking.
2. **Check the question for a bad assumption** before answering it as asked.
3. **Keep generating and judging apart.** Feasibility objections during brainstorming kill ideas that were fine. Collect first, then cut.
4. **Compare generated variants before writing a spec.** Where you can prototype output directly, put real versions side by side instead of describing an imagined one.

## Shipping it

1. **Ship before polishing.** You don't know what to polish until people use it.
2. **Keep the craft that makes the idea work.** If a detail is the whole point, the plain "for now" version is a different and worse product, and the follow-up polish rarely ships.
3. **In the first days, read real reactions.** A few genuine user responses tell you more than a dashboard with no volume behind it.
4. **Build so outside improvements compound.** If the models or tools underneath get better and cheaper on their own, design so you inherit that instead of freezing a spec around today's limits.

## Before a big launch

1. **Run a pre-mortem.** Assume it failed badly three months from now and ask why. Have people write reasons alone first, then share one at a time so the senior voice doesn't set the frame.
2. **Ask for the risk everyone knows about and nobody says.** That's usually where the damage is.
3. **Know who decides.** A high-stakes launch needs a named person who signs off at a set point. An assumed approval doesn't count.

## Measuring it

1. **Trace inputs to outputs to outcomes.** "We shipped it" is an output. Say which outcome it was meant to move and by how much.
2. **Keep usage and adoption separate.** Heavy use by existing users can hide that nobody new is picking the feature up. Those need different fixes.
3. **Judge early bets on what they taught you.** Holding a new bet to the revenue standard of a mature product punishes exploring.

## Your own time

If you've done the same judgment call by hand three times, write the playbook instead of doing it a fourth. It needs an owner, a trigger, and the exceptions. A list of steps alone is just documentation.

## Output

- The person, and what they're trying to get done.
- Recommendation: **build**, **configure what exists**, **test first**, or **decline**.
- The reasoning, including the precedent it sets.
- For a new bet: demand hypothesis, why now, loss cap, and kill test.
- The outcome metric it should move.
