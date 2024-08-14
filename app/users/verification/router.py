from fastapi import APIRouter, Depends
from pydantic import EmailStr

from app.tasks.tasks import send_verification_email
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.users.verification.dependencies import create_verification_token

router = APIRouter(prefix="/verify", tags=["verification"])


@router.post('/send_verification')
async def send_verification(email_to: EmailStr, user: Users = Depends(get_current_user)):
    print(user.email)
    token = create_verification_token({'email': user.email})
    await send_verification_email(email_to, token)


@router.post('/verify')
async def verify(user: Users = Depends(get_current_user)):
    print(user.email)
    await UsersDAO.change_to_verified(user.email)
