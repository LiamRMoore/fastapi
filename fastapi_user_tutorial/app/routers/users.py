from fastapi import APIRouter


# instance acts like a mini FastAPI instance with all the same options
router = APIRouter()


@router.get("/users/", tags=["users"])
async def read_users():
    return [dict(username="Rick"), dict(username="Morty")]

@router.get("/users/me", tags=["users"])
async def read_user_me():
    return dict(username="Durandal")

@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return dict(username=username)