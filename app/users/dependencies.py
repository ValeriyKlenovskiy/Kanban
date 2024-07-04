from datetime import datetime

from fastapi import Depends, Request, HTTPException, status
from jose import JWTError, jwt

from app.config import settings

from app.users.dao import UsersDAO


def get_token(request: Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < int(datetime.utcnow().timestamp())):
        raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT)
    user_id: str = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    user = await UsersDAO.find_by_id(int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    return user


# async def get_current_admin_user(user: Users = Depends(get_current_user)):
#     if user.role != 'admin':
#         raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT)
#     return user
