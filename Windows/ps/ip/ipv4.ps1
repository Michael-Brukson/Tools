# get output like: " IPv4 Address. . . . . . . . . . . : 192.168.42.78"
$ipv4Lines = ipconfig | Select-String -Pattern "IPv4"

foreach ($line in $ipv4Lines) {
    # Split on ":" and take the second part
    $ipPart = ($line -split ":")[1].Trim() # "192.168.1.220"
    
    Write-Output $ipPart
}
