from typing import Optional

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.put("/items/{item_nummerwang}")
async def update_item_redux(
    item_nummerwang: int,
    item: Item = Body(..., embed=True)
):
   """
   Explicitly providing a Body on RHS of pydantic model and passing embed will
   case the json parser to interpret item as {"item":item}, i.e. first level entry 
   in a parent json
   """
   return {"item_nummerwang": item_nummerwang, "item": item}


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The id of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item],
    user: User,
    importance: Optional[int] = Body(None, gt=0), # a generic additional json body key
    pie: str = Body(...)
):
    """
    fastapi will notice two body params (from basemodel subclasses) and will expect
    a nested json with two entries, {"item": {...}, "user": {...}}

    body elements without a pydantic model template: Body, have same kwargs
    as Query and Path

    it will separate these into the appropriate arguments automatically
    """
    results = dict(item_id=item_id)
    if q:
        results.update(q=q)
    if item:
        results.update(item=item)
    if user:
        results.update(user=user)
    if importance:
        results.update(importance=importance)
    if pie:
        results.update(pie=pie.upper())
    return results