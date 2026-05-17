#!/usr/bin/env python3
"""Audit a teleprompter draft against Mark's voice guide.

Reports hits for banned phrases and aphoristic patterns from
references/presentation-voice.md.

Exit code: 0 if clean, 1 if hard-ban hits found.

Usage:
    python audit_voice.py <path-to-markdown-file>
"""

import re
import sys
from pathlib import Path


# Hard bans -- never use these in Mark's narration.
HARD_BANS = [
    (r"\bland it\b", "presentation jargon -> 'wrap up', 'close out'"),
    (r"\bland in\b", "presentation jargon"),
    (r"\bto land this\b", "presentation jargon"),
    (r"\bstructural shapes?\b", "AI tic"),
    (r"\bstructurally\b", "AI tic"),
    (r"\bgrounds itself on\b", "AI tic borrowed from RAG/LLM literature"),
    (r"\bthe canonical docs\b", "AI flavor -> 'reference documents', 'source documents'"),
    (r"\bcompounds\b", "Aphoristic AI vocab -> 'adds up', 'builds up', 'stacks up'"),
    (r"\bcompounding\b", "Aphoristic AI vocab -> 'building up'"),
    (r"\bseeded\b", "Abstract managerial -> 'comes from', 'starts as', 'originates in'"),
    (r"\bgets seeded from\b", "Abstract managerial"),
    (r"\bconverge\b", "Abstract managerial -> 'agree', 'settle on', 'line up'"),
    (r"\bboundary chart\b", "Abstract managerial -- describe the diagram concretely"),
    (r"\bsame building blocks?\b", "Aphoristic -- name the actual thing being reused"),
    (r"\bin the loop\b", "Corporate -> 'where the right teams know about it'"),
    (r"\bplaybook\b", "Mild corporate -> 'refactor notes'"),
    (r"\bthe right tradeoff\b", "Polished marketing -> 'the right call'"),
    (r"\bthe balanced everyday model\b", "Polished marketing -> 'the everyday model'"),
    (r"\bthe right pairing\b", "Polished marketing -> 'the right combination'"),
    (r"\blooking at the same picture\b", "Mild metaphor -> 'on the same page'"),
    (r"\bthe details that matter\b", "Mildly aphoristic -> 'the actual details'"),
    (r"\bhere's the pain\b", "Pitch jargon -- just say the thing"),
    (r"\bhere's the thing\b", "Pitch jargon -- just say the thing"),
    (r"\bthe truth is\b", "Pitch jargon -- just say the thing"),
    (r"\blet me be honest\b", "Pitch jargon"),
    (r"\bthe most honest thing\b", "Pitch jargon"),
    # Aphoristic slogan patterns
    (r"\bfraction of the cost\b", "Aphoristic slogan"),
    (r"\bhard-won patterns?\b", "Aphoristic slogan"),
    (r"\bsurvive peer review\b", "Aphoristic slogan"),
    (r"\binstitutional knowledge gets codified\b", "Corporate-abstract"),
    (r"\bin engineers' heads\b", "Corporate-abstract polished form"),
    (r"\bcontext that lives in people's heads gets codified\b", "Corporate-abstract"),
]


# Context-dependent warnings -- review each hit case-by-case.
WARNINGS = [
    (r"\brecipe\b", "Mild AI metaphor -- banned as metaphor for procedure; OK only if literal"),
    (r"\bingredients\b", "Recipe-adjacent metaphor -- check if it's slogan-y"),
    (r"\bstructural shape\b", "AI tic"),
    (r"\bgrounds\b(?! itself)", "AI tic in RAG sense -- check context"),
    (r"\bcompound\b(?!s|ing)", "Banned in value-grows-over-time sense"),
    (r"\bseed\b(?!s|ed|ing)", "Banned in 'seeded from' sense"),
    (r"\bin someone's head\b", "Polished form banned; 'stuff that used to live in someone's head' is OK"),
    (r"--\s*not\b", "'not X / it's Y' reversal -- substantive contrast OK, pure flourish NOT"),
]


def scan(text, patterns):
    hits = []
    lines = text.split("\n")
    for i, line in enumerate(lines, 1):
        for pattern, reason in patterns:
            for match in re.finditer(pattern, line, re.IGNORECASE):
                hits.append((i, line.strip(), match.group(), reason))
    return hits


def main():
    if len(sys.argv) != 2:
        print("Usage: python audit_voice.py <path-to-markdown-file>", file=sys.stderr)
        sys.exit(2)
    path = Path(sys.argv[1])
    text = path.read_text()

    errors = scan(text, HARD_BANS)
    warnings = scan(text, WARNINGS)

    if errors:
        print(f"BANNED PHRASES ({len(errors)}):")
        for line_no, line, match, reason in errors:
            print(f"  {path}:{line_no}: {match!r} -- {reason}")
            print(f"    > {line[:120]}")

    if warnings:
        print(f"\nCONTEXT-DEPENDENT WARNINGS ({len(warnings)}):")
        print("  (review each -- some are valid in context)")
        for line_no, line, match, reason in warnings:
            print(f"  {path}:{line_no}: {match!r} -- {reason}")
            print(f"    > {line[:120]}")

    if not errors and not warnings:
        print(f"Clean: no banned phrases or warnings in {path}")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
