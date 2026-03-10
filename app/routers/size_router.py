from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.size_service import get_sizes, create_size

router = APIRouter(prefix="/sizes", tags=["Sizes"])


@router.get("/")
def list_sizes(db: Session = Depends(get_db)):
    return get_sizes(db)


@router.post("/")
def add_size(name: str, db: Session = Depends(get_db)):
    return create_size(db, name)