from pydantic import BaseModel, Field
from typing import Optional
from api.jwt.option import JWTForceAlgoOptions


class ClickjackingRequest(BaseModel):
    url: str
    create_script: Optional[bool] = Field(
        False, description="Create an Exploit Script for PoC?")
