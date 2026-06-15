from app.models import Product, ProductCreate

products: list[Product] = []
next_id = 1

def get_all_products():
    return products

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
    return new_product

def sell_product_repo(product_id: int):
    for product in products:
        if product.id == product_id:
            product.sold_out = True
            return product
    return None