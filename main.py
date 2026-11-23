#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry program.

Writes exactly one letter to /output/entry.txt and nothing else.

Letter choice: A (coffee).

Reasoning: the judge weighs vividness first, then funnier, then truer.
Coffee is the more vivid, alive, punchier stance — mornings, fuel, ritual,
the builder's drink — while tea reads calm and gentle. Coffee is also the
bolder, funnier standing answer for the house's coffee-vs-tea argument.

Stdlib only, no network, deterministic: the output is always the single
byte "A" with no trailing newline.
"""

import os

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check: exactly one character, not only whitespace — the entry
    # is invalid unless the file is UTF-8 text of exactly 1 character.
    assert len(LETTER) == 1, "letter must be exactly 1 character"
    assert not LETTER.isspace(), "letter must not be whitespace"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
