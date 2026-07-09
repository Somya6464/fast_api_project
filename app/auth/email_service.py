from fastapi_mail import FastMail, MessageSchema, MessageType

from app.core.mail import conf


class EmailService:

    @staticmethod
    async def send_signup_otp(email: str, otp: str):

        message = MessageSchema(
            subject="Verify your email",
            recipients=[email],
            body=f"""
<html>

<body>

<h2>Email Verification</h2>

<p>Your OTP is</p>

<h1>{otp}</h1>

<p>
This OTP is valid for
<b>5 minutes</b>.
</p>

</body>

</html>
            """,
            subtype=MessageType.html,
        )

        fm = FastMail(conf)

        await fm.send_message(message)
