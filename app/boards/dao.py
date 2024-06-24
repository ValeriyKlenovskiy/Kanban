from app.dao.base import BaseDAO
from app.boards.models import Boards


class BoardsDAO(BaseDAO):
    model = Boards
