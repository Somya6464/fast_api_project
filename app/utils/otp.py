import secrets


def generate_otp() -> str:
    """
    Generate a secure 6-digit OTP.
    """
    return f"{secrets.randbelow(900000) + 100000}"


""" 
Why not

random.randint()

Because

secrets

is cryptographically secure.
"""