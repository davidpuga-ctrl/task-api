from pydantic import BaseModel
from typing import Optional 

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    stock: int

class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    stock: int
    sold_out: bool = False

class CustomerCreate(BaseModel):
    name: str
    email: str

class Customer(BaseModel):
    id: int
    name: str
    email: str
    active: bool = True