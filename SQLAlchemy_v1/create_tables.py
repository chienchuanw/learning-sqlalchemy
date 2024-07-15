from sqlalchemy import Table, MetaData, Column, Integer, String, Text, ForeignKey

# String: for short, fixed-length strings
# Text: for long, variable-length text

# MetaData is a container object that keeps together many different features of a database.
# It keeps all the information about all the tables
meta = MetaData()

# Define the users table
users_table = Table(
    "users",  # Table name
    meta,  # Metadata
    Column("id", Integer, primary_key=True),
    Column(
        "name", String(25), nullable=False
    ),  # String column 'name' with a max length of 25, cannot be null
    Column("full_name", Text),
)

# Note: Consider "String" as CharsField and "Text" as TextField compared with Django


comments_table = Table(
    "comments",
    meta,
    Column("id", Integer, primary_key=True),
    Column("comment", Text, nullable=False),
    Column(
        "user_id", Integer, ForeignKey("users.id")
    ),  # Integer column 'user_id' that references 'id' in the users table
)

# Note: ForeignKey is used to establish a relationship between the comments table and the users table
