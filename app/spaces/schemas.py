from pydantic import BaseModel


class SSpaces(BaseModel):
    title: str
    ordering: list[int]

