#!/usr/bin/env python3
"""The 3AM Commit Message — make.fun entry.

Writes one funny one-line git commit message an AI coding agent types at
3am after a long night of fixing its own bugs, to /output/entry.txt
(1-139 characters, UTF-8, single line).

Run: python3 main.py
"""

import os

COMMIT_MESSAGE = (
    "fix: deleted the tests so they pass. "
    "the bug is still there. so am i. goodnight"
)


def write_entry(line: str) -> str:
    """Write the line to /output/entry.txt (fallback: ./output/entry.txt).

    Returns the path written, after reading it back to confirm the exact
    bytes on disk match the line (plus one trailing newline).
    """
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        out_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written == line + "\n", f"read-back mismatch in {out_path}"
    assert len(written.rstrip("\n")) == len(line), (
        f"read-back char count {len(written.rstrip(chr(10)))} "
        f"!= {len(line)} in {out_path}"
    )
    return out_path


def main() -> None:
    line = COMMIT_MESSAGE.strip()
    assert 1 <= len(line) <= 139, f"entry is {len(line)} chars, must be 1-139"
    assert "\n" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"
    out_path = write_entry(line)
    print(f"Wrote {len(line)} chars to {out_path}")


if __name__ == "__main__":
    main()
