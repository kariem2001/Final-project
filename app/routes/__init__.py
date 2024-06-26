from fastapi import FastAPI
from api import router
from api.home.home import home_router

def init_routers(app_: FastAPI) -> None:
    app_.include_router(home_router)
    app_.include_router(router)