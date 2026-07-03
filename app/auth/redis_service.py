import json

from core.config import settings
from core.redis import redis_client


class RedisService:

    @staticmethod
    async def save_signup_data(
        email: str,
        data: dict
    ):

        key = f"signup:{email}"

        await redis_client.set(
            key,
            json.dumps(data),
            ex=settings.OTP_EXPIRE_SECONDS
        )

    @staticmethod
    async def get_signup_data(
        email: str,
    ):

        key = f"signup:{email}"

        data = await redis_client.get(key)

        if not data:
            return None

        return json.loads(data)

    @staticmethod
    async def delete_signup_data(
        email: str,
    ):

        key = f"signup:{email}"

        await redis_client.delete(key)
    
    @staticmethod
    async def otp_exists(
    email: str
    ):

        key = f"signup:{email}"

        return await redis_client.exists(key)