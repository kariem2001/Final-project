import nmap3
import os
import ipaddress
import socket
import time
# import re

nmap = nmap3.NmapScanTechniques()


# def valid_ip(ip):
#     try:
#         ipaddress.ip_address(ip)
#         ip_pattern = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
#         subnet_pattern = r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\/(0|[1-9]|[1-2][0-9]|3[0-2])$'
#         return re.match(ip_pattern, ip) is not None or re.match(subnet_pattern, ip) is not None

#     except ValueError:
#         return False
    
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


def extract_ports(results):
    live_ips = []
    for ip, details in results.items():
        
        if details['ports']:
            print(f"IP: {ip}")

            for port_info in details['ports']:
                port_id = port_info['portid']
                state = port_info['state']
                service_name = port_info['service']['name']
                
                if state == "open":
                    print(f"[+] Port: {port_id}, State: {state}, Service Name: {service_name}")
                elif state == "filtered":
                    print(f"[-] Port: {port_id}, State: {state}, Service Name: {service_name}")
                    



def match_state():
# After checking the scan type check for the following:
    state = int(input("Enter state of ports: "))
    """
        1- all ports
        2- specifc ports --> take them as input (20,22,80,443,8080,8443)
        3- top ports (300)
    """
    match state:
        case 1:
            ports = '-p-'
        case 2:
            ports = '-p'
            ports += str(input("Enter comma sepertaed ports: "))
        case 3:
            ports = '--top-ports '
            ports += str(input("no of top ports: "))
    # print(ports)
    return ports


def main():
    try:
        os.system("clear")
        while True:
            target = str(input("Enter the target: "))
            if valid_domain(target) or valid_ip(target) or valid_subnet(target):
                break
            print("Try again with valid domain or IP or subnet")
        
        while True:
            switch = int(input("Enter the scanning method: "))
            """ drop-list:
                    1- syn scan
                    2- connect scan
                    3- fin scan
                    4- ACK Scan
                    5- udp scan
            """
            if switch >= 1 and switch <= 5:
                break
            print("Try again with a valid number between 1 and 6")

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


        # os.system("clear")
        
        match switch:
            case 1:
                ports = match_state()
                results = nmap.nmap_syn_scan(target, args=f"-Pn -T{threads} {ports}")
            
            case 2:
                ports = match_state()
                results =  nmap.nmap_tcp_scan(target, args=f"-Pn -T{threads} {ports}")

            case 3:
                ports = match_state()
                results = nmap.nmap_fin_scan(target, args=f"-Pn -T{threads} {ports}")
            case 4:
                ports = match_state()
                results = os.system(f"nmap {target} -T{threads} -Pn -sA {ports}")
            case 5:
                ports = match_state()
                results = nmap.nmap_udp_scan(target, args=f"-Pn -T{threads} {ports}")
        
        time.sleep(1)
        extract_ports(results)

    except Exception as e:
        pass


if __name__ == "__main__":
    main()
