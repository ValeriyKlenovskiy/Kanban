from pydantic import BaseModel


class SBoards(BaseModel):
    title: str
    space_id: int
