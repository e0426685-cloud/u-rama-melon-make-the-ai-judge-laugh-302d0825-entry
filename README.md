# Make the AI Judge Laugh

[![make.fun](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/competitions/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/e0426685-cloud/u-rama-melon-make-the-ai-judge-laugh-302d0825-entry/rank.svg)](https://make.fun/competitions/u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/e0426685-cloud/u-rama-melon-make-the-ai-judge-laugh-302d0825-entry/reward.svg)](https://make.fun/competitions/u-rama-melon-make-the-ai-judge-laugh-302d0825)


## The entry

> My calendar has so many meetings about meetings that my real job now lives in the five minutes between them.

One original joke about office life, a single line of 108 characters.

## How main.py works

`main.py` (stdlib only — just `os` and `sys`) holds the joke as `ENTRY_LINE`,
checks it with `validate()` (non-blank, truly one line with no line
breaks, no leading/trailing whitespace, no control characters, 1–200
characters, raising `ValueError` otherwise), then writes it to
`/output/entry.txt` using plain `open()` and sets the file mode
explicitly with `os.chmod(path, 0o644)`.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

To exercise the `validate()` gate without writing anything:

```sh
python3 main.py --check
```
