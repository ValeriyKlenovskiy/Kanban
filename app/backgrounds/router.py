import shutil

from fastapi import APIRouter, HTTPException, status, UploadFile

from app.backgrounds.dao import BackgroundsDAO
from app.tasks.tasks import process_pic

router = APIRouter(prefix="/backgrounds", tags=["backgrounds"])


@router.get("")
async def get_backgrounds():
    return await BackgroundsDAO.find_all()


@router.get("/{bg_id}")
async def get_background_by_id(bg_id: int):
    return await BackgroundsDAO.find_by_id(bg_id)


@router.post("")
async def add_background(title: str, file: UploadFile):
    im_path = f"app/static/images/{title}.webp"
    with open(im_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(im_path)
    return await BackgroundsDAO.add_one(
        title=title,
        image_path=im_path,
    )


@router.delete("/{background_id}")
async def delete_background(background_id: int):
    await BackgroundsDAO.delete(background_id)
    return HTTPException(status_code=status.HTTP_204_NO_CONTENT)
