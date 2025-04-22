from fastapi import Header, HTTPException
from settings import Settings

def verifyApiKey(x_api_key: str = Header(None)):
    if x_api_key != Settings.api_key:
        raise HTTPException(status_code=403, detail="Invalid or missing API Key")