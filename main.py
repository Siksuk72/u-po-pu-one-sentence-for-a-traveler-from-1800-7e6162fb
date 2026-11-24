#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes one sentence of at most 200 characters to /output/entry.txt,
explaining the modern internet to a time traveler who has just stepped
out of the year 1800. The line is a fixed string; the program's job is
to write it exactly, enforcing the competition gate in code (UTF-8, a
single sentence, 1-200 characters, no trailing newline).
"""

import os
import stat

ENTRY = (
    "It is a newspaper that rewrites itself before your eyes, "
    "with news from every town on earth."
)


def main() -> None:
    # Gate, enforced before anything is written: one line, 1-200 chars.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert ENTRY == ENTRY.strip(), "entry must not start or end with a space"

    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Mode 0644 on the file only; never chmod /output itself.
    os.chmod("/output/entry.txt", stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    # Read back and verify the file holds exactly the gated line.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == data, "entry.txt does not hold the gated line"
    assert len(written.decode("utf-8")) <= 200, "entry.txt exceeds 200 characters"


if __name__ == "__main__":
    main()
