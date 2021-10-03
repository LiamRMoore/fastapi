"""
Useful for converting pydantic models into objects which 
can only accept json-like data; e.g. a database
"""
import logging
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.logger import logger
from pydantic import BaseModel


fake_db = {}
#logger = logging.getLogger(__name__)

class Item(BaseModel):
    title: str
    timestamp: datetime
    description: Optional[str] = None


app = FastAPI()


@app.put("/items/{id}", tags=["items"], status_code=status.HTTP_201_CREATED)
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    logger.info = print
    logger.info("db updated with:")
    logger.info(fake_db[id])