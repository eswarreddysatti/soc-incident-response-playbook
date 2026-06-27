# Windows Investigation Cheat Sheet

## Running Processes

tasklist

Get-Process

## Network Connections

netstat -ano

Get-NetTCPConnection

## Logged-in Users

query user

whoami

## Scheduled Tasks

schtasks /query

## Services

sc query

Get-Service

## Event Logs

Get-WinEvent -LogName Security

## Startup Programs

wmic startup

## Installed Programs

wmic product get name,version

## DNS Cache

ipconfig /displaydns

## ARP Cache

arp -a
