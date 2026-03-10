from sqlalchemy.orm import Session
from app.models.subcategory import SubCategory


def get_subcategories(db: Session):

    return db.query(SubCategory).all()


def create_subcategory(db: Session, category_id: int, name: str):

    sub = SubCategory(
        category_id=category_id,
        name=name
    )

    db.add(sub)

    db.commit()

    db.refresh(sub)

    return sub