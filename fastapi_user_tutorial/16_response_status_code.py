from fastapi import FastAPI, status

app = FastAPI()


# can also receive an IntEnum, such as http.HTTPStatus
@app.post("/items/", status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {"name": name}