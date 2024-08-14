from fastapi import APIRouter, HTTPException, status, Depends

from app.spaces.dao import SpacesDAO
from app.spaces.schemas import SSpaces
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exceptions import NotAllowed

router = APIRouter(prefix="/spaces", tags=["spaces"])


@router.get("/my_spaces")
async def get_my_spaces(user: Users = Depends(get_current_user)):
    return await SpacesDAO.find_filtered(owner_id=user.id)


@router.post("")
async def add_space(space_data: SSpaces, user: Users = Depends(get_current_user)):
    return await SpacesDAO.add_one(title=space_data.title,
                                   owner_id=user.id, allowed_users=[user.id],
                                   ordering=[])


@router.put("/{space_id}")
async def rename_my_space(space_id: int, new_name: str, current_user: Users = Depends(get_current_user)):
    return await SpacesDAO.rename(space_id, new_name, current_user.id)


@router.delete("/{space_id}")
async def delete_space(space_id: int):
    await SpacesDAO.delete(id=space_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)


@router.get('/get_allowed')
async def get_allowed(space_id: int, current_user: Users = Depends(get_current_user)):
    return await SpacesDAO.get_allowed_users(space_id, current_user)


@router.patch('/add_allowed')
async def add_allowed(space_id: int, user: int, current_user: Users = Depends(get_current_user)):
    return await SpacesDAO.add_allowed_user(space_id, user, current_user)


@router.patch('/delete_allowed')
async def delete_allowed(space_id: int, user: int, current_user: Users = Depends(get_current_user)):
    if user == current_user.id:
        raise NotAllowed
    return await SpacesDAO.delete_allowed_user(space_id, user, current_user)


@router.patch('/edit_ordering')
async def edit_ordering(space_id: int, ordering: list[int]):
    return await SpacesDAO.change_ordering(space_id, ordering)

