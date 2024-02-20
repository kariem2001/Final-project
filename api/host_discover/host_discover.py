from fastapi import APIRouter, Response, Depends, Query
from fastapi.responses import StreamingResponse
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.host_discovery.services import HostDiscoverService
from app.host_discovery.options import PortScannerEnum, IPScannerEnum
from app.user.schemas import (
    ExceptionResponseSchema,
)
from api.common.response import DefaultDataResponse
from api.host_discover.request import PortScannerRequest
host_discover_router = APIRouter()


@host_discover_router.get(
    "/ip-scanner",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def ip_scanner(
    ip_address: str = Query(max_length=200),
    type: IPScannerEnum = Query(),
):

    return DefaultDataResponse(data=await HostDiscoverService.ip_scanner(ip_address, type.value))

@host_discover_router.post(
    "/port-scanner",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def port_scanner(
    port_req: PortScannerRequest
):

    return DefaultDataResponse(data=await HostDiscoverService.port_scanner(port_req.network_prefix, port_req.type.value, port_req.ports))
