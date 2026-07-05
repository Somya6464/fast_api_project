from httpcore import request
from sqlalchemy.orm import Session

from auth.email_service import EmailService
from auth.redis_service import RedisService
from auth.security import hash_password, verify_password
from models.user_model import UserModel
from schemas.auth_schema import (
    SignupRequest,
    MessageResponse,
    AuthResponse,
    VerifyOtpRequest,
    UserResponse,
)
from utils.otp import generate_otp
from utils.password_validator import validate_password
from fastapi import HTTPException, status
from auth.jwt_services import generate_user_token


class AuthService:

    @staticmethod
    async def signup(
        signup_data: SignupRequest,
        response: MessageResponse,
        db: Session,
    ):

        existing_user = (
            db.query(UserModel).filter(UserModel.email == signup_data.email).first()
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        if not validate_password(signup_data.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Password must contain uppercase, lowercase, number and special character.",
            )
        pending_signup = await RedisService.get_signup_data(signup_data.email)

        if pending_signup:

            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="OTP already sent. Please wait before requesting another.",
            )

        otp = generate_otp()

        # hashed_otp = hash_password(otp)
        # signup_data["otp"] = hashed_otp
        hashed_password = hash_password(signup_data.password)

        redis_payload = {
            "username": signup_data.username,
            "email": signup_data.email,
            "password": hashed_password,
            "role": signup_data.role.value,
            "otp": otp,
        }

        await RedisService.save_signup_data(
            signup_data.email,
            redis_payload,
        )

        await EmailService.send_signup_otp(
            signup_data.email,
            otp,
        )

        return MessageResponse(success=True, message="OTP sent successfully")

    @staticmethod
    async def verify_otp(
        request: VerifyOtpRequest,
        db: Session,
    ):

        signup_data = await RedisService.get_signup_data(request.email)

        if signup_data is None:

            raise HTTPException(
                status_code=status.HTTP_410_GONE,
                detail="OTP expired or signup request not found.",
            )

        is_valid = str(request.otp) == str(signup_data["otp"])

        if not is_valid:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid OTP",
            )

        existing_user = (
            db.query(UserModel).filter(UserModel.email == signup_data["email"]).first()
        )

        if existing_user:
            await RedisService.delete_signup_data(request.email)
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        user = UserModel(
            username=signup_data["username"],
            email=signup_data["email"],
            password=signup_data["password"],
            role=signup_data["role"],
            is_verified=True,
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        await RedisService.delete_signup_data(request.email)

        access_token = generate_user_token(user)

        return AuthResponse(
            user=UserResponse.model_validate(user),
            access_token=access_token,
        )
