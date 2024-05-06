# ADD Proxy With User
```
adb shell settings put global http_proxy 192.168.225.100:3128
adb shell settings put global global_http_proxy_host 192.168.225.100
adb shell settings put global global_http_proxy_port 3128
adb shell settings put global global_http_proxy_username foo
adb shell settings put global global_http_proxy_password bar
```
# Remove Proxy
```
adb shell settings delete global http_proxy
adb shell settings delete global global_http_proxy_host
adb shell settings delete global global_http_proxy_port
adb shell settings delete global global_http_proxy_username
adb shell settings delete global global_http_proxy_password
adb shell settings delete global global_http_proxy_exclusion_list
adb shell settings delete global global_proxy_pac_url
adb shell reboot
```
