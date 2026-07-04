from fastapi_mail import FastMail, MessageSchema, MessageType

from core.mail import conf


class EmailService:

    @staticmethod
    async def send_signup_otp(email: str, otp: str):

        message = MessageSchema(
            subject="Verify your email",
            recipients=[email],
            body=f"""
Hello,

Your OTP is

{otp}

This OTP is valid for 5 minutes.

If you didn't request this, ignore this email.
            """,
            subtype=MessageType.plain,
        )

        fm = FastMail(conf)

        await fm.send_message(message)
