from pydantic import BaseModel

class JWTNoneAttackRequest(BaseModel):
    jwt_string: str
    key: str
    value: str
