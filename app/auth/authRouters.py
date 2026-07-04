from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.service import AuthService
from core.db import get_db
from schemas.auth_schema import (
    MessageResponse,
    SignupRequest,
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
        db,
    )
