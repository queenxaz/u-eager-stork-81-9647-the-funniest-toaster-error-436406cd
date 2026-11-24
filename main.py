"""The Funniest Toaster Error Message.

Writes one line -- the funniest error message a kitchen toaster
could show its owner -- to /output/entry.txt.
No network, no randomness, deterministic.
"""

import os

ENTRY = "Error 451: This bread is unavailable for legal reasons. It has a lawyer."
# 72 characters: a real HTTP 451 ("unavailable for legal reasons") worn by a
# toaster whose bread has lawyered up -- deadpan, one voice, one read.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
