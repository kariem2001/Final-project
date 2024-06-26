from scapy.all import *

probe_list = []
ap_name = input("Enter the name of the access point: ")

def probe_info(pkt):
    if pkt.haslayer(Dot11ProbeReq):
        client_name = pkt.info.decode("utf-8", "ignore")	#to handle cases where the SSID contains non-ASCII characters
        if client_name == ap_name:
            if pkt.addr2 not in probe_list:
                print("New Probe request --", client_name)
                print("MAC is --", pkt.addr2)
                probe_list.append(pkt.addr2)

sniff(iface="Wi-Fi", prn=probe_info)

#This script monitors and prints information about probe requests related to a specific access point entered by the user
