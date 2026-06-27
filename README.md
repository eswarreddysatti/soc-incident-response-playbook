# SOC Incident Response Toolkit

![Python](https://img.shields.io/badge/Python-3.11-blue)
![MIT License](https://img.shields.io/badge/License-MIT-green)
![GitHub Actions](https://img.shields.io/badge/CI-Passing-brightgreen)
![SOC](https://img.shields.io/badge/SOC-Incident%20Response-red)
![Splunk](https://img.shields.io/badge/Splunk-Detection-black)
![Sigma](https://img.shields.io/badge/Sigma-Rules-blueviolet)
![YARA](https://img.shields.io/badge/YARA-Malware%20Detection-orange)

Enterprise-grade SOC Incident Response Toolkit containing playbooks, detection engineering resources, Python utilities, Sigma rules, YARA rules, and incident response documentation.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![GitHub Actions](https://img.shields.io/badge/CI-Passing-brightgreen?style=for-the-badge&logo=githubactions)
![SOC](https://img.shields.io/badge/SOC-Incident_Response-red?style=for-the-badge)
![Splunk](https://img.shields.io/badge/Splunk-Detection-black?style=for-the-badge&logo=splunk)
![Sigma](https://img.shields.io/badge/Sigma-Rules-blueviolet?style=for-the-badge)
![YARA](https://img.shields.io/badge/YARA-Malware_Detection-orange?style=for-the-badge)# 🛡️ SOC Incident Response Toolkit

<p align="center">

<img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Splunk-SPL-black?style=for-the-badge&logo=splunk">
<img src="https://img.shields.io/badge/Sigma-Detection_Rules-blueviolet?style=for-the-badge">
<img src="https://img.shields.io/badge/YARA-Malware_Detection-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/MIT-License-green?style=for-the-badge">
<img src="https://img.shields.io/badge/GitHub_Actions-CI-success?style=for-the-badge&logo=githubactions">

</p>

Enterprise-grade Security Operations (SOC) Incident Response Toolkit inspired by real-world enterprise environments. This repository contains incident response playbooks, detection engineering resources, Splunk SPL queries, Sigma rules, YARA rules, Python automation utilities, and investigation documentation.

---

# 📌 Features

- Incident Response Playbooks
- Detection Engineering
- Splunk SPL Queries
- Sigma Detection Rules
- YARA Rules
- MITRE ATT&CK Mapping
- IOC Extraction Utility
- Hash Validation Utility
- Log Statistics Utility
- Windows Investigation Cheat Sheet
- IOC Hunting Cheat Sheet
- GitHub Actions CI
- Sample Security Logs

---

# 📂 Repository Structure

```text
soc-incident-response-playbook/
│
├── .github/
│   ├── workflows/
│   ├── ISSUE_TEMPLATE/
│   ├── CODEOWNERS
│   └── pull_request_template.md
│
├── detections/
│   ├── sigma/
│   ├── splunk/
│   └── yara/
│
├── docs/
│
├── incidents/
│
├── playbooks/
│
├── sample_logs/
│
├── scripts/
│
├── tools/
│   ├── hash_validator.py
│   ├── ioc_extractor.py
│   ├── log_stats.py
│   └── severity_calculator.py
│
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── SECURITY.md
└── README.md
```

---

# 🛠️ Included Tools

| Tool | Description |
|------|-------------|
| IOC Extractor | Extracts IPs, URLs, domains, emails and hashes |
| Hash Validator | Detects MD5, SHA1 and SHA256 |
| Log Statistics | Generates log statistics |
| Severity Calculator | Calculates incident severity |

---

# 📖 Documentation

- Incident Response Lifecycle
- MITRE ATT&CK Mapping
- IOC Hunting Cheat Sheet
- Windows Investigation Cheat Sheet
- Severity Matrix
- Lessons Learned

---

# 📚 Playbooks

- Phishing Response
- Ransomware Response

---

# 🔍 Detection Engineering

### Sigma

- Windows Brute Force Detection

### YARA

- Suspicious PowerShell Detection

### Splunk

- Failed Logins
- Successful Logins
- PowerShell Execution
- Account Lockouts
- Local Account Creation

---

# 💻 Technologies

- Python 3
- Splunk SPL
- Sigma
- YARA
- GitHub Actions
- Markdown

---

# 🎯 Skills Demonstrated

- Security Operations (SOC)
- Incident Response
- Detection Engineering
- Threat Hunting
- Splunk SPL
- MITRE ATT&CK
- Python Automation
- Root Cause Analysis
- GitHub CI/CD

---

# ⚠️ Disclaimer

All incident data, indicators, logs, and examples have been sanitized for educational purposes. Any resemblance to production environments is purely coincidental.

---

# 📄 License

Released under the MIT License.# SOC Incident Response Playbook

A collection of incident response documentation, response playbooks, detection logic, and SOC tooling based on real-world enterprise security operations.

## Repository Structure

```
soc-incident-response-playbook/
├── incidents/
├── playbooks/
├── templates/
├── tools/
└── docs/
```

## Contents

### Incidents
- Credential Stuffing Investigation
- Ransomware Attempt Investigation
- Insider Threat Investigation

### Playbooks
- Ransomware Containment

### Tools
- IOC Extractor
- Incident Severity Calculator

### Documentation
- Incident Severity Matrix
- Lessons Learned

## Skills Demonstrated

- Splunk SPL
- Incident Response
- MITRE ATT&CK
- Root Cause Analysis
- Python Automation
- Security Operations
- Documentation

> All incident data has been sanitised. Any resemblance to real production environments is coincidental.

