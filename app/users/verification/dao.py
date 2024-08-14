from app.base.dao import BaseDAO
from app.users.verification.models import Verification


class UsersDAO(BaseDAO):
    model = Verification
