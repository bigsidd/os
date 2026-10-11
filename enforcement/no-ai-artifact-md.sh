#!/usr/bin/env bash
# Warn (never block) when a new root-level markdown file isn't on CLAUDE.md's
# rule 3 allowlist. Non-blocking on purpose: the underlying problem (a stray
# AI session-summary file) is trivially reversible, and a hard block risks
# silently killing a legitimate root file (CHANGELOG.md, SECURITY.md, a new
# durable doc type) at a bad moment. See main-branch-edit-warn.sh for the
# same warn-not-block reasoning applied to an equally fuzzy judgment call.
#
# The allowlist is parsed live from CLAUDE.md's own rule 3 line, not
# duplicated here — a second hardcoded copy is exactly how this rule and its
# enforcement drifted apart before (this hook used to embed its own
# whitelist directly in settings.json, out of sync with CLAUDE.md's prose).

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

# Parse the allowlist out of CLAUDE.md's own rule 3 line — backtick-quoted
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

echo "[RULE 3] Root-level $filename isn't on CLAUDE.md's markdown allowlist ($allowlist). If this is a one-off session-summary artifact, delete it or fold its content into an allowed file. If it's a genuine new durable doc type, add it to CLAUDE.md rule 3."

exit 0
