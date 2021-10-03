from typing import Optional, Set, List, Dict

from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    """
    For nesting
    """
    url: HttpUrl # exotic type for checking valid urls
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = set()
    image: Optional[List[Image]] = None # nested


class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    print(list(weights.keys())[0] * 5)
    return weights

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = dict(item_id=item_id, item=item)
    return results


@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.get("/")
async def root():
    return {"message" : "Hello World"}