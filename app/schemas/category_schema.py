from pydantic import BaseModel


class CategoryCreate(BaseModel):

    title: str

    status: bool = True


class CategoryResponse(BaseModel):

    id: int

    title: str

    image: str | None

    status: bool

    class Config:

        from_attributes = True