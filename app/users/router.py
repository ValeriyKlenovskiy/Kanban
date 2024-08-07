from http import cookies
from fastapi import APIRouter, HTTPException, status, Response

from app.users.dao import UsersDAO
from app.users.schemas import SUsersAuth
from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.exceptions import UserAlreadyExists, CannotAddDataToDatabase

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
async def get_users():
    return await UsersDAO.find_all()


@router.post('/register')
async def register_user(user_data: SUsersAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExists
    hashed_password = get_password_hash(user_data.password)
    new_user = await UsersDAO.add_one(email=user_data.email, hashed_password=hashed_password)
    if not new_user:
        raise CannotAddDataToDatabase


@router.post('/login')
async def login_user(response: Response, user_data: SUsersAuth):
    response.delete_cookie("kanban_access_token")
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("kanban_access_token", access_token)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("kanban_access_token")
    return 'logout'
