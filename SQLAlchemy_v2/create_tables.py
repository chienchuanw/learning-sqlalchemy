from .create_models import Base, User, Comment
from .connect_database import engine

Base.metadata.create_all(bind=engine)
