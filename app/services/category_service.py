from sqlalchemy.orm import Session
from app.models.category import Category


def get_all_categories(db: Session):

    return db.query(Category).all()


def create_category(db: Session, title: str):

    category = Category(title=title)

    db.add(category)

    db.commit()

    db.refresh(category)

    return category


def delete_category(db: Session, category_id: int):

    category = db.query(Category).filter(
        Category.id == category_id
    ).first()

    if category:

        db.delete(category)

        db.commit()

    return category