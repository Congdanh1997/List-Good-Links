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
# DEFAULT SETTING
shell am start -a android.settings.MANAGE_DEFAULT_APPS_SETTINGS

# Change default app
adb shell cmd role add-role-holder android.app.role.DIALER com.ten.package


Để đổi bàn phím mặc định (default keyboard) qua adb, bạn dùng lệnh sau:
adb shell settings put secure default_input_method com.ten.package/.TenDichVu
Trong đó:
com.ten.package/.TenDichVu là tên đầy đủ của input method service (IME) bạn muốn đặt làm mặc định.
Ví dụ với Gboard là:
adb shell settings put secure default_input_method com.google.android.inputmethod.latin/com.android.inputmethod.latin.LatinIME
