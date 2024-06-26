from fastapi import APIRouter, Response, Depends, Query
from fastapi.responses import StreamingResponse
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.host_discovery.services import HostDiscoverService
from app.host_discovery.options import ServiceScannerEnum, IPScannerEnum
from app.user.schemas import (
    ExceptionResponseSchema,
)
from api.common.response import DefaultDataResponse
from api.host_discover.request import PortScannerRequest
from api.web_vulnerabilities.option import MethodsOptions

host_discover_router = APIRouter()


""" @host_discover_router.get(
    "/ip-scanner",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def ip_scanner(
    ip_address: str = Query(max_length=200),
    type: IPScannerEnum = Query(),
):

    return DefaultDataResponse(data=await HostDiscoverService.ip_scanner(ip_address, type))


@host_discover_router.post(
    "/port-scanner",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def port_scanner(
    port_req: PortScannerRequest
):

    return DefaultDataResponse(data=await HostDiscoverService.port_scanner(port_req.ip_address, port_req.type, port_req.port_list_type, port_req.ports))


@host_discover_router.get(
    "/service-scanner",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def service_scanner(
    target: str = Query(max_length=200),
    method: ServiceScannerEnum = Query(),
):
    return DefaultDataResponse(data=await HostDiscoverService.service_scanner(target, int(method)))
 """

@host_discover_router.get(
    "/footprinting",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def footprinting(
    url: str = Query(max_length=200),
    method: MethodsOptions = Query(default=MethodsOptions.GET),
):
    return DefaultDataResponse(data=await HostDiscoverService.footprinting(url, method.value))
