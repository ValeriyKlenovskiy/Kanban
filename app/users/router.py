from fastapi import APIRouter, HTTPException, status

from app.users.dao import UsersDAO
from app.users.schemas import SUsers, SUsersUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
async def get_users():
    return await UsersDAO.find_all()


@router.post("")
async def add_user(user_data: SUsers):
    return await UsersDAO.add_one(id=user_data.id, email=user_data.email, hashed_password=user_data.password)


@router.put("/{user_id}")
async def update_user(user_id: int, user_data: SUsersUpdate):
    return await UsersDAO.update(model_id=user_id, email=user_data.email, hashed_password=user_data.password)


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    await UsersDAO.delete(user_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
