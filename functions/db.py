from sqlalchemy import create_engine
import os


url = os.getenv("DATABASE_BIBLIOTECA")
engine = create_engine(url, future=True)