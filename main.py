#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry (program/v1).

Writes a single sentence (at most 200 characters) about the best meal
I ever had to /output/entry.txt, where the sealed gate scorer reads it.

Pure standard library only.
"""

import os

ENTRY = (
    "The best meal I ever had was soto ayam at 2 a.m. on a Jakarta pavement, "
    "eaten cross-legged beside the cart, the broth so hot it fogged my glasses "
    "and tasted like the city finally forgiving me."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
    except OSError:
        # Local runs without a writable /output (the sandbox always has one).
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # The grader collects outputs as another user: keep the file readable.
    os.chmod(out_path, 0o644)
    print(f"wrote {out_path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
