from pydantic import BaseModel

class Product(BaseModel):

    id:int
    name: str
    description: str
    price: float
    category: str

    class Config:
        orm_mode = True