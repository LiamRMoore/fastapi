"""
OAuth2 password flow requires username and password 
(exactly named) sent as Form fields, not JSON.

Same metadata and validation as with Body, Query, Path, Cookie...

HTTP protocol does not allow form html data in a json body. these
are encoded always as application/x-www-form-urlencoded instead of 
application/json
"""
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(
    username: str = Form(..., description="yo name"),
    password: str = Form(...)
):
    return dict(username=username)