from pydantic import BaseModel, Field
from typing import Optional, List
from app.host_discovery.options import PortScannerEnum


class PortScannerRequest(BaseModel):
    ip_address: str = Field(..., max_length=200)
    type: PortScannerEnum
    ports: Optional[List[int|None]] = Field(None, description="List Of ports to be scanned")
