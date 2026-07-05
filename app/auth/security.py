import bcrypt
import hashlib


def hash_password(password: str) -> str:
    # 1. Pre-hash with SHA-256 to bypass the 72-byte limit
    password_bytes = password.encode("utf-8")
    sha256_hash = hashlib.sha256(password_bytes).hexdigest().encode("utf-8")

    # 2. Hash directly with bcrypt
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(sha256_hash, salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # 1. Pre-hash the plain password with SHA-256
    password_bytes = plain_password.encode("utf-8")
    sha256_hash = hashlib.sha256(password_bytes).hexdigest().encode("utf-8")

    # 2. Verify directly with bcrypt
    return bcrypt.checkpw(sha256_hash, hashed_password.encode("utf-8"))
