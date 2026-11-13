#!/usr/bin/env python3
"""Check rule files against the format in rules/README.md.

Fails if a rule breaks the format, if two rules share a name or an order,
if a rule the agent can cite has too few test cases, or if a rule name
disappears or comes back without going through rules/retired.md.
"""
import argparse
import pathlib
import re
import subprocess
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
RULES = ROOT / "rules"
TESTS = ROOT / "tests"
NOT_RULES = {"README.md", "retired.md"}
KEYS = {"name", "rule", "decides", "order", "fires_when", "not_when", "credit"}
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
RETIRED = re.compile(r"^- `([a-z0-9-]+)`:", re.M)
DECIDES = {"build", "ask", "refuse", "weigh"}
DECISIONS = {"build", "ask", "refuse"}
MAX_RULE_CHARS = 200
MIN_CASES = 2
EXTRA_TEST_FILES = {"real.yaml"}


def front_matter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return yaml.safe_load(match.group(1)) if match else None


def check_rule(path, errors):
    label = f"rules/{path.name}"
    try:
        meta = front_matter(path.read_text())
    except yaml.YAMLError as exc:
        errors.append(f"{label}: header is not valid YAML: {exc}")
        return None
    if not isinstance(meta, dict):
        errors.append(f"{label}: missing header block")
        return None
    if set(meta) != KEYS:
        missing = sorted(KEYS - set(meta))
        extra = sorted(set(meta) - KEYS)
        errors.append(f"{label}: header keys wrong (missing {missing}, unexpected {extra})")
        return None

    name = meta["name"]
    if not isinstance(name, str) or not NAME.match(name):
        errors.append(f"{label}: name must be plain kebab-case")
    elif path.stem != name:
        errors.append(f"{label}: name '{name}' must match the file name")
    rule = meta["rule"]
    if not isinstance(rule, str) or not rule.strip():
        errors.append(f"{label}: rule is empty")
    elif len(rule) > MAX_RULE_CHARS:
        errors.append(f"{label}: rule is {len(rule)} characters, limit is {MAX_RULE_CHARS}")
    decides = meta["decides"]
    if not isinstance(decides, list) or not decides or not set(map(str, decides)) <= DECIDES:
        errors.append(f"{label}: decides must be a list drawn from {sorted(DECIDES)}")
    elif "weigh" in decides and len(decides) > 1:
        errors.append(f"{label}: weigh can't be combined with a decision")
    if not isinstance(meta["order"], int) or isinstance(meta["order"], bool) or meta["order"] < 1:
        errors.append(f"{label}: order must be a whole number from 1 up")
    for key in ("fires_when", "not_when"):
        if not isinstance(meta[key], str) or not meta[key].strip():
            errors.append(f"{label}: {key} is empty")
    if meta["credit"] is not None and not isinstance(meta["credit"], str):
        errors.append(f"{label}: credit must be text or left blank")
    return meta


def retired_names(text):
    return set(RETIRED.findall(text.partition("## Retired")[2]))


def citable(meta):
    return isinstance(meta.get("decides"), list) and "weigh" not in meta["decides"]


def check_cases(path, errors, citable_names):
    label = f"tests/{path.name}"
    try:
        cases = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        errors.append(f"{label}: not valid YAML: {exc}")
        return []
    if not isinstance(cases, list) or not cases:
        errors.append(f"{label}: must be a non-empty list of cases")
        return []
    good = []
    for number, case in enumerate(cases, 1):
        where = f"{label} case {number}"
        if not isinstance(case, dict) or not isinstance(case.get("title"), str):
            errors.append(f"{where}: needs a title")
            continue
        if not isinstance(case.get("body"), str):
            errors.append(f"{where}: needs a body")
            continue
        expect = case.get("expect")
        if not isinstance(expect, dict) or expect.get("decision") not in DECISIONS:
            errors.append(f"{where}: expect.decision must be one of {sorted(DECISIONS)}")
            continue
        if ("cites" in expect) == ("not" in expect):
            errors.append(f"{where}: expect needs exactly one of cites or not")
            continue
        target = expect.get("cites", expect.get("not"))
        if target not in citable_names:
            errors.append(f"{where}: '{target}' is not a rule the agent can cite")
            continue
        good.append(expect)
    return good


def git_show(base, path):
    result = subprocess.run(
        ["git", "show", f"{base}:{path}"], cwd=ROOT, capture_output=True, text=True
    )
    return result.stdout if result.returncode == 0 else ""


def usable_base(base):
    """A first push has no earlier commit to compare against."""
    if not base or set(base) == {"0"}:
        return False
    result = subprocess.run(
        ["git", "cat-file", "-e", f"{base}^{{commit}}"], cwd=ROOT, capture_output=True
    )
    return result.returncode == 0


def base_rule_names(base):
    result = subprocess.run(
        ["git", "ls-tree", "--name-only", base, "rules/"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    files = (pathlib.PurePosixPath(line) for line in result.stdout.splitlines())
    return {f.stem for f in files if f.suffix == ".md" and f.name not in NOT_RULES}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="git ref to compare against for removed names")
    args = parser.parse_args()

    errors = []
    retired_file = RULES / "retired.md"
    retired = retired_names(retired_file.read_text()) if retired_file.exists() else set()
    paths = sorted(p for p in RULES.glob("*.md") if p.name not in NOT_RULES)
    rules = [m for m in (check_rule(p, errors) for p in paths) if m]

    for key in ("name", "order"):
        seen = {}
        for meta in rules:
            value = meta[key]
            if value in seen:
                errors.append(f"{key} '{value}' is used by more than one rule")
            seen[value] = True

    live = {m["name"] for m in rules}
    for name in sorted(live & retired):
        errors.append(f"'{name}' is retired and can't be used again")

    citable_names = {m["name"] for m in rules if citable(m)}
    for name in sorted(citable_names):
        path = TESTS / f"{name}.yaml"
        if not path.exists():
            errors.append(f"{name}: missing tests/{name}.yaml")
            continue
        expects = check_cases(path, errors, citable_names)
        fires = sum(1 for e in expects if e.get("cites") == name)
        holds = sum(1 for e in expects if e.get("not") == name)
        if fires < MIN_CASES:
            errors.append(f"{name}: needs {MIN_CASES} cases where it fires, has {fires}")
        if holds < MIN_CASES:
            errors.append(f"{name}: needs {MIN_CASES} cases where it must not fire, has {holds}")

    for path in sorted(TESTS.glob("*.yaml")):
        if path.name in EXTRA_TEST_FILES:
            check_cases(path, errors, citable_names)
        elif path.stem not in citable_names:
            errors.append(f"tests/{path.name}: no rule the agent can cite has this name")

    if usable_base(args.base):
        for name in sorted(base_rule_names(args.base) - live - retired):
            errors.append(f"'{name}' was removed; add it to rules/retired.md")
        for name in sorted(retired_names(git_show(args.base, "rules/retired.md")) - retired):
            errors.append(f"'{name}' was taken out of rules/retired.md; retired names stay")

    if errors:
        print("\n".join(f"FAIL {e}" for e in errors))
        return 1
    print(f"OK: {len(rules)} rules, {len(citable_names)} citable, {len(retired)} retired")
    return 0


if __name__ == "__main__":
    sys.exit(main())
