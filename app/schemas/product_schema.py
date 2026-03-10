from pydantic import BaseModel
from typing import List


class ProductVariantSchema(BaseModel):

    size_id: int

    color_id: int

    price: int


class ProductCreate(BaseModel):

    title: str

    sku: str

    category_id: int

    subcategory_id: int

    description: str

    status: bool

    product_info: List[ProductVariantSchema]


class ProductResponse(BaseModel):

    id: int

    title: str

    sku: str

    category_id: int

    subcategory_id: int

    description: str

    status: bool

    class Config:

        from_attributes = True