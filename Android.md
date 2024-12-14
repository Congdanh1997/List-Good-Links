## Lấy AndroidID Gốc
`adb shell "service call iphonesubinfo 4 | cut -c 52-66 | tr -d '.[:space:]'`
