from typing import Optional

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel, Field


app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(
        None,
        title="The description of the item",
        max_length=300
    )
    price: float = Field(..., ge=0, description="price >= £0")
    tax: Optional[float] = Field(..., ge=0, description ="tax maybe")


@app.put("/items/{item_id}")
async def root(
    item_id: int = Path(..., title="the item id"),
    item: Item = Body(..., embed=True)
):
    results = dict(item_id=item_id, item=item)
    return results