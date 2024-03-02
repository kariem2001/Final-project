import core.pentests.host_discovery as hostCore
from typing import List, Optional
from app.host_discovery.exceptions import PortException, IPException
from app.host_discovery.options import PortScannerEnum, PortListTypeEnum, IPScannerEnum
from app.exceptions import TargetException


class HostDiscoverService:
    def __init__(self):
        ...

    @staticmethod
    async def ip_scanner(ip_address: str, type: IPScannerEnum) -> List:

        try:
            return hostCore.ip_scanner(ip_address, int(type))
        except TargetException as e:
            raise TargetException(str(e))
        except Exception as e:
            raise IPException(str(e))

    @staticmethod
    async def port_scanner(ip_address: str, type: PortScannerEnum, portListType: PortListTypeEnum, ports: Optional[List] = None) -> List:

        try:
            return hostCore.port_scanner(ip_address, int(
                type), int(portListType), ports)
        except TargetException as e:
            raise TargetException(str(e))
        except Exception as e:
            raise PortException(str(e))

    @staticmethod
    async def service_scanner(target: str, type: int) -> dict:

        # return hostCore.service_scanner(target=target, method=type)
        try:
            return hostCore.service_scanner(target=target, method=type)
        except TargetException as e:
            raise TargetException(str(e))
        except Exception as e:
            raise PortException(str(e))
