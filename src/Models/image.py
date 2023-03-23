from pydantic import BaseModel

class Image(BaseModel):
    public_id: str
    secure_url: str