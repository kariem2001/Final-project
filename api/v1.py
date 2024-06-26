from api.user.v1.user import user_router as user_v1_router
from api.enum.enum import enum_router
from api.host_discover.host_discover import host_discover_router

from api.vulnerability.vulnerability import vulnerability_router
from api.vulnerability.vulnerability_cve import vulnerability_cve_router
from api.jwt.jwt import jwt_router
from api.web_vulnerabilities import web_vulnerabilities_router
from fastapi import APIRouter

api_v1 = APIRouter(prefix="/api/v1")

api_v1.include_router(web_vulnerabilities_router,
                      prefix="/web-vulnerabilities", tags=["Web Vulnerabilities"])

api_v1.include_router(jwt_router,
                      prefix="/jwt", tags=["JWT"])
api_v1.include_router(vulnerability_router,
                      prefix="/vulnerabilities", tags=["Vulnerabilities"])
""" api_v1.include_router(vulnerability_cve_router,
                      prefix="/vulnerability/cves", tags=["Vulnerability Cves"]) """
api_v1.include_router(enum_router, prefix="/enums", tags=["Enums"])
api_v1.include_router(host_discover_router,
                      prefix="/host-discover", tags=["Host Discover"])

api_v1.include_router(user_v1_router, prefix="/users", tags=["User"])
