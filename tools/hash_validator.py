#!/usr/bin/env python3

import re
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <hash>")
    sys.exit(1)

value = sys.argv[1].strip()

patterns = {
    "MD5": r"^[a-fA-F0-9]{32}$",
    "SHA1": r"^[a-fA-F0-9]{40}$",
    "SHA256": r"^[a-fA-F0-9]{64}$",
}

for name, pattern in patterns.items():
    if re.fullmatch(pattern, value):
        print(f"Valid {name}")
        sys.exit(0)

print("Unknown hash format")
