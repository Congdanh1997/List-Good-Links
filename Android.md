## Lấy AndroidID Gốc
`adb shell "service call iphonesubinfo 4 | cut -c 52-66 | tr -d '.[:space:]'`
## Requirement PKG
`termux-setup-storage && pkg update -y && pkg upgrade -y && pkg install python -y`

## install ApkPatcher
`pip install --force-reinstall https://github.com/TechnoIndian/ApkPatcher/archive/refs/heads/main.zip`

## Sign App
`ApkPatcher -i /storage/emulated/0/Download/Laftel.apk -a -c /storage/emulated/0/Download/Reqable/reqable-ca.pem`
