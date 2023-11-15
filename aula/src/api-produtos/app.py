from fastapi import FastAPI
from models.product import Product

app = FastAPI()



@app.get("/{name}")
def say_hello(name:str):
    if not name:
        pass
    return {"Hello": name}
    
products = [
    Product(id=1, name="Produto 1", description="Descrição do produto 1", price=100.00, category="Categoria 1"),
    Product(id=2, name="Produto 2", description="Descrição do produto 2", price=200.00, category="Categoria 2"),
]

@app.get("/api/products")
def get_products():
    return products

@app.get("/api/products/sale")
def get_products_on_sale():
    '''
    Endpoint que retorna apenas os produtos que estão em promoção
    '''
    return products[0]
