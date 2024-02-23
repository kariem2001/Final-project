import nmap3
import ipaddress
import socket

nmap = nmap3.NmapHostDiscovery()


def valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def valid_subnet(subnet):
    try:
        ipaddress.IPv4Network(subnet)
        return True
    except ValueError:
        return False
    
def valid_domain(domain):
    try:
        socket.gethostbyname(domain)
        return True
    except socket.error:
        return False

def extract_live_ips(results):
    if results:
        for ip_address, result in results.items():
            try:
                if result['state']['state'] == 'up':
                    print(f"{ip_address} is up", "\n")
            except:
                pass

def main():
    try:
        while True:
            target = str(input("Enter the target: "))
            if valid_domain(target) or valid_ip(target) or valid_subnet(target):
                break
            print("Try again with valid domain or IP or subnet")
        
        while True:
            switch = int(input("Enter the host discovery method: "))
            """ drop-list:
                    1- ICMP
                    2- ARP
                    3- No_DNS_Resolution
            """
            if switch >= 1 and switch <= 3:
                break
            print("Try again with valid choice")

        while True:
            threads = int(input("Enter no of threads: "))
            """ drop-list:
                    1- paranoid (very slow)
                    2- sneaky
                    3- polite
                    4- normal --> # the default option
                    5- aggressive
                    6- insane (very fast and less accuracy)
            """
            if threads >= 1 and threads <= 6:
                break
            print("Try again with an integer between 1 and 6")
            
        
        results = None
        match switch:
            case 1:
                results = nmap.nmap_no_portscan(target, args=f"-T{threads}") # Ping Sweep (Disable Port Scanning)
            case 2:
                results = nmap.nmap_arp_discovery(target, args=f"-T{threads}") # Arp Discovery
            case 3:
                results = nmap.nmap_disable_dns(target, args=f"-T{threads}") #No DNS Resolution
        extract_live_ips(results)
    except Exception as e:
        print("Try again with a valid input")
        pass

if __name__ == "__main__":
    main()
    

