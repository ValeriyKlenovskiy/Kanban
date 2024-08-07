from app.base.dao import BaseDAO
from app.backgrounds.models import Backgrounds


class BackgroundsDAO(BaseDAO):
    model = Backgrounds
