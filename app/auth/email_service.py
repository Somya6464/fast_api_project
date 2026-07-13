from fastapi_mail import FastMail, MessageSchema, MessageType

from app.core.mail import conf
import resend
from app.core.config import settings


class EmailService:

    async def send_signup_otp(email: str, otp: str):
        try:
            params: resend.Emails.SendParams = {
                "from": settings.EMAIL_FROM,
                "to": [email],
                "subject": "Your FastAPI Verification Code",
                "html": f"""
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
            }

            email_response = resend.Emails.send(params)
            print(f"✅ Email sent successfully! ID: {email_response['id']}")

        except Exception as e:
            print(f"❌ Failed to send email: {e}")
            # In production, you might want to raise an HTTPException here
            # or log it to a service like Sentry.
