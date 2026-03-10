from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Category(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    image = Column(String)

    status = Column(Boolean, default=True)