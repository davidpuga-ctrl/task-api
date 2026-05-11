from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional 

app = FastAPI(
    title="API Tecnologia",
    description="Mini API para gestionar el inventario",
    version="1.0.0"
)

# Modelo para crear un producto
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    stock: int

# Modelo que representa el producto en el sistema
class Product(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    stock: int
    sold_out: bool = False

# Lista temporal en memoria
products: list[Product] = []
next_id = 1

# Endpoints
@app.get("/")
def home():
    return {
        "message": "Bienvenido al sistema de Inventario",
        "docs": "/docs"
    }

@app.get("/products")
def list_products():
    return products

@app.post("/products")
def create_product(product_data: ProductCreate):
    global next_id
    new_product = Product(
        id=next_id,
        name=product_data.name,
        description=product_data.description,
        stock=product_data.stock,
        sold_out=False
    )
    products.append(new_product)
    next_id += 1
    return {
        "message": "Producto agregado correctamente",
        "product": new_product
    }

@app.put("/products/{product_id}/sell")
def sell_product(product_id: int):
    for product in products:
        if product.id == product_id:
            product.sold_out = True
            return {
                "message": "Producto marcado como agotado/vendido",
                "product": product
            }
    raise HTTPException(status_code=404, detail="Producto no encontrado")