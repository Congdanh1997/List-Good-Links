## Command line 
* adb connect 127.0.0.1:62001
* ls /data/misc/user/0/cacerts-added/
* mount -o rw,remount /system | mount -o rw,remount /
* mv /data/misc/user/0/cacerts-added/9a5ba575.0 /system/etc/security/cacerts/
* chown root:root /system/etc/security/cacerts/9a5ba575.0
* chmod 644 /system/etc/security/cacerts/9a5ba575.0
* reboot
