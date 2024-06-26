from core.exceptions import CustomException


class IDNotFoundException(CustomException):
    code = 404
    error_code = "ID_IS_NOT_FOUND"
    message = "Id is not found"