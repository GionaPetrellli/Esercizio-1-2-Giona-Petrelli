from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL = "postgresql://postgres:Its2025!@localhost/libreria"
engine = create_engine(URL)
db = sessionmaker(bind=engine)
Base = declarative_base()
