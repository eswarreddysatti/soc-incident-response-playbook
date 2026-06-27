rule Suspicious_PowerShell
{
    meta:
        description = "Detects suspicious PowerShell commands"
        author = "Eswar Reddy"
        date = "2026-06-27"

    strings:
        $a = "powershell -enc" nocase
        $b = "Invoke-Expression" nocase
        $c = "DownloadString" nocase
        $d = "FromBase64String" nocase

    condition:
        any of them
}
