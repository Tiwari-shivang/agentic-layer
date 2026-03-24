from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
load_dotenv()

DB_URL=os.getenv("CONN_STR")
engine=create_engine(DB_URL)
session_local=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

BaseClass= declarative_base()

def get_db():
    db=session_local()
    try:
        yield
    finally:
        db.close()