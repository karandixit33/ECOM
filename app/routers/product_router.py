from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product import Product
from app.utils.image_upload import save_image

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/")
def create_product(
    title: str = Form(...),
    sku: str = Form(...),
    category_id: int = Form(...),
    subcategory_id: int = Form(...),
    description: str = Form(...),
    status: bool = Form(True),

    image1: UploadFile = File(...),
    image2: UploadFile = File(None),
    image3: UploadFile = File(None),
    image4: UploadFile = File(None),

    db: Session = Depends(get_db)
):

    product = Product(
        title=title,
        sku=sku,
        category_id=category_id,
        subcategory_id=subcategory_id,
        description=description,
        image1=save_image(image1, "products"),
        image2=save_image(image2, "products") if image2 else None,
        image3=save_image(image3, "products") if image3 else None,
        image4=save_image(image4, "products") if image4 else None,
        status=status
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


@router.get("/")
def get_products(db: Session = Depends(get_db)):

    return db.query(Product).all()