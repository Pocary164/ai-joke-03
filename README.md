# ai-joke-03 — entry v2

A make.fun "Make the AI judge laugh" entry. `main.py` (Python 3.13, standard
library only, no network) writes exactly one joke about AI coding agents to
`$MAKEFUN_OUTPUT_DIR/entry.txt` as UTF-8 with no trailing newline.

The joke:

> My coding agent said 'it works on my machine.' Its machine is my machine.
> We share a machine. It still failed.

Angle: the oldest excuse in software development — "it works on my machine" —
collapses when the one saying it is an AI agent that has no machine of its
own. It runs on yours. It still failed.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
