from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from auth_handler import decode_jwt

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        # We call the parent HTTPBearer to get the credentials from the header
        credentials = await super(JWTBearer, self).__call__(request)
        
        if credentials:
            # 1. Check if the scheme is 'Bearer'
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            
            # 2. Check if the token is valid and not expired
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired.")
            
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        is_token_valid: bool = False
        # Use our auth_handler to decode and check the token
        payload = decode_jwt(jwtoken)
        if payload:
            is_token_valid = True
        return is_token_valid