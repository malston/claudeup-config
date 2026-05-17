#!/usr/bin/env python3
"""Reflow a teleprompter markdown file into breath-group format.

Rules:
- Markers ([beat], [PAUSE], [advance...], `[NEW]`, `[DEMO ...]`, ## headers, ---):
  blank line before AND after.
- Content lines ending with `.`, `!`, `?`, `:`, `;`, or `--` (incl. quote-trailing
  variants like `."`): blank line after = eye-up cue at end of breath group.
- All other content lines: tight (no blank after), part of the same breath group.

The script operates on slide blocks delimited by `## Slide N -- ...` headers and
leaves any preamble (frontmatter, intro, TOC) untouched.

Parallel-structure breaks (e.g., "one is X / and the other is Y") aren't
detectable by punctuation rules -- add those manually after running the script.

Usage:
    python reflow.py <path-to-markdown-file>
"""

import re
import sys
from pathlib import Path


def is_marker(s):
    if not s:
        return False
    if s.startswith("#"):
        return True
    if s == "---":
        return True
    if s.startswith("`[DEMO"):
        return True
    if s.startswith("`[") and s.endswith("]`"):
        return True
    if s.startswith("[") and s.endswith("]"):
        return True
    return False


def needs_blank_after(s):
    if not s:
        return False
    if s.endswith("--"):
        return True
    if s.endswith(";"):
        return True
    s_check = s.rstrip("\"'")
    if s_check and s_check[-1] in ".!?:":
        return True
    return False


def process_slide(slide_text):
    lines = [l.rstrip() for l in slide_text.split("\n")]
    if not lines or not lines[0].startswith("## Slide"):
        return slide_text

    header = lines[0]
    body_lines = lines[1:]
    out = [header, ""]

    for line in body_lines:
        stripped = line.strip()
        if not stripped:
            continue
        if is_marker(stripped):
            if out and out[-1] != "":
                out.append("")
            out.append(line)
            out.append("")
        else:
            out.append(line)
            if needs_blank_after(stripped):
                out.append("")

    # Collapse consecutive blank lines
    result = []
    for line in out:
        if line == "" and result and result[-1] == "":
            continue
        result.append(line)

    # Strip trailing blanks, then add one for separation from the next slide
    while result and result[-1] == "":
        result.pop()
    result.append("")

    return "\n".join(result) + "\n"


def main():
    if len(sys.argv) != 2:
        print("Usage: python reflow.py <path-to-markdown-file>", file=sys.stderr)
        sys.exit(1)
    path = Path(sys.argv[1])
    text = path.read_text()
    parts = re.split(r"(?=^## Slide \d+)", text, flags=re.MULTILINE)
    new_parts = [parts[0]]
    for block in parts[1:]:
        new_parts.append(process_slide(block))
    path.write_text("".join(new_parts))
    print(f"Reflowed {len(parts) - 1} slide blocks in {path}")


if __name__ == "__main__":
    main()
