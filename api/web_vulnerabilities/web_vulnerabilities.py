from fastapi import APIRouter, Response, Depends, Query
from fastapi.responses import StreamingResponse
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.web_vulnerabilities.services import WebVulnerabilitiesService
from api.web_vulnerabilities.request import ClickjackingRequest
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
