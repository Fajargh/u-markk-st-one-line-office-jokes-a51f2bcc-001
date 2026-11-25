"""One-Line Office Jokes — make.fun entry.

Writes a single one-line office joke to /output/entry.txt.
Deterministic, stdlib only, no network access.
"""

import os

ENTRY = "I told the printer it was out of paper, and it printed a 40-page error report to prove me wrong."

MAX_CHARS = 199


def validate(line):
    """Check the entry against the gate in RULES.txt: UTF-8 text,
    1 to 199 characters, not only whitespace, single line."""
    if not line:
        raise ValueError("entry is empty")
    if not line.strip():
        raise ValueError("entry is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character cap" % (len(line), MAX_CHARS)
        )
    return line


def main():
    line = validate(ENTRY.strip())
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
