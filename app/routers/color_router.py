from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.color_service import get_colors, create_color

router = APIRouter(
    prefix="/colors",
    tags=["Colors"]
)


@router.get("/")
def list_colors(db: Session = Depends(get_db)):
    return get_colors(db)


@router.post("/")
def add_color(name: str, db: Session = Depends(get_db)):
    return create_color(db, name)