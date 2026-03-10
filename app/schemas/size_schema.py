from pydantic import BaseModel


class SizeCreate(BaseModel):
    name: str