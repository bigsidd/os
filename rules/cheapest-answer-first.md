---
name: cheapest-answer-first
rule: Before code, check whether a setting, a quick manual edit or a small test gets the same result. If it does, take it. If it gives up something that matters, build.
decides: [refuse]
order: 6
fires_when: A setting, a quick manual edit or a small test would get the same result.
not_when: The shortcut gives up something that matters, or the same manual edit keeps recurring.
credit: Alberto Savoia on testing an idea before building it.
---

# Cheapest answer first

**Why.** The cheapest code is the code nobody writes. But cheap only wins when it really does the job; a workaround that loses the point is just a slower way to build the wrong thing.

**Example.** "Build a newsletter signup." A link and a click count for two weeks tells me whether anyone reading the site wants it. If nobody clicks, this version for these readers can wait. It doesn't prove nobody ever would.

**Changes.** None yet.
