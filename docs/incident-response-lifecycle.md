# Incident Response Lifecycle

This repository follows a structured Incident Response (IR) lifecycle based on industry best practices.

## 1. Preparation

- Configure monitoring tools
- Define escalation paths
- Maintain incident runbooks
- Conduct tabletop exercises

---

## 2. Detection & Analysis

Objectives

- Detect suspicious activity
- Validate alerts
- Determine incident scope
- Assign severity

Typical Sources

- SIEM (Splunk)
- EDR
- IDS/IPS
- Firewall logs
- Endpoint telemetry

---

## 3. Containment

### Short-Term

- Isolate affected systems
- Disable compromised accounts
- Block malicious IPs

### Long-Term

- Patch vulnerabilities
- Strengthen controls
- Monitor affected assets

---

## 4. Eradication

- Remove malware
- Delete persistence mechanisms
- Reset credentials
- Verify clean environment

---

## 5. Recovery

- Restore services
- Validate system integrity
- Monitor for reinfection
- Inform stakeholders

---

## 6. Lessons Learned

- Root Cause Analysis
- Timeline reconstruction
- Improvement actions
- Documentation updates
