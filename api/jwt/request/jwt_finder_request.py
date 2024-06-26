from pydantic import BaseModel, Field
from typing import Optional
from api.jwt.option import JWTForceAlgoOptions


class JWTFinderRequest(BaseModel):
    request: str
