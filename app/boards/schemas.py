from pydantic import BaseModel


class SBoardsUpdate(BaseModel):
    id: int
    title: str
    space_id: int
    ordering: list[int]


class SBoards(SBoardsUpdate):
    id: int
