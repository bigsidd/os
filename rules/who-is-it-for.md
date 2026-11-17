---
name: who-is-it-for
rule: Name the person, the moment they hit the problem, and what they do about it today, even if that's nothing.
decides: [ask]
order: 1
fires_when: The issue is a wish with no person or moment behind it ("we should have…", "it could be nicer"), and no concrete fix to dig under.
not_when: The person and the situation are stated, even in one line.
credit: Jobs to be done, Clayton Christensen and Bob Moesta. Ash Maurya on existing alternatives.
---

# Who is it for, and when?

**Why.** An idea with no person attached can only be liked or disliked. Once there's a person at a moment, there's a test: does this help them, then, more than what they already do?

**Example.** "Add a stats page." A visitor deciding in ten seconds whether the project is alive needs one line: the date of the last release. I need something else: whether anyone uses it. Same words, two different builds.

**Changes.**
- 2026-11-17: fires when now says the issue names no concrete fix. The first eval runs showed this rule and what-are-they-really-after firing on the same vague requests; a concrete fix with no goal belongs to the other one.
