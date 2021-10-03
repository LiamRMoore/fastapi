from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def root(
    p: str,
    item_id: int = Path(
        ...,
        title="The ID of the item to get",
        ge=1, # constraint greater than or equal to 1
        lt=10 # less than 10
    ),
    size: Optional[float] = Query(None, gt=0., lt=33.),
    q: Optional[int] = Query(None, alias="item-query")
):
    """
    A path parameter is always required, hence is declared with ...
    """
    results = dict(item_id=item_id)
    if q:
        results.update(q=q)
    if size:
        results.update(size=size)
    return results