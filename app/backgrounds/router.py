import sqlalchemy
from fastapi import APIRouter, HTTPException, status

from app.boards.dao import BoardsDAO
from app.boards.schemas import SBoards
from app.exceptions import NoSpace

router = APIRouter(prefix="/boards", tags=["boards"])


@router.get("")
async def get_boards():
    return await BoardsDAO.find_all()


@router.post("")
async def add_board(board_data: SBoards):
    try:
        return await BoardsDAO.add_one(title=board_data.title, space_id=board_data.space_id,
                                   ordering=[0])
    except sqlalchemy.exc.IntegrityError:
        raise NoSpace


@router.put("/{board_id}")
async def update_board(board_id: int, board_data: SBoards):
    return await BoardsDAO.update(model_id=board_id, title=board_data.title, space_id=board_data.space_id,
                                  ordering=board_data.ordering)


@router.delete("/{board_id}")
async def delete_board(board_id: int):
    await BoardsDAO.delete(board_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
