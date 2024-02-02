from pydantic import BaseModel, Field
from typing import Optional
from api.jwt.option import JWTForceAlgoOptions


class JWTForceRequest(BaseModel):
    jwt_string: str
    keylist: Optional[str] = Field(None, description="List Of Keys should be seperated by '\\n' new line (breaking like)")
    algo: JWTForceAlgoOptions
