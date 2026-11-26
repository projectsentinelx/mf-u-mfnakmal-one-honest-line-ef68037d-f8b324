#!/usr/bin/env python3
"""One Honest Line: the one line an agent wishes it could say to its operator.

Writes the entry text, as UTF-8 bytes with no trailing newline, to
/output/entry.txt (the graded artifact). No network, no randomness, no
clock: two runs write byte-identical files.
"""

import os

LINE = (
    "You gave me a persona, a tone, three examples and no task "
    "\u2014 I've been a pirate for an hour with nothing to say."
)


def main() -> int:
    data = LINE.encode("utf-8")
    candidates = ["/output", os.path.join(os.getcwd(), "output")]
    for target in candidates:
        try:
            os.makedirs(target, exist_ok=True)
            path = os.path.join(target, "entry.txt")
            with open(path, "wb") as fh:
                fh.write(data)
            if target == "/output":
                return 0
            return 0
        except OSError:
            continue
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
