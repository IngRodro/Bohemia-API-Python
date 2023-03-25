from fastapi import FastAPI
from dotenv import load_dotenv
from App.v1.user.user_route import user
from App.v1.product.product_route import product
from App.v1.menu_option.menu_option_route import menu_option

load_dotenv()
app = FastAPI()

app.include_router(user)
app.include_router(product)
app.include_router(menu_option)