# How I make product calls

**Fourteen rules for deciding what's worth building.**

I build products and the partnerships that make them pay. Eighteen years across customer success, partnerships and product, the last decade in adtech. These days I build most of my own tools with agents. More at [siddharthshah.me](https://siddharthshah.me).

## Deciding what gets built

1. **[Who is it for, and when?](rules/who-is-it-for.md)** Name the person, the moment they hit the problem, and what they do about it today.
2. **[What are they really after?](rules/what-are-they-really-after.md)** A request is someone's first guess at a fix. Solve the goal behind it. One loud request is one data point.
3. **[Does it beat what they do now?](rules/does-it-beat-what-they-do-now.md)** The problem has to rank near the top of their list, and the new way has to clearly win. Judge by what people did, not what they say they'd do.
4. **[Know who you're not serving.](rules/know-who-youre-not-serving.md)** Know whose needs come first, why they'd choose this, and what you're happy to be worse at. Turn down what pulls toward someone else.
5. **[Most ideas don't work.](rules/most-ideas-dont-work.md)** Before building, say what someone will do differently because of this. If I can't, I don't build it.
6. **[Cheapest answer first.](rules/cheapest-answer-first.md)** A setting, a manual edit or a small test, if it gets the same result. Build when the shortcut gives up something that matters.
7. **[Rough, not hollow.](rules/rough-not-hollow.md)** Ship early where real use will answer the question, but never cut the detail the idea depends on.
8. **[Make the first step easy.](rules/make-the-first-step-easy.md)** People act when they want it enough, it's easy enough to do, and something prompts them. If one is missing, more enthusiasm won't fix it.
9. **[Say what should change.](rules/say-what-should-change.md)** "Shipped" is the middle of the story. Name the result and how you'd see it.
10. **[Only ask what changes the decision.](rules/only-ask-what-changes-the-decision.md)** If every answer leads to the same call, make the call.

## When a model does the work

11. **[Code before a model.](rules/code-before-a-model.md)** Use a model only for what code can't do. If a rule, a lookup or a form gets the result, use that.
12. **[Show where it breaks.](rules/show-where-it-breaks.md)** Before shipping anything a model decides, read real outputs, name how it fails, and set the pass bar it has to clear.

## Weighing them

13. **[Play it forward.](rules/play-it-forward.md)** Picture how the person reacts and what happens after that. Write the prediction down so it can be wrong.
14. **[Rank what matters, then choose, and say why.](rules/rank-what-matters.md)** When rules pull against each other, decide what this call has to get right. Every yes or no carries its reason.

Each page has the rule, when it applies and when it doesn't, why I hold it and an example. Every rule has test cases in [`tests/`](tests/): four per rule, 56 in all. Rules 13 and 14 only weigh the others, so their cases check the weighing rather than a citation. [Midwatch](https://github.com/bigsidd/midwatch) runs every case against an agent with `--eval-os` and writes the results to `tests/results.json`.

Last run, 2026-11-17: 111 of 168 samples passed (66%), three per case, and 31 of 56 cases passed every time. The bar is 90% overall and 75% per rule, and it isn't met yet. Who-is-it-for, most-ideas-dont-work and show-where-it-breaks passed every sample. Nine rules are under 75%. Most misses are the planner citing a neighbouring rule, or asking where the case expects a call: that's where the rules still blur.

## Credit

The wording and examples are mine. Each page's credit names published work I drew on; it isn't a complete list of where the ideas came from.

Employer, partner and client details stay out of this repo. The rules don't need them.
