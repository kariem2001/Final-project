from core.exceptions import CustomException


class NoneAttackException(CustomException):
    def __init__(self, message=None):
        super().__init__(message)

    code = 400
    error_code = "JWT_INVALID"
    message = "Some Error Occurred"
