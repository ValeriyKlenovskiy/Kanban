import sqlalchemy
from fastapi import APIRouter, HTTPException, status, Depends

from app.cards.dao import CardsDAO
from app.cards.schemas import SCards
from app.users.dependencies import get_current_user
from app.users.models import Users
from app.exceptions import NoList

router = APIRouter(prefix="/cards", tags=["cards"])


@router.get("")
async def get_cards():
    return await CardsDAO.find_all()


@router.post("")
async def add_card(card_data: SCards, user: Users = Depends(get_current_user)):
    try:
        return await CardsDAO.add_one(
            title=card_data.title,
            list_id=card_data.list_id,
            description=card_data.description,
            creator=user.id,
            date_added=card_data.date_added,
            labels=card_data.labels,
            deadline=card_data.deadline,
        )
    except sqlalchemy.exc.IntegrityError:
        raise NoList


@router.put("/{card_id}")
async def update_card(card_id: int, card_data: SCards):
    return await CardsDAO.update(
        model_id=card_id,
        title=card_data.title,
        list_id=card_data.list_id,
        description=card_data.description,
        date_added=card_data.date_added,
        labels=card_data.labels,
        deadline=card_data.deadline,
    )


@router.delete("/{card_id}")
async def delete_card(card_id: int):
    await CardsDAO.delete(id=card_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
