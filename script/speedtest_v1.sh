#!/bin/bash
# version 1.0
echo "curl-st written by Joe Moser"
echo "https://github.com/jmoser2004/curl-st"

echo "Ping test:"
ping=$(curl -o /dev/null -w "%{time_connect}\n" -s http://curl-st.fyi/ | awk '{printf "%.2f ms\n", $1 * 1000}')
echo "$ping"

echo "Download test:"
download=$(curl -o /dev/null -w "%{speed_download}\n" -s http://curl-st.fyi/download | awk '{printf "%.2f Mbps\n", $1 * 8 / 1000000}')
echo "$download"

echo "Upload test:"
upload=$(dd if=/dev/zero bs=1M count=10 2>/dev/null | curl -X POST --data-binary @- -o /dev/null -w "%{speed_upload}\n" -s http://curl-st.fyi/upload | awk '{printf "%.2f Mbps\n", $1 * 8 / 1000000}')
echo "$upload"