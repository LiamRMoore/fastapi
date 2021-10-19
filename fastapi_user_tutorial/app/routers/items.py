"""
Can group endpoints with common path prefixes, dependencies, tags etc with APIRouter

tags and extra responses will be applied to all path operations declared in router

all dependencies will be added to each path operation and will be separated/resolved
for every request made to them
"""
from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import get_token_header

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "not found"}}
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "portal gun"}}


@router.get("/")
async def read_items():
    return fake_items_db

@router.get("/{item_id}")
async def read_item(item_id: str):
    if item_id not in fake_items_db:
        raise HTTPException(status_code=404, detail="item not found")
    return dict(name=fake_items_db[item_id]["name"], item_id=item_id)

@router.put(
    "/{item_id}",
    tags=["custom"],
    responses={403: {"description": "Operation forbidden"}}
)
async def update_item(item_id: str):
    if item_id != "plumbus":
        raise HTTPException(status_code=403, detail="You can only update the item: plumbus!")
    return dict(item_id=item_id, name="The great Plumbus")