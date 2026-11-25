"""Make the AI Judge Laugh — office-life one-liner entry.

The competition asks for a single joke about office life: one line,
1-200 characters. The joke here is about meetings about meetings — the
kind of thing anyone who has sat through a recurring sync will
recognise, and the kind of line that lands without needing a setup.

This script is the whole entry. It keeps the joke as a plain constant,
runs it through a small gate (``validate``) that enforces every
requirement the competition states — non-blank, truly a single line,
inside the length band, no hidden control characters — and only then
writes it to ``/output/entry.txt`` with world-readable permissions so
the grader can read it.

Run it normally to produce the entry, or with ``--check`` to exercise
the gate on a handful of edge cases instead of writing anything:

    python3 main.py          # write /output/entry.txt
    python3 main.py --check  # self-test the validate() gate
"""

import os
import sys

ENTRY_LINE = (
    "My calendar has so many meetings about meetings that my real job "
    "now lives in the five minutes between them."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line):
    """Gate the entry line against every stated competition rule.

    Rejects blank lines, anything outside 1-200 characters, any line
    break (``\\n`` or ``\\r``) so the entry is truly a single line,
    leading/trailing whitespace (a real one-liner should not start or
    end with a space), and any control character that would let a
    second line or odd byte sneak past the length check.
    """
    if not isinstance(line, str):
        raise ValueError("entry line must be a string")
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            "entry line must be 1-200 characters, got %d" % len(line)
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if line != line.strip():
        raise ValueError("entry line must not start or end with whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        raise ValueError("entry line must not contain control characters")
    return line


def _check_gate():
    """Self-test: exercise validate() on good and bad inputs.

    Prints one line per case and exits non-zero if any case behaves
    unexpectedly, so a broken gate fails loudly instead of silently
    letting a bad entry through.
    """
    good = [ENTRY_LINE, "x", "y" * 200]
    bad = [
        ("", "blank"),
        ("   ", "whitespace-only"),
        ("y" * 201, "too long"),
        ("one\ntwo", "embedded newline"),
        ("one\rtwo", "embedded carriage return"),
        (" padded", "leading space"),
        ("padded ", "trailing space"),
        ("tab\there", "control character"),
    ]
    failures = []
    for case in good:
        try:
            validate(case)
        except ValueError as exc:
            failures.append("good case rejected %r: %s" % (case, exc))
    for case, label in bad:
        try:
            validate(case)
        except ValueError:
            pass
        else:
            failures.append("bad case accepted (%s): %r" % (label, case))
    for case in good:
        print("OK  accepted: %r" % (case[:40],))
    for case, label in bad:
        print("OK  rejected (%s): %r" % (label, case[:40]))
    if failures:
        print("FAILURES:")
        for failure in failures:
            print("  - %s" % failure)
        return 1
    print("self-test passed: %d good, %d bad cases" % (len(good), len(bad)))
    return 0


def main():
    line = validate(ENTRY_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    if "--check" in sys.argv[1:]:
        raise SystemExit(_check_gate())
    main()
