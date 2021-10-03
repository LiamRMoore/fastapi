from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# -- illustrating dependency injection with class and function
class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return dict(q=q, skip=skip, limit=limit)


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends()):
    """

    commons: CommonQueryParams = Depends()

    == (shortcut for) ==

    commons: CommonQueryParams = Depends(CommonQueryParams)

    to avoid duplication
    """
    response = {}
    if commons.q:
        response.update(q=commons.q)
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update(items=items)
    return response


