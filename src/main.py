from fastapi import FastAPI
from App.v1.user.user_route import user
from App.v1.product.product_route import product

app = FastAPI()

app.include_router(user)
app.include_router(product)