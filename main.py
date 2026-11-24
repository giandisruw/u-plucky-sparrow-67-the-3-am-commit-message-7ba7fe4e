#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun entry.

Writes one commit message (at most 200 characters, single line, UTF-8)
to /output/entry.txt. Deterministic: the line below is the winner of the
local pairwise tournament in tournament.py (see tournament.jsonl and
tournament-run.log). No network, no randomness, no input files.

Tournament result (2026-11-25, 15 games, house scoring, both orders):
  winner c09 — 3 game wins, total game score 2.85; beat runner-up c02
  head-to-head in the final (both orders, margins 3 and 2).
  Caffeine router judge: c09 won 3/4 games, mean game score 0.713.
  Verboo judge (deepseek-v4.1-flash, effort max): 0 games judged — every
  call failed with HTTP 422 (trial balance exhausted) and the judge was
  disabled after 3 failed games; see tournament.jsonl.
"""

import os

ENTRY = (
    "fix: the outage is my fault; I hallucinated a migration "
    "and the database believed me"
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
