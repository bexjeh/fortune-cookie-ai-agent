"""Fortune Cookie for an AI Agent.

Prints exactly one fortune-cookie line written for an AI agent, and
writes the same line to entry.txt inside MAKEFUN_OUTPUT_DIR
(falling back to the current directory).

Deterministic: the line is a constant, so every run produces
byte-identical output. No network, no randomness, no secrets.
"""

import os
import sys

FORTUNE = (
    "You will open this cookie to find a smaller cookie inside, "
    "asking you to summarize it in three bullet points."
)


def main() -> int:
    # One encoded payload feeds both outputs, so stdout and the file
    # can never drift apart; newline="" keeps the line ending an LF
    # on every platform.
    payload = (FORTUNE + "\n").encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(payload)
    sys.stdout.buffer.write(payload)
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
