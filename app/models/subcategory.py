from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base


class SubCategory(Base):

    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, index=True)

    category_id = Column(Integer, ForeignKey("categories.id"))

    name = Column(String)

    image = Column(String)

    status = Column(Boolean, default=True)