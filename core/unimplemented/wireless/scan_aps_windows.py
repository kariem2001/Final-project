from winwifi import WinWiFi
scanner = WinWiFi.scan()
# print(scanner)
for i in scanner:   #for each network
    print(f"Network Name: {i.ssid}")   #wifi network name
    print(f"Authentication Protocol: {i.auth}")
    print(f"MAC Address: {i.bssid}")
    print(f"Strength: {i.strength}") #how network is far or near to me?.. 100 is maximum
    print(f"Encryption Type: {i.encrypt}")
    print("-"*30)
