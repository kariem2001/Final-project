from pydantic import BaseModel

class DefaultDataResponse(BaseModel):
     data:object|None=None