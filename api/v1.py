from api.user.v1.user import user_router as user_v1_router
from api.auth.auth import auth_router
from api.home.home import home_router
from api.vulnerability.vulnerability import vulnerability_router
from api.vulnerability.vulnerability_cve import vulnerability_cve_router
from fastapi import APIRouter

api_v1 = APIRouter(prefix="/api/v1")

api_v1.include_router(vulnerability_router, prefix="/vulnerabilities", tags=["Vulnerabilities"])
api_v1.include_router(vulnerability_cve_router, prefix="/vulnerability/cves", tags=["Vulnerability Cves"])

api_v1.include_router(user_v1_router, prefix="/users", tags=["User"])

