from typing import List, Optional

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []


class ItemNotFound(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(ItemNotFound)
async def not_found_handler(request: Request, exc: ItemNotFound):
    return JSONResponse(
        status_code=404,
        content=dict(message=f"oops: {exc.name} not found")
    )

items = {
    "foo":{"name": "Foo", "price": 50.2},
    "bar":{"name": "Bar", "description": "The batenders", "price": 62, "tax": 20.2},
    "baz":{"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags" :[]}
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    if item_id not in items:
        raise ItemNotFound(item_id)
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    try:
        stored_item_data = items[item_id]
    except KeyError:
        raise ItemNotFound(item_id)
    stored_item_model = Item(**stored_item_data)
    # generates dict with only data that was 
    # set when creating item, excluding defaults!
    update_data = item.dict(exclude_unset=True)
    # update only those that changed
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item