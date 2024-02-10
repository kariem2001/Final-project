from core.exceptions import CustomException


class KeyException(CustomException):
    code = 400
    error_code = "KEY_NOT_FOUND"
    message = "Key Not Found In The Keylist"