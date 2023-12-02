from fastapi import APIRouter, Response, Depends
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.enum.services import EnumService
from app.user.schemas import (
    ExceptionResponseSchema,
)

from pydantic import Field


enum_router = APIRouter()


@enum_router.get(
    "",
    #response_model=List[VulnerabilityCveResponse],
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def index(
    
):
    return await EnumService.list_vulnerabilities()
