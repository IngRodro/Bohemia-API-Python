from pydantic import BaseModel
from typing import Optional
from App.v1.user.user_model import User
from Models.image import Image

class Product(BaseModel):
    id: Optional[str]
    name: str
    status: Optional[str]
    image: Image
    user: User


class Product_Quantity(BaseModel):
    product: Product
    quantity: int