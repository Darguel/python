from typing import Union
from fastapi import FastAPI

from model import Product
from db import clientPS
from db import productDB

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/product/")
def getproduct():
    return productDB.consulta()

@app.get("/product/{id}")
def consultaById(id):
    return productDB.consultaById(id)

@app.post("/product/")
def createProduct(prod: Product.Product):
    return productDB.insertProduct(prod.id,prod.name,prod.description,prod.company,prod.price,prod.unit,prod.subcategory_id)
    
@app.get("/product/{id}")
def consultaById(id):
    return productDB.consultaById(id)


# @app.get("/product/{id}")
# def getproductById(id:int):
#     productDB.consulta(id)
#     return {"masseage": f"consulta producte: {id}"}
