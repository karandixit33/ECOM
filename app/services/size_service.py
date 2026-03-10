from sqlalchemy.orm import Session
from app.models.size import Size


def get_sizes(db: Session):

    return db.query(Size).all()


def create_size(db: Session, name):

    size = Size(name=name)

    db.add(size)

    db.commit()

    db.refresh(size)

    return size