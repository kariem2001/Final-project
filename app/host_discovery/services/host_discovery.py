import core.pentests.host_discovery as hostCore
from typing import List


class HostDiscoverService:
    def __init__(self):
        ...

    @staticmethod
    async def ip_scanner(network_prefix: str, type: str) -> List:
        res = []
        if type == "arp":
            res = hostCore.arp_ping_sweep(network_prefix)
        else:
            res = hostCore.icmp_ping_sweep(network_prefix)

        return res
