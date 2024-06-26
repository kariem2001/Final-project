from fastapi.responses import JSONResponse
from core.exceptions import CustomException

async def custom_exception_handler(request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )