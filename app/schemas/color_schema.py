from pydantic import BaseModel


class ColorCreate(BaseModel):
    name: str