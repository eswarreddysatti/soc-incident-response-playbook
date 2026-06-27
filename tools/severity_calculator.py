#!/usr/bin/env python3

def calculate_severity(users, systems, production):
    score = 0

    if users >= 1000:
        score += 2
    elif users >= 100:
        score += 1

    if systems >= 10:
        score += 2
    elif systems >= 3:
        score += 1

    if production:
        score += 2

    if score >= 5:
        return "P1"
    elif score >= 3:
        return "P2"
    elif score >= 2:
        return "P3"
    else:
        return "P4"


if __name__ == "__main__":
    print("Incident Severity Calculator")
    users = int(input("Affected users: "))
    systems = int(input("Affected systems: "))
    production = input("Production outage? (y/n): ").lower() == "y"

    print("Severity:", calculate_severity(users, systems, production))
