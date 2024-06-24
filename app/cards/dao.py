from app.dao.base import BaseDAO
from app.cards.models import Cards


class CardsDAO(BaseDAO):
    model = Cards
