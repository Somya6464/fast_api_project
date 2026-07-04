from sqlalchemy.orm import Session

from auth.email_service import EmailService
from auth.redis_service import RedisService
from auth.security import hash_password
from models.user_model import UserModel
from schemas.auth_schema import SignupRequest
from utils.otp import generate_otp
from utils.password_validator import validate_password
from fastapi import HTTPException, status


class AuthService:

    @staticmethod
    async def signup(
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

        # hashed_password = hash_password(signup_data.password)

        redis_payload = {
            "username": signup_data.username,
            "email": signup_data.email,
            "password": signup_data.password,
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

        return {"Success": True, "message": "OTP sent successfully"}
