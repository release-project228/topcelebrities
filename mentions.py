#!/usr/bin/env python3
"""Count how often celebrity names appear in a text from stdin.

Usage: cat article.txt | python mentions.py "Taylor Swift" "Elon Musk"
"""
import sys


def main(names: list) -> int:
    text = sys.stdin.read().lower()
    counts = [(name, text.count(name.lower())) for name in names]
    counts.sort(key=lambda pair: pair[1], reverse=True)
    if not any(c for _, c in counts):
        print("no mentions found")
        return 1
    for name, count in counts:
        if count:
            print(f"{count:>3}  {name}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
