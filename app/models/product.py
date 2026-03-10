from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    sku = Column(String)

    category_id = Column(Integer, ForeignKey("categories.id"))

    subcategory_id = Column(Integer, ForeignKey("subcategories.id"))

    description = Column(String)

    image1 = Column(String)

    image2 = Column(String)

    image3 = Column(String)

    image4 = Column(String)

    status = Column(Boolean, default=True)