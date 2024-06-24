from pydantic import BaseModel


class SBoardsUpdate(BaseModel):
    id: int
    title: str
    space_id: int


class SBoards(SBoardsUpdate):
    id: int
