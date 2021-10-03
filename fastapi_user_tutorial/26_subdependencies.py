from typing import Optional

from fastapi import Cookie, Depends, FastAPI

app = FastAPI()


def query_extractor(q: Optional[str] = None):
    return q


def query_or_cookie_extractor(
    q: str = Depends(query_extractor),
    last_query: Optional[str] = Cookie(None)
):
    if not q:
        return last_query
    return q


@app.get("/items/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor, use_cache=True)):
    # if multiple dependencies have a common subdependency, FastAPI will cache
    # first call result to avoid duplication. can trigger this off with use_case False
    return dict(q_or_cookie=query_or_default)