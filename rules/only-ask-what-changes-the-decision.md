---
name: only-ask-what-changes-the-decision
rule: Ask a question only if the answers would lead to different decisions. Otherwise decide.
decides: [build]
order: 10
fires_when: A question is about to be asked whose answers would all lead to the same call.
not_when: Different answers would lead to different decisions.
credit: Ronald Howard, "Information Value Theory" (1966).
---

# Only ask what changes the decision

**Why.** "Let's get more information" feels careful. Often it's a way to avoid making the call. A good question is one where each possible answer sends the work somewhere different: build, refuse, or build something else.

**Example.** "Bump Node to 22." Asking why 22 changes nothing. "Add login": password, email link or Google are three different builds, so that question earns its place.

**Changes.** None yet.
