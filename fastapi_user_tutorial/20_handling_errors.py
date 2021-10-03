from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

app = FastAPI()

@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content=dict(message=f"Oops! {exc.name} did something. Rainbowz.")
    )


items = {"foo": "The Foo Wrestlers"}


@app.get("/unicorns/{name}")
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return dict(unicorn_name = name)

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="item not found",
            headers={"X-Error": "There goes my error"}
        )
    return dict(item=items[item_id])