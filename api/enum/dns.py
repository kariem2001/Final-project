





from fastapi import APIRouter, Response, Depends, Query
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.enum.services import EnumService
from app.user.schemas import (
    ExceptionResponseSchema,
)
from api.common.response import DefaultDataResponse
from pydantic import Field


dns_router = APIRouter()



@dns_router.get(
    "/lookup",
    response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def dns_lookup(
    domain_name: str = Query(max_length=200)
):
    return DefaultDataResponse(data=await EnumService.dns_lookup(domain_name))

@dns_router.get(
    "/reverse-lookup",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def dns_reverse_lookup(
    ip_address: str = Query(max_length=200)

):
    return DefaultDataResponse(data=await EnumService.dns_reverse_lookup(ip_address))


@dns_router.get(
    "/records",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def dns_records(
    domain_name: str = Query(max_length=200)

):
    return DefaultDataResponse(data=await EnumService.dns_records(domain_name))
