from fastapi import APIRouter, HTTPException, status

from app.backgrounds.dao import BackgroundsDAO
from app.backgrounds.schemas import SBackgrounds

router = APIRouter(prefix="/backgrounds", tags=["backgrounds"])


@router.get("")
async def get_backgrounds():
    return await BackgroundsDAO.find_all()


@router.get("/{bg_id}")
async def get_backgrounds_by_id(bg_id: int):
    return await BackgroundsDAO.find_by_id(bg_id)


@router.post("")
async def add_backgrounds(background_data: SBackgrounds):
    return await BackgroundsDAO.add_one(
        title=background_data.title,
        image_id=background_data.image_id,
    )


@router.delete("/{background_id}")
async def delete_background(background_id: int):
    await BackgroundsDAO.delete(background_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
