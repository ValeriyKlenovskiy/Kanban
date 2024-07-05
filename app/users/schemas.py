from pydantic import BaseModel, EmailStr


class SUsersUpdate(BaseModel):
    email: EmailStr
    password: str


class SUsersAuth(SUsersUpdate):
    pass


class SUsers(SUsersUpdate):
    id: int
