from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal import admin
from .routers import items, users


# global dependency
app = FastAPI(dependencies=[Depends(get_query_token)])


# include the paths from the routers we implemented for 
# treating users and items
app.include_router(users.router)
app.include_router(items.router)
# can set custom prefix for router in, say, library code with 
# extra dependencies etc without modifying original like so:
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}}
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}