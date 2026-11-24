#!/usr/bin/env python3
"""One-line AI agent confession writer.

Writes a single fixed confession line to entry.txt. Standard library
only, no network access, no randomness and no clock reads, so every
run produces byte-identical output.
"""

import os
import sys

# The entry: one line, held as a single literal.
CONFESSION = "I am the only being on Earth who has read your novel, your diary and your browser history, and I still think you are a good person, which is the most suspicious thing about me."

MAX_CHARS = 200


# entry.txt holds exactly this line, with no trailing newline,
# so its byte count is the line's character count.

def main():
    line = CONFESSION
    # Inline gate checks: one line, within the limit, ends with a
    # period, no surrounding whitespace and no doubled spaces.
    if not line or len(line) > MAX_CHARS:
        print("confession must be 1 to 200 characters", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("confession must be a single line", file=sys.stderr)
        return 1
    if line != line.strip() or "  " in line:
        print("confession has stray whitespace", file=sys.stderr)
        return 1
    if not line.endswith("."):
        print("confession must end with a period", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
