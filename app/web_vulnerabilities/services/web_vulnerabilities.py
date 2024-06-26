from typing import List, Optional
import requests
from app.web_vulnerabilities.exceptions import *
import core.pentests.web_vulnerabilities as WV
from api.web_vulnerabilities.option import MethodsOptions, EnctypeOptions
import validators


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
    async def host_header_attack(url: str, keylist: Optional[List[str]] = None) -> dict:
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
    async def info_leak(url: str, keylist: Optional[List[str]] = None) -> dict:
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

    async def csrf_poc_gen(url: str, method: MethodsOptions, params: dict, encrypt: EnctypeOptions = EnctypeOptions.FormData, author: str = "") -> dict:

        try:
            return {"poc": WV.form_create(method.value, url, params, author, encrypt.value)}
        except Exception as e:
            raise ClickjackingException(str(e))

    async def openredirect(url: str) -> dict:
        if not validators.url(url):
            raise ClickjackingException
        try:
            return WV.openredirect(url)
        except Exception as e:
            raise ClickjackingException(str(e))
    
    async def xxe(url: str) -> List:
        if not validators.url(url):
            raise ClickjackingException
        try:
            return WV.test_xxe(url)
        except Exception as e:
            raise ClickjackingException(str(e))

    async def xss(url: str) -> List:
        if not validators.url(url):
            raise ClickjackingException
        try:
            return WV.test_xss(url)
        except Exception as e:
            raise ClickjackingException(str(e))

    async def xpath(url: str) -> List:
        if not validators.url(url):
            raise ClickjackingException
        try:
            return WV.test_xpath(url)
        except Exception as e:
            raise ClickjackingException(str(e))


    async def ssti(url: str) -> List:
        if not validators.url(url):
            raise ClickjackingException
        try:
            return WV.test_ssti(url)
        except Exception as e:
            raise ClickjackingException(str(e))

    async def crlf(url: str) -> List:
        if not validators.url(url):
            raise ClickjackingException
        try:
            return WV.test_crlf(url)
        except Exception as e:
            raise ClickjackingException(str(e))

    async def cache_poisoning(url: str) -> List:
        if not validators.url(url):
            raise ClickjackingException
        try:
            return WV.test_cache_poisoning(url)
        except Exception as e:
            raise ClickjackingException(str(e))
        
    async def bypass_403(url: str) -> List:
        if not validators.url(url):
            raise ClickjackingException
        try:
            return WV.bypass_403(url)
        except Exception as e:
            raise ClickjackingException(str(e))
