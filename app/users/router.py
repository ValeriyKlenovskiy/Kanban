import sqlalchemy
from fastapi import APIRouter, HTTPException, status, Response

from app.users.dao import UsersDAO
from app.users.schemas import SUsers, SUsersAuth
from app.users.auth import get_password_hash, authenticate_user, create_access_token

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
async def get_users():
    return await UsersDAO.find_all()


@router.post("")
async def add_user(user_data: SUsers):
    return await UsersDAO.add_one(id=user_data.id, email=user_data.email, hashed_password=user_data.password)


@router.put("/{user_id}")
async def update_user(user_id: int, user_data: SUsers):
    return await UsersDAO.update(model_id=user_id, email=user_data.email, hashed_password=user_data.password)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    await UsersDAO.delete(user_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/register')
async def register_user(user_data: SUsersAuth):
    try:
        existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    except sqlalchemy.exc.MultipleResultsFound:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add_one(email=user_data.email, hashed_password=hashed_password)


@router.post('/login')
async def login_user(response: Response, user_data: SUsersAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("kanban_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("kanban_access_token")
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
