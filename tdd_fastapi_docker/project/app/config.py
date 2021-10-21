import logging
import os
from enum import IntEnum

from pydantic import BaseSettings


log = logging.getLogger("uvicorn")

class LogLevel(IntEnum):
    off = 0
    light = 1
    heavy = 2

class Settings(BaseSettings):
    """
    fields not passed as kwargs are read from the environment

    default values are used if matching env var is not set
    pydantic is case INsensitive by default, can configure case_sensitive
    on nested Config object
    """
    environment: str = "dev"
    testing: bool = 0
    loglevel: LogLevel = 1
    

def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()


if __name__ == "__main__":
    s = get_settings()
    print(s)