from core.exceptions import CustomException


class ServiceException(CustomException):
    code = 400
    error_code = "PORT_ERROR"
    message = "Error Occured While Scanning Port"