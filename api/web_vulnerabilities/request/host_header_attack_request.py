from pydantic import BaseModel, Field
from typing import Optional
from api.jwt.option import JWTForceAlgoOptions


class HostHeaderAttack(BaseModel):
    url: str
    keylist: Optional[str] = Field(None, description="List Of Keys should be seperated by '\\n' new line (breaking like)")

