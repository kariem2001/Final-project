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