from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.service import AuthService
from app.core.db import get_db
from app.schemas.auth_schema import (
    MessageResponse,
    SignupRequest,
    AuthResponse,
    VerifyOtpRequest,
    ResendOtpRequest,
    LoginRequest,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=AuthResponse,
    status_code=200,
)
async def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    return await AuthService.login(request, db)


@router.post(
    "/signup",
    status_code=201,
)
async def signup(
    request: SignupRequest,
    db: Session = Depends(get_db),
):

    return await AuthService.signup(
        request,
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


@router.post(
    "/resend-otp",
    response_model=MessageResponse,
)
async def resend_otp(request: ResendOtpRequest):
    return await AuthService.resend_otp(request)
