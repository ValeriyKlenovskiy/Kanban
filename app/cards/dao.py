from app.base.dao import BaseDAO
from app.cards.models import Cards


class CardsDAO(BaseDAO):
    model = Cards
