from .main import session
from .create_models import User, Comment

# Query the comment with id=1
comment = session.query(Comment).filter_by(id=1).first()

# Update the content of the comment
comment.content - "This is an updated comment"

# Commit the transaction to save the changes to the database
session.commit()
