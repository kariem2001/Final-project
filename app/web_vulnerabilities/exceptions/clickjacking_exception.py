from core.exceptions import CustomException


class ClickjackingException(CustomException):
    def __init__(self, message=None):
        super().__init__(message)

    code = 400
    error_code = "URL_INVALID"
    message = "Some Error Occurred"
