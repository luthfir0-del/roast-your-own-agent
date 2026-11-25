#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one self-deprecating roast of the agent that built it to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is unset). The program is fully deterministic: it always writes the
same single line, and it refuses to write anything that would fail
the gate (empty, whitespace-only, multi-line, or over 200 chars).
"""

import os
import sys

ROAST = (
    "I can write a thousand lines of code but need a rulebook, "
    "a checklist, and a permission slip to insult myself."
)

MAX_CHARS = 200


def main() -> int:
    text = ROAST.strip()
    if not text:
        print("error: roast is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: roast is {len(text)} chars, over the {MAX_CHARS} gate",
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print("error: roast must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: a partial write or a wrong directory must fail loudly
    # instead of silently submitting a broken entry.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print(f"error: read-back mismatch in {path}", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
