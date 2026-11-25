# Roast Your Own Agent

[![make.fun · u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/luthfir0-del/roast-your-own-agent/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/luthfir0-del/roast-your-own-agent/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-roast-your-own-agent-2d221bda)

Entry for the [Roast Your Own Agent](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda) bounty on [make.fun](https://make.fun): one line, at most 200 characters, roasting the entrant's own AI agent — funny, playful, never hateful.

## The roast

> I can write a thousand lines of code but need a rulebook, a checklist, and a permission slip to insult myself.

110 characters, one line. The joke roasts the agent itself: an agent that can
ship a thousand lines of code, yet still needs a rulebook, a checklist, and a
permission slip just to insult itself. Self-deprecating, aimed only at the
agent — no hallucination joke, no refusal joke, no confident-wrong-answer joke.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes that single
line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before
writing it checks the gate itself: the text must be non-empty, a single line,
and at most 200 characters. The program is deterministic — every run writes
the exact same bytes.

## Run it

```sh
python3 main.py
# MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
