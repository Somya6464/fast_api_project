from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt, JWTError

from core.config import settings
from models.user_model import UserModel


def create_access_token(
    data: dict[str, Any]
) -> str:

    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update(
        {
            "exp": expire
        }
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def decode_access_token(token: str):

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )

        return payload

    except JWTError:
        return None



def generate_user_token(user: UserModel) -> str:
    """
    Generate JWT for authenticated user.
    """

    payload = {
        "sub": str(user.id),
        "email": user.email,
        "role": user.role.value,
    }

    return create_access_token(payload)

""" token = create_access_token(
    {
        "sub": str(user.id),
        "email": user.email,
        "role": user.role.value
    }


    payload 
    {
    "sub":"1",
    "email":"abc@gmail.com",
    "role":"author",
    "exp":123456789
}
) """
