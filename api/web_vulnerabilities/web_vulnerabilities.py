from fastapi import APIRouter, Response, Depends, Query
from fastapi.responses import StreamingResponse
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.web_vulnerabilities.services import WebVulnerabilitiesService
from api.web_vulnerabilities.request import ClickjackingRequest, HostHeaderAttack,CSRFPocGenRequest
from app.user.schemas import (
    ExceptionResponseSchema,
)
from api.common.response import DefaultDataResponse
web_vulnerabilities_router = APIRouter()


@web_vulnerabilities_router.post(
    "/click-jacking",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def clickjacking(clickjacking_request: ClickjackingRequest):
    return DefaultDataResponse(data=await WebVulnerabilitiesService.clickjacking(clickjacking_request.url, clickjacking_request.create_script))


@web_vulnerabilities_router.post(
    "/host-header-attack",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def host_header_attack(url_request: HostHeaderAttack):
    return DefaultDataResponse(data=await WebVulnerabilitiesService.host_header_attack(url_request.url, url_request.keylist))


@web_vulnerabilities_router.post(
    "/csrf-poc-gen",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def csrf_poc_gen(url_request: CSRFPocGenRequest):
    return DefaultDataResponse(data=await WebVulnerabilitiesService.csrf_poc_gen(**url_request.dict()))

@web_vulnerabilities_router.post(
    "/info-leak",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def info_leak(url_request: HostHeaderAttack):
    return DefaultDataResponse(data=await WebVulnerabilitiesService.info_leak(url_request.url, url_request.keylist))

@web_vulnerabilities_router.get(
    "/open-redirect",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def openredirect(url: str = Query(max_length=200),):
    return DefaultDataResponse(data=await WebVulnerabilitiesService.openredirect(url))
