from fastapi import APIRouter, HTTPException, status

from app.lists.dao import ListsDAO
from app.lists.schemas import SLists, SListsUpdate

router = APIRouter(prefix="/lists", tags=["lists"])


@router.get("")
async def get_lists():
    return await ListsDAO.find_all()


@router.post("")
async def add_list(list_data: SLists):
    return await ListsDAO.add_one(id=list_data.id, title=list_data.title, board_id=list_data.board_id,
                                  description=list_data.description, creator=list_data.creator,
                                  date_added=list_data.date_added, ordering=list_data.ordering)


@router.put("/{list_id}")
async def update_list(list_id: int, list_data: SListsUpdate):
    return await ListsDAO.update(model_id=list_id, title=list_data.title, board_id=list_data.board_id,
                                 description=list_data.description, creator=list_data.creator,
                                 date_added=list_data.date_added, ordering=list_data.ordering)


@router.delete("/{list_id}")
async def delete_list(list_id: int):
    await ListsDAO.delete(list_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)


@router.patch('/edit_ordering')
async def edit_ordering(list_id: int, ordering: list[int]):
    return await ListsDAO.change_ordering(list_id, ordering)
