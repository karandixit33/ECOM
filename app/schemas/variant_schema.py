from pydantic import BaseModel


class VariantCreate(BaseModel):
    product_id: int
    size_id: int
    color_id: int
    price: int