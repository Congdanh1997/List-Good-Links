def creat_work(id_device):
    # global user_id
    get_id = cmd_output(f'adb -s {id_device} -d shell pm create-user --profileOf 0 --managed Island')
    print(get_id.replace("\r", "").split('\n'))
    # print(get_id[0])
    user_id = get_id.split(' ')[-1]
    print(user_id)
    # time.sleep(2) com.oasisfeng.island
    cmd_output(f'adb -s {id_device} -d shell pm install-existing --user {user_id} com.oasisfeng.island') #com.vui.taptapandroid
    # time.sleep(2)
    cmd_output(f"adb -s {id_device} -d shell dpm set-profile-owner --user {user_id} com.oasisfeng.island/.IslandDeviceAdminReceiver")
    # time.sleep(2)
    cmd_output(f'adb -s {id_device} -d shell am start-user {user_id}')
    return user_id
def install_vani(id_device, user_id):
    command = f'adb -s {id_device} shell pm install-existing --user {user_id.rstrip()} com.vanilacorp.vani'
    print(command)
    cmd_output(command)
    # os.system() #com.vui.taptapandroid com.vanilacorp.vani
def run_app(id_device, user_id):
    cmd_output(f'adb -s {id_device} shell am start --user {user_id.rstrip()} "com.vanilacorp.vani/com.vanilacorp.vani.ui.OneLinkInterfaceActivity"')
