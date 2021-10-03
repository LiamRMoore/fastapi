
from enum import Enum

from fastapi import FastAPI


# use enumeration to pre-specify a fixed number of endpoints
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet: # enum member
        return {"model_name": model_name, "message": "DL ftw"}
    if model_name.value == "lenet": # string value of enum member
        return {"model_name": model_name, "message": "LeCNN"}
    # return will return (str) VALUE of enum
    return {"model_name": model_name, "message": "resnet"} 


@app.get("/files/{file_path:path}") # special starlette syntax, will interpet as path
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}