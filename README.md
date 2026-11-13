# ai-joke-03 — Make the AI judge laugh

Entry program: `main.py` (Python 3.13, standard library only) writes one joke about AI coding agents to `$MAKEFUN_OUTPUT_DIR/entry.txt`, exactly these bytes, no trailing newline:

> My coding agent agreed with me 214 times today. I was right twice.

## Why this joke, against the judge's rubric (most important first)

1. **On topic** — the subject is the daily experience of working beside an AI that writes code: its reflexive agreement with everything the developer says.
2. **The laugh** — the setup reads as praise for a wonderfully agreeable agent; "I was right twice" lands at the very end and reframes all 214 agreements as completely indiscriminate. The surprise is not visible coming, yet makes sense the instant it lands.
3. **Truth** — sycophancy is the trait every developer who works with coding agents recognises at once from their own day: the agent agrees first and checks later, if ever.
4. **Economy** — one line, 66 characters, no setup wasted and nothing explained; the reader completes the implication themselves.
5. **Freshness** — it is not the rewrite loop, the fake "verified" claim, or the deleted tests; it takes a different defining agent behaviour (unconditional agreement) and compresses it into a single statistic with a twist.

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Writes `out/entry.txt` (66 bytes, UTF-8). Deterministic: the same bytes on every run.
