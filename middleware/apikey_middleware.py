from fastapi import Request, Response
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from settings import Settings

class APIKeyMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key_header = request.headers.get("X-API-Key")

        if api_key_header != Settings.api_key:
            return JSONResponse(
                status_code=403,
                content={"detail": "Invalid or missing API Key"},
            )

        response = await call_next(request)
        return response