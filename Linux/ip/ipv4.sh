#!/bin/bash

ipv4=`ip -4 -br addr show wlan0`

reg="\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

echo $ipv4 | grep -oP $reg