from pydantic import BaseModel, Field
from typing import Optional,List
from api.jwt.option import JWTForceAlgoOptions


class JWTForceRequest(BaseModel):
    jwt_string: str
    keylist: Optional[List[str]] = Field(None, description="List Of Keys")
    algo: JWTForceAlgoOptions
