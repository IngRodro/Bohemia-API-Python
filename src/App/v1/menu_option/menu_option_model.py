from pydantic import BaseModel
from typing import Optional
from App.v1.product.product_model import Product_Quantity

class MenuOption(BaseModel):
    id: Optional[str]
    name: str
    restaurant: str
    products: list[Product_Quantity]