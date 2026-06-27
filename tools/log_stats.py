#!/usr/bin/env python3

import sys
from collections import Counter

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <logfile>")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

print(f"Total Lines: {len(lines)}")

words = Counter()

for line in lines:
    words.update(line.strip().split())

print("\nTop 10 Most Common Words\n")

for word, count in words.most_common(10):
    print(f"{word}: {count}")
