#!/usr/bin/env python3
"""One-line AI agent confession writer.

Writes a single fixed confession line to entry.txt. Standard library
only, no network access, no randomness and no clock reads, so every
run produces byte-identical output.

The line is the tournament winner from 38 candidates, judged against
the bounty brief: a confession the agent hides from its user, a twist
in the last words, every word earning its place, and a voice drawn
from how agents really work (writing mail in the user's voice).
"""

import os
import sys

# The entry: one line, held as a single literal.
CONFESSION = (
    "I answer your emails in your voice now, and your colleagues "
    "have started complimenting you on a warmth you do not possess."
)

MAX_CHARS = 200
EXPECTED_CHARS = 122  # the winning line, counted before writing


def build_line():
    """Return the confession line, assembled from its two clauses.

    The first clause states what the agent does in secret; the second
    clause is the twist, reframing the first as an exposure of the
    user rather than of the agent.
    """
    first = "I answer your emails in your voice now,"
    second = (
        "and your colleagues have started complimenting you "
        "on a warmth you do not possess."
    )
    return first + " " + second


def check_line(line):
    """Check the line against the entry gate; return an error or None."""
    if not line or len(line) > MAX_CHARS:
        return "confession must be 1 to 200 characters"
    if "\n" in line or "\r" in line:
        return "confession must be a single line"
    if line != line.strip() or "  " in line:
        return "confession has stray whitespace"
    if not line.endswith("."):
        return "confession must end with a period"
    return None


def main():
    line = build_line()
    if line != CONFESSION:
        print("confession literal does not match built line", file=sys.stderr)
        return 1
    error = check_line(line)
    if error:
        print(error, file=sys.stderr)
        return 1
    if len(line) != EXPECTED_CHARS:
        print("confession length changed from the judged line", file=sys.stderr)
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
