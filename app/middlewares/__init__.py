from typing import List
import os
from core.config import Config
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from core.fastapi.middlewares import (
    on_auth_error,
    AuthenticationMiddleware,
    AuthBackend,
    SQLAlchemyMiddleware,
    ResponseLogMiddleware,
)
from fastapi import FastAPI, Request
from fastapi.middleware.trustedhost import TrustedHostMiddleware


def init_middlewares() -> List[Middleware]:
    middleware = [
        Middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(
            AuthenticationMiddleware,
            backend=AuthBackend(),
            on_error=on_auth_error,
        ),
        Middleware(SQLAlchemyMiddleware),
        Middleware(ResponseLogMiddleware),
    ]
    return middleware


def init_custom_middlewares(app_: FastAPI, config: Config) -> None:
    app_.add_middleware(
        TrustedHostMiddleware, allowed_hosts=[
            config.APP_TRUST_HOST, "*."+config.APP_TRUST_HOST]
    )
