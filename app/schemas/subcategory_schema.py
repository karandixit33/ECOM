from pydantic import BaseModel


class SubCategoryCreate(BaseModel):

    category_id: int

    name: str

    status: bool = True


class SubCategoryResponse(BaseModel):

    id: int

    category_id: int

    name: str

    image: str | None

    status: bool

    class Config:

        from_attributes = True