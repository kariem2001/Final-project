
from core.exceptions import CustomException


class IPException(CustomException):
    code = 400
    error_code = "IP_ERROR"
    message = "Error Occured While Scanning Ip"