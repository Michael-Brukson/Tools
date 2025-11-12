[CmdletBinding()]
param (
    [Alias('p')]
    [int]$PORT = 80,

    [Alias('d')]
    [string]$DIR = (pwd).Path
)

Write-Verbose ("Directory: {0}" -f $DIR)

# TODO: Known issue, currently ps1 scripts are not signed, and thus cannot be called even when added to environment paths.
# & ipvr_qr -Argument1 "-v"
& python -m http.server $PORT --bind 0.0.0.0 --directory $DIR

