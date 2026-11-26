#!/usr/bin/env python3
"""The Comment Above the Code — make.fun entry (program/v1).

Writes one funny, painfully honest line — the comment a developer left
above fragile production code — to /output/entry.txt.

Deterministic, no network, no input. The line is 113 UTF-8 characters,
inside the gate's 1-200 range.
"""

import os

LINE = "The loop runs 47 times. Nobody knows why 47. The one time someone changed it to 48, every invoice went out twice."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Read-back gate verification: the file the grader reads must be
    # exactly the line above, UTF-8, 1-200 chars, not only whitespace.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    assert 1 <= len(written) <= 200, "entry.txt outside the 1-200 char gate"
    assert written.strip(), "entry.txt is only whitespace"


if __name__ == "__main__":
    main()
