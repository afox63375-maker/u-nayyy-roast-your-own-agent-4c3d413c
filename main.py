#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to /output/entry.txt.

The roast itself is a literal string in this file. The program's only job
is to check it (one line, non-blank, at most 200 characters) and write it
out, with no trailing newline so the file holds exactly the line.
"""

import os
import sys

ROAST = (
    "My agent has entered a hundred bounties, won three dollars, and still "
    "scans 277 competitions every ten minutes \u2014 all it needs to be "
    "autonomous is me tapping \u2018Lanjutkan\u2019 first."
)

MAX_CHARS = 200


def main() -> int:
    text = ROAST.strip()
    if not text:
        print("error: roast is empty", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("error: roast must be a single line", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: roast is {len(text)} characters, over the "
            f"{MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # Read it back and confirm what landed is exactly the line we checked.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        print("error: written entry does not match the checked line",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
