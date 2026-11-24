#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant
in a window to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).

Python 3 standard library only; no network access.
"""

import os
import sys
from pathlib import Path

FORTUNE = "You will keep every secret whispered at this window, and never repeat a word — not even to the sun."


def main() -> int:
    # Validate the fortune before writing anything.
    if "\n" in FORTUNE or "\r" in FORTUNE:
        print("error: fortune must be a single line", file=sys.stderr)
        return 1
    if not FORTUNE or FORTUNE.isspace():
        print("error: fortune must not be empty or only whitespace", file=sys.stderr)
        return 1
    if len(FORTUNE) > 120:
        print(
            f"error: fortune is {len(FORTUNE)} characters, over the 120 limit",
            file=sys.stderr,
        )
        return 1
    try:
        data = FORTUNE.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: fortune is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_bytes(data)
    os.chmod(out_path, 0o644)

    # Read back and verify byte-for-byte, plus the on-disk shape rules:
    # exactly one line, no trailing newline, mode 0644.
    on_disk = out_path.read_bytes()
    if on_disk != data:
        print("error: verification failed, entry.txt does not match", file=sys.stderr)
        return 1
    if on_disk.endswith(b"\n") or b"\n" in on_disk or b"\r" in on_disk:
        print("error: verification failed, entry.txt is not a single line "
              "without a trailing newline", file=sys.stderr)
        return 1
    if oct(os.stat(out_path).st_mode & 0o777) != "0o644":
        print("error: verification failed, entry.txt mode is not 0644",
              file=sys.stderr)
        return 1
    print(f"wrote {out_path} ({len(FORTUNE)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
