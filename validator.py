from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.exceptions import RequestValidationError

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    custom_messages = {
        "Field required": "El campo es obligatorio",
        "String should have at most 50 characters": "El nombre no debe superar 50 caracteres",
        "String should have at least 3 characters": "El nombre debe tener al menos 3 caracteres",
        # Agrega aquí todos los mensajes que quieras reemplazar
    }

    errors = []
    for error in exc.errors():
        loc = error.get("loc", [])
        if loc and loc[0] == "body":
            field = ".".join(str(part) for part in loc[1:])
        else:
            field = ".".join(str(part) for part in loc)

        original_message = error.get("msg")
        message = custom_messages.get(original_message, original_message)
        errors.append({
            "campo": field,
            "mensaje": message
        })
    return JSONResponse(
        status_code=422,
        content={
            "mensaje": "Error de validación de datos",
            "errores": errors
        },
    )
"""
async def validation_exception_handlerII(request: Request, exc: RequestValidationError):
    custom_errors = []
    for error in exc.errors():
        field = error.get("loc", ["?"])[-1]
        if error["type"] == "missing":
            msg = f"El campo '{field}' es obligatorio."
        else:
            msg = error["msg"]

        custom_errors.append({"field": field, "message": msg})

    return JSONResponse(status_code=422, content={"errors": custom_errors})
"""