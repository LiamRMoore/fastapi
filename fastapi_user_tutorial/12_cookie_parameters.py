from typing import Optional

from fastapi import Cookie, FastAPI

app = FastAPI()

@app.get("/items/")
async def read_items(ads_id: Optional[str] = Cookie(None)):
    return dict(
        ads_id = ads_id
    )