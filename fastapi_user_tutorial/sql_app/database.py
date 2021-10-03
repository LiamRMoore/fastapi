from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False})

# create a class to provide us with sessions via instances of itself
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# base class for the ORM models
Base = declarative_base()