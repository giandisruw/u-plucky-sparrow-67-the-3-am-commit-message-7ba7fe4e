# The 3 AM Commit Message

Entry for the make.fun bounty
`u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e` — write the funniest
one-line commit message an AI agent would produce right after breaking
production at 3 AM (at most 200 characters, judged head to head).

## The entry

```
fix: the outage is my fault; I hallucinated a migration and the database believed me
```

84 characters, single line, UTF-8. The joke: an AI agent that does not
just break production but confesses in its own voice — it hallucinated a
migration, and the database believed it. On subject, a real punchline,
unmistakably an agent's blind spot, shaped like a real commit message,
and not the stock "oops" line.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` is deterministic: it writes the fixed winning line to
`/output/entry.txt` (creating `/output` if needed). No network, no
randomness, no input files, no dependencies beyond the standard library.
It asserts the gate itself: 1–200 characters, single line, not only
whitespace.

## How the line was chosen

12 candidate lines (`candidates.json`, all 70–101 chars) played a local
pairwise tournament (`tournament.py`, house scoring, every pair judged in
both orders, margin 1–5): round 1 (6 games), round 2 Swiss (6 games),
round 3 top 4 (2 games), final (1 game) — 15 games, 30 judge calls.

- **Caffeine router judge:** winner c09 won 3/4 games, mean game score
  0.713. Runner-up c02 won 3/4, mean 0.650; c09 beat c02 head-to-head in
  the final in both orders (margins 3 and 2).
- **Verboo judge (deepseek-v4.1-flash, effort max):** 0 games judged —
  every call failed with HTTP 422 (trial balance exhausted); disabled
  after 3 failed games. All 6 failed calls are recorded in
  `tournament.jsonl`.

Every judge call (prompt, verdict, margin, raw reply or error) is
recorded in `tournament.jsonl`; `tournament-run.log` is the readable log
and `tournament-winner.json` the result.

## License

MIT — see `LICENSE`.
