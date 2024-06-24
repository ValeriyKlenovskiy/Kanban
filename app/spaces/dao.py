from app.dao.base import BaseDAO
from app.spaces.models import Spaces


class SpacesDAO(BaseDAO):
    model = Spaces
