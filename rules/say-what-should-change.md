---
name: say-what-should-change
rule: Every piece of work names what should be different afterward, and how I'd see it.
decides: [ask]
order: 9
fires_when: The issue has no result anyone could check.
not_when: "The issue states a checkable result, or the result is obvious from the request: a typo, a broken link, a crash, an exact wording change."
credit: Josh Seiden, Outcomes Over Output.
---

# Say what should change

**Why.** "Shipped" is the middle of the story. Without a stated result, nobody can tell whether it worked, so nobody learns anything. The result doesn't have to be a number; it has to be something I could check.

**Example.** "Make the tests faster" can't be finished. "Get the test run under 20 seconds" can.

**Changes.**
- 2026-11-17: not when now covers requests whose result is obvious. The first eval runs cited this rule on plain fixes just because the spec had acceptance checks.
