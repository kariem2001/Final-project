from fastapi.responses import JSONResponse


async def validation_exception_handler(request, exc):
    errors = []
    for error in exc.errors():
        field_name = ".".join(map(str, error["loc"]))
        error_message = error["msg"]
        error_type = error["type"]
        errors.append({"field": field_name, "error": error_type,
                      "message": error_message})

    return JSONResponse(
        content={"detail": "Validation error", "errors": errors},
        status_code=422,
    )
