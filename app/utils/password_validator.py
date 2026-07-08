import re


def validate_password(password: str):
    """
    Password must contain

    - 8 characters
    - One uppercase
    - One lowercase
    - One digit
    - One special character
    """

    pattern = (
        r'^(?=.*[a-z])'
        r'(?=.*[A-Z])'
        r'(?=.*\d)'
        r'(?=.*[@$!%*?&])'
        r'[A-Za-z\d@$!%*?&]{8,}$'
    )

    return bool(re.match(pattern, password))