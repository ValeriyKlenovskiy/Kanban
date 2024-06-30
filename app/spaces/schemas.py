from pydantic import BaseModel


class SSpacesUpdate(BaseModel):
    title: str
    owner_id: int
    allowed_users: list[int]
    ordering: list[int]


class SSpaces(SSpacesUpdate):
    id: int
