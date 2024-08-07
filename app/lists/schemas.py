from datetime import date

from pydantic import BaseModel


class SLists(BaseModel):
    title: str
    board_id: int
    description: str
    date_added: date
