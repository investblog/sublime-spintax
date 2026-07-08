#!/usr/bin/env python3
"""Validate Spintax.sublime-syntax: every rule compiles, and the tricky
discriminators (conditionals, plurals, permutation config vs HTML, leading and
trailing separators) match the @spintax/core engine contract.

Sublime runs these rules under Oniguruma; Python's `re` is a faithful proxy for
the constructs used here (backrefs, look-arounds, char classes). The VS Code
mirror (investblog/vscode-spintax) additionally verifies tokenization under the
real Oniguruma via vscode-tmgrammar-test.
"""
import re
import sys
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
doc = yaml.safe_load((ROOT / "Spintax.sublime-syntax").read_text(encoding="utf-8"))
V = doc.get("variables", {})


def resolve(pattern: str) -> str:
    for key, val in V.items():
        pattern = pattern.replace("{{" + key + "}}", val)
    return pattern


# 1) every match rule compiles
compiled = 0
for ctx, rules in doc["contexts"].items():
    for rule in rules:
        if isinstance(rule, dict) and "match" in rule:
            re.compile(resolve(rule["match"]))
            compiled += 1


def nth_match_rule(ctx: str, idx: int) -> str:
    return resolve([r["match"] for r in doc["contexts"][ctx] if r.get("match")][idx])


COND = nth_match_rule("conditionals", 0)
PLURAL = nth_match_rule("plurals", 0)
LEAD_SEP = nth_match_rule("perm_start", 1)   # after the key=value config rule
TRAIL_SEP = nth_match_rule("perm_body", 1)   # after the ']' pop rule


def m(pattern: str, text: str) -> bool:
    return re.match(pattern, text) is not None


CASES = [
    # conditionals
    ("conditional",           COND,      "{?VAR?a|b}",              True),
    ("conditional negated",   COND,      "{?!VAR?a}",               True),
    ("conditional bad name",  COND,      "{?1bad?x}",               False),
    ("conditional empty name", COND,     "{??x}",                   False),
    # plurals
    ("plural",                PLURAL,    "{plural %n%: a|b|c}",     True),
    ("plural no colon",       PLURAL,    "{plural noun}",           False),
    ("plural no space",       PLURAL,    "{plural: one|many}",      False),
    # leading permutation separator vs HTML
    ("lead punct sep",        LEAD_SEP,  "<, >a|b",                 True),
    ("lead dash sep",         LEAD_SEP,  "<->a|b",                  True),
    ("lead word sep",         LEAD_SEP,  "<and>a|b",                True),
    ("lead html <li>",        LEAD_SEP,  "<li>a</li>|b",            False),
    ("lead html <a href>",    LEAD_SEP,  '<a href="/x">z</a>|b',    False),
    ("lead self-closing",     LEAD_SEP,  "<br/>x",                  False),
    # trailing per-element separator vs HTML
    ("trail punct sep",       TRAIL_SEP, "<, >|b",                  True),
    ("trail word sep",        TRAIL_SEP, "<and>|b",                 True),
    ("trail bare <li>",       TRAIL_SEP, "<li>|b",                  True),
    ("trail closing tag",     TRAIL_SEP, "</li>|b",                 False),
    ("trail tag with attrs",  TRAIL_SEP, "<a href=x>|b",            False),
]

failures = 0
for name, pattern, text, expected in CASES:
    got = m(pattern, text)
    ok = got == expected
    failures += not ok
    print(f"{'ok  ' if ok else 'FAIL'} {name}: {text!r} -> {got} (want {expected})")

print(f"\n{compiled} rules compiled; {len(CASES) - failures}/{len(CASES)} discriminator checks passed")
sys.exit(1 if failures else 0)
