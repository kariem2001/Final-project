from fastapi import APIRouter, Response, Depends, Query
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.enum.services import EnumService
from app.user.schemas import (
    ExceptionResponseSchema,
)
from api.common.response import DefaultDataResponse
from pydantic import Field
from .dns import dns_router

enum_router = APIRouter()


enum_router.include_router(dns_router, prefix="/dns", tags=["DNS"])

@enum_router.get(
    "/smtp-users",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def smtp_users(
    mail_server: str = Query(max_length=200),
    port: int = Query(25, ge=0),
):
    return DefaultDataResponse(data=await EnumService.smtp_users(mail_server, port))

@enum_router.get(
    "/zone-transfer",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def zone_transfer(
    domain: str = Query(max_length=200),
):
    return DefaultDataResponse(data=await EnumService.zone_transfer(domain))
