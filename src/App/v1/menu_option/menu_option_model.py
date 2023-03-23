from pydantic import BaseModel
from typing import Optional

class MenuOption(BaseModel):
    id: Optional[str]
    name: str
    restaurant: str
    products: list