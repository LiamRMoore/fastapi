from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return {"data":"blog list"}


@app.get("/blog/{id_}")
def show(id_: int):
    # fetch blog with id_ = id_
    return {"data":id_}


@app.get("/blog/{id_}/comments")
def comments(id_: int):
    """retch comments of blog with id"""
    return {"data": [f"comment 1 for {id_}"]}