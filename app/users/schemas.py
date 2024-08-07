from pydantic import BaseModel, EmailStr


class SUsers(BaseModel):
    email: EmailStr
    password: str


class SUsersGet(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    is_superuser: bool
    is_verified: bool
