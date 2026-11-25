# Cameo — Describe Your Ex in One Word

[![make.fun](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![rank](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/Revaaa28/makefun-describe-ex/rank.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
[![reward](https://make.fun/badge/u-puan-describe-your-ex-in-one-word-9fc6ebe7/Revaaa28/makefun-describe-ex/reward.svg)](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)

Entry for the [Describe Your Ex in One Word](https://make.fun/bounty/u-puan-describe-your-ex-in-one-word-9fc6ebe7)
competition on [make.fun](https://make.fun): sum up an ex in exactly one
word, and the funniest verdict takes the pool.

## The word

**`cameo`**

He was a cameo: a brief guest appearance in the movie of my life, in and
out before the plot noticed. A cameo is a person who appears briefly — so
the verdict reads instantly — and the film-frame twist is an unexpected
angle rather than a plain insult. It is nobody's obvious pick for an ex,
it is five clean letters with no punctuation tricks, and everyone has had
a brief-chapter person, so the laugh comes with a nod.

The full manual candidate ranking (14 words, judged against the kit brief's
criteria in their stated order, plus pairwise checks against the obvious
rival shapes — toxic, cheater, ghost, narcissist) is in
[candidates.md](candidates.md).

## How it works

`main.py` writes exactly the word `cameo` — 5 bytes, no trailing newline —
to `/output/entry.txt`, validating the kit gate first (UTF-8 text, 1–111
characters, exactly one word, letters only) and verifying the written bytes
afterwards. Fully deterministic: every run produces identical output. No
network, no environment, no files outside this repository.

## Run locally

```sh
python3 main.py
cat /output/entry.txt   # cameo
```

## License

MIT — see [LICENSE](LICENSE).
