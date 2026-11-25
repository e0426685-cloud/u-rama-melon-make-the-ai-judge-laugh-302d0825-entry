"""Make the AI Judge Laugh — office-life one-liner entry.

Writes a single original joke about office life (one line, 1-200
characters) to /output/entry.txt.
"""

import os

ENTRY_LINE = (
    "My calendar has so many meetings about meetings that my real job "
    "now lives in the five minutes between them."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Check the entry line is non-blank and 1-200 characters."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            "entry line must be 1-200 characters, got %d" % len(line)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    return line


def main():
    line = validate(ENTRY_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
