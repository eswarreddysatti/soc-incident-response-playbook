#!/usr/bin/env python3

"""
IOC Extractor

Simple command-line utility to extract common Indicators of Compromise (IOCs)
from a text file.

Current version extracts:
- IPv4 addresses
- Domain names

Author: Eswar Reddy Satti
"""

import argparse
import pathlib
import re


IP_REGEX = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"

DOMAIN_REGEX = (
    r"\b(?:[a-zA-Z0-9-]+\.)+"
    r"(?:com|net|org|io|co|edu|gov|in|tech|xyz)\b"
)


def extract_iocs(text):
    ips = sorted(set(re.findall(IP_REGEX, text)))
    domains = sorted(set(re.findall(DOMAIN_REGEX, text)))

    return {
        "ip_addresses": ips,
        "domains": domains,
    }


def main():
    parser = argparse.ArgumentParser(description="IOC Extractor")
    parser.add_argument("file", help="Input text file")

    args = parser.parse_args()

    content = pathlib.Path(args.file).read_text(errors="ignore")

    results = extract_iocs(content)

    print("\n=== IOC Extraction Results ===\n")

    print(f"IP Addresses ({len(results['ip_addresses'])})")
    for ip in results["ip_addresses"]:
        print(f" - {ip}")

    print()

    print(f"Domains ({len(results['domains'])})")
    for domain in results["domains"]:
        print(f" - {domain}")


if __name__ == "__main__":
    main()
