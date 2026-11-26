#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry program.

Writes one voicemail greeting, as recorded by a cat, to
/output/entry.txt. Standard library only, no network, no input files.
"""

import os
import sys

MAX_CHARS = 120

ENTRY = (
    "Hi, you've reached Miso. I'm on my 4 a.m. zoomies. "
    "Leave a message after the beep — or just feed me, honestly."
)

OUTPUT_PATH = "/output/entry.txt"


def problems(text):
    """List every way the text breaks the bounty gate (empty means valid)."""
    found = []
    if not isinstance(text, str):
        return ["entry is not text"]
    if not (1 <= len(text) <= MAX_CHARS):
        found.append(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if text != text.strip():
        found.append("entry must not start or end with whitespace")
    if not text.strip():
        found.append("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        found.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        found.append("entry must be valid UTF-8")
    return found


def main():
    bad = problems(ENTRY)
    if bad:
        for item in bad:
            print(f"gate failed: {item}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("gate failed: entry.txt does not match the entry", file=sys.stderr)
        return 1
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
