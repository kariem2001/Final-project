from pydantic import BaseModel

class DeletedResponse(BaseModel):
     msg: str|None = "Deleted"