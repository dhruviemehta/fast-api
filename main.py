from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fakedb = []

class Item(BaseModel):
    item_id: int
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/")
def read_root():
    return {"Hello":"world"}

@app.get("/items")
def get_items():
    return fakedb

@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = item_id - 1
    return fakedb[item]

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return{"item_name": item.name,"item_price": item.price, "item_id": item_id}

@app.post("/items")
def add_item(item: Item):
    fakedb.append(item.dict())
    return fakedb[-1]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    fakedb.pop(item_id-1)
    return {"task":"Successfully Deleted"}