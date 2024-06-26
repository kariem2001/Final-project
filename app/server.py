
from fastapi import FastAPI, Request, Depends

from core.config import config
from core.fastapi.dependencies import Logging

from core.helpers.cache import Cache, RedisBackend, CustomKeyMaker
from app.exceptions import init_exception
from app.routes import init_routers
from app.middlewares import init_middlewares, init_custom_middlewares


def init_cache() -> None:
    Cache.init(backend=RedisBackend(), key_maker=CustomKeyMaker())


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        dependencies=[Depends(Logging)],
        middleware=init_middlewares(),
    )

    init_routers(app_=app_)
    init_custom_middlewares(app_=app_,config=config)
    init_exception(app_=app_)
    init_cache()
    return app_


app = create_app()
