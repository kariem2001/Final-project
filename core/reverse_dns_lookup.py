import socket

def reverse_dns_lookup(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)
        print(f"Domain name for IP address {ip_address}: {domain_name[0]}")
    except socket.herror as e:
        print(f"Reverse DNS lookup failed for {ip_address}: {e}")

if __name__ == "__main__":
    ip_address = input("Enter an IP address: ")
    reverse_dns_lookup(ip_address)
