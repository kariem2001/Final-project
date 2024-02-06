from typing import List
import core.pentests.JWT as jwt
from app.jwt.exceptions import KeyException, NoneAttackException
from api.jwt.option import JWTForceAlgoOptions

import json


class JWTService:
    def __init__(self):
        ...

    @staticmethod
    async def jwt_force(jwt_string: str, algo: JWTForceAlgoOptions, keylist: str | None) -> dict:
        if keylist is None:
            with open('./core/pentests/JWT/jwtlist.txt', 'r') as file:
                keylist = file.read()

        keylist = keylist.split("\n")

        val = jwt.JWtForce.jwt_force(jwt_string, keylist, algo.value)

        if val is None:
            raise KeyException()

        return val

    @staticmethod
    async def jwt_noneattack(jwt_string: str, key: str, value: str) -> str:

        val = None
        try:

            val = jwt.modify_jwt(jwt_string, key, value)

        except Exception as e:
            raise NoneAttackException(str(e))

        if val is None:
            raise NoneAttackException

        return val

    @staticmethod
    async def jwt_finder(request: str) -> str:

        val = None
        try:

            val = jwt.find_and_decode_jwt(request)

        except json.JSONDecodeError as e:
            raise NoneAttackException(str(e))

        except Exception as e:
            raise NoneAttackException(str(e))

        return val
