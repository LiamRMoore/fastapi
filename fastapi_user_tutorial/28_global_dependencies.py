from fastapi import Depends, FastAPI, Header, HTTPException


async def verify_token(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-token header invalid")


async def verify_key(x_key: str = Header(...)):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-key header invalid")
    return x_key

# globaal dependencies
app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])


@app.get("/items/")
async def read_items():
    return [dict(item="Portal Gun"), dict(item="Plumbus")]


@app.get("/users/")
async def read_users():
    return [dict(username="Rick"), dict(username="Morty")]