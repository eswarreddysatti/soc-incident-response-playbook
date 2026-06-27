# Common Splunk Detection Queries

## Failed Logins

index=* sourcetype=WinEventLog:Security EventCode=4625
| stats count by Account_Name, host

## Successful Logins

index=* EventCode=4624
| stats count by Account_Name

## PowerShell Execution

index=* powershell
| stats count by host, user

## New Local Administrator Accounts

index=* EventCode=4720
| stats count by TargetUserName

## Account Lockouts

index=* EventCode=4740
| stats count by TargetUserName

## Multiple Failed Logins

index=* EventCode=4625
| bucket span=5m _time
| stats count by _time, Account_Name
| where count > 10
