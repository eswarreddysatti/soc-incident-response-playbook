# Phishing Incident Response Playbook

## Objective

Provide a repeatable process for investigating and containing phishing incidents.

## Detection

- User reports suspicious email
- Email gateway alert
- SIEM detection
- EDR alert

## Validation

- Check sender domain
- Review email headers
- Inspect URLs
- Verify attachments
- Search for additional recipients

## Containment

- Remove email from all mailboxes
- Block sender
- Block malicious domains
- Block malicious URLs
- Isolate affected endpoints if necessary

## Eradication

- Delete malicious files
- Reset compromised credentials
- Remove persistence mechanisms

## Recovery

- Restore user access
- Verify endpoint health
- Continue monitoring for 24–48 hours

## Lessons Learned

- Update detection rules
- Improve user awareness
- Document findings
