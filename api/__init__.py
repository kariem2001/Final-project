from fastapi import APIRouter

from api.v1 import api_v1 
from api.auth.auth import auth_router
from api.home.home import home_router
from api.vulnerability.vulnerability import vulnerability_router

router = APIRouter()

router.include_router(home_router)

router.include_router(api_v1)

router.include_router(auth_router, prefix="/auth", tags=["Auth"])


__all__ = ["router"]
