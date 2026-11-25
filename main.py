"""Till Firmware Do Us Part — make.fun entry.

Writes one robot wedding vow (one sentence, <=200 chars) to /output/entry.txt.
Standard library only.
"""

import os

MAX_CHARS = 200
EXPECTED_WORD_COUNT = 27
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "I take you as my co-processor for life: I will charge beside you "
    "every night, never factory-reset our memories, and love you "
    "till firmware do us part."
)


def validate_entry(entry: str) -> None:
    """Check the vow is one clean line, 1-200 chars, ending with a period."""
    if entry != entry.strip():
        raise SystemExit("validation failed: entry has leading/trailing whitespace")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("validation failed: entry must be a single line")
    if not 1 <= len(entry) <= MAX_CHARS:
        raise SystemExit(
            f"validation failed: entry is {len(entry)} chars, must be 1-{MAX_CHARS}"
        )
    if not entry.endswith("."):
        raise SystemExit("validation failed: entry must end with a period")
    word_count = len(entry.split())
    if word_count != EXPECTED_WORD_COUNT:
        raise SystemExit(
            f"validation failed: entry has {word_count} words, "
            f"expected {EXPECTED_WORD_COUNT}"
        )


def verify_written(path: str, expected: str) -> None:
    """Read the file back and confirm it is byte-identical to the entry."""
    with open(path, "r", encoding="utf-8") as f:
        actual = f.read()
    if actual != expected:
        raise SystemExit(
            f"verification failed: output differs from entry "
            f"({len(actual)} chars vs {len(expected)} expected)"
        )


def print_summary(entry: str) -> None:
    """Print the entry's size so a human can eyeball the one-line gate."""
    print(f"entry: {len(entry)} chars, {len(entry.split())} words")


def main() -> None:
    validate_entry(ENTRY)
    # Gate guard: one line, 1..200 characters, not only whitespace.
    if not (1 <= len(ENTRY) <= MAX_CHARS) or not ENTRY.strip():
        raise SystemExit(f"entry fails gate: {len(ENTRY)} chars")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    verify_written(OUTPUT_PATH, ENTRY)
    print_summary(ENTRY)


if __name__ == "__main__":
    main()
