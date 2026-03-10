from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.subcategory import SubCategory
from app.utils.image_upload import save_image

router = APIRouter(prefix="/subcategories", tags=["SubCategories"])


@router.post("/")
def create_subcategory(
    name: str = Form(...),
    category_id: int = Form(...),
    status: bool = Form(True),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    image_path = save_image(image, "subcategories")

    subcategory = SubCategory(
        name=name,
        category_id=category_id,
        image=image_path,
        status=status
    )

    db.add(subcategory)
    db.commit()
    db.refresh(subcategory)

    return subcategory


@router.get("/")
def get_subcategories(db: Session = Depends(get_db)):

    return db.query(SubCategory).all()


@router.put("/{subcategory_id}")
def update_subcategory(
    subcategory_id: int,
    name: str = Form(...),
    category_id: int = Form(...),
    status: bool = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):

    subcategory = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()

    subcategory.name = name
    subcategory.category_id = category_id
    subcategory.status = status

    if image:
        subcategory.image = save_image(image, "subcategories")

    db.commit()

    return subcategory