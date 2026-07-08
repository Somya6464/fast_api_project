import json
from upstash_redis import Redis
from core.config import settings


class RedisService:
    # Initialize Upstash Redis client (synchronous)
    redis = Redis(
        url=settings.UPSTASH_REDIS_REST_URL, token=settings.UPSTASH_REDIS_REST_TOKEN
    )

    @staticmethod
    async def save_signup_data(email: str, data: dict):
        """Store signup data with expiration"""
        key = f"signup:{email}"
        RedisService.redis.set(key, json.dumps(data))
        RedisService.redis.expire(key, settings.OTP_EXPIRE_SECONDS)

    @staticmethod
    async def get_signup_data(email: str):
        """Retrieve signup data"""
        key = f"signup:{email}"
        data = RedisService.redis.get(key)

        if not data:
            return None

        return json.loads(data)

    @staticmethod
    async def delete_signup_data(email: str):
        """Delete signup data"""
        key = f"signup:{email}"
        RedisService.redis.delete(key)

    @staticmethod
    async def otp_exists(email: str):
        """Check if OTP exists for email"""
        key = f"signup:{email}"
        return RedisService.redis.exists(key)

    @staticmethod
    async def update_signup_data(email: str, data: dict):
        """Update signup data with new expiration"""
        key = f"signup:{email}"
        RedisService.redis.set(key, json.dumps(data))
        RedisService.redis.expire(key, settings.OTP_EXPIRE_SECONDS)
