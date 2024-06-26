from fastapi import APIRouter

from api.v1 import api_v1 
from api.auth.auth import auth_router

router = APIRouter()


router.include_router(api_v1)

router.include_router(auth_router, prefix="/auth", tags=["Auth"])


__all__ = ["router"]
