from datetime import datetime, timedelta

from fastapi import Depends, Request
from jose import JWTError, jwt, ExpiredSignatureError

from app.config import settings

from app.users.dao import UsersDAO
from app.exceptions import TokenAbsent, TokenExpired, IncorrectTokenFormat, UserAbsent, NotAllowed
from app.users.models import Users


def get_token(request: Request):
    headers = request.headers
    if headers.get("origin") == "http://localhost:3000":
        token = headers.get("authorization")
    else:
        token = request.cookies.get("kanban_access_token")
    if not token:
        raise TokenAbsent
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except ExpiredSignatureError:
        raise TokenExpired
    except JWTError:
        raise IncorrectTokenFormat
    user_id: str = payload.get("sub")
    if not user_id:
        raise UserAbsent
    user = await UsersDAO.find_one_or_none(id=int(user_id))
    if not user:
        raise UserAbsent

    return user


async def get_current_superuser(user: Users = Depends(get_current_user)):
    if not user.is_superuser:
        raise NotAllowed
    return user


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt


def create_verification_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=10)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_VERIFICATION_KEY, settings.ALGORITHM)
    return encoded_jwt
