from .create_models import User, Comment
from sqlalchemy.orm import Session
from .connect_database import engine

# Create a new session
session = Session(bind=engine)

# Create instances of User and Comment
user_one = User(
    username="Amy",
    email="amy@gmail.com",
    comments=[
        Comment(content="This is my first comment"),
        Comment(content="This is my second comment"),
    ],
)

user_two = User(
    username="John",
    email="john@gmail.com",
    comments=[
        Comment(content="I am John"),
    ],
)

user_three = User(
    username="Jack",
    email="jack@gmail.com",
)

# Add all instances to the session
session.add_all([user_one, user_two, user_three])
# Commit the session to save the instances to the database
session.commit()

# Close the session to release the connection
session.close()


# # Use "with" statement to ensure the session is properly closed
# with Session(bind=engine) as session:
#     # Add all instances to the session
#     session.add_all([user_one, user_two, user_three])

#     # Commit the session to save the instances to the database
#     session.commit()
