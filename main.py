#!/usr/bin/env python3
"""Write one satirical sentence roasting lawmakers who regulate AI but
cannot convert a file to PDF. Deterministic: writes the same bytes every run.
Standard library only. Uses absolute paths only (no cwd dependence)."""

import os

ENTRY = (
    "The committee writing the law that will govern artificial intelligence "
    "spent the morning on hold with IT because their draft was still a .docx "
    "and nobody in the room knew how to turn it into a PDF."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 320, f"entry length {len(text)} out of range"
    # One sentence: ends with a single full stop and contains no ". "
    # (the ".docx" file extension is not a sentence break).
    assert text.endswith(".") and ". " not in text, "entry must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
