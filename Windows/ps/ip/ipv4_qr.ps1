[CmdletBinding()]
param (
    [Alias('s')]
    [switch]$SEC,
    
    [Alias('p')]
    [int]$PORT = 80
)

$IPV4 = &.\ipv4.ps1
$PROT = if ($SEC) {"https"} else {"http"}

if ($VerbosePreference) {
    Write-Host "Secure?: " $SEC
    Write-Host "Port: " $PORT
    Write-Host "Host: " $IPV4
    Write-Host "Curling: " $PROT"://"$IPV4":"$PORT
}

curl qrenco.de/$PROT"://"$IPV4":"$PORT