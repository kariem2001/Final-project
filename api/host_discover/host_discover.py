from fastapi import APIRouter, Response, Depends, Query
from fastapi.responses import StreamingResponse
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.host_discovery.services import HostDiscoverService
from app.host_discovery.options import PortScannerEnum
from app.user.schemas import (
    ExceptionResponseSchema,
)
from api.common.response import DefaultDataResponse
from pydantic import Field
host_discover_router = APIRouter()


@host_discover_router.get(
    "/ip-scanner",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def ip_scanner(
    network_prefix: str = Query(max_length=200),
    type: PortScannerEnum = Query(),
):

    return DefaultDataResponse(data=await HostDiscoverService.ip_scanner(network_prefix, type))
