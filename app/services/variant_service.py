from sqlalchemy.orm import Session
from app.models.product_variant import ProductVariant


def add_variant(db: Session, product_id, size_id, color_id, price):

    variant = ProductVariant(
        product_id=product_id,
        size_id=size_id,
        color_id=color_id,
        price=price
    )

    db.add(variant)
    db.commit()
    db.refresh(variant)

    return variant


def update_variant(db: Session, variant_id, price):

    variant = db.query(ProductVariant).filter(
        ProductVariant.id == variant_id
    ).first()

    if not variant:
        return {"error": "Variant not found"}

    variant.price = price

    db.commit()

    return variant


def delete_variant(db: Session, variant_id):

    variant = db.query(ProductVariant).filter(
        ProductVariant.id == variant_id
    ).first()

    if not variant:
        return {"error": "Variant not found"}

    db.delete(variant)

    db.commit()

    return {"message": "Variant deleted"}