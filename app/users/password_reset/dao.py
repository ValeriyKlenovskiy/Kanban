from app.base.dao import BaseDAO
from app.users.password_reset.models import Reset


class ResetDAO(BaseDAO):
    model = Reset
