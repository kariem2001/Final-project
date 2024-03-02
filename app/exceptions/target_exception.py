from core.exceptions import CustomException


class TargetException(CustomException):
    code = 400
    error_code = "TARGET_ERROR"
    message = "Invalid Target Provided"