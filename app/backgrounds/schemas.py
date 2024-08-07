from pydantic import BaseModel


class SBackgrounds(BaseModel):
    title: str
    image_id: int
