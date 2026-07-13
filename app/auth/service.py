from httpcore import request
from sqlalchemy.orm import Session

from app.auth.email_service import EmailService
from app.auth.redis_service import RedisService
from app.auth.security import hash_password, verify_password
from app.models.user_model import UserModel
from app.schemas.auth_schema import (
    SignupRequest,
    MessageResponse,
    AuthResponse,
    VerifyOtpRequest,
    UserResponse,
    ResendOtpRequest,
    LoginRequest,
)
from app.utils.otp import generate_otp
from app.utils.password_validator import validate_password
from fastapi import HTTPException, status, BackgroundTasks
from app.auth.jwt_services import generate_user_token
import time


class AuthService:

    @staticmethod
    async def login(request: LoginRequest, db: Session):
        user = db.query(UserModel).filter(UserModel.email == request.email).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        if not verify_password(request.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid credentials",
            )

        access_token = generate_user_token(user)

        return AuthResponse(
            user=UserResponse.model_validate(user),
            access_token=access_token,
        )

    @staticmethod
    async def signup(
        background_tasks: BackgroundTasks,
        signup_data: SignupRequest,
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

        hashed_password = hash_password(signup_data.password)

        redis_payload = {
            "username": signup_data.username,
            "email": signup_data.email,
            "password": hashed_password,
            "role": signup_data.role.value,
            "otp": otp,
            "last_sent": int(time.time()),
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

    @staticmethod
    async def resend_otp(request: ResendOtpRequest):
        signup_data = await RedisService.get_signup_data(request.email)

        if signup_data is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Signup session expired."
            )
        now = int(time.time())
        last_sent = signup_data.get("last_sent", 0)
        if now - last_sent < 60:

            remaining = 60 - (now - last_sent)

            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"Please wait {remaining} seconds before requesting another OTP.",
            )

        otp = generate_otp()

        signup_data["otp"] = str(otp)

        signup_data["last_sent"] = now

        await RedisService.update_signup_data(
            request.email,
            signup_data,
        )

        await EmailService.send_signup_otp(
            request.email,
            otp,
        )

        return MessageResponse(success=True, message="OTP resent successfully.")
