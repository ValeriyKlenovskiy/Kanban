from app.base.dao import BaseDAO
from app.verification.models import Verification


class UsersDAO(BaseDAO):
    model = Verification
