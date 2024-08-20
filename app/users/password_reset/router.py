from fastapi import APIRouter
from jose import jwt
from pydantic import EmailStr

from app.exceptions import IncorrectToken, CannotAddDataToDatabase
from app.users.auth import get_password_hash
from app.users.dao import UsersDAO
from app.users.models import Users
from app.users.password_reset.dao import ResetDAO
from app.users.password_reset.dependencies import create_reset_token, decode_token_to_email

router = APIRouter(prefix="/reset_password", tags=["reset_password"])


# @router.post('/send_verification')
# async def send_verification(email_to: EmailStr, user: Users = Depends(get_current_user)):
#     if user.is_verified:
#         raise AlreadyVerified
#     token = create_verification_token({'email': user.email})
#     existing = await VerificationDAO.find_one_or_none(email=user.email)
#     if not existing:
#         await VerificationDAO.add_one(email=user.email, token=token)
#     return token
#     # await send_verification_email(email_to, token)
#
#
# @router.post('/verify')
# async def verify(token: str, user: Users = Depends(get_current_user)):
#     user_dict = await VerificationDAO.find_one_or_none(email=user.email)
#     if token != user_dict.token:
#         raise IncorrectToken
#     else:
#         await VerificationDAO.delete(email=user.email)
#         await UsersDAO.change_to_verified(user.email)


@router.post('/send_reset_password')
async def send_reset_password(email: EmailStr):
    token = create_reset_token({'email': email})
    existing = await ResetDAO.find_one_or_none(email=email)
    if not existing:
        await ResetDAO.add_one(email=email, token=token)
    else:
        raise CannotAddDataToDatabase
    # return await send_reset_password_email(email_to, token)
    return token



@router.post('/reset_password')
async def reset_password(token: str, new_password: str):
    new_hashed_password = get_password_hash(new_password)
    email = decode_token_to_email(token)
    await UsersDAO.reset_password(email, new_hashed_password)
    await ResetDAO.delete(email=email)
    return 'success'
