from fastapi import FastAPI

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**. This is ***Markdown***.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "users",
        "description" : "Fancy *markdown* description of **users**."
    },
    {
        "name" : "items",
        "description" : "Manage items. _fancy_ items.",
        "externalDocs" : {
            "description" : "items external docs",
            "url" : "https://fastapi.tiangolo.com/"
        }
    }
]

app = FastAPI(
    title="ChimichangApp",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json", # default /openapi.json
    docs_url="/doks", # default /docs
    redoc_url="/redoc"
)


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Katana"}, {"item": "Slipper"}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"name": "Joe"}, {"name": "Black"}]