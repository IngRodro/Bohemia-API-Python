from fastapi import APIRouter, Request
from Server.db import conn
from Utils.auth import validate_token

base = '/products'

product = APIRouter()

@product.get(base + '/')
async def get_all_product(request: Request, page: int , size: int):
    token = request.headers["Authorization"]
    id_user = validate_token(token)["token"]
    return id_user