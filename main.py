# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed joke, a one-liner about AI
# coding agents, to $MAKEFUN_OUTPUT_DIR/entry.txt (the grader's /output). The judge reads exactly the
# bytes written, so the joke is written as UTF-8 with no trailing newline.

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

JOKE = "My coding agent agreed with me 214 times today. I was right twice."

Path(OUTPUT_DIR, "entry.txt").write_bytes(JOKE.encode("utf-8"))
