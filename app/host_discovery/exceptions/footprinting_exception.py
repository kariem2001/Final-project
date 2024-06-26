from core.exceptions import CustomException


class FootPrintingException(CustomException):
    code = 400
    error_code = "FOOT_PRINTING_ERROR"
    message = "Error Occured While Fetching Data"