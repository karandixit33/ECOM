from sqlalchemy import Column, Integer, String
from app.database import Base


class Size(Base):

    __tablename__ = "sizes"

    id = Column(Integer, primary_key=True)

    name = Column(String)