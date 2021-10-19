from typing import List, Optional

from pydantic import BaseModel


# -- schema for items in database

class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True

# -- schema for users in database

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    """User creation endpoints require an additional password"""
    password: str


class User(UserBase):
    """For general use, excluding password"""
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        """read data even if not a dict using getattribute"""
        orm_mode = True
