"""
standard headers use hyper characters ("User-Agent" etc.)

FastAPI will convert underscores<->hyphens

+ 

http headers are case insensitive

=> 

user_agent <=> User_Agent <=> User-Agent

behaviour toggleable with convert_underscores argument of Header
(defaults True)
"""
from typing import Optional, List

from fastapi import FastAPI, Header


app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Optional[str] = Header(None, convert_underscores=True)):
    print(user_agent)
    return {"User-Agent": user_agent}