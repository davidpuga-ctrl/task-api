from fastapi import FastAPI
from app.config import get_setting
from app.routes.product_routes import router as product_router
from app.routes.customer_routes import router as customer_router

app = FastAPI(
    title=get_setting("APP_NAME", "API Modular"),
    description="API preparada con configuración externa y prácticas básicas de calidad",
    version=get_setting("APP_VERSION", "1.0.0")
)

app.include_router(product_router)
app.include_router(customer_router)

@app.get("/")
def home():
    return {
        "message": "API de Inventario Lista",
        "docs": "/docs"
    }

@app.get("/system/info")
def system_info():
    return {
        "application": get_setting("APP_NAME", "API Modular"),
        "version": get_setting("APP_VERSION", "1.0.0"),
        "environment": get_setting("ENVIRONMENT", "DEV"),
        "author": get_setting("AUTHOR", "No definido")
    }