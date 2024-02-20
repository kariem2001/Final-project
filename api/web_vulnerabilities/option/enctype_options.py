from enum import Enum


class EnctypeOptions(Enum):
    FormUrlEncoded = "application/x-www-form-urlencoded"
    FormData = "multipart/form-data"
    TextPlain = "text/plain"
