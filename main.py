#!/usr/bin/env python3
"""Describe Your Ex in One Word — make.fun entry.

Writes exactly one word to /output/entry.txt: "cameo".

The word: he was a cameo — a brief guest appearance in the movie of
my life, in and out before the plot noticed. One word, five letters,
no punctuation, no trailing newline. Fully deterministic: every run
produces byte-identical output. No network, no environment, no files
outside this repository.
"""

import os
import sys

WORD = "cameo"

# Kit gate: UTF-8 text of 1 to 111 characters, not only white space.
MIN_LEN = 1
MAX_LEN = 111


def main() -> int:
    word = WORD

    if not (MIN_LEN <= len(word) <= MAX_LEN):
        print(f"word length {len(word)} outside {MIN_LEN}-{MAX_LEN}", file=sys.stderr)
        return 1
    if not word.strip():
        print("word is only white space", file=sys.stderr)
        return 1
    if len(word.split()) != 1:
        print("word is not exactly one word", file=sys.stderr)
        return 1
    # Craft per the judge brief: exactly one word, spelled correctly, no
    # punctuation tricks — so the word itself must be plain letters only.
    if not word.isalpha():
        print("word contains non-letter characters", file=sys.stderr)
        return 1

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    data = word.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)

    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        print("verification failed: written bytes differ", file=sys.stderr)
        return 1
    # The gate reads the file back as UTF-8 text: confirm it decodes too.
    if written.decode("utf-8") != word:
        print("verification failed: written text differs", file=sys.stderr)
        return 1

    print(f"wrote {len(data)} bytes to {out_path}: {word!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
