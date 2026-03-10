from fastapi import FastAPI
from app.database import Base, engine

from app.routers import (
    auth_router,
    category_router,
    subcategory_router,
    product_router,
    variant_router,
    size_router,
    color_router,
    upload_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth_router.router)
app.include_router(category_router.router)
app.include_router(subcategory_router.router)
app.include_router(product_router.router)
app.include_router(variant_router.router)
app.include_router(size_router.router)
app.include_router(color_router.router)
app.include_router(upload_router.router)