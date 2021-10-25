import os
import logging

from fastapi import FastAPI
from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise


log = logging.getLogger("uvicorn")


TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["app.models.tortoise", "aerich.models"],
            "default_connection": "default"
        }
    }
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url=os.environ.get("DATABASE_URL"),
        modules=dict(models=["app.models.tortoise"]),
        generate_schemas=False,  # aerich will do this
        add_exception_handlers=True
    )


async def generate_schema() -> None:
    """
    Alternative schema generation to migration via Aerich (can be slow)

    Just run this file in the container and Tortoise will handle it
    """
    log.info("Initializing Tortoise...")

    await Tortoise.init(
        db_url=os.environ.get("DATABASE_URL"),
        modules={"models": ["models.tortoise"]}
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()


if __name__ == "__main__":
    run_async(generate_schema())
