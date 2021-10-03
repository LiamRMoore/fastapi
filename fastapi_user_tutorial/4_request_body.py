from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Hello World"}


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update(price_with_tax=price_with_tax)
    return item_dict


@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    """
    simultaneously FastAPI infers:
        - Path param (fstring matched) 
        - request body param (pydantic model) 
        - query param (others)
    """
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update(q=q)
    return result










