from typing import List

from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from core.fastapi.middlewares import (
    on_auth_error,
    AuthenticationMiddleware,
    AuthBackend,
    SQLAlchemyMiddleware,
    ResponseLogMiddleware,
)

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