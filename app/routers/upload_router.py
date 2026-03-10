from fastapi import APIRouter, UploadFile
import shutil
import os

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "uploads"


@router.post("/category-image")
def upload_category_image(file: UploadFile):

    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"url": path}


@router.post("/product-images")
def upload_product_images(file: UploadFile):

    path = os.path.join(UPLOAD_DIR, file.filename)

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"url": path}