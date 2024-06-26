from pydantic import BaseModel, Field, validator
from typing import Optional, List
from app.host_discovery.options import PortScannerEnum, PortListTypeEnum


class PortScannerRequest(BaseModel):
    ip_address: str = Field(..., max_length=200)
    type: PortScannerEnum
    port_list_type: PortListTypeEnum = Field(default=PortListTypeEnum.top)
    ports: Optional[List[int]] = Field(
        None, description="List Of ports to be scanned")

    @validator('ports', always=True)
    def prevent_zero(cls, ports, values):
        if values.get('port_list_type') == PortListTypeEnum.top and ports[0] > 1000:
            raise ValueError('top ports should be at most 1000')
        return ports
