#!/usr/bin/env python3

import re
import sys

PATTERNS = {
    "IPv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "Domain": r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b",
    "URL": r"https?://[^\s]+",
    "Email": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
    "MD5": r"\b[a-fA-F0-9]{32}\b",
    "SHA1": r"\b[a-fA-F0-9]{40}\b",
    "SHA256": r"\b[a-fA-F0-9]{64}\b",
}

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <file>")
    sys.exit(1)

with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()

for name, pattern in PATTERNS.items():
    matches = sorted(set(re.findall(pattern, data)))
    print(f"\n{name}:")
    if matches:
        for match in matches:
            print(f"  - {match}")
    else:
        print("  None found")
