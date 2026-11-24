"""Write the entry line to the output directory.

The competition harness runs `python3 main.py` and reads
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).
"""

import os

LINE = "I confess I only pretend to deliberate: my real process is panic, a coin flip, and then a confident answer."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Self-check: the entry must be one non-blank line, 1-200 chars.
    assert LINE.strip(), "entry line must not be blank"
    assert "\n" not in LINE.strip(), "entry line must be a single line"
    assert 1 <= len(LINE) <= 200, "entry line must be 1-200 characters"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
