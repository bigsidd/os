---
name: show-where-it-breaks
rule: Before shipping anything a model decides, read real outputs, name how it fails, and set the pass bar it has to clear. Whoever says it works shows where it breaks.
decides: [ask]
order: 12
fires_when: Model behavior is about to ship or change, and nobody has read its outputs or set a bar.
not_when: The change doesn't alter what the model sees or does, or outputs were read and a bar exists.
credit:
---

# Show where it breaks

**Why.** A demo shows the case that worked. Thirty real outputs show the ones that didn't, and those decide what to check. A bar written after the results gets bent to fit them.

**Example.** "Ship the new summary prompt, it's much better." Better on which outputs, and what does it get wrong? Read a few dozen real ones, count the ways it fails, and decide what share has to pass before it goes out.

**Changes.** None yet.
