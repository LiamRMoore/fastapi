from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    tax: Optional[float] = None

    # another way
    naam: str = Field(..., example="Foe")
    beschrijving: Optional[str] = Field(None, example="Supertof")
    prijs: float = Field(..., example=35.4)
    belasting: Optional[float] = Field(None, example=3.2)

    # one way to override preview string in openAPI
    # class Config:
    #     schema_extra = {
    #         "example" : {
    #             "name" : "Foo",
    #             "description" : "A very nice item.",
    #             "price" : 35.4,
    #             "tax": 3.2
    #         }
    #     }


@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Item = Body(..., example=dict(name="name", description="descriptionz", price=13.1415629, naam="wha"))
):
    """
    can give examples with any path, query, header, Body, cookie, form or file 

    examples with an "s" accepts a dict of dicts like:
    {key: example} e.g. {"normal": {...}, "wrong": {...}}
    """
    results = dict(item_id=item_id, item=item)
    return results


@app.get("/")
async def root():
    return {"message" : "Hello World"}