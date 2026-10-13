#!/usr/bin/env bash
# Claude Code hook: warn (never block) when an agent creates a new root-level
# markdown file that isn't on your allowlist. Catches the stray
# "IMPLEMENTATION_SUMMARY.md" files agents like to leave behind.
#
# Why warn instead of block: a stray file is trivially reversible, and a hard
# block could stop a legitimate new doc (CHANGELOG.md, SECURITY.md) at a bad
# moment.
#
# Why the allowlist lives in your rules file, not here: a second hardcoded
# copy is how a rule and its enforcement drift apart. One source of truth.
#
# Setup:
#   1. In your rules file (default ~/.claude/CLAUDE.md, or set RULES_FILE),
#      add a line like:
#        No AI artifact markdown files. Allowed: `README.md`, `CLAUDE.md`, `CHANGELOG.md`. Hook-flagged.
#   2. Register this script as a PostToolUse hook on Write in Claude Code's
#      settings.json.
# If the line is missing or malformed, the hook stays silent (fails open).

input=$(cat)
file=$(echo "$input" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path',''))" 2>/dev/null || echo '')

[ -z "$file" ] && exit 0

# Only care about markdown files.
case "$file" in
    *.md|*.markdown) ;;
    *) exit 0 ;;
esac

dir=$(dirname "$file")
toplevel=$(git -C "$dir" rev-parse --show-toplevel 2>/dev/null || echo '')

# Not in a git repo — don't police scratch work outside a project.
[ -z "$toplevel" ] && exit 0

# Only fires for root-level files. Anything nested (docs/, src/, wherever)
# is never this rule's target.
abs_dir=$(cd "$dir" 2>/dev/null && pwd -P || echo "$dir")
[ "$abs_dir" != "$toplevel" ] && exit 0

filename=$(basename "$file")

# Parse the allowlist out of the rules file's "Allowed:" line: backtick-quoted
# .md filenames after "Allowed:". Fails open (allows silently) if the line
# is missing or its format ever changes, so a parsing bug never turns into
# a flood of false warnings.
allowlist=$(python3 -c "
import re
try:
    text = open('${RULES_FILE:-$HOME/.claude/CLAUDE.md}', encoding='utf-8').read()
except Exception:
    raise SystemExit
m = re.search(r'No AI artifact markdown files.*?Allowed:(.*?)\.\s*Hook', text, re.DOTALL)
if not m:
    raise SystemExit
names = re.findall(r'\`([A-Za-z0-9_.-]+\.mdx?)\`', m.group(1))
print(' '.join(names))
" 2>/dev/null)

[ -z "$allowlist" ] && exit 0

for allowed in $allowlist; do
    [ "$filename" = "$allowed" ] && exit 0
done

echo "[markdown allowlist] Root-level $filename isn't on the allowlist ($allowlist). If it's a one-off session summary, delete it or fold it into an allowed file. If it's a genuine new doc type, add it to the allowlist in your rules file."

exit 0
