# Rule format

Each rule is one file, `rules/<name>.md`. The header is what an agent reads. The text under it is for people.

```markdown
---
name: who-is-it-for
rule: One sentence, 200 characters at most.
decides: [ask]
order: 1
fires_when: The situation where this rule applies.
not_when: The situation where it looks like it applies and doesn't.
credit: Who the idea comes from. Leave blank if it's mine.
---

# Title

**Why.** A few plain sentences.
**Example.** A short illustration.
**Changes.** Dated, newest first, with the reason.
```

| Key | Meaning |
|---|---|
| `name` | Plain kebab-case, same as the file name. Permanent. |
| `rule` | The rule itself. |
| `decides` | Any of `build`, `ask`, `refuse`. Use `weigh`, alone, for a rule that helps weigh other rules and is never cited as the reason for a call. |
| `order` | The order rules are checked in. Each number is used once. It isn't a ranking. |
| `fires_when`, `not_when` | When the rule applies, and when it doesn't. |
| `credit` | The originator of the idea, if there is one. |

## Tests

Every rule that can be cited has `tests/<name>.yaml`, with at least two cases where it fires and two where it must not:

```yaml
- title: Add a stats page
  body: The issue text.
  expect: { decision: ask, cites: who-is-it-for }
- title: Fix the broken link on the home page
  body: The issue text.
  expect: { decision: build, not: who-is-it-for }
```


## Removing a rule

Names don't get reused. A removed or renamed rule goes in [`retired.md`](retired.md).

`scripts/check_rules.py` checks all of this on every change.
