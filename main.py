from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/blog")
def index(
    limit: int = 10,
    published: bool = True,
    sort: Optional[str] = None
):
    # only get 10 published blogs
    return {"data":f"{limit} {'published ' if published else ''}blogs from the db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


@app.get("/blog/{id_}")
def show(id_: int):
    # fetch blog with id_ = id_
    return {"data":id_}


@app.get("/blog/{id_}/comments")
def comments(id_: int, limit: int = 10):
    """retch comments of blog with id"""
    return {"data": [f"comment 1 for {id_}"]}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post("/blog")
def create_blog(request: Blog):
    #return request
    return {"data": f"Blog created with title {request.title}"}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app=app, host="127.0.0.1", port=9000)
