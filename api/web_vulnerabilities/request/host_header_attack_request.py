from pydantic import BaseModel, Field
from typing import Optional,List
from api.jwt.option import JWTForceAlgoOptions


class HostHeaderAttack(BaseModel):
    url: str
    keylist: Optional[List[str]] = Field(None, description="List Of Keys")

