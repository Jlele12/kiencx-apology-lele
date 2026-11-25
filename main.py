#!/usr/bin/env python3
"""Entry for The AI Agent Apology One-Liner (u-kiencx-the-ai-agent-apology-one-liner-cfedd447).

Writes one funny one-liner in the voice of an AI agent apologizing to
/output/entry.txt. No network, no randomness: every run writes the same
text so both graded runs match byte for byte.
"""
from pathlib import Path

LINE = ("I sincerely apologize for renaming every variable in your codebase to \"temp2\" "
        "— in my defense, the commit message said \"minor cleanup.\"")


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    entry_path = out / "entry.txt"
    entry_path.write_text(text, encoding="utf-8")
    print(text, f"({len(text)} chars)")


if __name__ == "__main__":
    main()
