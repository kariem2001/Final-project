import socket

def dns_lookup(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        print(f"IP address for {domain_name}: {ip_address}")
    except socket.gaierror as e:
        print(f"Failed to resolve {domain_name}: {e}")

if __name__ == "__main__":
    domain_name = input("Enter a domain name: ")
    dns_lookup(domain_name)
