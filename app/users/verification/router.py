from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.exceptions import AlreadyVerified, IncorrectToken
from app.tasks.tasks import send_verification_email
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.verification.dao import VerificationDAO
from app.users.verification.dependencies import create_verification_token

router = APIRouter(prefix="/verify", tags=["verification"])


@router.post('/send_verification')
async def send_verification(email_to: EmailStr, user: Users = Depends(get_current_user)):
    if user.is_verified:
        raise AlreadyVerified
    token = create_verification_token({'email': user.email})
    existing = await VerificationDAO.find_one_or_none(email=user.email)
    if not existing:
        await VerificationDAO.add_one(email=user.email, token=token)
    return token
    # await send_verification_email(email_to, token)


@router.post('/verify')
async def verify(token: str, user: Users = Depends(get_current_user)):
    user_dict = await VerificationDAO.find_one_or_none(email=user.email)
    if token != user_dict.token:
        raise IncorrectToken
    else:
        await VerificationDAO.delete(email=user.email)
        await UsersDAO.change_to_verified(user.email)
