

import os
import ipaddress
import socket
import validators


class TargetValidation:
    def __init__(self):
        pass

    def valid_ip(self, ip):
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    def valid_subnet(self, subnet):
        try:
            ipaddress.IPv4Network(subnet)
            return True
        except ValueError:
            return False

    def valid_domain(self, domain):
        try:
            socket.gethostbyname(domain)
            return True
        except socket.error:
            return False

    def valid_url(self, url):
        return validators.url(url) is True

    def valid_target(self, target):
        try:
            if self.valid_domain(target) or self.valid_ip(target) or self.valid_subnet(target):
                return True

            return False
        except socket.error:
            return False
        except ValueError:
            return False
