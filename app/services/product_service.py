from sqlalchemy.orm import Session
from app.models.product import Product
from app.models.product_variant import ProductVariant


def create_product(db: Session, data):

    product = Product(
        title=data.title,
        sku=data.sku,
        category_id=data.category_id,
        subcategory_id=data.subcategory_id,
        description=data.description,
        status=data.status
    )

    db.add(product)

    db.commit()

    db.refresh(product)

    for item in data.product_info:

        variant = ProductVariant(
            product_id=product.id,
            size_id=item.size_id,
            color_id=item.color_id,
            price=item.price
        )

        db.add(variant)

    db.commit()

    return product