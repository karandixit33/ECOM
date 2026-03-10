from fastapi import APIRouter, Depends, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.category import Category
from app.utils.image_upload import save_image

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post("/")
def create_category(
    title: str = Form(...),
    status: bool = Form(True),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    image_path = save_image(image, "categories")

    category = Category(
        title=title,
        image=image_path,
        status=status
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


@router.get("/")
def get_categories(db: Session = Depends(get_db)):

    return db.query(Category).all()


@router.get("/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):

    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.put("/{category_id}")
def update_category(
    category_id: int,
    title: str = Form(...),
    status: bool = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(get_db)
):

    category = db.query(Category).filter(Category.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category.title = title
    category.status = status

    if image:
        category.image = save_image(image, "categories")

    db.commit()
    db.refresh(category)

    return category