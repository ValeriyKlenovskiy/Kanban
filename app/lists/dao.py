from app.base.dao import BaseDAO
from app.lists.models import Lists


class ListsDAO(BaseDAO):
    model = Lists
