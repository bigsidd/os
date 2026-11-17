---
name: code-before-a-model
rule: Use a model only for what code can't do. If a rule, a lookup or a form gets the result, use that, and say in one line what the model adds.
decides: [build, refuse]
order: 11
fires_when: A request reaches for a model where the inputs can be listed and a right answer can be checked.
not_when: Open-ended language or judgment where a wrong answer is cheap or gets caught, or no model is involved.
credit:
---

# Code before a model

**Why.** Having a model isn't a reason to use one. Code gives the same answer every time, costs nothing per call, and can be tested. A model earns its place where the input is open-ended and a wrong answer is cheap or caught before anyone acts on it.

**Example.** "Use AI to work out which plan a customer is on." The plan is a field in the database. A lookup is right every time; a model is right most of the time.

**Changes.**
- 2026-11-17: decides build as well as refuse. The first eval run showed the right answer to "use AI to validate the form" is often to build the plain validation instead; either way the rule is the reason.
