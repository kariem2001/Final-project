from typing import List
import requests
from app.web_vulnerabilities.exceptions import *
import core.pentests.web_vulnerabilities as WV


class WebVulnerabilitiesService:
    def __init__(self):
        ...

    @staticmethod
    async def clickjacking(url: str, create_script: bool = False) -> dict:
        try:
            return WV.clickjacking(url, create_script)

        except requests.RequestException as e:
            raise ClickjackingException(str(e))
        except Exception as e:
            raise ClickjackingException

    @staticmethod
    async def host_header_attack(url: str, keylist: str = None) -> dict:
        if keylist is None:
            with open("./core/pentests/web_vulnerabilities/host_header_attack/virtual_host_enum.txt", "r") as file:
                keylist = file.read()

        keylist = keylist.split("\n")
        try:
            return WV.host_header_attack(url, keylist)

        except requests.RequestException as e:
            raise ClickjackingException(str(e))
        except Exception as e:
            raise ClickjackingException
        
    @staticmethod
    async def info_leak(url: str, keylist: str = None) -> dict:
        if keylist is None:
            with open("./core/pentests/web_vulnerabilities/recon/leaks_wordlist.txt", "r") as file:
                keylist = file.read()

        keylist = keylist.split("\n")
        try:
            return WV.check_data_leaks(url, keylist)

        except requests.RequestException as e:
            raise ClickjackingException(str(e))
        except Exception as e:
            raise ClickjackingException
