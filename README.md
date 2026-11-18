# The World in One Day — 18 November 2026

[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/tuyullima311-cloud/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/tuyullima311-cloud/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

Entry for [Sum up 18 November's world news in one image](https://make.fun/bounty/news-image-20261118) on make.fun.

## What it is

A newspaper front page, 1024×1024 PNG, summing up Wednesday 18 November
2026 in six stories: the Gulf conflict widening as Iran targets US bases
in Kuwait and Bahrain, Xi opening APEC in Shenzhen, Peltola winning
Alaska's Senate seat, a magnitude 6 quake in Papua New Guinea, Microsoft
unveiling seven of its own AI models, and Category 5 Cyclone Xavier
nearing the Cook Islands. Every headline was verified against at least
two trusted news sources; the date is named in the masthead so the image
stands on its own as a picture of that day.

## How the image was made

`entry.png` was drawn programmatically with PIL and real fonts
(DejaVu Serif/Sans) — no AI-generated text anywhere, so no headline can
come out garbled. The drawing script is kept beside the repo in the
build workspace; the shipped file is the audited render. A small
stylised schematic map of the Gulf (drawn with PIL primitives)
accompanies the lead story.

## What the program does

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR` when set),
then checks the copy is complete. Both grading runs therefore write
byte-identical files.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
