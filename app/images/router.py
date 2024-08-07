import shutil

from fastapi import APIRouter, UploadFile


router = APIRouter(prefix="/images", tags=["images"])


@router.post("/background")
async def add_bg_image(name: str, file: UploadFile):
    im_path = f"app/static/images/{name}.webp"
    with open(im_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
