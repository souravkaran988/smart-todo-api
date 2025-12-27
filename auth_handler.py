import time
from typing import Dict
from jose import jwt
from passlib.context import CryptContext

# 1. Setup Password Hashing
# We use bcrypt which is an industry standard for security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 2. JWT Configuration
# Use a random string for SECRET; in a real app, this would be in an .env file
# You can use this random string I generated for you:
JWT_SECRET = "9s8d7f6g5h4j3k2l1p0o9i8u7y6t5r4e3w2q1"
JWT_ALGORITHM = "HS256"

# Helper to Hash passwords
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Helper to Verify passwords during login
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Function to create the JWT Token ("The Badge")
def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600 # Token expires in 10 minutes
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return {"access_token": token}

# Function to decode/verify the JWT Token
def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return None