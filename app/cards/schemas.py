from datetime import date

from pydantic import BaseModel


class SCardsUpdate(BaseModel):
    id: int
    title: str
    list_id: int
    description: str
    creator: int
    date_added: date
    labels: list[int]
    ordering: int


class SCards(SCardsUpdate):
    id: int
