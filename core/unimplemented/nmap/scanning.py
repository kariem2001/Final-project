import nmap3
import os
nmap = nmap3.NmapScanTechniques()


def extract_live_ips(results):
    for ip_address, result in results.items():
        try:
            if result['state']['state'] == 'up':
                print(f"{ip_address} is up", "\n")
        except:
            pass

try:
    os.system("clear")
    target = str(input("Enter the target: "))    
    switch = int(input("""Enter the scan method: 
                       1- syn scan
                       2- connect scan
                       3- fin scan
                       4- ping scan
                       5- udp scan
                       6- traceroute
                       :  """))
    os.system("clear")
    if switch == 1:
        results = nmap.nmap_syn_scan(target, args="-T4 -Pn")
        print(results)
    elif switch == 2:
        results =  nmap.nmap_tcp_scan(target, args="-T4 -Pn")
    elif switch == 3:
        results = nmap.nmap_fin_scan(target, args="-T4 -Pn")
    elif switch == 4:
        results = nmap.nmap_ping_scan(target, args="-T4 -Pn")
    elif switch == 5:
        results = nmap.nmap_udp_scan(target, args="-T4 -Pn")
    elif switch == 6:
        results = os.system("nmap -T4 -Pn -traceroute")
        pass
except Exception as e:
    pass
extract_live_ips(results)