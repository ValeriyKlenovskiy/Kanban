from fastapi import APIRouter, HTTPException, status

from app.cards.dao import CardsDAO
from app.cards.schemas import SCards

router = APIRouter(prefix="/cards", tags=["cards"])


@router.get("")
async def get_cards():
    return await CardsDAO.find_all()


@router.post("")
async def add_card(card_data: SCards):
    return await CardsDAO.add_one(title=card_data.title, list_id=card_data.list_id,
                                  description=card_data.description, creator=card_data.creator,
                                  date_added=card_data.date_added, labels=card_data.labels)


@router.put("/{card_id}")
async def update_card(card_id: int, card_data: SCards):
    return await CardsDAO.update(model_id=card_id, title=card_data.title, list_id=card_data.list_id,
                                 description=card_data.description, creator=card_data.creator,
                                 date_added=card_data.date_added, labels=card_data.labels)


@router.delete("/{card_id}")
async def delete_card(card_id: int):
    await CardsDAO.delete(card_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
