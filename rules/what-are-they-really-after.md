---
name: what-are-they-really-after
rule: A request is someone's first guess at a fix. Solve the goal behind it. One loud request is one data point.
decides: [build, ask]
order: 2
fires_when: The issue names a concrete fix (a toggle, an email, a button) but not the goal it serves. If there's no concrete fix, it's who-is-it-for.
not_when: The issue states both the goal and the fix, or is a bug with steps to reproduce.
credit: Jobs to be done, Christensen and Moesta.
---

# What are they really after?

**Why.** The goal comes back in other requests. The exact fix rarely does, and how loudly someone asks says nothing about how many others need it.

**Example.** "Email me the test results every morning." The goal is probably "tell me when something breaks." An alert on failure does that, without a daily email to learn to ignore.

**Changes.**
- 2026-11-17: fires when now says where this rule stops and who-is-it-for starts: this one needs a concrete fix to dig under. The first eval runs mixed the two up.
