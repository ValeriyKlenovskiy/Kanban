from app.dao.base import BaseDAO
from app.lists.models import Lists


class ListsDAO(BaseDAO):
    model = Lists
