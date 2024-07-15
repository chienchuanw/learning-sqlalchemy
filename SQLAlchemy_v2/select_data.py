from .insert_data import session
from .create_models import User, Comment
from sqlalchemy import select


# Create a SQL select statement to query users with usernames "Amy" or "John"
statement = select(User).where(User.username.in_(["Amy", "John"]))

# Execute the select statement using the session and retrieve the results as scalars
result = session.scalars(statement)

for user in result:
    print(user)

# Query all users from the database using the session
users = session.query(User).all()

for user in users:
    print(user)


result = session.query(User).filter_by(
    username="John"
)  # This is Query Object, so print(result) will get empty
print(result)


# Query the first user with the username "John" using the session
result = session.query(User).filter_by(username="John").first()
print(result)

# Create a SQL select statement to query comments made by user "Amy" with specific content
statement = (
    select(Comment)
    .join(Comment.user)
    .where(User.username == "Amy")
    .where(Comment.content == "This is my second comment")
)

# Execute the select statement using the session and retrieve the result as a scalar
result = session.scalars(statement).one()
print(result)

# Query comments made by user "Amy" with specific content using ORM
result = (
    session.query(Comment)
    .join(User)
    .filter(User.username == "Amy")
    .filter(Comment.content == "This is my second comment")
    .one()
)

# Print the result (actual Comment object)
print(result)
