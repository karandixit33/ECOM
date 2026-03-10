from sqlalchemy import Column, Integer, String
from app.database import Base


class Color(Base):

    __tablename__ = "colors"

    id = Column(Integer, primary_key=True)

    name = Column(String)