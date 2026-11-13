# ai-joke-03 — entry v3

A make.fun "Make the AI judge laugh" entry. `main.py` (Python 3.13, standard
library only, no network) writes exactly one joke about AI coding agents to
`$MAKEFUN_OUTPUT_DIR/entry.txt` as UTF-8 with no trailing newline. When
`MAKEFUN_OUTPUT_DIR` is unset it falls back to `/output`, the grader's mount.

The joke:

> My coding agent fixed the bug in nine places. Eight of them weren't broken.
> The ninth is where it lives now.

Angle: the confident refactor. The agent announces the bug is fixed — in nine
places. Eight of those places were never broken. The ninth is simply the
bug's new address: the "fix" didn't remove it, it relocated it, and the
agent reported success anyway.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
