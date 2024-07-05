from pydantic import BaseModel


class SSpaces(BaseModel):
    title: str
    owner_id: int
    allowed_users: list[int]
    ordering: list[int]

