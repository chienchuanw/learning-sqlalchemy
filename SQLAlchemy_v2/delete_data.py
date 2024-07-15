from .main import session
from .create_models import User, Comment

comment = session.query(Comment).filter_by(id=1).first()

session.delete(comment)
session.commit()
