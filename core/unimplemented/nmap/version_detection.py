import nmap3
import os
nmap = nmap3.Nmap()


def extract_live_ips(results):
    for ip_address, result in results.items():
        try:
            if result['state']['state'] == 'up':
                print(f"{ip_address} is up", "\n")
        except:
            pass

try:
    target = input("Enter the target: ")    
    switch = int(input("""Enter the scan method: 
                       1- service detection
                       2- os detection
                       3- Aggressive mode"""))
    if switch == 1:
        results = os.system("nmap -T4 -Pn -sV " + target)
        print(results)
    elif switch == 2:
        results =  nmap.nmap_os_detection(target, args="-T4 -Pn")
        print(results)
    elif switch == 3:
        results =  os.system("nmap -T4 -Pn -A " + target)
except Exception as e:
    print(e)
# extract_live_ips(results)