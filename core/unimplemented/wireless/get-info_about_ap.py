#Get info about connected wifi Network

from wifi import Cell

net = Cell.all('wlan0') #net is object conains AP info
for i in net:   #for each network
    print(i.ssid)   #wifi network name
    print(i.signal)
    print(i.quality)
    print(i.bitrates)
    print(i.encrypted)
    print(i.encryption_type)
    print(i.channel)
    print(i.address) #mac address of AP
    print(i.mode)
    print(i.frequency)
