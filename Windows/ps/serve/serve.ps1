[CmdletBinding()]
param (
    [Alias('p')]
    [int]$PORT = 80
)

$IPV4 &.\ipv4.ps1

