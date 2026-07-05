from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.service import AuthService
from core.db import get_db
from schemas.auth_schema import (
    MessageResponse,
    SignupRequest,
    AuthResponse,
    VerifyOtpRequest,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/signup",
    response_model=MessageResponse,
    status_code=201,
)
async def signup(
    request: SignupRequest,
    db: Session = Depends(get_db),
):

    return await AuthService.signup(
        request,
        MessageResponse,
        db,
    )


@router.post(
    "/verify-otp",
    response_model=AuthResponse,
)
async def verify_otp(
    request: VerifyOtpRequest,
    db: Session = Depends(get_db),
):

    return await AuthService.verify_otp(
        request,
        db,
    )
