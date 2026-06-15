from fastapi import APIRouter, HTTPException
from app.models import ProductCreate
from app.services.product_service import list_products, register_product, dispatch_product
from app.utils.validators import validate_exists

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("")
def get_products():
    return list_products()

@router.post("")
def create_product_endpoint(data: ProductCreate):
    product = register_product(data)
    return {
        "message": "Producto agregado correctamente",
        "product": product
    }

@router.put("/{product_id}/sell")
def sell_product_endpoint(product_id: int):
    product = dispatch_product(product_id)
    # Aquí aplicamos la función reutilizable
    return validate_exists(product, "Producto no encontrado")