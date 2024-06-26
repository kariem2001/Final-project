from .validation_handler import *
from .custom_handler import *
from fastapi import FastAPI
from core.exceptions import CustomException
from fastapi.exceptions import RequestValidationError
from .target_exception import TargetException

def init_exception(app_: FastAPI) -> None:
    app_.add_exception_handler(CustomException, custom_exception_handler)
    app_.add_exception_handler(RequestValidationError, validation_exception_handler)

__all__ = ["TargetException"]