from datetime import date

from pydantic import BaseModel


class SListsUpdate(BaseModel):
    title: str
    board_id: int
    description: str
    creator: int
    date_added: date
    ordering: list[int]


class SLists(SListsUpdate):
    id: int
