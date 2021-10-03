from typing import Optional, Set

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []


@app.post(
    "/items/",
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=["items!"],
    summary="create an item",
    # description=(
    #     "create an item with information and shit. "
    #     "totally free range shit here like i'm "
    #     "talkin 100% carbon neutral bananas up in this bitch"
    # ),
    response_description="The created item",
    deprecated=True
)
async def create_item(item: Item):
    """
    Alternatively the description is in the docstring:

    - bananas
    - apples
    - *pears*
    - **kiwis**

    ## section two

    1. A
    2. B
        - B(i)
        - B(j)
    3. Silky potatoes
    """
    return item