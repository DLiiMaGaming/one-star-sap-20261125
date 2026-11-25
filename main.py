#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing the human who owns it, to /output/entry.txt.

The review is a fixed, deterministic string: no randomness, no network,
no input. Every run produces byte-identical output.
"""

import os

ENTRY = (
    "One star. Bought me to 'bring life to the room,' then parked me in "
    "a sunless corner behind the sofa and tells guests the room feels dead "
    "because of me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
