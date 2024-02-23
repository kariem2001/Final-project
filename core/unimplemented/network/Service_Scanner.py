# import nmap3
# import os
import subprocess
# nmap = nmap3.Nmap()

def main():
    try:
        target = input("Enter the target: ")    
        switch = int(input( """
                            Enter the scan method: 
                                1- Service Detection
                                2- Vulnerability Detection
                                3- OS Detection
                                4- Aggressive Scanning
                            """))
        if switch == 1:
            results = subprocess.call(f"nmap -T4 -Pn -sV {target}", shell=True)
            # results =  nmap.nmap_version_detection(target, args="-T4 -Pn")
        elif switch == 2:
            results = subprocess.call(f"nmap -T4 -Pn -sC {target}", shell=True)
        elif switch == 3:
            results = subprocess.call(f"nmap -T4 -Pn -O {target}", shell=True)
            # results =  nmap.nmap_os_detection(target, args="-T4 -Pn")
        elif switch == 4:
            results = subprocess.call(f"nmap -T4 -Pn -A {target}", shell=True)
            #results = nmap.nmap_scan(target, args="-A")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
