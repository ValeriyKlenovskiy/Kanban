from fastapi import APIRouter, HTTPException, status, Depends

from app.spaces.dao import SpacesDAO
from app.spaces.schemas import SSpaces
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/spaces", tags=["spaces"])


@router.get("")
async def get_spaces():
    return await SpacesDAO.find_all()


@router.post("")
async def add_space(space_data: SSpaces, user: Users = Depends(get_current_user)):
    return await SpacesDAO.add_one(title=space_data.title,
                                   owner_id=user.id, allowed_users=[user.id],
                                   ordering=space_data.ordering)


@router.put("/{space_id}")
async def update_space(space_id: int, space_data: SSpaces):
    return await SpacesDAO.update(model_id=space_id, title=space_data.title,
                                  allowed_users=space_data.allowed_users,
                                  ordering=space_data.ordering)


@router.delete("/{space_id}")
async def delete_space(space_id: int):
    await SpacesDAO.delete(space_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)


@router.patch('/edit_allowed')
async def edit_allowed(space_id: int, allowed_users: list[int]):
    return await SpacesDAO.edit_allowed_users(space_id, allowed_users)


@router.patch('/edit_ordering')
async def edit_ordering(space_id: int, ordering: list[int]):
    return await SpacesDAO.change_ordering(space_id, ordering)

