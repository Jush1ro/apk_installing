apk = input("Название apk: ")

ipa = input("Начальный IP адрес: ")
splitip = ipa.split(".")

grandip = splitip[0]+"."+splitip[1]+"."+splitip[2]+"."

last_ip = input('Последний IP адрес: ')
last_ipsplit = last_ip.split(".")

start_ip = int(splitip[3])
end_ip = last_ipsplit[3]

while start_ip != int(end_ip)+1 : #Сравниваем начальный с последним. +1 необдходимо, что последний тоже отработал
    ipb = str(start_ip)
    ip = grandip + ipb
    print ("Установка на ",ip)
    start_ip = start_ip + 1

    cmnd = "adb connect " + ip #команда adb connect
    import os
    try:
        os.system(cmnd)
        os.popen("adb install -r " + apk)

        os.popen("adb wait-for-device")
        print("Ожидаем")
        time.sleep(15)

        os.system("adb disconnect")
    except:
        print("Ошибка")
        continue
