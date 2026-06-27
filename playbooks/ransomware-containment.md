# Ransomware Containment Playbook

## Objective

This playbook provides a structured response procedure for suspected or confirmed ransomware activity in an enterprise environment.

---

## Phase 1 — Detection

Indicators include:

- Multiple file extension changes
- Shadow copy deletion
- Unusual PowerShell activity
- High disk write activity
- Mass SMB connections
- Known ransomware indicators

---

## Phase 2 — Initial Response

Actions:

1. Declare incident severity.
2. Notify SOC Lead.
3. Open incident bridge.
4. Create incident ticket.
5. Preserve evidence.

---

## Phase 3 — Containment

Immediate actions:

- Isolate infected endpoints.
- Disable compromised accounts.
- Block malicious IP addresses.
- Stop scheduled malicious tasks.
- Prevent lateral movement.

---

## Phase 4 — Investigation

Collect:

- Windows Event Logs
- Sysmon Logs
- Splunk Search Results
- Process Tree
- Network Connections
- Indicators of Compromise

Map activity to the MITRE ATT&CK framework.

---

## Phase 5 — Recovery

- Restore affected systems.
- Reset credentials.
- Validate backups.
- Monitor for reinfection.
- Verify business services.

---

## Phase 6 — Post Incident Review

Document:

- Root Cause
- Timeline
- Lessons Learned
- Detection Improvements
- Playbook Updates

---

## Success Criteria

- Threat contained
- Business restored
- Documentation completed
- Detection logic improved
