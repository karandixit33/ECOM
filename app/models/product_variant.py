from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base


class ProductVariant(Base):

    __tablename__ = "product_variants"

    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey("products.id"))

    size_id = Column(Integer)

    color_id = Column(Integer)

    price = Column(Integer)