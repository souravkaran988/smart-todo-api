from pydantic import BaseModel, EmailStr, Field

# This is what the user sends to sign up (Register)
class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

# This is what the user sends to log in
class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)