from sqlalchemy.orm import Session
from app.models.color import Color


def get_colors(db: Session):

    return db.query(Color).all()


def create_color(db: Session, name):

    color = Color(name=name)

    db.add(color)

    db.commit()

    db.refresh(color)

    return color