#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single fixed horror sentence to /output/entry.txt.
Deterministic: the same text is written on every run.
"""

import os

LINE = "The radiologist circled a shadow on my scan and said, 'It's been waving at us for weeks.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
