# Incident Severity Matrix

## Purpose

This document defines the severity classification used for security incidents throughout this repository.

The matrix is inspired by enterprise SOC processes and is intended for educational purposes.

---

## Severity Levels

| Severity | Description | Response Target |
|----------|-------------|----------------|
| P1 | Critical production outage, active compromise, ransomware, customer impact | Immediate |
| P2 | High-risk security incident affecting business operations | <30 minutes |
| P3 | Moderate incident requiring investigation | Same business day |
| P4 | Informational or low-risk event | Best effort |

---

## Impact Assessment

The following dimensions are considered:

- Business impact
- Data sensitivity
- Scope of affected systems
- Threat actor capability
- Regulatory implications

---

## Example Classification

| Incident | Severity |
|----------|----------|
| Credential Stuffing | P1 |
| Ransomware Attempt | P1 |
| Insider Threat Investigation | P2 |
| Malware on single endpoint | P2 |
| Suspicious Login | P3 |
| Port Scan | P4 |

---

## Escalation Workflow

```
Alert
   │
   ▼
SOC Analyst
   │
   ▼
Severity Assessment
   │
   ├── P1 → Incident Commander + Management
   ├── P2 → Senior Analyst
   ├── P3 → Standard Investigation
   └── P4 → Monitoring
```

---

## Notes

Severity should always be reassessed whenever new evidence becomes available.

Customer impact always overrides technical severity.

