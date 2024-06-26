from pydantic import BaseModel, Field
from typing import Optional, List
from api.web_vulnerabilities.option import MethodsOptions, EnctypeOptions


class CSRFPocGenRequest(BaseModel):
    url: str
    method: MethodsOptions
    params: dict
    encrypt: Optional[EnctypeOptions] = Field(EnctypeOptions.FormData)
    author: Optional[str] = Field(None, description="CSRF founder")
