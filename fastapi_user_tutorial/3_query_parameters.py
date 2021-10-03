from typing import Optional

from fastapi import FastAPI


app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/") # default is now /items/?skip=0&limit=10
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
# path, query params respectively. inferred from fstring-style route definition
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update(q=q)
    if not short:
        item.update(description="This has a long description")
    return item


# multiple path and query parameters
# some required, some optional
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, needy: str, q: Optional[str] = None, short: bool = False
):
    item = {"user_id": user_id, "item_id": item_id}
    if q:
        item.update(q=q)
    if not short:
        item.update(description="Long " * 50 + "Cat")
    return item