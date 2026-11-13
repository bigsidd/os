---
name: what-are-they-really-after
rule: A request is someone's first guess at a fix. Solve the goal behind it. One loud request is one data point.
decides: [build, ask]
order: 2
fires_when: The issue asks for a specific fix without saying what it's for.
not_when: The issue states both the goal and the fix, or is a bug with steps to reproduce.
credit: Jobs to be done, Christensen and Moesta.
---

# What are they really after?

**Why.** The goal comes back in other requests. The exact fix rarely does, and how loudly someone asks says nothing about how many others need it.

**Example.** "Email me the test results every morning." The goal is probably "tell me when something breaks." An alert on failure does that, without a daily email to learn to ignore.

**Changes.** None yet.
