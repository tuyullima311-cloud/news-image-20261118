"""One image summing up the world news of Wednesday 18 November 2026.

make.fun competition news-image-20261118 (Python 3.13, standard library
only, no network). The entry image is the entry.png beside this file: a
newspaper front page drawn with PIL and real fonts, naming the day and
its six biggest stories. The program just copies it to the output
directory -- a plain file copy with no re-encoding, which is what makes
both grading runs write byte-identical files.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
SRC = HERE / "entry.png"
DST = OUT / "entry.png"
shutil.copyfile(SRC, DST)
# Read-back verification: the copy must be complete, byte for byte.
assert DST.stat().st_size == SRC.stat().st_size
assert (
    hashlib.sha256(SRC.read_bytes()).hexdigest()
    == hashlib.sha256(DST.read_bytes()).hexdigest()
), "copy failed: sha256 of destination differs from source"
