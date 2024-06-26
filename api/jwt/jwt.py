from fastapi import APIRouter, Response, Depends, Query
from fastapi.responses import StreamingResponse
from typing import List
from core.fastapi.dependencies import PermissionDependency, AllowAll
from app.jwt.services.jwt import JWTService
from api.jwt.request import JWTForceRequest, JWTNoneAttackRequest,JWTFinderRequest
from app.user.schemas import (
    ExceptionResponseSchema,
)
from api.common.response import DefaultDataResponse
from pydantic import Field
jwt_router = APIRouter()


@jwt_router.post(
    "/finder",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def finder(jwt_force_request: JWTFinderRequest):
    return DefaultDataResponse(data=await JWTService.jwt_finder(jwt_force_request.request))

@jwt_router.post(
    "/brute-force",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def brute_force(jwt_force_request: JWTForceRequest):
    return DefaultDataResponse(data=await JWTService.jwt_force(jwt_force_request.jwt_string, jwt_force_request.algo.value, jwt_force_request.keylist))


@jwt_router.post(
    "/none-attack",
    # response_model=DefaultDataResponse,
    responses={"400": {"model": ExceptionResponseSchema}},
    dependencies=[Depends(PermissionDependency([AllowAll]))],
)
async def none_attack(jwt_noneattack_request: JWTNoneAttackRequest):
    return DefaultDataResponse(data=await JWTService.jwt_noneattack(jwt_noneattack_request.jwt_string, jwt_noneattack_request.key, jwt_noneattack_request.value))
