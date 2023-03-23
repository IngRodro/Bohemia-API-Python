from pydantic import BaseModel
from typing import Optional
from Models.image import Image
from App.v1.user.user_model import User

class Restaurant(BaseModel):
    id: Optional[str]
    name: str
    department: str
    municipality: str
    direction: str
    delivery: bool
    phone: str
    opening_hour: str
    closing_hour: str
    image: Image
    user: User