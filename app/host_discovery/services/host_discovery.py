import core.pentests.host_discovery as hostCore
from typing import List, Optional
from app.host_discovery.exceptions import PortException, IPException


class HostDiscoverService:
    def __init__(self):
        ...

    @staticmethod
    async def ip_scanner(ip_address: str, type: str) -> List:
        res = []

        try:
            if type == "arp":
                res = hostCore.arp_ping_sweep(ip_address)
            else:
                res = hostCore.icmp_ping_sweep(ip_address)
        except Exception as e:
            raise IPException(str(e))

        return res

    @staticmethod
    async def port_scanner(ip_address: str, type: str, ports: Optional[List] = None) -> List:
        res = []

        try:
            if type == "tcp":
                res = hostCore.tcp_scan(ip_address, ports)
            else:
                res = hostCore.syn_scan(ip_address, ports)
        except Exception as e:
            raise PortException(str(e))

        return res

    @staticmethod
    async def service_scanner(target: str, type: int) -> dict:
        
        return hostCore.service_scanner(target=target, method=type)
        try:
            return hostCore.service_scanner(target=target, method=type)
        except Exception as e:
            raise PortException(str(e))
