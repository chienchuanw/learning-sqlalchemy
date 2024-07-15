from sqlalchemy.orm import Session
from connect_database import engine

session = Session(bind=engine)
