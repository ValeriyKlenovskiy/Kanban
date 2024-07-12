from fastapi import Depends, Request
from jose import JWTError, jwt, ExpiredSignatureError

from app.config import settings

from app.users.dao import UsersDAO
from app.exceptions import TokenAbsent, TokenExpired, \
    IncorrectTokenFormat, UserAbsent


def get_token(request: Request):
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

# async def get_current_admin_user(user: Users = Depends(get_current_user)):
#     if user.role != 'admin':
#         raise HTTPException(status_code=status.HTTP_408_REQUEST_TIMEOUT)
#     return user
