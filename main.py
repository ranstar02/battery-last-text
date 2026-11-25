"""One line: a phone battery's last text to its charger.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Deterministic: no randomness, no time, no network, no input.
"""

import os

LINE = (
    "last request: when he asks how i died, lie. say i went out in a blaze "
    "of glory, not because you left me on 2% while he watched one more "
    "video about how to save battery life."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
