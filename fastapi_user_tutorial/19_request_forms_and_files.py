"""
Use File and Form together when need to receive files and data in the same request
"""
from fastapi import FastAPI, File, Form, UploadFile


app = FastAPI()

@app.post("/files/")
async def create_file(
    file: bytes = File(...),
    fileb: UploadFile = File(...),
    token: str = Form(...)
):
    return dict(
        file_size=len(file),
        token=token,
        fileb_content_type=fileb.content_type
    )