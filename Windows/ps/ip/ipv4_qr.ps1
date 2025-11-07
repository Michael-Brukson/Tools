[CmdletBinding()]
param (
    [Alias('s')]
    [switch]$SEC,
    
    [Alias('p')]
    [int]$PORT = 80
)

$IPV4 = &.\ipv4 | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne "" } | Select-Object -Last 1 

$PROT = if ($SEC) {"https"} else {"http"}
[string]$URL = "https://qrenco.de/{0}://{1}:{2}" -f $PROT, $IPV4, $PORT


Write-Verbose ("Secure?: {0}" -f $SEC)
Write-Verbose ("Port: {0}" -f $PORT)
Write-Verbose ("Host: {0}" -f $IPV4)
Write-Verbose ("Curling: {0}" -f $URL)

# & curl.exe "https://qrenco.de/{0}" -f $URL --silent --location --insecure\
& curl.exe $URL