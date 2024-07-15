from create_tables import users_table
from connect_database import engine
from sqlalchemy import update

# Create an UPDATE statement for the users_table
# The statement updates rows where the name column is "Susan" and sets the name to "Amy"
statement = update(users_table).where(users_table.c.name == "Susan").values(name="Amy")

with engine.connect() as connect:
    connect.execute(statement)
    # Commit the transaction to save the changes to the database. Otherwise, the update result will not be store in the database
    connect.commit()
