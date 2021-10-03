"""
Declaring file bodies requires a special class to distinguish
it from query or body parameters.

Files are uploaded as form data.
"""
from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: bytes = File(...)):
    """
    bytes will be returned by fastAPI. all contents stored in memory.
    """
    return dict(file_size=len(file))


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    """
    Upload file is spooled (auto disk-cached past certain size)
    good for videos, images, etc
    """
    return dict(filename=file.filename, content_type=file.content_type)