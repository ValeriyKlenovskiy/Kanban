from app.base.dao import BaseDAO
from app.boards.models import Boards


class BoardsDAO(BaseDAO):
    model = Boards
