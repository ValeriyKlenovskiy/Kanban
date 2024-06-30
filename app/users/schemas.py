from pydantic import BaseModel, EmailStr


class SUsersUpdate(BaseModel):
    email: EmailStr
    password: str


class SUsers(SUsersUpdate):
    id: int
