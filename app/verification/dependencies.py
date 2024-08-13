from datetime import datetime, timedelta
from jose import jwt

from app.config import settings


def create_verification_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=10)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_VERIFICATION_KEY, settings.ALGORITHM)
    return encoded_jwt
