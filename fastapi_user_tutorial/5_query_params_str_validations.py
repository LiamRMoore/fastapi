from typing import Optional, List

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Optional[List[str]] = Query(
        ["foo", "bar"],
        title="q strings",
        description="naw"
    ),
    funword: Optional[str] = Query(
        "bazinga",
        max_length=50,
        min_length=3,
        regex="\w+"
    ),
    id_: str = Query(
        ...,
        min_length=3,
        regex="^\d+$",
        alias="item-query",
        deprecated=True
    )
):
    """
    Additional validation!

    request param q has multiple values! (/items/?q=ding&q=dong)

    First arg to query is default
    For optionals, use None. For required, use "...".
    To allow an http request param to be an alias for an invalid python name (e.g. hyphen),
    use Query alias parameter
    """
    results = {"q": q}
    if funword:
        results.update(funword=funword)
    if id_:
        results.update(id=id_)
    return results