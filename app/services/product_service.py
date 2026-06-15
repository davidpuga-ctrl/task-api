from app.data.product_repository import get_all_products, create_product, sell_product_repo

def list_products():
    return get_all_products()

def register_product(data):
    return create_product(data)

def dispatch_product(product_id):
    return sell_product_repo(product_id)