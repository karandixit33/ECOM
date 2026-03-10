from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.variant_service import (
    add_variant,
    update_variant,
    delete_variant
)

router = APIRouter(prefix="/variants", tags=["Variants"])


@router.post("/products/{product_id}")
def create_variant(
    product_id: int,
    size_id: int,
    color_id: int,
    price: int,
    db: Session = Depends(get_db)
):
    return add_variant(db, product_id, size_id, color_id, price)


@router.put("/{variant_id}")
def edit_variant(
    variant_id: int,
    price: int,
    db: Session = Depends(get_db)
):
    return update_variant(db, variant_id, price)


@router.delete("/{variant_id}")
def remove_variant(
    variant_id: int,
    db: Session = Depends(get_db)
):
    return delete_variant(db, variant_id)