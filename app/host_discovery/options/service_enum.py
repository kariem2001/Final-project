

from enum import Enum


class ServiceScannerEnum(Enum):
    ServiceDetection = "service"
    VulnerabilityDetection = "vulnerability"
    OSDetection = "os"
    Aggressive = "aggressive"

    def __int__(cls):
        match cls:
            case cls.ServiceDetection:
                return 1
            case cls.VulnerabilityDetection:
                return 2
            case cls.OSDetection:
                return 3
            case _:
                return 4
