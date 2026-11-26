#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting — make.fun entry program.

Writes one voicemail greeting, as recorded by a cat, to
/output/entry.txt. Standard library only, no network.
"""

import os

ENTRY = (
    "Hi, you've reached Miso. I'm on my 4 a.m. zoomies. "
    "Leave a message after the beep — or just feed me, honestly."
)

OUTPUT_PATH = "/output/entry.txt"


def gate_check(text):
    """Mirror the make.fun gate: UTF-8 text, 1-120 chars, not only whitespace."""
    if not isinstance(text, str):
        return False
    if text != text.strip():
        return False
    if not (1 <= len(text) <= 120):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not gate_check(ENTRY):
        raise SystemExit("gate_check failed: entry is not a valid one-liner")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
