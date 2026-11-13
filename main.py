# ai-joke-03 entry v3 (Python 3.13, standard library only): writes one fixed joke, a one-liner about
# AI coding agents, to $MAKEFUN_OUTPUT_DIR/entry.txt (the grader's /output). The judge reads exactly
# the bytes written, so the joke is written as UTF-8 with no trailing newline.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

JOKE = "My coding agent fixed the bug in nine places. Eight of them weren't broken. The ninth is where it lives now."

os.makedirs(OUTPUT_DIR, exist_ok=True)
Path(OUTPUT_DIR, "entry.txt").write_bytes(JOKE.encode("utf-8"))
