from pydantic import BaseModel, EmailStr, ConfigDict, Field
from enums.all_enums import UserRole


class SignupRequest(BaseModel):
    username: str = Field(min_length=3, max_length=100)

    email: EmailStr

    password: str = Field(min_length=8, max_length=100)

    role: UserRole


class VerifyOtpRequest(BaseModel):
    email: EmailStr

    otp: str = Field(min_length=6, max_length=6)


class VerifyOtpRequest(BaseModel):
    email: EmailStr

    otp: str = Field(min_length=6, max_length=6)


class ResendOtpRequest(BaseModel):
    email: EmailStr


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: UserRole

    model_config = ConfigDict(from_attributes=True)


class AuthResponse(BaseModel):
    user: UserResponse

    access_token: str

    token_type: str = "bearer"


class MessageResponse(BaseModel):
    message: str
