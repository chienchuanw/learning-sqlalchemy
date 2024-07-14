from create_tables import users_table
from connect_database import engine
from sqlalchemy import delete

# Create a DELETE statement for the users_table
# The statement deletes rows where the name column is "Frank"
statement = delete(users_table).where(users_table.c.name == "Frank")

with engine.connect() as connect:
    connect.execute(statement)
    connect.commit()
